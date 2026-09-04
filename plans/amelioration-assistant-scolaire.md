# Plan d'amélioration - Assistant Scolaire

## 📋 Besoins identifiés

### 1. Navigation directe
- Permettre d'accéder directement à la section Bus ou Planning
- Via une page d'accueil avec boutons de choix
- Via des paramètres URL pour liens directs

### 2. Sélection du jour pour les horaires de bus
- Problème actuel : le soir, on ne voit que les derniers bus de la journée
- Solution : ajouter un sélecteur de jour pour voir les horaires du lendemain

---

## 🎯 Solutions proposées

### Solution 1 : Page d'accueil avec choix rapide

**Concept :**
- Créer une page d'accueil (écran de démarrage) avec deux grandes cartes cliquables
- Carte "Horaires Bus" avec icône de bus
- Carte "Emploi du temps" avec icône de calendrier
- Design moderne et épuré pour un choix rapide

**Avantages :**
- Interface claire et intuitive
- Choix rapide au démarrage
- Possibilité de revenir à l'accueil via un bouton

**Implémentation :**
- Ajouter un nouvel onglet "Accueil" qui s'affiche par défaut
- Deux grandes cartes avec animations au survol
- Bouton "Accueil" dans la navigation du bas

---

### Solution 2 : Navigation par URL (Deep Linking)

**Concept :**
- Détecter les paramètres URL au chargement de la page
- Exemples d'URLs :
  - `assistant.html` → Page d'accueil
  - `assistant.html?view=bus` → Ouvre directement les horaires de bus
  - `assistant.html?view=planning` → Ouvre directement le planning
  - `assistant.html?view=bus&day=2` → Bus du mardi
  - `assistant.html?view=planning&day=3` → Planning du mercredi

**Avantages :**
- Création de raccourcis/favoris spécifiques
- Partage de liens directs
- Intégration possible avec d'autres applications

**Implémentation :**
- Fonction JavaScript pour parser les paramètres URL
- Initialisation de l'état en fonction des paramètres
- Mise à jour de l'URL lors de la navigation (optionnel)

---

### Solution 3 : Sélecteur de jour pour les horaires de bus

**Concept actuel :**
- Les horaires affichés sont filtrés par le jour en cours
- Le soir, on ne voit plus que les derniers bus

**Nouvelle approche :**
- Ajouter un sélecteur de jour similaire à celui du planning
- Boutons : Aujourd'hui | Demain | Lun | Mar | Mer | Jeu | Ven
- Par défaut : afficher "Aujourd'hui"
- Le soir (après 18h par exemple), suggérer automatiquement "Demain"

**Variante intelligente :**
- Si l'heure actuelle > dernier bus du jour → basculer automatiquement sur le lendemain
- Afficher un badge "Demain" sur le widget du prochain bus
- Permettre de revenir à "Aujourd'hui" manuellement

**Implémentation :**
- Ajouter une ligne de boutons au-dessus de la section horaires
- Logique pour calculer le jour suivant (gérer le passage du vendredi au lundi)
- Mise à jour dynamique de l'affichage

---

## 🎨 Améliorations de design supplémentaires

### 1. Page d'accueil
```
┌─────────────────────────────────┐
│     Mon Assistant Scolaire      │
│     [Date et heure]             │
├─────────────────────────────────┤
│                                 │
│  ┌───────────────────────────┐  │
│  │     🚌 Horaires Bus       │  │
│  │                           │  │
│  │  Prochain bus dans 15min  │  │
│  └───────────────────────────┘  │
│                                 │
│  ┌───────────────────────────┐  │
│  │   📅 Emploi du temps      │  │
│  │                           │  │
│  │  Prochain cours : Maths   │  │
│  └───────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

### 2. Section Bus avec sélecteur de jour
```
┌─────────────────────────────────┐
│  [HAWK 3] [Ligne 2]             │
├─────────────────────────────────┤
│  Jour : [Auj.] Demain Lu Ma ... │
├─────────────────────────────────┤
│  Prochain bus : 17:10           │
│  Dans 25 minutes                │
├─────────────────────────────────┤
│  [Aller] [Retour]               │
├─────────────────────────────────┤
│  Liste des horaires...          │
└─────────────────────────────────┘
```

### 3. Navigation améliorée
- Ajouter un bouton "Accueil" dans la barre de navigation du bas
- 3 onglets : Accueil | Bus | Planning
- Icônes plus grandes et espacées

---

## 📝 Plan d'implémentation

### Phase 1 : Structure de base
1. Créer la page d'accueil avec les deux cartes principales
2. Ajouter le bouton "Accueil" dans la navigation
3. Implémenter la logique de navigation entre les sections

### Phase 2 : Deep Linking
1. Créer une fonction `parseURLParams()` pour lire les paramètres
2. Modifier `window.onload` pour initialiser selon l'URL
3. Tester les différentes combinaisons d'URLs

### Phase 3 : Sélecteur de jour pour les bus
1. Ajouter l'interface du sélecteur de jour
2. Créer une fonction `setSelectedBusDay(day)` 
3. Modifier `updateBusTab()` pour utiliser le jour sélectionné
4. Implémenter la logique "intelligente" (basculement auto vers demain)

### Phase 4 : Améliorations visuelles
1. Améliorer les animations de transition
2. Ajouter des indicateurs visuels (badges "Demain", "Prochain", etc.)
3. Optimiser l'espacement et la lisibilité
4. Tester sur mobile

### Phase 5 : Tests et ajustements
1. Tester tous les scénarios de navigation
2. Vérifier le comportement le soir (après dernier bus)
3. Tester les liens directs
4. Ajustements finaux

---

## 🔧 Modifications techniques principales

### Fichier HTML

#### Ajout de la page d'accueil
```html
<!-- TAB 0 : ACCUEIL -->
<div id="tab-home" class="tab-pane active">
    <div class="space-y-4 py-8">
        <!-- Carte Bus -->
        <button onclick="switchTab('bus')" class="w-full">
            <div class="bg-gradient-to-br from-hawk-900 to-hawk-950 border-2 border-hawk-600 rounded-3xl p-6 hover:scale-105 transition-transform">
                <!-- Contenu carte bus -->
            </div>
        </button>
        
        <!-- Carte Planning -->
        <button onclick="switchTab('planning')" class="w-full">
            <div class="bg-gradient-to-br from-slate-900 to-slate-950 border-2 border-slate-700 rounded-3xl p-6 hover:scale-105 transition-transform">
                <!-- Contenu carte planning -->
            </div>
        </button>
    </div>
