#!/usr/bin/env python3
"""
Convert the published web digest (digest/index.html) into an email-safe HTML
newsletter (table layout, inline styles, sections expanded) + a plain-text part.

Usage: python3 build_email.py <source_digest.html> <out_prefix>
  writes <out_prefix>.html and <out_prefix>.txt
The email is built FROM the given source, so run it on the CURRENT live page at
approval time and any edits Jamie made are carried through automatically.
"""
import sys, html, re

def _tidy(t):
    """Close up whitespace that sits before punctuation, and collapse runs."""
    t = re.sub(r"\s+([,.;:!?])(?!\d)", r"\1", t)  # keep the space before decimals like .42
    return re.sub(r"\s{2,}", " ", t).strip()

from bs4 import BeautifulSoup

COR="#b3411f"; DARK="#1a1a1a"; TXT="#33302b"; MUT="#8a7f70"; BODY="#4a453d"; LINE="#e7e1d6"; BAR="#242b38"; FONT="Arial,Helvetica,sans-serif"

def esc(s): return html.escape(s or "", quote=True)

def business():
    """Sender identity for the footer, read from config/config.yaml (business:).
    A plain line reader, so this script needs no YAML package."""
    import os
    out={"legal_name":"","postal_address":"","privacy_url":"https://thereclab.ai/privacy","email_notice":""}
    path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","config.yaml")
    try:
        inside=False
        for line in open(path,encoding="utf-8"):
            if re.match(r"^business:\s*$",line): inside=True; continue
            if inside and re.match(r"^\S",line): break
            m=re.match(r"^\s+(legal_name|postal_address|privacy_url|email_notice):\s*(.*?)\s*(#.*)?$",line) if inside else None
            if m: out[m.group(1)]=m.group(2).strip().strip('"').strip("'")
    except OSError:
        pass
    return out

