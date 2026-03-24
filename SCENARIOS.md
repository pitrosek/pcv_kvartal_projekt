# Příklady scénářů pro hru

## Příklad 1 - IT Osobnosti

**Obrázek:** Albert Einstein
**Tajenka:** ALBERT EINSTEIN
**Cílová skupiny:** Třídy 8-9 (základní znalost slavných vědců)

---

## Příklad 2 - IT Firmy a Loga

**Obrázek:** Logo Microsoftu
**Tajenka:** MICROSOFT
**Cílová skupiny:** Třídy 7-9 (znalost velkých IT firem)

---

## Příklad 3 - Historické Fotografie

**Obrázek:** První počítač ENIAC
**Tajenka:** ENIAC
**Cílové skupiny:** Třídy 8-9 (dějiny informatiky)

---

## Příklad 4 - IT Vynálezy a Zařízení

**Obrázek:** První mobilní telefon
**Tajenka:** MOBIL
**Cílové skupiny:** Třídy 6-7 (základní IT pojmy)

---

## Tipsy na Přípravy Obrázků

### Co je dobré vybrat:
- ✅ Jasné, rozpoznatelné obrázky
- ✅ Obrázky s dobrým kontrastem
- ✅ Fotografie slavných osobností
- ✅ Dobře viditelná loga
- ✅ Historické fotografie IT zařízení

### Co být ostrý:
- ❌ Příliš tmavé nebo rozmazané obrázky
- ❌ Příliš abstrakt
- ❌ Malé detaily
- ❌ Nejasné či rozmazané prvky

### Ideální velikost obrázku:
- Doporučujeme: **400×400px nebo větší**
- Formát: Čtvercový je nejlepší
- Kvalita: JPEG nebo PNG (bez ztrát)

---

## Systém Bodování - Příklady

### Scénář 1: Základní Bodování
```
Počáteční body: 120
Odvykrytí 1. políčka: 0 bodů (zdarma)
Odvykrytí 2. políčka: -1 bod
Odvykrytí 3. políčka: -2 body
Odvykrytí 4. políčka: -3 body
...
Chybná odpověď: -20 bodů

Příklad hry:
- Start: 120 bodů
- Odkryj 5 políček: 120 + 0 - 1 - 2 - 3 - 4 = 110 bodů
- Odhalil 3 písmena: 110 - 0 - 1 - 2 = 107 bodů
- Špatná odpověď: 107 - 20 = 87 bodů
- Správná odpověď: 87 bodů (finální skóre)
```

### Scénář 2: Agresivnější Bodování
```
Počáteční body: 100
Cena za políčko: -2, -4, -6, -8... (násobek 2)
Cena za písmeno: -3, -6, -9, -12...
Chybná odpověď: -30 bodů
```

### Scénář 3: Tolerantnější Bodování
```
Počáteční body: 150
Cena za políčko: 0, -1, -1, -2, -2, -3...
Cena za písmeno: 0, -1, -1, -2...
Chybná odpověď: -15 bodů
```

---

## Časy her - Doporučení

- **Lehká hra (základní škola 1. stupeň):** 15 minut
- **Normální hra (základní škola 2. stupeň):** 10 minut
- **Obtížná hra (nadaní žáci, střední škola):** 5 minut
- **Bleskový kolo (finále):** 3 minuty

---

## Modifikace Pravidel

### Variantu A: Bez Penalizace za Písmena
Písmena se odhalují zdarma, pouze politčka obrázku mají cenu.

### Varianta B: Cena pouze za Chyby
Odvykrytí je zdarma, penalty pouze za špatné odpovědi (-30 bodů).

### Varianta C: Bonusy za Rychlost
Pokud tým uhodne do určitého času (např. 2 minut), dostane bonus bodů.

---

## Přípravný Checklist

- [ ] Obrázky připravены a uloženy v `assets/` složce
- [ ] Testováno načtení každého obrázku
- [ ] Tajenky jsou správné a bez překlepů
- [ ] Časy v `config/game_config.py` jsou nastaveny správně
- [ ] Zkontrolován systém bodů
- [ ] Aplikace byla spuštěna a otestována
- [ ] Připraveny tipy obsluhy pro moderátora
- [ ] Zaškoleni všichni operátoři aplikace

---

## Tipy pro Obsluhu během Soutěže

1. **Příprava:**
   - Aplikaci spusťte s dostatečným předstihem
   - Otestujte načtení prvního obrázku
   - Zkontrolujte zvuk a viditelnost displeje

2. **Během hry:**
   - Nechte tým aby si sám klikal na políčka
   - Buďte neutrální k nápověděm
   - Zaznamenávejte časy

3. **Konec hry:**
   - Automaticky se zobrazí finální skóre
   - Zapište si skóre všech týmů
   - Připravte další kolo s novým obrázkem

---

## Inspirace pro Témata

- 💻 **Informatika:** Osobnosti (Tim Berners-Lee, Ada Lovelace, Steve Jobs)
- 🌐 **Internet:** Loga služeb (Google, Facebook, YouTube)
- 📱 **Mobilní technologie:** Ikonické telefony/zařízení
- 🎮 **Herní průmysl:** Konzole a herní postavy
- 🔬 **Věda a IT:** Vědecké objevy (DNA, prvky tabulky)
- 🇨🇿 **Česká IT:** Čeští vědci a informatici
- 🏢 **Byznysu:** Známé firmy a jejich zakladatelé

---

Hodně štěstí! 🎉
