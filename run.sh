#!/bin/bash
# Spouštěč aplikace Pexeso pro Linux/Mac
# Úkol: Instalace závislostí a spuštění aplikace

echo "========================================"
echo "  Pexeso - Soutěžní Aplikace"
echo "========================================"
echo ""

# Kontrola Pythonu
if ! command -v python3 &> /dev/null; then
    echo "CHYBA: Python 3 není nainstalován."
    echo "Prosím nainstalujte Python 3.7+ z https://www.python.org"
    exit 1
fi

echo "[OK] Python je nainstalován."
python3 --version
echo ""

# Instalace závislostí
echo "Instaluji závislosti (Pillow)..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "CHYBA: Nepovedlo se nainstalovat závislosti."
    exit 1
fi

echo ""
echo "[OK] Všechny závislosti jsou nainstalovány."
echo ""

# Spuštění aplikace
echo "Spouštím aplikaci..."
python3 main.py

exit $?
