# Algorithmes génétiques

## 1. Introduction

Les **algorithmes génétiques (AG)** font partie de la famille des **algorithmes évolutionnaires**, c’est-à-dire des méthodes d’optimisation qui s’inspirent du **processus de sélection naturelle** décrit par Charles Darwin.  
L’idée est de **faire évoluer une population de solutions candidates** en appliquant des mécanismes biologiques simulés : **sélection**, **croisement** et **mutation**.

À chaque génération, les solutions **les plus adaptées** (selon une mesure appelée _fitness_) sont **conservées, croisées et légèrement modifiées**, dans l’espoir de produire des **descendants meilleurs**.  
Ce processus est **répété sur plusieurs générations**, jusqu’à ce qu’on obtienne une solution satisfaisante.

### Quand utiliser un algorithme génétique ?

Les AG sont particulièrement utiles lorsque :

- L’espace de recherche est **trop grand** pour être exploré de manière exhaustive
- Aucune **formule mathématique explicite** ne permet d’optimiser le problème
- Le problème présente de **nombreux optima locaux** (non convexe, discontinu…)
- Les **données sont bruitées**, incomplètes ou difficiles à modéliser
- On cherche une **solution approchée** acceptable plutôt qu’un optimum exact

Exemples : conception automatique, planification, ingénierie, jeux, optimisation combinatoire...

## 2. Principes biologiques simulés

Un algorithme génétique simule une **évolution artificielle** au sein d’une population.  
Chaque élément de cette population représente une **solution possible** au problème, codée sous une forme manipulable (binaire, tableau, permutation…).

Voici les principaux concepts biologiques modélisés :

### 2.1. **Population**

- Ensemble de **solutions candidates** (appelées _individus_ ou _chromosomes_)
- Taille constante ou variable selon les générations
- Chaque individu représente **un point de l’espace de recherche**

### 2.2. **Gènes et codage**

- Un **gène** est une unité d’information de la solution (bit, nombre, symbole…)
- L’ensemble des gènes forme le **génotype** (ex : une chaîne binaire)
- Ce génotype est **décodé** pour produire le **phénotype** (la solution réelle dans le problème)

💡 Le choix du codage a un **impact important sur la performance** de l’algorithme.

### 2.3. **Fonction d’évaluation (fitness)**

- Permet de mesurer la **qualité d’un individu**
- Plus un individu a une fitness élevée, plus il est **susceptible de se reproduire**
- La fitness est spécifique au problème (ex : score à maximiser, coût à minimiser)

### 2.4. **Sélection**

- Mécanisme qui **favorise les meilleurs individus** (ou les plus adaptés) pour la reproduction
- Objectif : **transmettre les bons gènes** à la génération suivante
- Méthodes courantes : **roulette**, **tournoi**, **rang**, **élite**

### 2.5. **Croisement (recombinaison)**

- Combine les gènes de deux parents pour créer un ou plusieurs **descendants**
- Peut se faire en un point, deux points, ou uniformément
- Objectif : **mélanger l'information génétique** de manière constructive

### 2.6. **Mutation**

- Modifie **aléatoirement un ou plusieurs gènes** d’un individu
- Permet d’**introduire de la diversité** et d’éviter le blocage dans des optima locaux
- Taux de mutation faible (typiquement entre 1 % et 5 %)

### 2.7. **Remplacement (survie)**

- Après génération des descendants, on décide qui **reste dans la population**
- Soit on **remplace entièrement** la population, soit on garde une **partie des meilleurs**
- L’**élitisme** consiste à **conserver automatiquement les meilleurs individus**

## 3. Schéma général d’un algorithme génétique

```text
1. Initialiser une population de solutions aléatoires
2. Évaluer la fitness de chaque individu
3. Répéter jusqu’à condition d’arrêt :
    a. Sélectionner des individus selon leur fitness
    b. Croiser certains couples pour produire des descendants
    c. Appliquer des mutations aléatoires
    d. Évaluer les nouveaux individus
    e. Mettre à jour la population (avec ou sans remplacement)
```