def main(src, outp):
    soup=BeautifulSoup(open(src).read(), "html.parser")
    biz=business()
    identity="You are receiving this because you subscribed at thereclab.ai/digest."
    notice=biz["email_notice"]
    notice_html=""
    if notice:
        notice_html=(f'<p style="margin:0 0 18px;padding:10px 12px;background-color:#f3ede2;font-family:{FONT};font-size:13px;color:{BODY};line-height:1.5;">'
                     f'{esc(notice)} <a href="{esc(biz["privacy_url"])}" style="color:{COR};">Privacy policy</a></p>')
        print("NOTE: this email carries the one-off notice from config/config.yaml (business.email_notice). "
              "Clear it after this send.", file=sys.stderr)
    if biz["legal_name"] and biz["postal_address"]:
        identity=f"TheRecLab Weekly Digest is sent by {biz['legal_name']}, {biz['postal_address']}. "+identity
    else:
        print("WARNING: config/config.yaml has no business legal_name or postal_address, so the "
              "email footer does not say who sends it. Fill both in before a send.", file=sys.stderr)
    kicker=soup.select_one(".kicker").get_text(strip=True)
    date=soup.select_one(".date").get_text(strip=True)
    sub=soup.select_one(".subtitle")
    sub_html="".join(str(c) for c in sub.children) if sub else ""

    # week in brief: brief-label + brief-text pair, then the standouts heading
    bl=soup.select_one(".summary .brief-label")
    # The brief is up to two paragraphs: the recruiting news, then a separate
    # paragraph opening "And in the world of AI,". Keep every one, in order.
    brief_paras=[b.get_text(" ", strip=True) for b in soup.select(".summary .brief-text")]
    brief_paras=[b for b in brief_paras if b]
    brief_label=bl.get_text(strip=True) if bl else ""
    theme="\n\n".join(brief_paras)
    sh=soup.select_one(".summary h2.sh")
    standout_heading=sh.get_text(" ", strip=True) if sh else "Standout content from this week"
    standouts=[]
    for li in soup.select(".summary ul li"):
        a=li.find("a")
        if not a: continue
        href=a.get("href","")
        atext=a.get_text(" ", strip=True)
        pick_el=li.select_one(".pick")
        pick=pick_el.get_text(" ", strip=True) if pick_el else ""
        # WHY: prefer the dedicated .why span; fall back to body text after the title
        why_el=li.select_one(".why")
        if why_el:
            why=why_el.get_text(" ", strip=True)
        else:
            body=li.select_one(".body")
            btext=(body.get_text(" ", strip=True) if body else li.get_text(" ", strip=True))
            why=btext[len(atext):].lstrip(" ,").strip()
        standouts.append((pick, href, atext, why))

    # sections
    sections=[]
    for sec in soup.select("section"):
        lbl_el=sec.select_one("summary.sec .lbl")
        if not lbl_el: continue
        label=lbl_el.decode_contents()  # keep &amp; entities
        items=[]
        for art in sec.select("article.item"):
            src_el=art.select_one(".src")
            src_txt=src_el.decode_contents() if src_el else ""  # keeps brand span
            cdate=art.select_one(".cdate").get_text(strip=True) if art.select_one(".cdate") else ""
            a=art.select_one("a.ttl")
            if a:
                href=a.get("href",""); title=a.get_text(" ", strip=True)
            else:
                vg=art.select_one(".vgroup-title")
                href=""; title=vg.get_text(" ", strip=True) if vg else ""
            g=art.select_one(".guest")
            guest=g.get_text(" ", strip=True) if g else ""
            bullets=[]
            for bli in art.select("ul.pts li"):
                ba=bli.find("a")
                # get_text(" ") joins child nodes with a space, which puts a space
                # before the punctuation that follows a <span class="rt"> release
                # name: "WhatsApp messaging , live now." Only grouped vendor blocks
                # have that markup, which is why it went unnoticed until 11 Sep 2026.
                bullets.append((_tidy(bli.get_text(" ", strip=True)),
                                ba.get("href","") if ba else ""))
            items.append((src_txt, cdate, href, title, guest, bullets))
        sections.append((label, items))

    # --- render HTML email ---
    def bullet_li(bt, bh):
        if bh:
            return f'<li style="margin:0 0 5px;"><a href="{bh}" style="color:{BODY};text-decoration:none;">{esc(bt)}</a></li>'
        return f'<li style="margin:0 0 5px;">{esc(bt)}</li>'
    def item_html(src_txt, cdate, href, title, guest, bullets):
        # src_txt may contain a <span class="brand">by X</span>; strip class, keep muted
        st=src_txt.replace('<span class="brand">','<span style="color:#9a8f70;font-weight:normal;">')
        b="".join(bullet_li(bt,bh) for bt,bh in bullets)
        gh=f'<p style="margin:4px 0 0;font-family:{FONT};font-size:13px;font-style:italic;color:{MUT};">{esc(guest)}</p>' if guest else ""
        if href:
            title_html=f'<a href="{href}" style="font-family:{FONT};font-size:18px;font-weight:bold;color:{DARK};text-decoration:none;line-height:1.3;">{esc(title)}</a>'
        else:
            title_html=f'<p style="margin:0;font-family:{FONT};font-size:18px;font-weight:bold;color:{DARK};line-height:1.3;">{esc(title)}</p>'
        return (f'<tr><td style="padding:16px 20px 14px;border-bottom:1px solid {LINE};">'
                f'<p style="margin:0 0 3px;font-family:{FONT};font-size:12px;font-weight:bold;color:{COR};text-transform:uppercase;letter-spacing:1px;">{st} <span style="color:{MUT};font-weight:normal;">&middot; {esc(cdate)}</span></p>'
                f'{title_html}'
                f'{gh}<ul style="margin:9px 0 0;padding-left:20px;color:{BODY};font-family:{FONT};font-size:14px;line-height:1.5;">{b}</ul></td></tr>')

    def bar(label):
        return (f'<tr><td bgcolor="{BAR}" style="background-color:{BAR};color:#f3ede2;font-family:{FONT};font-size:11px;font-weight:bold;letter-spacing:2px;text-transform:uppercase;padding:11px 20px;">{label}</td></tr>')

    so_html="".join(
        f'<p style="margin:0 0 12px;font-family:{FONT};font-size:14px;line-height:1.5;color:{BODY};">'
        + (f'<span style="font-family:{FONT};font-size:11px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:{COR};">{esc(pick)}</span><br>' if pick else '')
        + f'<a href="{href}" style="color:{DARK};text-decoration:none;font-weight:bold;">{esc(atext)}</a>'
        + (f'<br><span style="color:{BODY};">{esc(why)}</span>' if why else '') + '</p>'
        for pick, href, atext, why in standouts)

    sect_html="".join(bar(lbl)+"".join(item_html(*it) for it in items) for lbl,items in sections)

    # one <p> per brief paragraph; the last keeps the wider gap before the standouts
    brief_html="\n".join(
        f'<p style="margin:0 0 {18 if i==len(brief_paras)-1 else 10}px;font-family:{FONT};font-size:14px;color:{BODY};line-height:1.55;">{esc(b)}</p>'
        for i,b in enumerate(brief_paras))
    email=f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>{esc(kicker)}</title></head>