</div>
```

#### Sélecteur de jour pour les bus
```html
<!-- Day Selector for Bus -->
<div class="flex gap-2 overflow-x-auto pb-2 mb-4">
    <button onclick="setBusDay('today')" id="bus-day-today" class="px-4 py-2 rounded-xl text-xs font-bold bg-hawk-600 text-white">
        Aujourd'hui
    </button>
    <button onclick="setBusDay('tomorrow')" id="bus-day-tomorrow" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-400">
        Demain
    </button>
    <!-- Autres jours... -->
</div>
```

### JavaScript

#### Ajout au STATE
```javascript
let STATE = {
    activeTab: 'home', // Commence sur l'accueil
    activeLine: 'hawk3',
    activeDir: 'aller',
    selectedBusDay: null, // null = aujourd'hui, 1-5 = jour spécifique
    simulatedDay: null,
    simulatedTime: null,
    realDate: new Date()
};
```

#### Fonction de parsing URL
```javascript
function parseURLParams() {
    const params = new URLSearchParams(window.location.search);
    const view = params.get('view'); // 'bus' ou 'planning'
    const day = params.get('day'); // 1-5
    
    if (view) {
        STATE.activeTab = view;
    }
    if (day) {
        const dayNum = parseInt(day);
        if (dayNum >= 1 && dayNum <= 5) {
            STATE.selectedBusDay = dayNum;
            STATE.simulatedDay = dayNum;
        }
    }
}
```

#### Fonction pour le jour des bus
```javascript
function getBusDisplayDay() {
    if (STATE.selectedBusDay) return STATE.selectedBusDay;
    
    const currentDay = getCurrentDay();
    const currentTime = getCurrentTime();
    const currentMins = timeToMins(currentTime);
    
    // Si après 18h et plus de bus aujourd'hui, suggérer demain
    if (currentMins > 1080) { // 18h = 1080 minutes
        const lineData = BUS_DATA[STATE.activeLine];
        const dirData = lineData[STATE.activeDir];
        const todayTrips = dirData.trips.filter(t => t.days.includes(currentDay));
        const hasMoreTrips = todayTrips.some(t => timeToMins(t.dep) > currentMins);
        
        if (!hasMoreTrips) {
            // Retourner le jour suivant (gérer vendredi -> lundi)
            return currentDay === 5 ? 1 : currentDay + 1;
        }
    }
    
    return currentDay;
}
```

---

## 📱 Aperçu des améliorations

### Avant
- Navigation uniquement par onglets en bas
- Horaires bus limités au jour en cours
- Pas d'accès direct aux sections

### Après
- Page d'accueil avec choix rapide
- Liens directs via URL
- Sélecteur de jour pour les bus
- Basculement intelligent vers le lendemain
- Navigation améliorée avec 3 onglets

---

## ✅ Points de validation

- [ ] La page d'accueil s'affiche correctement
- [ ] Les cartes sont cliquables et mènent aux bonnes sections
- [ ] Les liens URL fonctionnent (`?view=bus`, `?view=planning`)
- [ ] Le sélecteur de jour des bus fonctionne
- [ ] Le basculement automatique vers demain fonctionne le soir
- [ ] La navigation entre les sections est fluide
- [ ] Le design est cohérent et moderne
- [ ] L'application fonctionne bien sur mobile
