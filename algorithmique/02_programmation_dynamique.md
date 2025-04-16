# Programmation dynamique

## 1. Introduction

La **programmation dynamique** (ou **dynamic programming**, abrégée **DP**) est une méthode algorithmique puissante permettant de **résoudre efficacement des problèmes complexes en les décomposant en sous-problèmes plus simples**.

Elle est particulièrement efficace lorsqu’un problème possède deux propriétés fondamentales :

- Des **sous-problèmes qui se recoupent** : les mêmes calculs apparaissent plusieurs fois dans une approche naïve (souvent récursive).
- Une **structure optimale** : une solution optimale peut être construite à partir des solutions optimales de sous-problèmes (principe d’**optimalité de Bellman**).

Plutôt que de recalculer plusieurs fois les mêmes résultats, la programmation dynamique **mémorise** les solutions déjà obtenues, soit :

- **en les stockant** (dans un tableau, un dictionnaire…) pour les réutiliser (**mémoïsation**, approche récursive optimisée),
- **en les calculant directement dans un certain ordre**, souvent de bas en haut (**programmation tabulaire**, approche itérative).

Cette méthode est très utilisée pour :

- les **problèmes d’optimisation**
- les **problèmes de dénombrement**
- les **problèmes de décision combinatoire**

## 2. Quand utiliser la programmation dynamique ?

Un problème peut être résolu efficacement par programmation dynamique s’il satisfait **les deux critères suivants** :

### 2.1. Sous-problèmes qui se recoupent

- Un **même sous-problème** revient plusieurs fois dans l’algorithme naïf (souvent de manière exponentielle).
- Typiquement observé dans les **algorithmes récursifs** naïfs où l’arbre d’appel contient beaucoup de **répétitions inutiles**.

_Exemple :_  
Dans le calcul naïf de la suite de Fibonacci, `F(3)` est appelé plusieurs fois par des branches différentes.

### 2.2. Structure optimale (principe d’optimalité)

- Une solution **optimale globale** peut être **construite à partir des solutions optimales des sous-problèmes**.
- Autrement dit, **prendre la meilleure décision à chaque étape locale** permet d’atteindre la solution globale (ce qui **n’est pas toujours vrai**, d’où l’intérêt du test préalable).

_Exemple :_  
Dans le problème du sac à dos 0/1, la meilleure valeur obtenue pour une capacité donnée repose sur les **meilleures valeurs précédentes**.

### 2.3. Autres indices utiles

- Le problème peut se **décrire comme une fonction avec paramètres entiers** (poids, index, taille, etc.).
- Le nombre total d’états possibles est **polynomialement borné** (ex : `n × W`, `n²`, etc.).
- Une **formule de récurrence** peut être définie pour relier un état à d’autres.

## 3. Principe de fonctionnement

La **programmation dynamique** consiste à **résoudre un problème en construisant progressivement la solution à partir de sous-problèmes plus simples**, tout en **évitant les redondances** grâce à la **mémorisation** des résultats déjà calculés.

Elle repose sur une **structure d’état** (qu’on doit identifier), et une **formule de transition** (ou récurrence) qui permet de **faire avancer le calcul**.

### 3.1. Étapes générales

Voici les 5 grandes étapes d’un algorithme dynamique bien construit :

1. **Définir l’état dynamique**  
   → Quels paramètres décrivent un sous-problème ?  
   Exemple : `dp[i][w] = valeur maximale possible avec les i premiers objets et capacité w`

2. **Établir la relation de transition (récurrence)**  
   → Comment obtenir `dp[i]` à partir des `dp[j]` plus petits ?  
   Exemple : `dp[i] = max(dp[i-1], dp[i-2] + valeur[i])`

3. **Initialiser les cas de base**  
   → Que vaut la solution pour les cas les plus simples ?  
   Exemple : `dp[0] = 0`, `dp[1] = valeur[1]`, etc.

4. **Choisir l’ordre de parcours**  
   → **Top-down (mémoïsation)** ou **Bottom-up (tableau)**  
   On choisit l’approche selon la clarté du problème ou les contraintes de performance.

