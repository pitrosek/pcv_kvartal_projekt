@echo off
REM Spouštěč aplikace Pexeso
REM Úkol: Instalace závislostí a spuštění aplikace

echo ========================================
echo  Pexeso - Soutěžní Aplikace
echo ========================================
echo.

REM Kontrola Pythonu
python --version >nul 2>&1
if errorlevel 1 (
    echo CHYBA: Python není nainstalován nebo není v PATH.
    echo Prosím nainstalujte Python 3.7+ z https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python je nainstalován.
echo.

REM Instalace závislostí
echo Instaluji závislosti (Pillow)...
pip install -r requirements.txt

if errorlevel 1 (
    echo CHYBA: Nepovedlo se nainstalovat závislosti.
    pause
    exit /b 1
)

echo.
echo [OK] Všechny závislosti jsou nainstalovány.
echo.

REM Spuštění aplikace
echo Spouštím aplikaci...
python main.py

if errorlevel 1 (
    echo.
    echo CHYBA: Aplikace selhala.
    pause
    exit /b 1
)

exit /b 0
