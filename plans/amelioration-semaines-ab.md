# Plan d'amélioration : Système de semaines A/B avec switch manuel

## 🎯 Objectif

Améliorer le système de semaines A/B pour permettre :
1. Un affichage automatique intelligent (adapté au jour consulté)
2. Un switch manuel pour basculer entre semaines A et B
3. Une gestion ergonomique le weekend

## 📊 Solution proposée : Système hybride Auto/Manuel

### Concept

```
┌─────────────────────────────────────────────────┐
│ Mon Assistant                                   │
│ vendredi 5 septembre                            │
│                                                 │
│ [Auto ▼] [Semaine A] [Semaine B]              │
│   ↑         ↑ actif     ↑ inactif              │
│   │         └─────────────┘                     │
│   └─ Mode sélection                             │
└─────────────────────────────────────────────────┘
```

### Modes de fonctionnement

#### Mode 1 : Auto (par défaut) ⭐
- **Comportement** : La semaine affichée s'adapte automatiquement
  - En semaine : affiche la semaine du jour actuel
  - Le weekend : affiche la semaine du lundi suivant
  - Quand on sélectionne un jour : affiche la semaine de ce jour

- **Interface** :
  ```
  [Auto ▼] Semaine A
  ```

#### Mode 2 : Manuel (Semaine A forcée)
- **Comportement** : Affiche toujours les cours de la semaine A
  - Peu importe le jour actuel
  - Utile pour planifier à l'avance

- **Interface** :
  ```
  [Manuel ▼] Semaine A ✓
  ```

#### Mode 3 : Manuel (Semaine B forcée)
- **Comportement** : Affiche toujours les cours de la semaine B
  - Peu importe le jour actuel
  - Utile pour planifier à l'avance

- **Interface** :
  ```
  [Manuel ▼] Semaine B ✓
  ```

## 🎨 Design de l'interface

### Option A : Toggle simple (RECOMMANDÉ)

```
┌─────────────────────────────────────────┐
│ Emploi du temps                         │
│                                         │
│ [Lu] [Ma] [Me] [Je] [Ve]               │
│                                         │
│ Semaine: [Auto ▼] [A] [B]              │
│          └─────┘   ↑   ↑               │
│          Dropdown  Toggle buttons       │
└─────────────────────────────────────────┘
```

**Comportement** :
- Dropdown "Auto" : 
  - Clic → bascule entre "Auto" / "Manuel"
- Boutons A/B :
  - En mode Auto : affiche la semaine calculée (non cliquable)
  - En mode Manuel : cliquable pour choisir A ou B

### Option B : Toggle avec indicateur visuel

```
┌─────────────────────────────────────────┐
│ Emploi du temps                         │
│                                         │
│ [Lu] [Ma] [Me] [Je] [Ve]               │
│                                         │
│ ┌─────────────────────────────────┐    │
│ │ 🔄 Auto  │ Semaine A │ Semaine B│    │
│ │          │    ✓      │          │    │
│ └─────────────────────────────────┘    │
│                                         │
│ Cliquer pour forcer une semaine        │
└─────────────────────────────────────────┘
```

### Option C : Badge cliquable (PLUS SIMPLE) ⭐⭐

```
┌─────────────────────────────────────────┐
│ Mon Assistant                           │
│ vendredi 5 septembre                    │
│                                         │
│ [🔄 Semaine A ▼]  ← Badge cliquable     │
│                                         │
│ Clic → Menu:                            │
│ ┌──────────────────┐                   │
│ │ ✓ Auto (Sem. A)  │                   │
│ │   Forcer Sem. A  │                   │
│ │   Forcer Sem. B  │                   │
│ └──────────────────┘                   │
└─────────────────────────────────────────┘
```

## 🔧 Implémentation technique

### 1. État à ajouter

```javascript
STATE = {
    // ... existant
    weekMode: 'auto',        // 'auto', 'forceA', 'forceB'
    displayedWeek: null      // null = auto, 'A' ou 'B' si forcé
}
```

### 2. Nouvelle fonction : `getDisplayedWeek()`

```javascript
function getDisplayedWeek() {
    // Si mode manuel, retourner la semaine forcée
    if (STATE.weekMode === 'forceA') return 'A';
    if (STATE.weekMode === 'forceB') return 'B';
    
    // Mode auto : calculer selon le contexte
    if (STATE.activeTab === 'planning' && STATE.selectedPlanningDay) {
        // Calculer la semaine du jour sélectionné
        return getWeekForDay(STATE.selectedPlanningDay);
    }
    
    // Par défaut : semaine actuelle
    return getCurrentWeek();
}
```

### 3. Fonction : `getWeekForDay(dayOfWeek)`

```javascript
function getWeekForDay(dayOfWeek) {
    const currentDay = getCurrentDay();
    
    // Si on est le weekend et qu'on regarde lundi
    if ((currentDay === 0 || currentDay === 6) && dayOfWeek === 1) {
        // Calculer la semaine du lundi suivant
        const nextMonday = new Date(STATE.realDate);
        const daysUntilMonday = (8 - currentDay) % 7;
        nextMonday.setDate(nextMonday.getDate() + daysUntilMonday);
        
        const diffTime = nextMonday - WEEK_A_REFERENCE;
        const diffWeeks = Math.floor(diffTime / (1000 * 60 * 60 * 24 * 7));
        return diffWeeks % 2 === 0 ? 'A' : 'B';
    }
    
    // Sinon, retourner la semaine actuelle
    return getCurrentWeek();
}
```

