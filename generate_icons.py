#!/usr/bin/env python3
"""
Script pour générer les icônes PNG de l'application PWA
Utilise cairosvg si disponible, sinon crée des instructions
"""

import os
import sys

try:
    import cairosvg
    CAIROSVG_AVAILABLE = True
except ImportError:
    CAIROSVG_AVAILABLE = False

def generate_icons():
    """Génère les icônes PNG à partir du SVG"""
    
    svg_file = 'icons/icon-192.svg'
    
    if not os.path.exists(svg_file):
        print(f"❌ Erreur: Le fichier {svg_file} n'existe pas")
        return False
    
    if CAIROSVG_AVAILABLE:
        print("✅ cairosvg détecté, génération des icônes...")
        
        # Générer icon-192.png
        cairosvg.svg2png(
            url=svg_file,
            write_to='icons/icon-192.png',
            output_width=192,
            output_height=192
        )
        print("✅ icons/icon-192.png créé")
        
        # Générer icon-512.png
        cairosvg.svg2png(
            url=svg_file,
            write_to='icons/icon-512.png',
            output_width=512,
            output_height=512
        )
        print("✅ icons/icon-512.png créé")
        
        return True
    else:
        print("\n⚠️  cairosvg n'est pas installé")
        print("\n📋 Options pour générer les icônes PNG :\n")
        print("Option 1 - Installer cairosvg (recommandé):")
        print("  pip3 install cairosvg")
        print("  python3 generate_icons.py")
        print("\nOption 2 - Utiliser un service en ligne:")
        print("  1. Ouvrir icons/icon-192.svg dans un navigateur")
        print("  2. Faire une capture d'écran ou utiliser https://cloudconvert.com/svg-to-png")
        print("  3. Créer icon-192.png (192x192) et icon-512.png (512x512)")
        print("  4. Placer les fichiers dans le dossier icons/")
        print("\nOption 3 - Utiliser Inkscape (si installé):")
        print("  inkscape icons/icon-192.svg --export-type=png --export-filename=icons/icon-192.png -w 192 -h 192")
        print("  inkscape icons/icon-192.svg --export-type=png --export-filename=icons/icon-512.png -w 512 -h 512")
        print("\nOption 4 - Utiliser ImageMagick (si installé):")
        print("  convert -background none -resize 192x192 icons/icon-192.svg icons/icon-192.png")
        print("  convert -background none -resize 512x512 icons/icon-192.svg icons/icon-512.png")
        
        return False

if __name__ == '__main__':
    success = generate_icons()
    sys.exit(0 if success else 1)