5. **Lire la solution finale**  
   → La réponse se trouve généralement dans `dp[n]` ou `dp[n][k]`, selon les cas.

### 3.2. Deux approches fondamentales

#### a) Top-down (récursif avec mémoïsation)

- On écrit une fonction récursive `f(i)` qui appelle ses sous-problèmes
- On utilise une **structure mémoire** (ex : dictionnaire, tableau) pour ne pas recalculer un état déjà connu
- C’est une **approche naturelle** si le raisonnement est récursif

📌 _Exemple :_

```python
memo = {}
def f(i):
    if i in memo:
        return memo[i]
    # cas de base
    ...
    # appel récursif
    memo[i] = f(...) + ...
    return memo[i]
```

#### b) Bottom-up (tabulaire)

- On **remplit un tableau** de manière itérative, en **respectant l’ordre des dépendances**
- On commence par les **cas de base**, puis on construit progressivement vers le haut
- C’est souvent **plus rapide** et **plus stable** (pas de récursion)

📌 _Exemple :_

```python
dp = [0] * (n + 1)
dp[0] = ...
for i in range(1, n + 1):
    dp[i] = ...
```

### 3.3. Représentation visuelle

Voici une représentation générique d’un **tableau dynamique** utilisé en bottom-up :

```
État : dp[i] = solution au sous-problème i

i     :   0     1     2     3     4     5
dp[i] :   0    ...   ...   ...   ...   ?
                     ↑     ↑     ↑
           dépend de ces valeurs
```

> Comprendre la **structure des dépendances** entre états est **clé** dans tout algorithme dynamique.

## 4. Exemple complet : suite de Fibonacci

### Énoncé

Calculer `F(n)`, la `n`-ième valeur de la suite de Fibonacci définie par :

```
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)  pour n ≥ 2
```

Ce problème classique est idéal pour illustrer le passage d’une solution récursive inefficace à une version optimisée via la programmation dynamique.

### Version récursive simple (inefficace)

```python
def fib_naif(n):
    if n <= 1:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)
```

🔴 **Problème** :

- L’arbre des appels récursifs contient énormément de **redondances** (les mêmes appels sont faits des milliers de fois).
- La complexité est **exponentielle** : `O(2^n)`

### Version top-down avec mémoïsation

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

✅ **Avantages** :

- Évite les appels redondants : chaque `fib(k)` est calculé **au plus une fois**.
- Complexité réduite à **O(n)**

📌 **Remarque** : On utilise ici un **dictionnaire** `memo` partagé entre appels pour stocker les résultats intermédiaires.

### Version bottom-up (itérative)

```python
def fib_iter(n):
    if n <= 1:
        return n
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]
```

✅ **Avantages** :

- Aucun appel récursif → plus stable, plus rapide
- Complexité en **temps** : `O(n)`
- Complexité en **espace** : `O(n)` (car on garde tous les termes)

### Version optimisée en espace (`O(1)`)

Comme chaque terme dépend uniquement des deux précédents, on peut **réduire l’espace mémoire à deux variables** :

