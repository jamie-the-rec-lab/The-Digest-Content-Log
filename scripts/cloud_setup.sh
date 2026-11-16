#!/bin/bash
# Cloud environment setup script for the weekly digest.
#
# This file is a RECORD. The copy that actually runs lives in the cloud
# environment's settings (environment menu, Edit, Setup script). If you change
# one, change the other, and note it in docs/CHANGELOG.md.
#
# It runs once when a session's machine starts, before the job. It cannot see
# the environment's secrets, and does not need to.
#
# Kept deliberately small and forgiving: a missing optional tool must never stop
# the Wednesday run. Only the essentials fail loudly.

set -u

# Essential: the email builder parses the live page.
# python3 -m pip, not bare pip: the image has two Pythons and bare pip can install
# into the other one (this stopped the 15 and 16 Nov 2026 runs before they began).
python3 -m pip install -q --break-system-packages "beautifulsoup4>=4.12" || python3 -m pip install -q "beautifulsoup4>=4.12"
python3 -c "import bs4" || { echo "SETUP FAILED: beautifulsoup4 did not install for $(command -v python3)"; exit 1; }

# Optional: reading scanned report PDFs (pdftoppm, then tesseract). Without
# these a scanned report is a recorded gap, not a broken run.
if ! command -v tesseract >/dev/null || ! command -v pdftoppm >/dev/null; then
  (apt-get update -qq && apt-get install -y -qq tesseract-ocr poppler-utils) >/dev/null 2>&1 \
    || echo "setup note: OCR tools not installed; scanned PDFs will be recorded as gaps"
fi

echo "setup ok: python $(python3 --version 2>&1 | cut -d' ' -f2), bs4 present, ocr: $(command -v tesseract >/dev/null && echo yes || echo no)"
exit 0