### Explication étape par étape

#### **1. Initialisation**

- Génération aléatoire d’une **population initiale** d’individus (solutions)
- Chaque individu est une solution **codée selon un schéma choisi** (binaire, tableau de réels, permutations, etc.)
- Taille typique : entre **20 et 500 individus**

#### **2. Évaluation**

- On **calcule la fitness** de chaque individu à l’aide de la fonction d’évaluation définie
- Cette étape **guide l’évolution** : seuls les plus adaptés seront sélectionnés

#### **3. Boucle principale (évolution)**

La boucle évolutive peut durer :

- un **nombre fixe de générations**
- ou jusqu’à **atteinte d’un score cible**, ou **stagnation des performances**

##### **a. Sélection**

- Choix des **parents** en fonction de leur fitness
- Méthodes courantes :
  - **Roulette** : probabilité proportionnelle à la fitness
  - **Tournoi** : sélection des meilleurs parmi des sous-groupes aléatoires
  - **Élite** : les meilleurs passent automatiquement à la génération suivante

##### **b. Croisement (recombinaison)**

- Création de nouveaux individus en **croisant les gènes de deux parents**
- Objectif : **combiner les bonnes caractéristiques**
- Types de croisement :
  - Un point
  - Deux points
  - Uniforme (chaque gène vient au hasard de l’un ou l’autre parent)

##### **c. Mutation**

- Modification aléatoire d’un ou plusieurs gènes
- Maintient une **diversité génétique** dans la population
- Empêche l’algorithme de **se bloquer dans un optimum local**
- Le **taux de mutation** est faible mais crucial

##### **d. Évaluation des descendants**

- On **évalue la fitness des nouveaux individus**
- Ceux-ci seront ensuite potentiellement intégrés dans la population

##### **e. Mise à jour de la population**

- **Remplacement** : quels individus seront présents à la génération suivante ?
  - **Remplacement complet** : seuls les enfants survivent
  - **Remplacement partiel** : on garde les meilleurs de l’ancienne population
  - **Élitisme** : les meilleurs individus ne sont jamais supprimés

### Condition d'arrêt

L’évolution s’arrête généralement lorsque :

- un **nombre maximal de générations** est atteint
- une **solution satisfaisante** est trouvée
- la population **ne progresse plus** (convergence)

## 4. Exemple simple : maximiser une fonction

### Problème

On cherche à **maximiser la fonction** :

```
f(x) = x²
```

pour `x` ∈ [0, 31], c’est-à-dire pour `x` codé sur **5 bits** (de `00000` à `11111`).

Chaque individu est donc représenté par **un entier compris entre 0 et 31**, que l’on peut manipuler **comme une suite binaire de 5 bits**.

L’objectif est que l’algorithme évolue vers des individus ayant des valeurs proches de **31**, puisque `f(x)` est croissante et maximale en `x = 31`.

### Étapes de l’algorithme génétique

1. **Population initiale** : 6 entiers aléatoires entre 0 et 31
2. **Évaluation (fitness)** : on calcule `x²` pour chaque individu
3. **Sélection** : on choisit deux parents avec une probabilité **proportionnelle à leur fitness**
4. **Croisement** : on coupe aléatoirement les bits entre deux parents pour créer un descendant
5. **Mutation** : un bit aléatoire peut être inversé avec une petite probabilité
6. **Remplacement** : les enfants et une partie des parents forment la nouvelle population

### Code commenté

```python
import random

# Fonction de fitness = objectif à maximiser
def fitness(x):
    return x * x
```

- On maximise `f(x) = x²`
- Un x proche de 31 aura une fitness élevée (jusqu’à 961)

```python
# Sélection proportionnelle à la fitness (roulette)
def selection(pop):
    return random.choices(pop, weights=[fitness(x) for x in pop], k=2)
```

- On choisit deux parents dans la population
- Les individus avec une meilleure fitness ont **plus de chances** d’être choisis

