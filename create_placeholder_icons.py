#!/usr/bin/env python3
"""Crée des icônes placeholder simples pour la PWA"""

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def create_icon(size, filename):
    """Crée une icône simple avec PIL"""
    # Créer une image avec fond vert
    img = Image.new('RGB', (size, size), color='#10b981')
    draw = ImageDraw.Draw(img)
    
    # Dessiner un cercle blanc au centre
    margin = size // 4
    draw.ellipse([margin, margin, size - margin, size - margin], 
                 fill='white', outline='#059669', width=size//20)
    
    # Dessiner les initiales "AS" (Assistant Scolaire)
    try:
        font_size = size // 3
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "AS"
    # Centrer le texte
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - size // 20
    
    draw.text((x, y), text, fill='#10b981', font=font)
    
    # Sauvegarder
    img.save(filename, 'PNG')
    print(f"✅ {filename} créé ({size}x{size})")

if __name__ == '__main__':
    if not PIL_AVAILABLE:
        print("❌ PIL/Pillow n'est pas installé")
        print("Installation: pip3 install Pillow")
        print("\nAlternative: Ouvrez icons/generate_icon.html dans votre navigateur")
        exit(1)
    
    create_icon(192, 'icons/icon-192.png')
    create_icon(512, 'icons/icon-512.png')
    print("\n✅ Icônes créées avec succès!")
    print("💡 Vous pouvez les remplacer avec icons/generate_icon.html pour un meilleur design")
