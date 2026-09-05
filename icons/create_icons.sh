#!/bin/bash
# Script pour créer des icônes placeholder simples

# Créer une icône 192x192 avec sips (outil macOS natif)
sips -s format png --resampleHeightWidth 192 192 icons/icon-192.svg --out icons/icon-192.png 2>/dev/null

# Créer une icône 512x512
sips -s format png --resampleHeightWidth 512 512 icons/icon-192.svg --out icons/icon-512.png 2>/dev/null

if [ -f "icons/icon-192.png" ] && [ -f "icons/icon-512.png" ]; then
    echo "✅ Icônes créées avec succès!"
else
    echo "⚠️  sips n'a pas pu convertir le SVG"
    echo "📋 Veuillez ouvrir icons/generate_icon.html dans votre navigateur"
    echo "    et télécharger les icônes manuellement"
fi
