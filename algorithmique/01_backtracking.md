# Cours : Le Backtracking (Algorithmes de retour sur trace)

## 1. Introduction

Le **backtracking**, ou **retour sur trace**, est une méthode algorithmique pour résoudre des problèmes de **recherche de solution(s)** dans un **espace d’états** souvent très grand.  
L'idée générale est d'explorer toutes les solutions possibles **de manière récursive**, en **abandonnant les chemins sans issue** dès qu'on s’aperçoit qu’ils ne peuvent pas conduire à une solution.

Ce paradigme repose sur une approche **exploratoire et récursive** :

- À chaque étape, on **choisit une option possible**
- On avance vers une solution **en construisant un état partiel**
- Si cet état devient **invalide** (ne respecte plus les contraintes), on **revient en arrière** pour essayer une autre option

Cette approche permet d’explorer un **arbre de décisions** de manière efficace, en **évitant d’examiner des branches qui ne mèneront jamais à une solution**.

Bien que le backtracking puisse sembler coûteux en termes de performances (complexité souvent exponentielle), il est dans la pratique **très puissant grâce à l’élagage** ("pruning") des chemins impossibles. Il constitue ainsi une **base simple et robuste** pour aborder des problèmes combinatoires ou de satisfaction de contraintes.

## 2. Quand utiliser le backtracking ?

Le backtracking est adapté aux problèmes où :

- On peut construire une solution **étape par étape**
- On peut **tester si une solution partielle est valide**
- Il est possible d’**abandonner une branche** dès qu’elle devient invalide

Ce type d’approche est particulièrement utile lorsque :

- Le nombre de solutions possibles est grand ou inconnu
- On souhaite **trouver toutes les solutions**, ou **la première valide**
- Il n’existe pas d’algorithme déterministe plus rapide connu

Le backtracking permet aussi de gérer naturellement des **contraintes complexes** (par exemple, deux éléments ne doivent pas être voisins, une valeur ne peut apparaître qu’une seule fois, etc.).

### Exemples classiques :

- **Résolution de Sudoku** : placer les chiffres en respectant les contraintes de ligne, colonne et bloc
- **Problème des N reines** : placer N reines sur un échiquier sans qu'elles ne se menacent
- **Génération de permutations / combinaisons** : utile en tests, exploration d'ordres possibles
- **Parcours de labyrinthe** : retrouver un chemin d’un point A à un point B
- **Coloration de graphes** : attribuer une couleur à chaque nœud sans conflits entre voisins
- **Problèmes de partition** : diviser un ensemble en sous-ensembles selon des règles

Dans tous ces cas, le backtracking fournit une solution **simple à implémenter**, modulable, et qui peut être optimisée avec des techniques comme :

