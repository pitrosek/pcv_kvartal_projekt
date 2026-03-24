# 🎯 Příručka pro Moderátory - Pexeso Soutěž

## Úvod

Tato příručka je určena pro osoby, které budou aplikaci Pexeso provozovat během znalostní soutěže na škole.

---

## Příprava Před Soutěží

### 1. Technická Příprava (1 den předem)

**Kontrolní seznam:**

- [ ] Počítač je připravený
- [ ] Python 3.7+ je nainstalován
- [ ] Pillow je nainstalován (`pip install Pillow`)
- [ ] Aplikace se spouští: `python main.py` ✅
- [ ] Testovací obrázky fungují
- [ ] Všechny herní obrázky jsou v `assets/` složce
- [ ] Všechny tajenky jsou správně napsané (bez překlepů)
- [ ] Displej je funkční a viditelný
- [ ] Projektování je nastaveno (je-li potřebné)

### 2. Příprava Obrázků

**Tipy pro výběr:**

1. **Vhodné obrázky:**
   - ✅ Jasné a čitelné fotografie
   - ✅ Populární tváře, loga nebo objekty
   - ✅ Vhodné pro věkovou kategorii
   - ✅ Edukační hodnota

2. **Nevhodné obrázky:**
   - ❌ Velmi tmavé nebo rozmazané
   - ❌ Příliš abstraktní
   - ❌ Příliš malé detaily
   - ❌ Ostudné nebo nevhodné obsahu

3. **Optimální velikost:**
   - Minimální: 300×300px
   - Doporučeno: 400×400px nebo větší
   - Formát: PNG nebo JPG (bez ztráty kvality)

### 3. Příprava Tajenek

**Jak napsat tajenku:**

- Jednoduché slovo: `PYTHON`, `MIKROSEKUND`
- Složitější: `ALBERT EINSTEIN`, `MICROSOFT WINDOWS` (s mezerami)
- Bez háčků/čárek (pokud je to možné, jinak je zadejte s diakritikou)
- **Vždy** zadejte VELKÝMI PÍSMENY

**Příklady správných tajenek:**
```
✅ PYTHON
✅ JAVA
✅ INTERNET
✅ ALBERT EINSTEIN
✅ MICROSOFT CORPORATION
```

**Příklady špatných tajenek:**
```
❌ python (malá písmena)
❌ Python (smíšené)
❌ *Python* (speciální znaky)
```

---

## Průběh Soutěž - Krok za Krokem

### Příprava Týmu (5 minut před kolem)

1. **Tým je připravený** u displeje
2. **Ověřit jména** členů týmu
3. **Vysvětlit pravidla:**
   - Počáteční body: **120**
   - Časový limit: **10 minut**
   - Každé odkrytí políčka stojí body
   - Chybná odpověď: **-20 bodů**
   - Cíl: Uhodnout tajenku s maximálním skórem

### Spuštění Kola (0 minut)

1. **Spustit aplikaci:**
   ```bash
   python main.py
   ```

2. **Kliknout** na "Načíst obrázek"

3. **Vybrat** obrázek pro toto kolo

4. **Zadat** správnou tajenku, když se zeptá

5. **Resetovat čas** (restart nebo pokračovat dle nastavení)

### Průběh Hry (0-10 minut)

**Úlohy týmu:**
- Klikat na políčka pro odhalení obrázku
- Používat nápovědy písmen (pokud je to dovoleno)
- Určit správnou odpověď
- Zadat odpověď přesně jak ji mají zapsanou

**Úlohy moderátora:**
- Sledovat čas
- Zaznamenávat průběh
- Zajistit férové hraní
- Pomoci s technickými problémy

### Konec Kola (10:00 nebo po správné odpovědi)

1. **Čas vypršel** → aplikace zobrazí finální skóre
2. **Správná odpověď** → skóre je uloženo
3. **Zaznamenat skóre** týmu
4. **Poděkovat** týmu
5. **Restartovat** na další kolo

---

## Bodový Systém - Vysvětlení

### Jak se počítají body:

```
START: 120 bodů
      ↓
Odkrytí 1. políčka: +0 bodů (ZDARMA)
Odkrytí 2. políčka: -1 bod
Odkrytí 3. políčka: -2 body
Odkrytí 4. políčka: -3 body
... (pokračuje dál)
      ↓
Nápověda 1. písmene: +0 bodů (ZDARMA)
Nápověda 2. písmene: -1 bod
... (stejně jako politčka)
      ↓
NEBO
      ↓
Špatná odpověď: -20 bodů (a pokračuje se v hraje)
Správná odpověď: Finální skóre (hra končí)
```

### Příklad Výpočtu:

```
Tým: Superhrači
Počáteční body: 120

Akce 1: Odkrytí 1. políčka
  Cena: 0 (je to prvně)
  Nový skór: 120 + 0 = 120 bodů

Akce 2: Odkrytí 2. políčka
  Cena: -1
  Nový skór: 120 - 1 = 119 bodů

Akce 3: Odkrytí 3. políčka
  Cena: -2
  Nový skór: 119 - 2 = 117 bodů

Akce 4: Nápověda 1. písmene
  Cena: 0 (je to prvně)
  Nový skór: 117 + 0 = 117 bodů

Akce 5: Nápověda 2. písmene
  Cena: -1
  Nový skór: 117 - 1 = 116 bodů

Akce 6: Tým zadá špatnou odpověď
  Cena: -20
  Nový skór: 116 - 20 = 96 bodů

Akce 7: Tým zadá správnou odpověď
  HRA KONČÍ!
  FINÁLNÍ SKÓRE: 96 bodů
```

---

## Kontrolní Seznamy

### Před Soutěží (Den Před)

- [ ] Aplikace je spuštěná a funguje
- [ ] Všechny obrázky jsou v `assets/`
- [ ] Všechny tajenky jsou připravené (bez překlepů)
- [ ] Displej/projektor je funkční
- [ ] Zvuk je vhodně nastavený (pokud se používá)
- [ ] Časovač je synchronizovaný
- [ ] Záloha obrázků je na USB disku
- [ ] Tým obsluhy je zaškolený

### Před Každým Kolem (5 minut)

- [ ] Počítač je zapnutý a aplikace je připravená
- [ ] Displej je viditelný všem soutěžícím
- [ ] Obrázek je v `assets/` složce
- [ ] Tajenka je znám moderátorovi
- [ ] Tým je přítomný a připravený
- [ ] Časomíra je na místě (hodiny, časovač)
- [ ] Protokol je připravený pro záznam skóre

### Během Kola (10 minut)

- [ ] Čas se měří
- [ ] Tým je aktivní
- [ ] Odpovědi se zaznamenávají
- [ ] Technické problémy se řeší
- [ ] Pravidla se dodržují

### Po Kole

- [ ] Finální skóre je zaznamenáno
- [ ] Výsledek je zveřejněn
- [ ] Aplikace je restartovaná
- [ ] Nový obrázek je vybraný
- [ ] Další tým je připravený

---

## Řešení Běžných Problémů

### ❌ Aplikace se nespuští

```bash
# Zkuste:
python main.py

# Pokud to nefunguje:
python -m pip install --upgrade Pillow
python main.py
```

### ❌ Obrázek se nenačítá

1. Zkontrolujte, že soubor je v `assets/` složce
2. Ověřte, že má správný formát (.png, .jpg, .jpeg, .bmp)
3. Zkuste použít testovací obrázek
4. Přejmenujte soubor (bez mezer, bez speciálních znaků)

### ❌ Čas není správný

Aplikace počítá čas od spuštění kola. Pokud chcete jiný čas:
- Upravte `game_time_seconds` v `config/game_config.py`
- Výchozí: 600 (10 minut) = 600 sekund
- Příklady: 300 = 5 minut, 900 = 15 minut

### ❌ Tým tvrdí, že zadal správně, ale aplikace říká, že je to špatně

1. **Zkontrolujte tajenku** v `config/game_config.py` - jsou tam háčky?
2. **Zkontrolujte vstup** - měl by být bez háčků, jako byste to napsali anglicky
3. **Porovnávejte velká a malá písmena** - aplikace je senzitivní
4. Pokud je chyba v aplikaci, můžete:
   - Restartovat aplikaci
   - Ručně přidat body (po dohodě s ostatními týmy)

