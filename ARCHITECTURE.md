# 📘 Dokumentace - Architektura Aplikace

## Přehled Struktury

```
pexeso_vitek/
├── main.py                      # ⭐ Hlavní aplikace (Tkinter)
├── config/
│   ├── __init__.py             # Python package marker
│   └── game_config.py          # ⚙️ Konfigurační parametry hry
├── assets/                     # 🖼️ Složka pro obrázky
│   └── (uživatelské obrázky)
├── requirements.txt            # 📦 Python závislosti
├── run.bat                     # ▶️ Spouštěč (Windows)
├── run.sh                      # ▶️ Spouštěč (Linux/Mac)
├── README.md                   # 📖 Hlavní dokumentace
├── QUICKSTART.md              # 🚀 Rychlý start
├── SCENARIOS.md               # 📝 Příklady her
└── ARCHITECTURE.md            # 📘 Tento soubor
```

---

## Komponenty Aplikace

### 1. **GameState** (Třída)
Spravuje stav hry během hraní.

**Atributy:**
- `points`: Aktuální počet bodů (int)
- `grid_size`: Velikost mřížky, defaultně 4 (int)
- `total_cells`: Celkový počet políček (16 pro 4×4)
- `revealed_cells`: Set odhalených políček (set)
- `revealed_letters`: Set odhalených písmen tajenky (set)
- `start_time`: Čas startu hry (float)
- `game_active`: Je hra aktivní? (bool)
- `answer`: Aktuální vstup uživatele (string)
- `game_answer`: Správná tajenka (string)

**Metody:**
- `reset()`: Reset stavu na začátek

---

### 2. **ImageProcessor** (Třída)
Zpracovává obrázky a dělí je do mřížky.

**Atributy:**
- `image_path`: Cesta k obrázku (string)
- `grid_size`: Velikost mřížky (int)
- `tiles`: Lista dílků obrázku (list)
- `original_image`: Celý obrázek (PIL Image)

**Metody:**
- `load_and_process_image()`: Načtení a zpracování
- `divide_image()`: Rozdělení na mřížku
- `get_tile(index)`: Získání konkrétního dílku
- `get_full_image_photo()`: Vrátí celý obrázek jako PhotoImage

---

### 3. **QuizApplication** (Hlavní Třída)
Hlavní aplikace s Tkinter GUI.

**Atributy:**
- `root`: Tkinter root window
- `game_state`: Instance GameState
- `image_processor`: Instance ImageProcessor
- `photo_tiles`: Cache PhotoImage objektů

**Hlavní Metody:**
- `setup_ui()`: Vytvoření uživatelského rozhraní
- `load_image()`: Načtení obrázku ze souboru
- `reveal_cell(index)`: Odhalení políčka
- `hint_letter(index)`: Nápověda pro písmeno
- `submit_answer()`: Odeslání odpovědi
- `update_ui()`: Refresh UI
- `update_letter_display()`: Aktualizace zobrazení písmen
- `update_timer()`: Aktualizace časovače

---

## Tok Hry

```
START
  ↓
[Načtení Obrázku]
  ↓
[Zadání Tajenky]
  ↓
[Inicializace GameState: 120 bodů, čas 10:00]
  ↓
┌─ HERNÍ SMYČKA ──────────────────────┐
│                                     │
│ Čeká na akci hráče:                 │
│  • Kliknutí na políčko → odhalení  │
│  • Kliknutí na nápovědu → písmeno  │
│  • Zadání odpovědi → check          │
│                                     │
│ Aktualizuje:                        │
│  • Body                             │
│  • UI                               │
│  • Čas                              │
│                                     │
└─────────────────────────────────────┘
  ↓
[Vypršel čas NEBO správná odpověď]
  ↓
[Zobrazení Finálního Skóre]
  ↓
END
```

---

## Bodová Systémy

### Funkcí: `get_reveal_cost(cell_number)`
```python
Politčko 1: 0 bodů    (zdarma)
Politčko 2: -1 bod
Politčko 3: -2 body
Politčko 4: -3 body
Politčko N: -(N-1) bodů
```