```python
def fib_opt(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

✅ **Avantage** :

- Même complexité en temps `O(n)`
- Complexité en espace **constante** `O(1)`

### Comparatif des versions

| Version | Temps | Mémoire | Stabilité | Remarques |
||--|--|--||
| Récursive naïve | `O(2^n)` | `O(n)` | ❌ | Très lent dès `n > 30` |
| Top-down mémo | `O(n)` | `O(n)` | ✅ | Simple et efficace |
| Bottom-up | `O(n)` | `O(n)` | ✅ | Sans récursion |
| Optimisée (2 vars)| `O(n)` | `O(1)` | ✅✅ | Version recommandée en pratique |

## 5. Exemple plus avancé : Problème du sac à dos 0/1

### Énoncé

On dispose de `n` objets, chacun ayant :

- un **poids** `poids[i]`
- une **valeur** `valeurs[i]`

On souhaite remplir un **sac de capacité maximale `W`** en choisissant certains objets **sans les fractionner**, de sorte que :

- la **valeur totale** des objets sélectionnés soit **maximale**
- le **poids total** ne dépasse pas `W`

> On parle de **sac à dos 0/1** car on prend **chaque objet en entier (1)** ou pas du tout (0).

### Définition de l’état

On définit une table `dp[i][j]` où :

- `i` est le **nombre d’objets considérés** (de 0 à `n`)
- `j` est la **capacité du sac restante** (de 0 à `W`)
- `dp[i][j]` représente la **valeur maximale** que l'on peut obtenir **avec les `i` premiers objets et une capacité `j`**

### Formule de récurrence

Pour chaque objet `i` et chaque capacité `j`, on a deux choix :

1. **Ne pas prendre l’objet `i`** : on garde la valeur précédente → `dp[i-1][j]`
2. **Prendre l’objet `i`** (si son poids est ≤ `j`) :
   - on ajoute sa valeur
   - on déduit son poids de la capacité
   - on ajoute sa valeur à `dp[i-1][j - poids[i-1]]`

D’où la formule :

```
dp[i][j] = max(
    dp[i-1][j],                                 # sans l’objet i
    dp[i-1][j - poids[i-1]] + valeurs[i-1]      # avec l’objet i
)  si poids[i-1] ≤ j
```

Sinon :

```
dp[i][j] = dp[i-1][j]      # on ne peut pas prendre l’objet i
```

### Implémentation (bottom-up)

```python
def sac_a_dos(valeurs, poids, W):
    n = len(valeurs)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if poids[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - poids[i - 1]] + valeurs[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
```

### Exemple concret

```python
valeurs = [60, 100, 120]
poids   = [10, 20, 30]
W       = 50

print(sac_a_dos(valeurs, poids, W))  # Résultat : 220
```

📦 On prend les objets 2 (100) et 3 (120) → total 220 pour un poids de 50.

### Visualisation (extrait de tableau `dp`)

```
dp[i][j] → valeur maximale avec les i premiers objets et capacité j

     j →     0   1   2  ...  19  20  21  ...  50
i
↓
0         [ 0,  0,  0, ... ,  0,  0,  0, ... ,  0 ]
1 (obj1)  [ 0,  0,  0, ... ,  0, 60, 60, ... , 60 ]
2 (obj2)  [ 0,  0,  0, ... , 60,100,100,... ,160 ]
3 (obj3)  [ 0,  0,  0, ... ,100,120,120,... ,220 ]
```

### Complexité

| Aspect | Valeur |
||-|
| Temps | `O(n × W)` |
| Mémoire | `O(n × W)` |
| Type | Programmation dynamique tabulaire |
| Possibilité d’optimisation | Oui, on peut réduire la mémoire à `O(W)` en utilisant 1D |

### Optimisation mémoire

Comme on n’utilise que la ligne `i-1` à chaque itération, on peut **remplacer la matrice 2D par un tableau 1D**, parcouru **à l’envers** :

```python
def sac_a_dos_opt(valeurs, poids, W):
    n = len(valeurs)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, poids[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - poids[i]] + valeurs[i])

    return dp[W]
```

## 6. Exemple avancé : Rendu de monnaie (nombre de façons)

### Énoncé

On dispose d’un ensemble de **pièces de différentes valeurs** (par exemple : `[1, 2, 5]`)  
On souhaite déterminer **de combien de façons distinctes** on peut rendre une somme `S`, **en utilisant un nombre illimité de pièces**.

> Ce problème est un classique de **dénombrement avec répétition**, et non d’optimisation.

### Définition de l’état

On définit une table `dp[i]` où :

- `i` est une **somme** (allant de `0` à `S`)
- `dp[i]` est le **nombre de façons de former la somme `i`**

### Cas de base

- `dp[0] = 1` : il y a **1 seule façon de rendre 0** (en ne prenant rien)

### Formule de transition

Pour chaque **pièce `c`**, on met à jour tous les `dp[i]` avec `i ≥ c` :

```
dp[i] += dp[i - c]
```

➡ Cela revient à dire : pour chaque montant `i`, on ajoute toutes les façons d’obtenir `i - c`, puis on ajoute une pièce de valeur `c`.

### Implémentation (bottom-up)

```python
def rendu_de_monnaie(pieces, S):
    dp = [0] * (S + 1)
    dp[0] = 1

    for piece in pieces:
        for i in range(piece, S + 1):
            dp[i] += dp[i - piece]

    return dp[S]