```python
# Croisement à un point (bitmask entre les deux parents)
def crossover(p1, p2):
    point = random.randint(1, 4)  # point de croisement entre 1 et 4 (sur 5 bits)
    mask = (1 << point) - 1       # ex : point = 3 → mask = 000111
    return (p1 & mask) | (p2 & ~mask)
```

- Combine les bits de `p1` et `p2` pour former un **enfant**
- Les bits **à droite** viennent de `p1`, les bits **à gauche** de `p2`

```python
# Mutation : inversion d’un bit avec probabilité de 10 %
def mutate(x):
    if random.random() < 0.1:
        bit = 1 << random.randint(0, 4)  # choisir un bit parmi les 5
        return x ^ bit                   # inverse ce bit avec XOR
    return x
```

- Permet d’introduire un peu d’**aléa génétique**
- Évite de **se bloquer dans des optima locaux**

```python
def algo_genetique():
    population = [random.randint(0, 31) for _ in range(6)]  # population initiale
    for generation in range(20):  # nombre de générations
        new_population = []
        for _ in range(3):  # 3 paires d’individus → 6 au total
            p1, p2 = selection(population)
            enfant = crossover(p1, p2)
            enfant = mutate(enfant)
            new_population.extend([p1, enfant])  # on garde le parent + l’enfant
        population = new_population  # mise à jour
    return max(population, key=fitness)  # meilleur individu final
```

### Résultat attendu

```python
print(algo_genetique())
```

- Affiche une **valeur de `x`** dans `[0, 31]`
- Après 20 générations, on obtient **souvent un `x` proche de 31**, donc **près de l’optimum global**

### Ce que montre cet exemple

- Même avec un problème très simple et un **encodage direct**, l’algorithme génétique **parvient à converger vers la meilleure solution**
- Il montre la **puissance du principe d’évolution**, même sans connaissance explicite du maximum
- Il est **facile à modifier** pour maximiser d’autres fonctions, explorer d'autres encodages (réels, permutations...)

## 5. Exemple avancé : Algorithme génétique pour le sac à dos 0/1

### Problème

On dispose de `n` objets, chacun avec :

- un **poids** `poids[i]`
- une **valeur** `valeurs[i]`

Capacité maximale du sac : `W`  
Objectif : **choisir un sous-ensemble d’objets** de valeur maximale sans dépasser la capacité du sac.

### Codage génétique

Chaque solution est représentée par un **chromosome binaire de longueur `n`** :

- `1` → l’objet est sélectionné
- `0` → l’objet est ignoré

Exemple : `10110` signifie : on prend l’objet 1, 3 et 4.

### Fonction de fitness

On calcule :

- la **somme des valeurs** des objets sélectionnés
- si la **somme des poids dépasse `W`**, on **pénalise fortement** la solution (ex : fitness = 0)

### Code Python commenté

```python
import random

# Données du problème
valeurs = [60, 100, 120]
poids   = [10, 20, 30]
W       = 50
n       = len(valeurs)
```

### Fonction de fitness

```python
def fitness(chromosome):
    total_val = total_pds = 0
    for i in range(n):
        if chromosome[i] == 1:
            total_val += valeurs[i]
            total_pds += poids[i]
    if total_pds > W:
        return 0  # solution invalide
    return total_val
```

- On **récompense les solutions valides** en retournant leur valeur totale
- On **élimine les solutions invalides** (poids > W)

### Génération d’un individu aléatoire

```python
def random_individu():
    return [random.randint(0, 1) for _ in range(n)]
```

### Sélection (roulette)

```python
def selection(pop):
    scores = [fitness(ind) for ind in pop]
    total = sum(scores)
    if total == 0:
        return random.sample(pop, 2)
    return random.choices(pop, weights=scores, k=2)
```

- Si tout le monde a une fitness nulle (au début), on choisit deux parents au hasard
- Sinon, on utilise une **sélection proportionnelle à la fitness**

### Croisement (à un point)

```python
def crossover(p1, p2):
    point = random.randint(1, n - 1)
    return p1[:point] + p2[point:]
```

