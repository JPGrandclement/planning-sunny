# 📱 Guide d'utilisation - Assistant Scolaire

## 🎯 Vue d'ensemble

L'assistant scolaire amélioré offre maintenant une navigation plus intuitive et des fonctionnalités avancées pour consulter les horaires de bus et l'emploi du temps.

---

## 🆕 Nouvelles fonctionnalités

### 1. Page d'accueil avec choix rapide

Au démarrage, vous arrivez sur une page d'accueil avec deux grandes cartes :

- **🚌 Horaires Bus** : Accès direct aux horaires HAWK 3 et Ligne 2
  - Affiche un aperçu du prochain bus
  
- **📅 Emploi du temps** : Accès direct au planning de la semaine
  - Affiche un aperçu du prochain cours

**Utilisation :** Cliquez simplement sur la carte correspondant à ce que vous voulez consulter.

---

### 2. Sélecteur de jour pour les horaires de bus

**Problème résolu :** Le soir, vous ne voyiez que les derniers bus de la journée.

**Solution :** Un sélecteur de jour est maintenant disponible avec les options :
- **Aujourd'hui** : Horaires du jour en cours
- **Demain** : Horaires du lendemain
- **Lu, Ma, Me, Je, Ve** : Horaires d'un jour spécifique

**Basculement intelligent :**
- Après 17h00, si tous les bus de la journée sont passés, l'application bascule automatiquement sur "Demain"
- Un badge jaune "Demain" apparaît sur le widget du prochain bus
- Vous pouvez toujours revenir manuellement à "Aujourd'hui"

---

### 3. Navigation par URL (Liens directs)

Vous pouvez maintenant créer des liens directs vers des sections spécifiques :

#### Exemples d'URLs :

**Accès direct aux horaires de bus :**
```
assistant_scolaire_ameliore.html?view=bus
```

**Accès direct au planning :**
```
assistant_scolaire_ameliore.html?view=planning
```

**Bus d'un jour spécifique (ex: Mardi) :**
```
assistant_scolaire_ameliore.html?view=bus&day=2
```

**Planning d'un jour spécifique (ex: Jeudi) :**
```
assistant_scolaire_ameliore.html?view=planning&day=4
```

#### Codes des jours :
- `1` = Lundi
- `2` = Mardi
- `3` = Mercredi
- `4` = Jeudi
- `5` = Vendredi

**Utilisation pratique :**
- Créez des favoris dans votre navigateur avec ces URLs
- Ajoutez des raccourcis sur l'écran d'accueil de votre téléphone
- Partagez des liens directs

---

### 4. Navigation améliorée avec 3 onglets

La barre de navigation en bas de l'écran contient maintenant 3 onglets :

1. **🏠 Accueil** : Retour à la page d'accueil
2. **🚌 Bus** : Horaires de bus
3. **📅 Planning** : Emploi du temps

L'onglet actif est mis en évidence en vert.

---

## 📖 Guide d'utilisation détaillé

### Consulter les horaires de bus

1. **Depuis l'accueil :** Cliquez sur la carte "Horaires Bus"
2. **Choisir la ligne :**
   - HAWK 3 (Principal) : Ligne principale
   - Ligne 2 (Altern.) : Ligne alternative
3. **Sélectionner le jour :**
   - Cliquez sur "Aujourd'hui", "Demain" ou un jour spécifique
4. **Choisir la direction :**
   - Aller : Vers l'école
   - Retour : Vers la maison

**Widget "Prochain bus" :**
- Affiche l'heure du prochain départ
- Indique le temps restant avant le départ
- Montre l'heure d'arrivée prévue
- Badge "Demain" si le bus est pour le lendemain

**Liste des horaires :**
- Le prochain bus est mis en évidence avec un badge "Prochain"
- Les bus passés sont grisés
- Certains bus ont des badges spéciaux (ex: "8h", "Mercredi")

---

### Consulter l'emploi du temps

1. **Depuis l'accueil :** Cliquez sur la carte "Emploi du temps"
2. **Sélectionner le jour :**
   - Cliquez sur Lu, Ma, Me, Je ou Ve
   - Le jour actuel est sélectionné par défaut
3. **Visualiser le planning :**
   - Les cours sont affichés chronologiquement
   - Le cours en cours est mis en évidence avec un badge "En cours"
   - Les cours passés sont légèrement grisés
   - Chaque cours affiche :
     - Horaires de début et fin
     - Matière (avec code couleur)
     - Salle

**Codes couleurs des matières :**
- 🔵 Bleu : Mathématiques
- 🌹 Rose : Français
- 🟡 Ambre : Histoire-Géo
- 🟣 Violet : Langues (Anglais, Espagnol)
- 🟢 Émeraude : Sciences (Physique-Chimie, SVT)
- 🟠 Orange : EPS
- 🩷 Rose clair : Arts Plastiques
- 🔵 Indigo : Éducation Musicale
- ⚪ Gris : Technologie, Repas

---

## 🛠️ Simulateur de temps

Pour tester l'application à différents moments de la journée :