```

### Exemple concret

```python
pieces = [1, 2, 5]
S = 5

print(rendu_de_monnaie(pieces, S))  # Résultat : 4
```

🟢 **Explication :**
Les 4 façons de rendre 5 :

- 1 + 1 + 1 + 1 + 1
- 1 + 1 + 1 + 2
- 1 + 2 + 2
- 5

### Visualisation du tableau `dp`

Pour `S = 5`, les valeurs successives de `dp` sont :

| i (somme) | 0 | 1 | 2 | 3 | 4 | 5 |
||||||||
| dp[i] | 1 | 1 | 2 | 2 | 3 | 4 |

> La valeur finale `dp[5] = 4` correspond au nombre total de combinaisons possibles.

### Complexité

| Aspect | Valeur |
||-|
| Temps | `O(n × S)` |
| Mémoire | `O(S)` |
| Type | Programmation dynamique 1D |
| Particularité | L’ordre des pièces **n’influence pas** le résultat |

### Variante possible

Si on cherche le **nombre minimal de pièces** nécessaires pour rendre une somme `S`, on change l’objectif du tableau :

- `dp[i] = min(dp[i], dp[i - c] + 1)`
- Initialisation : `dp[0] = 0`, `dp[i>0] = +∞`

Ce problème devient alors un **problème d’optimisation**, et la logique change légèrement.

## 7. Étude de complexité

La complexité d’un algorithme en programmation dynamique dépend principalement :

- du **nombre total d'états différents** à évaluer (taille de la table `dp`)
- du **temps nécessaire pour calculer chaque état**
- de la **structure choisie** (top-down ou bottom-up)

### 7.1. Complexité temporelle

| Approche                   | Description                                           | Complexité                             |
| -------------------------- | ----------------------------------------------------- | -------------------------------------- |
| **Top-down (mémoïsation)** | Appels récursifs + cache des résultats intermédiaires | `O(nombre d’états réellement visités)` |
| **Bottom-up (tabulaire)**  | Calcul itératif dans un tableau                       | `O(taille du tableau dp)`              |

#### 📌 Exemples concrets

| Problème                        | États (dp[i]) ou dp[i][j]        | Complexité en temps |
| ------------------------------- | -------------------------------- | ------------------- |
| Fibonacci                       | `dp[i]` avec `i ∈ [0..n]`        | `O(n)`              |
| Sac à dos 0/1                   | `dp[i][j]` avec `i ≤ n`, `j ≤ W` | `O(n × W)`          |
| Rendu de monnaie (nb façons)    | `dp[i]` avec `i ∈ [0..S]`        | `O(n × S)`          |
| Rendu de monnaie (min pièces)   | `dp[i]` avec `i ∈ [0..S]`        | `O(n × S)`          |
| Distance d’édition (alignement) | `dp[i][j]` avec `i ≤ n`, `j ≤ m` | `O(n × m)`          |

### 7.2. Complexité spatiale

La mémoire utilisée dépend du **nombre d’états qu’on conserve**.

| Approche            | Structure typique             | Complexité mémoire                 |
| ------------------- | ----------------------------- | ---------------------------------- |
| Top-down            | Cache (ex : dict)             | `O(n)` ou `O(n × k)` selon l’état  |
| Bottom-up classique | Tableau `dp[i]` ou `dp[i][j]` | `O(n)`, `O(n × W)`, etc.           |
| Optimisé (1D)       | Réduction ligne/colonne       | `O(W)` ou `O(S)` parfois suffisant |

> 💡 De nombreux problèmes permettent une **optimisation mémoire** en n'utilisant **qu’une ligne ou une colonne à la fois**, si les dépendances le permettent.

### 7.3. Remarques importantes

- Le **top-down** peut être plus simple à écrire mais consomme plus de **pile récursive** (→ risque de stack overflow si `n` est grand).
- Le **bottom-up** est souvent plus rapide et mieux maîtrisé en pratique.
- Il est important de bien **définir l’état** (`dp[...]`) et **d’analyser sa dimension** pour estimer la complexité globale.
