# 📱 Assistant Scolaire - PWA

Application web progressive (PWA) pour consulter facilement les horaires de bus et l'emploi du temps scolaire.

## ✨ Fonctionnalités

- 🚌 **Horaires de bus** : HAWK 3 et Ligne 2 avec calcul du prochain départ
- 📅 **Emploi du temps** : Planning hebdomadaire avec cours en cours mis en évidence
- 📱 **Installable** : Fonctionne comme une application native sur mobile
- 🔌 **Hors-ligne** : Accès aux données même sans connexion internet
- ⚡ **Rapide** : Chargement instantané grâce au cache
- 🎨 **Design moderne** : Interface sombre et intuitive optimisée pour mobile
- 🕐 **Simulateur de temps** : Pour tester l'application à différentes heures

## 🚀 Installation

### Déploiement sur GitHub Pages

Consultez le [Guide de Déploiement](GUIDE_DEPLOIEMENT.md) pour des instructions détaillées.

**Résumé rapide :**
1. Créez un dépôt GitHub public
2. Uploadez les fichiers : `index.html`, `manifest.json`, `sw.js`, et le dossier `icons/`
3. Activez GitHub Pages dans Settings > Pages
4. Accédez à votre site : `https://votre-username.github.io/assistant-scolaire/`

### Installation sur mobile

**Android (Chrome) :**
- Ouvrez l'URL dans Chrome
- Appuyez sur "Ajouter à l'écran d'accueil"

**iOS (Safari) :**
- Ouvrez l'URL dans Safari
- Appuyez sur Partager > "Sur l'écran d'accueil"

## 📁 Structure du projet

```
.
├── index.html              # Application principale
├── manifest.json           # Configuration PWA
├── sw.js                   # Service Worker (cache et hors-ligne)
├── icons/                  # Icônes de l'application
│   ├── icon-192.png
│   ├── icon-512.png
│   ├── icon-192.svg        # Source SVG
│   ├── generate_icon.html  # Générateur d'icônes
│   └── LISEZMOI.txt
├── GUIDE_DEPLOIEMENT.md    # Guide complet de déploiement
└── README.md               # Ce fichier
```

## 🔧 Personnalisation

### Modifier les horaires de bus

Éditez [`index.html`](index.html) et cherchez la section `BUS_DATA` (ligne ~326) :

```javascript
const BUS_DATA = {
    hawk3: {
        aller: {
            trips: [
                { dep: '07:55', arr: '08:05', days: [1,2,3,4,5] }
            ]
        },
        // ...
    }
};
```

### Modifier l'emploi du temps

Éditez [`index.html`](index.html) et cherchez la section `PLANNING` (ligne ~281) :

```javascript
const PLANNING = {
    1: [ // Lundi
        { start: '08:15', end: '09:10', subject: 'Mathématiques', room: 'Salle 201', color: 'blue' },
        // ...
    ]
};
```

### Personnaliser les icônes

1. Ouvrez `icons/generate_icon.html` dans votre navigateur
2. Téléchargez les icônes générées
3. Remplacez `icons/icon-192.png` et `icons/icon-512.png`

## 🎨 Technologies utilisées

- **HTML5** : Structure de l'application
- **Tailwind CSS** : Framework CSS pour le design
- **JavaScript Vanilla** : Logique de l'application (pas de framework)
- **PWA** : Service Worker pour le fonctionnement hors-ligne
- **GitHub Pages** : Hébergement gratuit

## 📊 Compatibilité

- ✅ Chrome/Edge (Android & Desktop)
- ✅ Safari (iOS & macOS)
- ✅ Firefox (Android & Desktop)
- ✅ Samsung Internet

## 🔄 Mises à jour

Pour mettre à jour l'application :

1. Modifiez `index.html` (horaires, emploi du temps, etc.)
2. Poussez les modifications vers GitHub
3. Les utilisateurs recevront automatiquement la mise à jour au prochain lancement

**Note :** Pensez à incrémenter la version dans `sw.js` (ligne 3) pour forcer la mise à jour du cache :

```javascript
const CACHE_VERSION = 'v1.0.1'; // Incrémenter ici
```

## 📝 Licence

Ce projet est libre d'utilisation pour un usage personnel et éducatif.

## 🤝 Contribution

Les suggestions et améliorations sont les bienvenues ! N'hésitez pas à créer une issue ou une pull request.

## 📞 Support

Pour toute question ou problème :
- Consultez le [Guide de Déploiement](GUIDE_DEPLOIEMENT.md)
- Vérifiez la section Dépannage
- Créez une issue sur GitHub

---

**Fait avec ❤️ pour faciliter le quotidien scolaire**
