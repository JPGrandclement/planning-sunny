# ✅ Checklist de Déploiement

Utilisez cette checklist pour vous assurer que tout est prêt avant le déploiement.

## 📋 Avant le déploiement

### Fichiers essentiels

- [ ] `index.html` existe et contient le code de l'application
- [ ] `manifest.json` existe avec les bonnes informations
- [ ] `sw.js` existe (Service Worker)
- [ ] `icons/icon-192.png` existe
- [ ] `icons/icon-512.png` existe

### Vérifications dans index.html

- [ ] Les liens vers `manifest.json` sont corrects (ligne ~14)
- [ ] Les liens vers les icônes sont corrects (lignes ~17-19)
- [ ] Le script d'enregistrement du Service Worker est présent (fin du fichier)
- [ ] Les horaires de bus sont à jour
- [ ] L'emploi du temps est à jour

### Vérifications dans manifest.json

- [ ] Le nom de l'application est correct
- [ ] Les chemins des icônes sont corrects (`./icons/icon-192.png`)
- [ ] La couleur du thème est définie (`#10b981`)

### Vérifications dans sw.js

- [ ] La version du cache est définie (`CACHE_VERSION`)
- [ ] Les URLs à mettre en cache sont listées
- [ ] Le chemin vers `index.html` est correct

## 🚀 Déploiement sur GitHub

### Création du dépôt

- [ ] Compte GitHub créé
- [ ] Nouveau dépôt créé (nom : `assistant-scolaire` ou autre)
- [ ] Dépôt configuré en **Public**

### Upload des fichiers

- [ ] `index.html` uploadé
- [ ] `manifest.json` uploadé
- [ ] `sw.js` uploadé
- [ ] Dossier `icons/` uploadé avec les 2 fichiers PNG
- [ ] (Optionnel) `README.md` uploadé

### Activation de GitHub Pages

- [ ] Settings > Pages ouvert
- [ ] Source : Branch `main` sélectionnée
- [ ] Folder : `/ (root)` sélectionné
- [ ] Bouton "Save" cliqué
- [ ] Attente de 2-3 minutes pour le déploiement

## 🧪 Tests après déploiement

### Test sur ordinateur

- [ ] L'URL fonctionne : `https://USERNAME.github.io/assistant-scolaire/`
- [ ] La page s'affiche correctement
- [ ] Les horaires de bus s'affichent
- [ ] L'emploi du temps s'affiche
- [ ] Le simulateur de temps fonctionne
- [ ] Console du navigateur : pas d'erreurs (F12)
- [ ] Console : "Service Worker enregistré avec succès" apparaît

### Test sur mobile (Android)

- [ ] L'URL s'ouvre dans Chrome
- [ ] La page s'affiche correctement
- [ ] Le bouton "Ajouter à l'écran d'accueil" apparaît
- [ ] L'installation fonctionne
- [ ] L'icône apparaît sur l'écran d'accueil
- [ ] L'application se lance en plein écran
- [ ] Les fonctionnalités marchent (bus, planning)

### Test sur mobile (iOS)

- [ ] L'URL s'ouvre dans Safari
- [ ] La page s'affiche correctement
- [ ] Partager > "Sur l'écran d'accueil" fonctionne
- [ ] L'icône apparaît sur l'écran d'accueil
- [ ] L'application se lance correctement
- [ ] Les fonctionnalités marchent (bus, planning)

### Test hors-ligne

- [ ] Ouvrir l'application une première fois (en ligne)
- [ ] Activer le mode avion
- [ ] Fermer et rouvrir l'application
- [ ] L'application se charge correctement
- [ ] Les données sont accessibles

## 🎨 Personnalisation (optionnel)

- [ ] Icônes personnalisées créées avec `icons/generate_icon.html`
- [ ] Icônes remplacées dans le dossier `icons/`
- [ ] Modifications poussées vers GitHub

## 📱 Partage avec votre fils

- [ ] URL partagée par SMS/WhatsApp
- [ ] Instructions d'installation envoyées
- [ ] Test effectué ensemble
- [ ] Confirmation que tout fonctionne

## 🔄 Maintenance future

- [ ] Savoir comment modifier les horaires (éditer `index.html` sur GitHub)
- [ ] Savoir comment mettre à jour le cache (incrémenter version dans `sw.js`)
- [ ] Marque-page du dépôt GitHub pour accès rapide

## 🆘 En cas de problème

### L'URL ne fonctionne pas
- [ ] Vérifier que GitHub Pages est activé
- [ ] Attendre 5 minutes supplémentaires
- [ ] Vérifier que le dépôt est public
- [ ] Essayer en navigation privée

### L'installation ne fonctionne pas
- [ ] Vérifier que l'URL utilise HTTPS (GitHub Pages le fait automatiquement)
- [ ] Vider le cache du navigateur
- [ ] Sur iOS, utiliser Safari (pas Chrome)
- [ ] Vérifier que `manifest.json` est accessible

### Le mode hors-ligne ne fonctionne pas
- [ ] Ouvrir la console (F12) et vérifier les erreurs
- [ ] Vérifier que le Service Worker est enregistré
- [ ] Vérifier les chemins dans `sw.js`
- [ ] Incrémenter la version du cache et redéployer

### Les modifications ne s'affichent pas
- [ ] Vider le cache : Ctrl+Shift+R (ou Cmd+Shift+R)
- [ ] Incrémenter `CACHE_VERSION` dans `sw.js`
- [ ] Attendre quelques minutes pour la propagation GitHub
- [ ] Fermer complètement l'app et la relancer

## 📊 Validation finale

Une fois tous les tests passés :

- [ ] ✅ L'application est accessible via l'URL
- [ ] ✅ L'installation fonctionne sur mobile
- [ ] ✅ Le mode hors-ligne fonctionne
- [ ] ✅ Toutes les fonctionnalités sont opérationnelles
- [ ] ✅ Votre fils peut utiliser l'application

## 🎉 Félicitations !

Votre Assistant Scolaire PWA est maintenant déployé et opérationnel !

---

**Date de déploiement** : _______________

**URL de l'application** : _______________

**Notes** : _______________
