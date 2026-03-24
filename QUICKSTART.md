# 🚀 Rychlý Start - Pexeso

## 5 minut ke spuštění aplikace

### Krok 1: Instalace Pythonu (pokud ho nemáte)
Stáhněte si Python 3.7+ z https://www.python.org

Při instalaci **ZAŠKRTNĚTE** volbu: ✅ "Add Python to PATH"

### Krok 2: Otevřete terminál/příkazový řádek

**Windows:**
- Stiskněte `Windows + R`
- Zadejte `cmd`
- Stiskněte Enter

**Linux/Mac:**
- Otevřete Terminal

### Krok 3: Navigace do složky projektu

```bash
# Změňte cestu na vaši lokaci (příklad pro Windows):
cd f:\student\it3\vitek\pcv_prg\pexeso_vitek

# Nebo na Linux/Mac:
cd ~/Projects/pexeso_vitek
```

### Krok 4: Spuštění

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

**Alternativně (všechny systémy):**
```bash
pip install -r requirements.txt
python main.py
```

---

## Při prvním spuštění

1. **Aplikace se otevře** v novém okně
2. **Klikněte** na tlačítko "Načíst obrázek"
3. **Vyberte** obrázek ze složky `assets/`
4. **Zadejte** správnou odpověď (tajenku)
5. **Hra začíná!**

---

## Příprava obrázků

1. Vytvořte složku `assets` v root adresáři
2. Umístěte tam sve obrázky (PNG, JPG, atd.)
3. Při spuštění si je vyberte

**Příklady:**
```
assets/
├── einstein.jpg
├── microsoft.png
├── telefon.jpg
└── ...
```

---

## Řešení problémů

### "ModuleNotFoundError: No module named 'PIL'"
```bash
pip install Pillow
```

### Aplikace se neotevírá
- Zkontrolujte, že máte Python 3.7+: `python --version`
- Reinstalujte Pillow: `pip install --force-reinstall Pillow`

### Obrázek se nenačítá
- Zkontrolujte formát (PNG, JPG, JPEG, BMP)
- Obsah obrázku na cestě bez speciálních znaků

---

## Úprava Pravidel

Otevřete soubor `config/game_config.py` a změňte:

```python
GAME_CONFIG = {
    "starting_points": 120,        # Změňte počáteční body
    "game_time_seconds": 600,      # Změňte čas (v sekundách)
    "wrong_answer_penalty": 20,    # Změňte penalizaci za chybu
}
```

Pak **resetujte aplikaci** (zavřete a spusťte znovu).

---

## Užitečné Klávesové Zkratky

| Akce | Klávesnice |
|------|-----------|
| Odeslat odpověď | `Enter` |
| Zavřít aplikaci | `Alt + F4` (Windows) nebo `Cmd + Q` (Mac) |

---

## Podpora

Máte-li problémy:
1. Přečtěte si README.md
2. Zkontrolujte SCENARIOS.md pro příklady
3. Zkuste reinstalovat závislosti

**Hodně štěstí! 🎮**