### ❌ Během hry vypadla elektrika

1. Aplikace si pamatuje body a čas od spuštění
2. Budete muset restart kola
3. Ručně si poznamenejte skóre, než restartujete
4. Lze přidat body ručně jako bonus (po dohodě)

---

## Moderování - Tipy a Triky

### Jak být spravedlivý:

1. **Všem týmům stejné časy** (10 minut přesně)
2. **Stejná pravidla** pro všechny
3. **Neukazujte tajenku** dříve, než je čas
4. **Zapisujte vše** pro třídění při reklamacích
5. **Buďte neutrální** - nefavorizujte žádný tým

### Jak motivovat:

1. **Chvalte snahu** - "Dobrý pokus!"
2. **Ukažte průběh** - "Máte ještě 3 minuty"
3. **Povzbuzujte** - "Jste na správné cestě"
4. **Berte zájem** - poslouchejte jejich strategie

### Jak zajistit bezpečnost dat:

1. **Chraňte tajenky** - neukazujte je ostatním
2. **Chraňte skóre** - pište je viditelně všem
3. **Zálohujte** - uložte si výsledky na USB
4. **Kontrolujte čas** - nekontrolujte počítač během hry

---

## Nastavení Těžkosti

### Lehké (pro mladší žáky):
```python
GAME_CONFIG = {
    "starting_points": 150,      # Více bodů
    "wrong_answer_penalty": 10,  # Menší trest
}
```

### Střední (doporučeno):
```python
GAME_CONFIG = {
    "starting_points": 120,      # Default
    "wrong_answer_penalty": 20,  # Default
}
```

### Těžké (pro pokročilé):
```python
GAME_CONFIG = {
    "starting_points": 80,       # Méně bodů
    "wrong_answer_penalty": 25,  # Větší trest
    "game_time_seconds": 300,    # Jen 5 minut
}
```

---

## FAQ - Často Kladené Otázky

**Jak přidám své obrázky?**
- Umístěte je do složky `assets/` a vyberte v aplikaci

**Mohu měnit počet bodů?**
- Ano, v `config/game_config.py`

**Co když se vzdá tým?**
- Hra se ukončí, zapíšete si skóre

**Jak dlouho trvá jedno kolo?**
- Standardně 10 minut + administrativní čas

**Mohu měnit čas?**
- Ano, změňte `game_time_seconds` v konfiguraci

---

## Záznam Výsledků

### Format Protokolu:

```
ZNALOSTNÍ SOUTĚŽ PEXESO - 2026

Kolo: 1
Obrázek: Albert Einstein
Tajenka: ALBERT EINSTEIN

|----|----------|-----------|------------|
| # | Tým      | Politčka | Nápovědy | Finální |
|----|----------|-----------|------------|
| 1 | Tým A    | 5        | 2        | 114    |
| 2 | Tým B    | 3        | 1        | 117    |
| 3 | Tým C    | 4        | 3        | 110    |
|----|----------|-----------|------------|

Vítězný tým tohoto kola: Tým B (117 bodů)
```

---

## Přílohy

### Tajenky pro Inspiraci:

**IT Osobnosti:**
- ALAN TURING
- GRACE HOPPER
- STEVE JOBS
- BILL GATES
- LINUS TORVALDS

**IT Firmy:**
- MICROSOFT
- APPLE
- GOOGLE
- FACEBOOK
- AMAZON

**Technologie:**
- INTERNET
- JAVASCRIPT
- DATABASE
- ALGORITMUS
- PROGRAMOVANI

---

## Závěrečné Rady

1. **Buďte připravení** - předem si vyzkoušejte všechno
2. **Buďte flexibilní** - věci se mohou pokazit, improvizujte
3. **Buďte spravedliví** - všechny týmy stejně
4. **Buďte pozitivní** - soutěž má být zábavná!
5. **Buďte techniky** - znáte počítač lépe než ostatní

---

## Kontakt a Podpora

Máte-li otázky k aplikaci:
1. Přečtěte si README.md
2. Zkontrolujte ARCHITECTURE.md
3. Podívejte se na SCENARIOS.md pro příklady

---

Hodně štěstí s moderováním! 🎯

Poslední aktualizace: 2026-03-24
