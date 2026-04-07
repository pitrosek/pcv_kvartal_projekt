# 🎮 Soutěžní Aplikace pro Znalostní Hry

Interaktivní aplikace pro znalostní soutěž základních škol. Soutěžící odhalují obrázek postupným otevíráním políček mřížky a pokoušejí se uhodnout tajenku.

## 📋 Požadavky

- Python 3.7+
- Tkinter (obvykle součást Pythonu)
- Pillow (PIL) pro práci s obrázky

## 🚀 Instalace

1. **Instalace závislostí:**
```bash
pip install -r requirements.txt
```

2. **Příprava obrázků:**
   - Vytvořit složku `assets` v kořenovém adresáři projektu
   - Umístit tam obrázky pro jednotlivé kola (.png, .jpg, .jpeg, .bmp)

3. **Spuštění aplikace:**
```bash
python main.py
```

## 🎯 Princip Hry

### Pravidla:
- **Počáteční body:** 120
- **Časový limit:** 10 minut (600 sekund)
- **Penalty za špatnou odpověď:** -20 bodů

### Odhalování politček:
- **1. políčko:** Zdarma (0 bodů)
- **2. políčko:** -1 bod
- **3. políčko:** -2 body
- **4. políčko:** -3 body
- (a tak dále, lineárně se zvyšující penalty)

### Herní průběh:
1. Aplikace načte obrázek a vytvoří 4×4 mřížku
2. Soutěžící si postupně vybírají políčka k odhalení
3. Při každém odhalení se platí odpovídající cena v bodech
4. Cílem je uhodnout tajenku (správnou odpověď)
5. Za správnou odpověď si hráči ponechají zbývající body
6. Za špatnou odpověď přijdou o 20 bodů a mohou pokračovat

## 📌 Konfigurace

Všechny parametry hry lze měnit v souboru `config/game_config.py`:

```python
GAME_CONFIG = {
    "starting_points": 120,      # Počáteční body
    "grid_size": 4,              # Velikost mřížky (4x4)
    "game_time_seconds": 600,    # Čas hry v sekundách (10 minut)
    "wrong_answer_penalty": 20,  # Penalty za špatnou odpověď
}
```

### Úprava ceny za odhalení:
Funkce `get_reveal_cost(cell_number)` v `game_config.py` určuje cenu za různá politčka.

**Aktuální logika:**
- Pozice 0 (první políčko): 0 bodů
- Pozice 1 (druhé políčko): -1
- Pozice 2 (třetí políčko): -2
- atd.

Lze ji snadno upravit na vlastní potřebu.

## 🖼️ Struktura Projektu

```
pexeso_vitek/
├── main.py                 # Hlavní aplikace
├── requirements.txt        # Závislosti
├── README.md              # Tento soubor
├── config/
│   └── game_config.py     # Konfigurace hry
└── assets/                # Složka pro obrázky
    ├── obrazek1.jpg
    ├── obrazek2.png
    └── ...
```

## 🎨 Uživatelské Rozhraní

### Horní Panel:
- **Body:** Aktuální bodové skóre
- **Nápověda:** Informace o nápověďích
- **Poslední tah:** Cena posledního pohybu
- **Čas:** Zbývající čas v MM:SS formátu

### Střední Část:
- **Mřížka 4×4:** Politčka k odhalení obrázku
- **Info panel:** Pokyny a informace pro hráče

### Dolní Panel:
- **Tajenka:** Zobrazení jednotlivých písmen (? = skrytý, viditelný = odhalený)
- **Vstup odpovědi:** Pole pro zadání správné odpovědi
- **Tlačítko Odeslat:** Odesílaní odpovědi (lze i Enter)
- **Tlačítko Načíst obrázek:** Pro výběr nového obrázku

## 💡 Tipy pro Nasazení v Soutěži

1. **Příprava Obrázků:**
   - Zvolte obrázky, které jsou zajímavé a edukativní
   - Zkontrolujte čitelnost částí obrázku
   - Doporučuji obrázky 400×400px nebo větší

2. **Testování:**
   - Vždy otestujte aplikaci před soutěží
   - Zkontrolujte časování a bodový systém
   - Ověřte, že se všechny obrázky správně načítají

3. **Obsluha během Soutěže:**
   - Vedoucí vybere obrázek pomocí tlačítka "Načíst obrázek"
   - Zadá odpovídající tajenku
   - Soutěžní tým vybírá políčka a snaží se uhodnout
   - Po vypršení času se hra automaticky ukončí

4. **Bezpečnost:**
   - Aplikace umožňuje skrytí odpovědi až do konce
   - Jednotlivá písmena se zobrazují pouze při jejich "odhalení"
   - Všechny funkce jsou intuitivní a bezpečné

## 🔧 Rozšíření a Úpravy

### Přidání Nápověd (Hint System):
V budoucí verzi lze přidat:
- Možnost zobrazení jednotlivých písmen za určitou cenu bodů
- Kombinace více herních módů
- Statistiky a výsledkový protokol

### Ukládání Výsledků:
Lze přidat funkcionalitu pro:
- Záznam skóre pro jednotlivé týmy
- Export výsledků do CSV/Excel
- Tisknutelné výsledky

### Grafických Vylepšení:
- Animace při odhalení políček
- Zvukové efekty
- Více barevných motivů

## ⚠️ Troubleshooting

**Chyba "ModuleNotFoundError: No module named 'PIL'":**
```bash
pip install Pillow
```

**Obrázek se nenačítá:**
- Zkontrolujte, že je obrázek ve správném formátu (PNG, JPG, JPEG, BMP)
- Ověřte cestu k souboru
- Zkuste obrázek změnit

**Aplikace se neotevírá:**
- Zkontrolujte, že máte Python 3.7+
- Ověřte instalaci všech závislostí

## 📧 Autor

Vytvořeno pro projekt znalostní soutěže základních škol.

---

**Hodně štěstí v soutěži!** 🏆