### Mutation (inversion aléatoire d’un bit)

```python
def mutate(individu, taux=0.1):
    return [
        bit if random.random() > taux else 1 - bit
        for bit in individu
    ]
```

### Algorithme principal

```python
def algo_genetique_sacados(generations=50, taille_pop=10):
    population = [random_individu() for _ in range(taille_pop)]

    for _ in range(generations):
        nouvelle_pop = []
        for _ in range(taille_pop // 2):
            p1, p2 = selection(population)
            enfant1 = mutate(crossover(p1, p2))
            enfant2 = mutate(crossover(p2, p1))
            nouvelle_pop.extend([enfant1, enfant2])
        population = nouvelle_pop

    meilleur = max(population, key=fitness)
    return meilleur, fitness(meilleur)
```

### Exemple d’utilisation

```python
sol, val = algo_genetique_sacados()
print("Meilleure solution trouvée :", sol)
print("Valeur totale :", val)
```

### Explication des résultats

- Le programme affiche un **vecteur binaire**, indiquant quels objets sont pris
- La valeur totale affichée est **la meilleure trouvée** après plusieurs générations
- Pour les données `[60, 100, 120]` et `W = 50`, la solution optimale est de prendre objets 2 et 3 → total 220

### Remarques

- Cet algorithme **approxime** une bonne solution, sans garantie d’optimalité
- Il peut être amélioré avec :
  - **élitisme** (garder les meilleurs individus)
  - **croisement plus intelligent**
  - **mutation adaptative**
  - **diversité contrôlée** pour éviter la convergence prématurée

## 6. Étude de complexité

L’**algorithme génétique** est un algorithme **probabiliste** et **heuristique** :  
il **n’a pas de garantie théorique d’optimalité**, mais offre souvent **des résultats efficaces en pratique**.  
Sa complexité dépend principalement de **paramètres réglables**.

### 6.1. Paramètres clés

| Paramètre | Description                          |
| --------- | ------------------------------------ |
| `N`       | Taille de la population              |
| `G`       | Nombre de générations                |
| `T_eval`  | Coût d’évaluation d’un individu      |
| `n`       | Longueur du chromosome (nb de gènes) |

### 6.2. Complexité temporelle

À chaque génération :

- On sélectionne `N` individus
- On effectue `N/2` croisements → `N` enfants
- On applique la mutation
- On évalue les `N` enfants

Donc **par génération** :

```
O(N × T_eval)
```

Et pour `G` générations :

```
O(G × N × T_eval)
```

#### 💡 Cas courants

| Problème                    | `T_eval` approximatif        | Complexité totale      |
| --------------------------- | ---------------------------- | ---------------------- |
| Fonction simple (`x²`)      | `O(1)`                       | `O(G × N)`             |
| Sac à dos (`n` objets)      | `O(n)` par individu          | `O(G × N × n)`         |
| Problème combinatoire (TSP) | `O(n)` ou `O(n²)` selon éval | `O(G × N × n)` ou `n²` |

### 6.3. Complexité spatiale

On stocke :

- La **population courante** de `N` individus
- Chaque individu est un chromosome de taille `n`

Donc :

```
O(N × n)
```

> La mémoire utilisée reste modérée, même pour des tailles importantes.

### 6.4. Remarques pratiques

- La **qualité des solutions** dépend plus des **paramètres** (mutation, sélection, diversité…) que de la complexité brute
- Les **AG sont faciles à paralléliser**, car l’évaluation des individus est indépendante
- L’**analyse théorique** est difficile car la convergence dépend de la **stochastique** de l’évolution


### 6.5. En résumé

| Aspect              | Valeur typique                                                |
| ------------------- | ------------------------------------------------------------- |
| Temps (théorique)   | `O(G × N × T_eval)`                                           |
| Espace              | `O(N × n)`                                                    |
| Optimalité garantie | ❌ (pas de garantie)                                          |
| Avantages           | Robuste, simple, flexible, global                             |
| Limites             | Lent pour des évaluations coûteuses, sensibilité aux réglages |
