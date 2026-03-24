"""
Demo skript pro generování testovacího obrázku
Vytvoří jednoduchou testovací image pro vyzkoušení aplikace
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_image():
    """Vytvoří jednoduchý testovací obrázek"""
    
    # Vytvoření složky assets, pokud neexistuje
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    # Vytvoření jednoduchého obrázku
    # Barvy
    bg_color = (70, 130, 180)  # Modrá
    text_color = (255, 255, 255)  # Bílá
    
    # Vytvoření obrázku
    img = Image.new('RGB', (400, 400), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Pokus na použití fontu
    try:
        # Pokusy různých fontů
        font_paths = [
            "C:\\Windows\\Fonts\\arial.ttf",  # Windows
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
            "/Library/Fonts/Arial.ttf"  # macOS
        ]
        
        font = None
        for path in font_paths:
            if os.path.exists(path):
                font = ImageFont.truetype(path, 60)
                break
        
        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Kreslení textu (TEST IMAGE)
    text = "TEST"
    # Výpočet pozice pro centrování
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (400 - text_width) // 2
    y = (400 - text_height) // 2
    
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Kreslení ohraničení
    draw.rectangle([(10, 10), (390, 390)], outline=(255, 165, 0), width=3)
    
    # Uložení obrázku
    output_path = "assets/test_image.png"
    img.save(output_path)
    print(f"✅ Testovací obrázek vytvořen: {output_path}")
    print(f"   Velikost: 400×400px")
    print(f"   Tajenka: PYTHON")
    return output_path

def create_colored_blocks_image():
    """Vytvoří obrázek s barevnými bloky"""
    
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    # Vytvoření obrázku s barevnými bloky
    img = Image.new('RGB', (400, 400), color=(255, 255, 255))
    pixels = img.load()
    
    # Vytvoření čtverce barevných bloků
    block_size = 100
    colors = [
        (255, 0, 0),      # Červená
        (0, 255, 0),      # Zelená
        (0, 0, 255),      # Modrá
        (255, 255, 0),    # Žlutá
        (255, 0, 255),    # Magenta
        (0, 255, 255),    # Cyan
        (255, 128, 0),    # Oranžová
        (128, 0, 255),    # Fialová
        (255, 128, 128),  # Světlá červená
        (128, 255, 128),  # Světlá zelená
        (128, 128, 255),  # Světlá modrá
        (255, 255, 128),  # Světlá žlutá
        (192, 192, 192),  # Šedá
        (255, 192, 203),  # Růžová
        (165, 42, 42),    # Hnědá
        (0, 128, 128),    # Tyrkysová
    ]
    
    # Vykreslení bloků
    color_idx = 0
    for y in range(0, 400, block_size):
        for x in range(0, 400, block_size):
            color = colors[color_idx % len(colors)]
            for py in range(y, y + block_size):
                for px in range(x, x + block_size):
                    pixels[px, py] = color
            color_idx += 1
    
    # Uložení
    output_path = "assets/colors_image.png"
    img.save(output_path)
    print(f"✅ Barevný obrázek vytvořen: {output_path}")
    print(f"   Velikost: 400×400px")
    print(f"   Tajenka: BARVY")
    return output_path

def create_gradient_image():
    """Vytvoří obrázek s přechodem"""
    
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    img = Image.new('RGB', (400, 400))
    pixels = img.load()
    
    # Vytvoření gradientu
    for y in range(400):
        for x in range(400):
            # Přechod z modré do červené
            r = int((x / 400) * 255)
            g = int((y / 400) * 255)
            b = 200
            pixels[x, y] = (r, g, b)
    
    output_path = "assets/gradient_image.png"
    img.save(output_path)
    print(f"✅ Gradientní obrázek vytvořen: {output_path}")
    print(f"   Velikost: 400×400px")
    print(f"   Tajenka: GRADIENT")
    return output_path

if __name__ == "__main__":
    print("=" * 50)
    print("  Generátor Testovacích Obrázků")
    print("=" * 50)
    print()
    
    print("Vytvářím testovací obrázky...")
    print()
    
    create_sample_image()
    create_colored_blocks_image()
    create_gradient_image()
    
    print()
    print("=" * 50)
    print("✅ Všechny testovací obrázky byly vytvořeny!")
    print()
    print("Nyní můžete spustit:")
    print("  python main.py")
    print()
    print("A vybrat jeden z obrázků ze složky 'assets'")
    print("=" * 50)