<body style="margin:0;padding:0;background-color:#efe9df;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#efe9df" style="background-color:#efe9df;">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background-color:#fbfaf7;">
<tr><td style="padding:32px 20px 20px;border-bottom:2px solid #1a1a1a;">
<p style="margin:0;font-family:{FONT};font-size:26px;font-weight:bold;color:{DARK};line-height:1.15;">{esc(kicker)}</p>
<p style="margin:10px 0 0;font-family:{FONT};font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#9a8f80;">{esc(date)}</p>
<p style="margin:14px 0 0;font-family:{FONT};font-size:14px;font-style:italic;color:{MUT};line-height:1.5;">{sub_html}</p>
</td></tr>
<tr><td style="padding:22px 20px 8px;">
{notice_html}
<p style="margin:0 0 6px;font-family:{FONT};font-size:11px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:{DARK};">{esc(brief_label)}</p>
{brief_html}
<p style="margin:0 0 12px;font-family:{FONT};font-size:11px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:{COR};">{esc(standout_heading)}</p>
{so_html}
</td></tr>
{sect_html}
<tr><td style="padding:20px;">
<p style="margin:0;font-family:{FONT};font-size:12px;color:#b0a695;line-height:1.55;">While sources are carefully selected by <a href="https://www.linkedin.com/in/jamiejaylyons/" style="color:#b0a695;text-decoration:underline;">Jamie Jay Lyons</a>, descriptions are generated by Claude. Reply any time with sources you think we should add.</p>
<p style="margin:14px 0 0;font-family:{FONT};font-size:12px;color:#b0a695;"><a href="https://thereclab.ai/digest/subscriber" style="color:{COR};text-decoration:none;font-weight:bold;">View this edition on the web</a> &nbsp;&middot;&nbsp; <a href="{{{{{{RESEND_UNSUBSCRIBE_URL}}}}}}" style="color:#b0a695;text-decoration:underline;">Unsubscribe</a> &nbsp;&middot;&nbsp; <a href="{esc(biz['privacy_url'])}" style="color:#b0a695;text-decoration:underline;">Privacy policy</a></p>
<p style="margin:10px 0 0;font-family:{FONT};font-size:11px;color:#b0a695;line-height:1.5;">{esc(identity)}</p>
</td></tr>
</table></td></tr></table></body></html>'''

    # plain text
    # Comma, not a dash. The digest voice bans em and en dashes, and the later
    # safety pass used to swap the dash for a comma while leaving its spaces,
    # producing "TheRecLab Weekly Digest ,  Version 2" in the plain text header.
    lines=[f"{kicker}, {date}", ""]+([notice+" Privacy policy: "+biz["privacy_url"], ""] if notice else [])+[brief_label, theme, "", standout_heading, ""]
    for pick, href, atext, why in standouts:
        lines.append(f"{pick.upper()+': ' if pick else ''}{atext}".strip())
        if why: lines.append(why)
        lines.append(href)
        lines.append("")
    lines.append("")
    for lbl,items in sections:
        lines.append(html.unescape(lbl).upper())
        for st,cd,href,title,guest,bullets in items:
            plain_src=BeautifulSoup(st,"html.parser").get_text(" ",strip=True)
            if href:
                lines.append(f"- {title} ({plain_src}, {cd}) {href}")
            else:
                lines.append(f"- {title} ({plain_src}, {cd})")
                for bt,bh in bullets:
                    lines.append(f"    * {bt}{(' '+bh) if bh else ''}")
        lines.append("")
    lines.append("View on the web: https://thereclab.ai/digest/subscriber")
    lines.append("Unsubscribe: {{{RESEND_UNSUBSCRIBE_URL}}}")
    lines.append("Privacy policy: "+biz["privacy_url"])
    lines.append("")
    lines.append(identity)
    text="\n".join(lines)

    # SAFETY NET: the digest must never contain em/en dashes; strip any that slip
    # through (in the source prose or an inserted separator) from both outputs.
    for ch in ("—","–"):        # em dash, en dash
        email=email.replace(ch, ", ")
        text=text.replace(ch, ", ")
    email=email.replace("&mdash;", ", ").replace("&ndash;", ", ")
    # AGGREGATE CLICK COUNTING (since 22 November 2026). Point each outside link
    # at https://thereclab.ai/go/v<N>/<n>, which counts the click in total (Vercel
    # Web Analytics, nothing per person) and forwards to the real page. Only links
    # in digest/go/v<N>.json are rewritten, the same file the site forwards from;
    # anything else stays a direct link. No file, no rewriting, with a warning.
    # Click counting through thereclab.ai/go/ was tried on 22 November 2026 and
    # dropped the same night (Jamie's call): the email carries direct links and
    # nothing in it is tracked. go_rewrite() is kept below, unused, in case.
    open(outp+".html","w").write(email)
    open(outp+".txt","w").write(text)
    print("wrote",outp+".html",len(email),"bytes;",outp+".txt",len(text),"bytes")
    print("sections:",[(BeautifulSoup(l,'html.parser').get_text(),len(i)) for l,i in sections])
    print("standouts:",len(standouts))


def go_rewrite(soup, email, text):
    import json, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from go_links import edition_version, go_url
    version = edition_version(soup)
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "digest", "go", version + ".json")
    if not os.path.exists(path):
        print(f"WARNING: {path} is missing, so the email uses direct links and no "
              "clicks will be counted. Run scripts/go_links.py on the live page first.",
              file=sys.stderr)
        return email, text, 0
    by_url = {u: go_url(version, n) for n, u in json.load(open(path)).items()}
    used = set()
    def sub(m):
        u = html.unescape(m.group(1))
        if u in by_url:
            used.add(u)
            return 'href="' + by_url[u] + '"'
        return m.group(0)
    email = re.sub(r'href="([^"]+)"', sub, email)
    text = "\n".join(by_url.get(line.strip(), line) for line in text.split("\n"))
    return email, text, len(used)

if __name__=="__main__":
    main(sys.argv[1], sys.argv[2])
