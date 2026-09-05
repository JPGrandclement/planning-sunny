# 🚀 Guide de Déploiement - Assistant Scolaire PWA

Ce guide vous explique comment déployer l'Assistant Scolaire sur GitHub Pages pour que votre fils puisse y accéder facilement depuis son téléphone.

## 📋 Prérequis

- Un compte GitHub (gratuit) : https://github.com/signup
- Git installé sur votre ordinateur

## 🎯 Étape 1 : Créer un dépôt GitHub

1. **Connectez-vous à GitHub** : https://github.com
2. **Créez un nouveau dépôt** :
   - Cliquez sur le bouton `+` en haut à droite > `New repository`
   - Nom du dépôt : `assistant-scolaire` (ou un autre nom de votre choix)
   - Description : "Assistant scolaire pour horaires de bus et emploi du temps"
   - Visibilité : **Public** (obligatoire pour GitHub Pages gratuit)
   - ✅ Cochez "Add a README file"
   - Cliquez sur `Create repository`

## 📤 Étape 2 : Pousser les fichiers vers GitHub

### Option A : Via l'interface web GitHub (plus simple)

1. Dans votre dépôt GitHub, cliquez sur `Add file` > `Upload files`
2. Glissez-déposez ces fichiers :
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - Le dossier `icons/` (avec icon-192.png et icon-512.png)
3. Ajoutez un message de commit : "Ajout de l'Assistant Scolaire PWA"
4. Cliquez sur `Commit changes`

### Option B : Via la ligne de commande (plus rapide)

```bash
# Dans le dossier de votre projet
cd /Users/jean-patrick.grandclement/workspace/perso/planning-sunny

# Initialiser Git (si pas déjà fait)
git init

# Ajouter les fichiers nécessaires
git add index.html manifest.json sw.js icons/

# Créer un commit
git commit -m "Ajout de l'Assistant Scolaire PWA"

# Lier au dépôt GitHub (remplacez VOTRE-USERNAME par votre nom d'utilisateur)
git remote add origin https://github.com/VOTRE-USERNAME/assistant-scolaire.git

# Pousser vers GitHub
git branch -M main
git push -u origin main
```

## 🌐 Étape 3 : Activer GitHub Pages

1. Dans votre dépôt GitHub, allez dans `Settings` (⚙️)
2. Dans le menu de gauche, cliquez sur `Pages`
3. Sous "Source", sélectionnez :
   - Branch : `main`
   - Folder : `/ (root)`
4. Cliquez sur `Save`
5. **Attendez 1-2 minutes** que le site soit déployé
6. L'URL de votre site apparaîtra en haut : `https://VOTRE-USERNAME.github.io/assistant-scolaire/`

## 📱 Étape 4 : Installer l'application sur le téléphone

### Sur Android (Chrome)

1. Ouvrez Chrome sur le téléphone
2. Allez sur l'URL : `https://VOTRE-USERNAME.github.io/assistant-scolaire/`
3. Attendez que la page se charge complètement
4. Un popup apparaîtra : "Ajouter Assistant Scolaire à l'écran d'accueil"
   - Si le popup n'apparaît pas : Menu (⋮) > "Ajouter à l'écran d'accueil"
5. Confirmez l'installation
6. L'icône "Mon Assistant" apparaît sur l'écran d'accueil ✅

### Sur iPhone/iPad (Safari)

1. Ouvrez Safari sur l'iPhone
2. Allez sur l'URL : `https://VOTRE-USERNAME.github.io/assistant-scolaire/`
3. Appuyez sur le bouton Partager (□↑)
4. Faites défiler et sélectionnez "Sur l'écran d'accueil"
5. Modifiez le nom si nécessaire : "Mon Assistant"
6. Appuyez sur "Ajouter"
7. L'icône apparaît sur l'écran d'accueil ✅

## 🔄 Étape 5 : Mettre à jour l'application

Quand vous modifiez les horaires ou l'emploi du temps :

### Via l'interface web GitHub

1. Allez sur votre dépôt GitHub
2. Cliquez sur `index.html`
3. Cliquez sur l'icône crayon (✏️) pour éditer
4. Modifiez les données (horaires de bus, emploi du temps)
5. Cliquez sur `Commit changes`
6. Les modifications seront en ligne en 1-2 minutes

### Via la ligne de commande

```bash
# Modifiez index.html localement
# Puis :
git add index.html
git commit -m "Mise à jour des horaires"
git push
```

### Sur le téléphone

- L'application se mettra à jour automatiquement au prochain lancement
- Ou fermez complètement l'app et relancez-la

## 🎨 Personnaliser les icônes (optionnel)

Si vous souhaitez améliorer les icônes :

1. Ouvrez `icons/generate_icon.html` dans votre navigateur
2. Téléchargez les nouvelles icônes générées
3. Remplacez `icons/icon-192.png` et `icons/icon-512.png`
4. Poussez les modifications vers GitHub

## ✅ Vérification

Pour vérifier que tout fonctionne :

1. ✅ L'URL est accessible : `https://VOTRE-USERNAME.github.io/assistant-scolaire/`
2. ✅ L'application s'affiche correctement sur mobile
3. ✅ Le bouton "Installer" apparaît (ou dans le menu)
4. ✅ Après installation, l'icône est sur l'écran d'accueil
5. ✅ L'application fonctionne hors-ligne après la première visite

## 🔧 Dépannage

### Le site ne s'affiche pas

- Vérifiez que GitHub Pages est activé dans Settings > Pages
- Attendez 2-3 minutes après l'activation
- Vérifiez que le dépôt est public

### L'installation PWA ne fonctionne pas

- Vérifiez que vous utilisez HTTPS (GitHub Pages le fait automatiquement)
- Sur iOS, utilisez Safari (pas Chrome)
- Videz le cache du navigateur et réessayez

### Les modifications ne s'affichent pas

- Videz le cache du navigateur : Ctrl+Shift+R (ou Cmd+Shift+R sur Mac)
- Sur mobile, fermez complètement l'app et relancez-la
- Attendez quelques minutes que GitHub Pages se mette à jour

## 📞 Partager l'application

Pour partager l'URL avec votre fils :

1. **SMS/WhatsApp** : Envoyez simplement l'URL
2. **QR Code** : Générez un QR code sur https://www.qr-code-generator.com/
3. **Raccourci** : Créez un raccourci avec https://bit.ly/ pour une URL plus courte

## 🎯 Résultat final

Votre fils aura :
- 📱 Une icône "Mon Assistant" sur son écran d'accueil
- ⚡ Accès instantané à ses horaires de bus et emploi du temps
- 🔌 Fonctionnement hors-ligne après la première visite
- 🔄 Mises à jour automatiques quand vous modifiez les données
- 🎨 Une interface moderne et facile à utiliser

## 💡 Conseils

- **Marque-page** : Ajoutez l'URL dans les favoris du navigateur
- **Widget** : Sur Android, vous pouvez créer un widget de raccourci
- **Notifications** : L'app peut être étendue pour envoyer des notifications (fonctionnalité avancée)

## 📚 Ressources supplémentaires

- Documentation GitHub Pages : https://pages.github.com/
- Documentation PWA : https://web.dev/progressive-web-apps/
- Tester votre PWA : https://www.pwabuilder.com/

---

**Besoin d'aide ?** Consultez la documentation GitHub ou créez une issue sur le dépôt.