- L’ordre de parcours intelligent (ex. essayer les valeurs les plus probables d'abord)
- Le "forward checking" (vérification des conséquences d’un choix avant de l’accepter)
- La mémorisation d’états déjà explorés

## 3. Principe de fonctionnement

Le **backtracking** suit un **modèle récursif**, dans lequel une solution est construite progressivement, étape par étape. À chaque étape, on essaie un **choix possible**, puis on passe à l’étape suivante si ce choix respecte les contraintes. Si une impasse est rencontrée, on **annule le choix (backtrack)** pour en tester un autre.

Autrement dit, c’est une **exploration en profondeur (depth-first)** de l’arbre des solutions, avec retour arrière dès qu’un chemin est jugé non pertinent.

### Étapes générales d’un algorithme en backtracking

1. **Initialisation** : on part d’un état vide (ex. placement vide, chemin vide)
2. **Condition d’arrêt** : si on a atteint une solution complète, on l’enregistre ou on la retourne
3. **Boucle d’exploration** : on teste tous les choix possibles à ce stade
4. **Filtrage** : on vérifie si le choix est valide (respect des contraintes)
5. **Récursion** : on avance avec ce choix (appel récursif)
6. **Retour arrière** : après l’appel, on retire le choix pour essayer les suivants

### Pseudo-code générique

```python
def backtrack(solution_partielle):
    if solution_partielle est complète:
        traiter(solution_partielle)
        return
    for chaque choix possible:
        if choix valide pour solution_partielle:
            ajouter choix à solution_partielle
            backtrack(solution_partielle)
            retirer choix de solution_partielle
```

### Représentation en arbre (exemple simplifié)

Pour le problème "choisir 2 éléments parmi {1, 2, 3}" :

```
         []
       /  |  \
     [1] [2] [3]
    /  \   ...
 [1,2][1,3] ...
```

Chaque **nœud** représente une solution partielle, et chaque **branche** un choix possible.  
Le backtracking explore toutes les branches, en revenant en arrière lorsqu’un chemin est terminé ou invalide.

## 4. Exemple complet : Combinaisons de k éléments parmi n

### Énoncé

Étant donnés deux entiers `n` et `k`, générer toutes les combinaisons possibles de `k` entiers distincts parmi `{1, 2, ..., n}`.  
**Exemple** : pour `n = 4`, `k = 2` →  
`[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]`

### Code Python

```python
def combinaisons(n, k):
    resultats = []

    def backtrack(debut, chemin):
        if len(chemin) == k:
            resultats.append(chemin[:])
            return
        for i in range(debut, n + 1):
            chemin.append(i)
            backtrack(i + 1, chemin)
            chemin.pop()

    backtrack(1, [])
    return resultats
```

### Explication

- `chemin` : solution partielle en cours de construction
- `debut` : garantit qu’on ne génère pas de doublons
- `append` / `pop` : ajout et retrait du choix courant
- L’appel récursif poursuit la construction si la solution partielle est valide

### Résultat pour `n = 4`, `k = 2`

```python
print(combinaisons(4, 2))
```

Sortie :

```python
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

Très bien, poursuivons avec un autre **exemple emblématique de backtracking** : le **problème des N reines**, présenté de façon pédagogique et structurée en Markdown.

## 5. Exemple complet : Le problème des N reines

### Énoncé

Placer `N` reines sur un échiquier `N × N` de façon à ce qu’**aucune reine ne puisse en attaquer une autre**.  
Deux reines se menacent si elles sont sur la **même ligne**, **même colonne** ou **même diagonale**.

### Approche par backtracking

- On place les reines **ligne par ligne**
- À chaque ligne, on essaie de placer une reine **dans une colonne sûre**
- Si aucun placement n’est possible à une ligne donnée, on **revient en arrière**
- Une solution est trouvée lorsqu’on a placé `N` reines

### Visualisation

Échiquier `4×4`, but : trouver toutes les manières de placer 4 reines sans conflit.

```
. . Q .       Q . . .       . . . Q       . Q . .
. . . .       . . . Q       . . Q .       . . . .
Q . . .       . Q . .       Q . . .       . . Q .
. . . Q       . . Q .       . Q . .       Q . . .
```

### Code Python (N reines)

```python
def est_valide(placement, ligne, colonne):
    for r in range(ligne):
        c = placement[r]
        if c == colonne or abs(c - colonne) == abs(r - ligne):
            return False
    return True

def n_reines(N):
    solutions = []

    def backtrack(ligne, placement):
        if ligne == N:
            solutions.append(placement[:])
            return
        for colonne in range(N):
            if est_valide(placement, ligne, colonne):
                placement.append(colonne)
                backtrack(ligne + 1, placement)
                placement.pop()

    backtrack(0, [])
    return solutions
```

### Résultat pour `N = 4`

```python
sols = n_reines(4)
for s in sols:
    print(s)
```

Sortie :

```python
[1, 3, 0, 2]
[2, 0, 3, 1]
```

Chaque nombre représente la **colonne** où la reine est placée pour chaque **ligne**.  
Par exemple, `[1, 3, 0, 2]` signifie :

- Reine en (0,1)
- Reine en (1,3)
- Reine en (2,0)
- Reine en (3,2)

### Affichage visuel (optionnel)

```python
def afficher_solution(solution):
    N = len(solution)
    for i in range(N):
        ligne = ['.'] * N
        ligne[solution[i]] = 'Q'
        print(' '.join(ligne))
    print()

for sol in n_reines(4):
    afficher_solution(sol)
```

## 6. Optimisations possibles du backtracking

Bien que puissant, le backtracking peut être **inefficace sur de grands espaces d’états** s’il est utilisé de manière naïve. Plusieurs techniques permettent d’en améliorer considérablement l’efficacité.

### 6.1. Pruning (élagage)

**Principe** : ne pas continuer l’exploration d’une branche si l’on sait à l’avance qu’elle ne peut pas aboutir à une solution valide.

**Exemple** :  
Dans le problème des N reines, on peut éviter d'essayer une colonne si on sait qu’elle est déjà utilisée, ou si la reine serait en conflit sur une diagonale.

**Bénéfice** : réduction drastique du nombre de nœuds explorés.

### 6.2. Ordre de parcours intelligent

**Principe** : essayer en priorité les choix les plus prometteurs, selon des **heuristiques** spécifiques au problème.

**Exemples** :

- Dans un Sudoku, remplir d’abord les cases les plus contraintes (avec le moins de possibilités)
- Dans une grille, explorer les directions dans un ordre favorisant une solution rapide

**Bénéfice** : augmentation des chances de trouver une solution rapidement.

### 6.3. Structures auxiliaires

**Principe** : utiliser des structures de données pour **accélérer la vérification des contraintes**.

**Exemples** :

- Un tableau `colonnes_utilisées` pour savoir si une colonne contient déjà une reine
- Des ensembles pour suivre les chiffres utilisés dans une ligne/colonne d’un Sudoku

**Bénéfice** : amélioration des performances en évitant des parcours inutiles.

### 6.4. Mémorisation / Cache

**Principe** : enregistrer des résultats intermédiaires pour ne pas refaire les mêmes calculs (mémorisation, parfois appelée “memoization”).

**Exemple** : dans un problème de chemin ou de partition, enregistrer les sous-problèmes déjà visités.

**Attention** : cette technique relève parfois davantage de la **programmation dynamique**, mais peut être utile dans certains backtrackings avec sous-problèmes répétitifs.

### 6.5. Limitation du nombre de solutions

**Principe** : arrêter l’exploration après avoir trouvé un certain nombre de solutions (par exemple, la première).

**Exemple** :

```python
if len(resultats) >= 1:
    return  # inutile de continuer
```

**Bénéfice** : permet d’éviter l’exploration complète quand une seule solution suffit.

### 6.6. Early detection d’invalidité

**Principe** : détecter le plus tôt possible qu’un choix rendra toute solution impossible.

**Exemple** : si on remplit une combinaison dont la somme dépasse un certain seuil, on abandonne immédiatement.

**Bénéfice** : amélioration de l'efficacité par réduction du nombre de branches explorées inutilement.

## 7. Étude de complexité (sans optimisations)

Le principal inconvénient du backtracking est que **le nombre total de solutions possibles à explorer peut être extrêmement élevé**. En l’absence d’élagage ou d’heuristique, l’algorithme parcourt un **arbre complet des états**, dont la taille est souvent **exponentielle**.

### 7.1. Complexité temporelle

La **complexité temporelle** dépend du **nombre de configurations explorées** et du **coût de traitement de chaque configuration**.

#### Cas général :

Si à chaque étape on a `b` choix possibles, et qu’il faut faire `d` étapes pour construire une solution complète, alors la complexité maximale est :

```
O(b^d)
```

> On parle ici de **complexité dans le pire des cas**, c’est-à-dire **sans pruning**, en explorant **toutes les branches** de l’arbre des solutions.

### 7.2. Exemples concrets

#### 1. **Permutations de n éléments**

- À chaque étape, on choisit un des éléments restants
- Nombre total de permutations : `n!`
- Complexité : `O(n!)`

#### 2. **Combinaisons de k parmi n**

- Nombre de solutions : `C(n, k) = n! / (k!(n-k)!)`
- Complexité : `O(C(n, k) × k)` (car chaque solution a `k` éléments)

#### 3. **Problème des N reines**

- Sans optimisation, on teste jusqu’à `N^N` placements (chaque reine peut aller dans `N` colonnes à chaque ligne)
- Complexité : `O(N^N)` (pire cas)
- Avec contraintes intégrées, le nombre est réduit mais reste exponentiel

#### 4. **Sudoku (grille 9×9)**

- Chaque case vide a jusqu’à 9 choix → très grand arbre
- Complexité dans le pire des cas : `O(9^n)` où `n` est le nombre de cases vides

### 7.3. Complexité spatiale

La **complexité en espace mémoire** dépend :

- De la profondeur maximale de l’appel récursif (pile d’appel) : `O(d)`
- Du stockage éventuel de solutions : `O(nombre_de_solutions × taille_solution)`

> En général, on considère que la complexité mémoire est raisonnable **tant que l’on ne stocke pas toutes les solutions**.
