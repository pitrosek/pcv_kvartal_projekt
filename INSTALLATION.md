# 📦 Instalační Příručka - Pexeso

## Úvod

Tato příručka vás provede instalací a prvním spuštěním aplikace **Pexeso** na jakémkoli počítači.

---

## Systemové Požadavky

| Požadavek | Minimální | Doporučené |
|-----------|-----------|----------|
| OS | Windows 7, Linux, macOS 10.12 | Windows 10+, Ubuntu 18.04+, macOS 11+ |
| RAM | 512 MB | 2+ GB |
| CPU | Intel/AMD (1GHz+) | Intel i5+/AMD Ryzen 5+ |
| Volné místo | 100 MB | 500+ MB |
| Python | 3.7 | 3.9, 3.10, 3.11 |

---

## Instalace - Krok za Krokem

### ✅ Krok 1: Instalace Pythonu

Pokud Python nemáte, nainstalujte si jej:

#### Windows:
1. Navštivte https://www.python.org/downloads/
2. Klikněte na "Download Python 3.x.x"
3. Spusťte instalátor
4. **DŮLEŽITÉ:** Zaškrtněte ✅ "Add Python to PATH"
5. Klikněte "Install Now"

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

#### macOS:
```bash
# Pomocí Homebrew (pokud máte instalovaný)
brew install python3

# Nebo si stáhněte z https://www.python.org/downloads/
```

#### Ověření:
```bash
python --version
# Měli byste vidět: Python 3.x.x
```

---

### ✅ Krok 2: Stažení Projektu

1. Stáhněte si projekt **pexeso_vitek**
2. Rozbalte ZIP soubor do libovolné složky
3. Pamatujte si cestu k projektu!

Příklad cesty:
- Windows: `C:\Users\Jmeno\Documents\pexeso_vitek`
- Linux: `/home/uzivatel/Projects/pexeso_vitek`
- macOS: `/Users/username/Projects/pexeso_vitek`

---

### ✅ Krok 3: Otevření Příkazového Řádku

#### Windows:
1. Otevřete **Start Menu**
2. Napište `cmd` a stiskněte Enter

#### Linux/macOS:
- Otevřete aplikaci **Terminal**

---

### ✅ Krok 4: Navigace do Projektu

Do příkazového řádku zadejte:

```bash
# Příklad (upravte cestu podle své lokace):
cd C:\Users\Jmeno\Documents\pexeso_vitek

# Nebo na Linuxu/Mac:
cd ~/Projects/pexeso_vitek
```

Ověřit, že jste ve správné složce:
```bash
dir        # Windows
ls         # Linux/macOS
```

Měli byste vidět soubory: `main.py`, `README.md`, atd.

---

### ✅ Krok 5: Instalace Závislostí

Instalace knihovny **Pillow** (pro práci s obrázky):

```bash
pip install -r requirements.txt
```

Ověřit instalaci:
```bash
python -c "from PIL import Image; print('OK')"
```

---

### ✅ Krok 6: Vytvoření Testovacích Obrázků (Doporučeno)

Vytvořte testovací obrázky pro vyzkoušení:

```bash
python create_test_images.py
```

Měli byste vidět:
```
✅ Testovací obrázek vytvořen: assets/test_image.png
✅ Barevný obrázek vytvořen: assets/colors_image.png
✅ Gradientní obrázek vytvořen: assets/gradient_image.png
```

---

### ✅ Krok 7: Spuštění Aplikace

#### Varianta A - Automatizovaný Spouštěč:

**Windows:**
```bash
run.bat
```

**Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```

#### Varianta B - Manuální Spuštění:

```bash
python main.py
```

---

## Při Prvním Spuštění

Jakmile se aplikace otevře:

1. **Kliknutí** na tlačítko "Načíst obrázek"
2. **Vybrat** jeden z testovacích obrázků ze složky `assets/`
3. **Zadat** správné odpovědi:
   - `test_image.png` → `PYTHON`
   - `colors_image.png` → `BARVY`
   - `gradient_image.png` → `GRADIENT`
4. **Hra začíná!** ✅

---

## Řešení Problémů

### ❌ "Python is not recognized"

**Problém:** Python není v PATH.

**Řešení:**
1. Odinstalujte Python
2. Znovu instalujte, ale **ZAŠKRTNĚTE** "Add Python to PATH"
3. Restartujte počítač

### ❌ "ModuleNotFoundError: No module named 'PIL'"

**Problém:** Pillow není nainstalován.

**Řešení:**
```bash
pip install Pillow
```

Nebo:
```bash
pip install --upgrade Pillow
```

### ❌ Aplikace se neotevírá

**Kontrolní seznam:**
1. Python verze: `python --version` (musí být 3.7+)
2. Zkontrolujte instalaci Pillow: `pip list`
3. Zkuste reinstalovat: `pip install --force-reinstall Pillow`
4. Spusťte znovu: `python main.py`

### ❌ Obrázek se nenačítá

**Možné příčiny:**
- Špatný formát (musí být PNG, JPG, JPEG nebo BMP)
- Cesta obsahuje speciální znaky
- Obrázek je poškozený

**Řešení:**
1. Zkontrolujte formát souboru
2. Přejmenujte obrázek bez speciálních znaků
3. Zkuste testovací obrázky z `create_test_images.py`

---

## Ověření Správné Instalace

Spusťte tento příkaz:

```bash
python -c "
import sys
import tkinter
from PIL import Image
print('✅ Python:', sys.version.split()[0])
print('✅ Tkinter: OK')
print('✅ Pillow: OK')
print('✅ Všechny závislosti jsou v pořádku!')
"
```

Měli byste vidět:
```
✅ Python: 3.x.x
✅ Tkinter: OK
✅ Pillow: OK
✅ Všechny závislosti jsou v pořádku!
```

---

## Příprava Vlastních Obrázků

1. Vyberte obrázek (400×400px nebo větší je ideální)
2. Umístěte jej do složky `assets/`
3. Při spuštění si jej vyberte
4. Zadejte správnou tajenku

### Doporučené Obrázky:
- 📸 Fotografie osobností
- 🏢 Loga společností
- 💻 Historické IT zařízení
- 🔬 Vědecké ilustrace

---

## Odinstalace

Chcete-li odstranit aplikaci:

### Windows:
1. Pouze smaž složku `pexeso_vitek`
2. Python si ponechá jako systémový soubor (pokud chcete, lze odinstalovat v Control Panel)

### Linux/macOS:
```bash
rm -rf ~/Projects/pexeso_vitek
```

---

## Aktualizace

Chcete-li aktualizovat aplikaci:

1. Stáhněte si novou verzi projektu
2. Zkopírujte nové soubory do existující složky
3. Existující obrázky v `assets/` se zachovají

---

## Pokročilá Nastavení

### Úprava Herních Parametrů

Otevřete `config/game_config.py`:

```python
GAME_CONFIG = {
    "starting_points": 120,      # Změňte počáteční body
    "game_time_seconds": 600,    # Změňte čas hry
    "wrong_answer_penalty": 20,  # Změňte penalizaci
}
```

### Změna Barev

V `config/game_config.py` změňte `COLORS`:

```python
COLORS = {
    "bg_main": "#YOUR_COLOR",
    # ... ostatní barvy
}
```

Barvy jsou v RGB hexa: https://htmlcolorcodes.com

---

## Spuštění bez Terminálu (Windows)

Pokud chcete běžné spuštění bez terminálu:

1. Vytvořte soubor `launcher.vbs`:
```vbscript
CreateObject("WScript.Shell").Run "python main.py", 0, False
```

2. Umístěte jej do kořenové složky projektu
3. Poklikejte na něj pro spuštění aplikace

---

## Systém Souborů Po Instalaci

```
pexeso_vitek/
├── main.py                      # Hlavní aplikace
├── config/
│   ├── __init__.py
│   └── game_config.py          # Konfigurační soubor
├── assets/                     # Vaše obrázky tady
│   ├── test_image.png         # Testovací obrázky
│   ├── colors_image.png
│   └── gradient_image.png
├── requirements.txt            # Závislostí
├── run.bat                     # Spouštěč (Windows)
├── run.sh                      # Spouštěč (Linux/Mac)
├── create_test_images.py      # Generátor testů
├── README.md                   # Dokumentace
└── ... další soubory
```

---

## Kontakt na Podporu

Máte-li problém, který jsem zde nepokryl:

1. Přečtěte si `README.md`
2. Zkontrolujte `ARCHITECTURE.md` pro technické detaily
3. Vyzkoušejte testovací obrázky z `create_test_images.py`

---

## Shrnutí - 5 Kroků k Úspěchu

1. ✅ Nainstalujte Python 3.7+
2. ✅ Stáhněte si projekt
3. ✅ Otevřete příkazový řádek v projektu
4. ✅ Spusťte: `pip install -r requirements.txt`
5. ✅ Spusťte: `python main.py`

**Hotovo! 🎉**

---

Poslední aktualizace: 2026-03-24