### 4. Interface utilisateur

#### Composant : Badge cliquable avec menu

```html
<!-- Dans le header -->
<div class="relative">
    <button onclick="toggleWeekMenu()" id="weekBadge" 
            class="text-[10px] font-bold px-2 py-0.5 rounded-full 
                   bg-hawk-500/20 text-hawk-400 border border-hawk-500/30 
                   uppercase tracking-wider cursor-pointer hover:bg-hawk-500/30">
        <span id="weekModeIcon">🔄</span>
        <span id="weekLabel">Semaine A</span>
        <span>▼</span>
    </button>
    
    <!-- Menu dropdown -->
    <div id="weekMenu" class="hidden absolute top-full mt-1 right-0 
                              bg-slate-900 border border-slate-700 rounded-xl 
                              shadow-xl z-50 min-w-[160px]">
        <button onclick="setWeekMode('auto')" 
                class="w-full px-3 py-2 text-left text-xs hover:bg-slate-800">
            <span id="autoCheck">✓</span> Auto (Sem. A)
        </button>
        <button onclick="setWeekMode('forceA')" 
                class="w-full px-3 py-2 text-left text-xs hover:bg-slate-800">
            <span id="forceACheck"></span> Forcer Semaine A
        </button>
        <button onclick="setWeekMode('forceB')" 
                class="w-full px-3 py-2 text-left text-xs hover:bg-slate-800">
            <span id="forceBCheck"></span> Forcer Semaine B
        </button>
    </div>
</div>
```

### 5. Fonctions JavaScript

```javascript
function toggleWeekMenu() {
    const menu = document.getElementById('weekMenu');
    menu.classList.toggle('hidden');
}

function setWeekMode(mode) {
    STATE.weekMode = mode;
    toggleWeekMenu(); // Fermer le menu
    updateUI();
}

function updateWeekBadge() {
    const displayedWeek = getDisplayedWeek();
    const badge = document.getElementById('weekBadge');
    const label = document.getElementById('weekLabel');
    const icon = document.getElementById('weekModeIcon');
    
    // Mettre à jour le texte
    label.innerText = `Semaine ${displayedWeek}`;
    
    // Mettre à jour l'icône
    if (STATE.weekMode === 'auto') {
        icon.innerText = '🔄';
    } else {
        icon.innerText = '📌'; // Épingle pour "forcé"
    }
    
    // Mettre à jour les couleurs
    if (displayedWeek === 'A') {
        badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-hawk-500/20 text-hawk-400 border border-hawk-500/30 uppercase tracking-wider cursor-pointer hover:bg-hawk-500/30';
    } else {
        badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-400 border border-purple-500/30 uppercase tracking-wider cursor-pointer hover:bg-purple-500/30';
    }
    
    // Mettre à jour les checkmarks du menu
    document.getElementById('autoCheck').innerText = STATE.weekMode === 'auto' ? '✓' : '';
    document.getElementById('forceACheck').innerText = STATE.weekMode === 'forceA' ? '✓' : '';
    document.getElementById('forceBCheck').innerText = STATE.weekMode === 'forceB' ? '✓' : '';
}
```

## 📱 Cas d'usage

### Cas 1 : Consultation normale en semaine
- **Contexte** : Mardi, semaine A
- **Mode** : Auto (par défaut)
- **Affichage** : "🔄 Semaine A"
- **Planning** : Cours de la semaine A

### Cas 2 : Weekend, consultation du lundi suivant
- **Contexte** : Samedi, semaine A se termine
- **Mode** : Auto
- **Affichage** : "🔄 Semaine B" (car lundi = semaine B)
- **Planning** : Cours de la semaine B du lundi

### Cas 3 : Planification à l'avance
- **Contexte** : Mardi, semaine A, mais veut voir semaine B
- **Action** : Clic sur badge → "Forcer Semaine B"
- **Mode** : Manuel (forceB)
- **Affichage** : "📌 Semaine B"
- **Planning** : Cours de la semaine B

### Cas 4 : Retour au mode auto
- **Action** : Clic sur badge → "Auto"
- **Mode** : Auto
- **Affichage** : "🔄 Semaine A" (semaine actuelle)
- **Planning** : Cours de la semaine actuelle

## ✅ Avantages de cette solution

1. **Intelligent par défaut** : Mode auto gère tout automatiquement
2. **Flexible** : Possibilité de forcer une semaine pour planifier
3. **Visuel clair** : 
   - 🔄 = mode auto
   - 📌 = mode forcé
4. **Compact** : Un seul badge cliquable
5. **Intuitif** : Menu dropdown simple
6. **Pas de confusion** : Le mode est toujours visible

## 🎯 Prochaines étapes

1. Implémenter `getWeekForDay()` et `getDisplayedWeek()`
2. Ajouter le badge cliquable avec menu dropdown
3. Implémenter les fonctions de switch
4. Mettre à jour `updatePlanningTab()` pour utiliser `getDisplayedWeek()`
5. Gérer la fermeture du menu au clic extérieur
6. Tester tous les cas d'usage