1. **Ouvrir le simulateur :** Cliquez sur l'horloge en haut à droite
2. **Modifier l'heure :** Sélectionnez une heure spécifique
3. **Modifier le jour :** Choisissez un jour de la semaine
4. **Appliquer :** Cliquez sur "Appliquer"
5. **Revenir au temps réel :** Cliquez sur "Revenir au temps réel"

**Utilisation :**
- Vérifier les horaires de bus pour demain soir
- Voir l'emploi du temps d'un autre jour
- Tester le basculement automatique vers "Demain"

---

## 💡 Astuces et conseils

### Pour les horaires de bus

✅ **Le soir après les cours :**
- L'application bascule automatiquement sur "Demain"
- Vous voyez directement les horaires du lendemain matin

✅ **Pour planifier à l'avance :**
- Utilisez le sélecteur de jour pour voir les horaires de n'importe quel jour
- Exemple : Vendredi soir, consultez les horaires du lundi

✅ **Créer des favoris :**
- Créez un favori `?view=bus` pour accéder directement aux horaires
- Créez un favori `?view=bus&day=1` pour les horaires du lundi

### Pour l'emploi du temps

✅ **Voir le cours en cours :**
- Le cours actuel est mis en évidence avec une bordure verte
- Un badge "En cours" apparaît

✅ **Préparer la semaine :**
- Consultez les jours suivants pour savoir quels livres apporter
- Vérifiez les salles pour ne pas vous perdre

✅ **Accès rapide :**
- Depuis l'accueil, l'aperçu montre le prochain cours
- Cliquez pour voir tout le planning

---

## 🔗 Exemples de liens directs à créer

### Sur ordinateur (Favoris)

1. **Horaires du matin :**
   - Nom : "🚌 Bus - Aller"
   - URL : `assistant_scolaire_ameliore.html?view=bus`

2. **Horaires du soir :**
   - Nom : "🚌 Bus - Retour demain"
   - URL : `assistant_scolaire_ameliore.html?view=bus&day=2` (adapter le jour)

3. **Planning de la semaine :**
   - Nom : "📅 Mon planning"
   - URL : `assistant_scolaire_ameliore.html?view=planning`

### Sur téléphone (Raccourcis écran d'accueil)

**iOS (Safari) :**
1. Ouvrez l'URL dans Safari
2. Appuyez sur le bouton Partager
3. Sélectionnez "Sur l'écran d'accueil"
4. Donnez un nom au raccourci

**Android (Chrome) :**
1. Ouvrez l'URL dans Chrome
2. Appuyez sur le menu (⋮)
3. Sélectionnez "Ajouter à l'écran d'accueil"
4. Donnez un nom au raccourci

---

## 🐛 Résolution de problèmes

### Le prochain bus n'apparaît pas
- Vérifiez que vous êtes sur le bon jour (Aujourd'hui/Demain)
- Vérifiez la direction (Aller/Retour)
- Vérifiez la ligne (HAWK 3 / Ligne 2)

### L'heure affichée est incorrecte
- Vérifiez que le simulateur n'est pas activé (l'heure devient orange)
- Cliquez sur l'horloge et "Revenir au temps réel"

### Le cours en cours n'est pas mis en évidence
- Vérifiez que vous êtes sur le bon jour
- L'heure système de votre appareil doit être correcte

### La page d'accueil ne s'affiche pas
- Vérifiez l'URL : elle ne doit pas contenir de paramètres
- Cliquez sur l'onglet "Accueil" en bas

---

## 📊 Récapitulatif des améliorations

| Fonctionnalité | Avant | Après |
|----------------|-------|-------|
| **Navigation** | 2 onglets (Bus, Planning) | 3 onglets (Accueil, Bus, Planning) |
| **Accès direct** | Non disponible | Liens URL directs |
| **Sélection jour bus** | Jour actuel uniquement | Aujourd'hui, Demain, ou jour spécifique |
| **Basculement intelligent** | Non | Oui (auto vers demain après 17h) |
| **Page d'accueil** | Non | Oui (avec aperçus) |
| **Aperçu prochain bus** | Non | Oui (sur page d'accueil) |
| **Aperçu prochain cours** | Non | Oui (sur page d'accueil) |

---

## 🎓 Pour aller plus loin

### Personnalisation possible

Si vous souhaitez personnaliser l'application :

1. **Modifier les horaires de bus :**
   - Éditez la section `BUS_DATA` dans le code JavaScript
   - Ajoutez/modifiez les horaires dans `trips`

2. **Modifier l'emploi du temps :**
   - Éditez la section `PLANNING` dans le code JavaScript
   - Changez les matières, horaires, salles

3. **Changer les couleurs :**
   - Modifiez la configuration Tailwind dans le `<head>`
   - Changez les couleurs `hawk` et `ligne2`

---

## 📞 Support

Pour toute question ou problème :
- Consultez ce guide
- Testez avec le simulateur de temps
- Vérifiez que vous utilisez un navigateur récent

---

**Version :** 2.0 - Améliorée  
**Date :** Septembre 2026  
**Compatibilité :** Tous navigateurs modernes (Chrome, Safari, Firefox, Edge)