Lze upravit v `config/game_config.py`.

### Funkcí: `get_letter_hint_cost(letter_number)`
Funguje stejně jako reveal cost.

---

## Barevný Motiv a Fonty

Definovány v `config/game_config.py`:

```python
COLORS = {
    "bg_main": "#2C3E50",          # Tmavá modř (pozadí)
    "bg_light": "#34495E",         # Světlejší modř
    "fg_text": "#ECF0F1",          # Bílý text
    "button_bg": "#3498DB",        # Modrá tlačítka
    "button_hover": "#2980B9",     # Tmavší modrá (hover)
    "points_color": "#F39C12",     # Zlatá (body)
    "error_color": "#E74C3C",      # Červená (chyba/čas)
    "success_color": "#27AE60",    # Zelená (úspěch)
}

FONTS = {
    "title": ("Arial", 28, "bold"),
    "large": ("Arial", 20, "bold"),
    "medium": ("Arial", 14, "normal"),
    "small": ("Arial", 10, "normal"),
}
```

Jednoduché jsou pro okamžitou personalizaci.

---

## Customizace a Rozšíření

### 1. Změna Bodů
```python
# config/game_config.py
GAME_CONFIG = {
    "starting_points": 150,  # Zvýšit počáteční body
    "wrong_answer_penalty": 30,  # Zvýšit penalizaci
}
```

### 2. Změna Času
```python
GAME_CONFIG = {
    "game_time_seconds": 300,  # 5 minut namísto 10
}
```

### 3. Vlastní Barvy
```python
COLORS = {
    "bg_main": "#1a1a1a",      # Tmavě šedá
    "button_bg": "#FF6B6B",    # Červená
    # ... ostatní barvy
}
```

### 4. Přidání Nové Funkce

Chcete přidat novou funkci? Například:
- Zvěs efekty
- Animace
- Statistiku

Editujte `main.py` a přidejte nové metody do třídy `QuizApplication`.

---

## Vývojové Poznámky

### Známé Omezení:
1. **Velikost obrázku:** Fixní 400×400px
   - Lze změnit v `ImageProcessor.load_and_process_image()`
   
2. **Max. délka tajenky:** 20 znaků
   - Lze změnit v `setup_ui()` kde je `for i in range(20)`

3. **Max. výška okna:** Fixně nastavena na 800px
   - Lze měnit v `__init__()` geometrie

### Co lze Zlepšit:
- [ ] Přidat persistenci (uložení her)
- [ ] Přidat zvuk
- [ ] Přidat statistiky
- [ ] Responsive design
- [ ] Dark/Light tema
- [ ] Vícejázykový systém

---

## Python Verze a Kompatibilita

- **Požadovaná:** Python 3.7+
- **Testováno na:** Python 3.8, 3.9, 3.10, 3.11
- **Tkinter:** Obvykle součást Python instalace
- **Pillow:** Musí se instalovat (`pip install Pillow`)

### Kompatibilita OS:
- ✅ Windows 7+ 
- ✅ Linux (všechny distribuce)
- ✅ macOS 10.12+

---

## Bezpečnost a Ochrana

Funkce ochrany proti odhalení odpovědi:

1. **Skrytá tajenka:** Písmena se zobrazují postupně
2. **Jednotlivé nápovědy:** Lze odhalovat jen jedno písmeno najednou
3. **Penalty za chybu:** Motivuje pečlivé hádání
4. **Časový limit:** Nedostatek času pro brutální prohledávání

---

## Ladění (Debugging)

Chcete-li ladění, přidejte do `main.py`:

```python
# Na začátek main.py
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# V relevantních místech:
logger.debug(f"Body: {self.game_state.points}")
logger.debug(f"Odhalená políčka: {self.game_state.revealed_cells}")
```

---

## Kontakt a Podpora

Pro otázky nebo problémy se obraťte na správce projektu.

---

Poslední aktualizace: 2026-03-24
