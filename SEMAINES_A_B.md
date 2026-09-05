# Système de Semaines A et B

## Vue d'ensemble

L'application intègre maintenant un système de semaines alternées A et B pour gérer les emplois du temps qui varient selon les semaines.

## Fonctionnalités

### 1. Calcul automatique de la semaine en cours

- **Date de référence** : 1er septembre 2026 (définie comme Semaine A)
- **Calcul** : Le système calcule automatiquement si on est en semaine A ou B en fonction du nombre de semaines écoulées depuis la date de référence
- **Alternance** : Les semaines alternent automatiquement (A → B → A → B...)

### 2. Indicateur visuel

- Un badge coloré dans l'en-tête affiche la semaine en cours
- **Semaine A** : Badge vert (couleur hawk)
- **Semaine B** : Badge violet

### 3. Filtrage des cours

Les cours sont maintenant marqués avec une propriété `week` :
- `'both'` : Cours présent chaque semaine (A et B)
- `'A'` : Cours uniquement en semaine A
- `'B'` : Cours uniquement en semaine B

L'application filtre automatiquement l'affichage pour ne montrer que les cours correspondant à la semaine en cours.

## Structure des données

Chaque cours dans le planning contient maintenant :

```javascript
{
    start: '08:15',
    end: '09:10',
    subject: 'Mathématiques',
    room: 'Salle 201',
    color: 'blue',
    teacher: 'CALVIER T.',
    week: 'both'  // ou 'A' ou 'B'
}
```

## Exemples de cours alternés

D'après l'emploi du temps :

### Lundi 11h15-12h10
- **Semaine A** : Anglais (BOISSET A., Salle 107)
- **Semaine B** : Vie de Classe (MAURIN C., Salle 106)

### Mardi 13h40-14h35
- **Semaine A** : Français (MAURIN C., Salle 106)
- **Semaine B** : Devoirs Faits (GERARD M., Salle CDI)

### Jeudi 11h15-12h10
- **Semaine A** : Physique-Chimie (THIEBDIA S., Salle 215)
- **Semaine B** : Vie de Classe (MAURIN C., Salle 106)

### Vendredi 10h20-11h15
- **Semaine A** : Physique-Chimie (THIEBDIA S., Salle 215)
- **Semaine B** : Vie de Classe (MAURIN C., Salle 106)

## Modification de la date de référence

Si vous devez ajuster la date de référence pour la semaine A, modifiez la constante dans le fichier `index.html` :

```javascript
const WEEK_A_REFERENCE = new Date('2026-09-01'); // Première semaine A
```

Changez cette date pour qu'elle corresponde au premier lundi de la première semaine A de votre année scolaire.

## Test avec le simulateur

Le simulateur de temps permet de tester le système :

1. Cliquez sur l'horloge en haut à droite
2. Modifiez la date pour voir l'alternance des semaines
3. Observez comment l'emploi du temps change selon la semaine

## Affichage dans l'interface

- **Page d'accueil** : Le prochain cours affiché tient compte de la semaine en cours
- **Page Planning** : Seuls les cours de la semaine en cours sont affichés
- **Informations professeur** : Le nom du professeur est maintenant affiché sous chaque cours
