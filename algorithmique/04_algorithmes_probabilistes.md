# Algorithmes probabilistes

## 1. Introduction

Un **algorithme probabiliste** est un algorithme qui utilise des **valeurs aléatoires** au cours de son exécution.  
Contrairement aux algorithmes déterministes, il peut **produire des résultats différents** à chaque exécution, même avec les **mêmes données en entrée**.

L’usage du hasard peut intervenir :

- pour orienter les choix (comme un pivot dans un tri rapide)
- pour générer des données aléatoires (ex : simulations)
- pour explorer efficacement un grand espace de solutions
- pour obtenir une solution **approchée**, mais calculable rapidement

Ce type d’algorithme est utilisé lorsque :

- Le **problème est trop coûteux** à résoudre de manière exacte
- On accepte une **solution rapide mais non garantie à 100 %**
- L’**approximation est suffisante** dans la pratique (ex : test de primalité, estimation)

## 2. Deux grandes familles d’algorithmes probabilistes

Il existe deux grands types d’algorithmes probabilistes, selon le compromis fait entre le **temps d’exécution** et la **fiabilité du résultat**.

### 2.1. Algorithmes de type _Las Vegas_

- Ils utilisent l’aléa pour accélérer l’exécution, mais **le résultat est toujours correct**.
- Le **temps d’exécution varie** selon les tirages aléatoires : certaines exécutions peuvent être très rapides, d'autres plus longues.
- L’aléa intervient dans les **décisions internes** à l’algorithme, mais **sans compromettre la fiabilité du résultat**.
- Ces algorithmes sont souvent des **versions optimisées** d’algorithmes classiques, en remplaçant des choix arbitraires par des choix aléatoires.

**Exemples** :

- **Tri rapide aléatoire (Randomized QuickSort)** : le choix du pivot au hasard permet d'éviter les pires cas systématiques (ex : tableau déjà trié), tout en garantissant un tri exact.
- **Algorithme de sélection aléatoire** : permet de trouver le k-ième plus petit élément dans un tableau en temps linéaire dans la moyenne.
- **Backtracking avec tirage aléatoire** : pour explorer plus rapidement certaines branches prometteuses.

**Avantage** :

- Résultat exact et garanti
- Parfois bien plus rapide que la version déterministe classique

**Inconvénient** :

- Pas de garantie sur le **temps d’exécution**, qui peut fluctuer fortement
- Nécessite parfois plusieurs tentatives (ex : génération aléatoire de structures valides)

### 2.2. Algorithmes de type _Monte Carlo_

- Le **temps d’exécution est borné**, souvent prédictible, mais **le résultat peut être incorrect** avec une certaine probabilité.
- Ce type d’algorithme fournit une **solution approximative** ou un **résultat probabiliste**, acceptable dans de nombreux contextes.
- L’**erreur** est généralement **contrôlable** : en répétant l’expérience, on peut rendre la probabilité d’erreur arbitrairement faible.
- Très utilisés dans des domaines où **l’exactitude totale n’est pas requise** ou impossible à obtenir efficacement.

**Exemples** :

- **Miller-Rabin** : test de primalité pour grands entiers (utilisé en cryptographie) avec faible risque d’erreur.
- **Estimation de π** par génération de points aléatoires dans un carré et comptage de ceux tombant dans un cercle.
- **Algorithme de Karger** : trouve une coupe minimale dans un graphe en contractant des arêtes au hasard. Plus on répète, plus la probabilité de succès augmente.
- **Méthodes de Monte Carlo** pour l’intégration numérique, les probabilités conditionnelles, ou les modèles physiques.

**Avantage** :

- Temps d’exécution constant ou borné
- Très rapide pour des problèmes inaccessibles en déterministe

**Inconvénient** :

- **Risque d’erreur** inhérent (mais généralement contrôlable)
- Difficulté à **prouver formellement** certains résultats

## 3. Applications typiques

Les algorithmes probabilistes sont utilisés dans de nombreux domaines, notamment lorsque les **algorithmes déterministes sont trop lents**, **trop complexes**, ou inexistants. Ils sont particulièrement adaptés aux contextes où l’on préfère **une réponse rapide avec un risque faible d’erreur** plutôt qu’une solution exacte trop coûteuse.

Voici quelques applications classiques :

### 3.1. Recherche de motif dans une chaîne – **Algorithme de Rabin-Karp**

- Objectif : détecter rapidement si un motif est présent dans un grand texte
- Technique : hachage aléatoire du motif et comparaison avec des hachages de sous-chaînes
- Type : **Monte Carlo** (risque de collision de hachage)

### 3.2. Test de primalité – **Miller-Rabin, Fermat**

- Objectif : savoir si un très grand entier est probablement premier
- Utilisation : cryptographie (RSA, clé publique)
- Type : **Monte Carlo** – possibilité d’erreur, mais répétitions réduisent drastiquement le risque

### 3.3. Estimation de π – **Méthode de Monte Carlo**

- Objectif : approximer π par simulation aléatoire de points dans un carré unité
- Idée : générer des points `(x, y)` et compter ceux dans un quart de cercle
- Type : **Monte Carlo** (estimation probabiliste)

### 3.4. Coupe minimale dans un graphe – **Algorithme de Karger**

- Objectif : trouver la plus petite coupe séparant un graphe
- Méthode : contraction aléatoire d’arêtes jusqu’à n’avoir que deux sommets
- Type : **Monte Carlo**, répété plusieurs fois pour augmenter la probabilité de succès

### 3.5. Méthodes de simulation (physique, finance, IA)

- Simulation de chaînes de Markov, processus stochastiques
- Exploration de grands espaces de solutions (ex : sampling, apprentissage)
- Planification approximative ou optimisation de fonctions bruitées

## 4. Exemple : Rabin-Karp (recherche de motif probabiliste)

### Problème

Étant donné :

- un texte `text` de longueur `n`
- un motif `pattern` de longueur `m`

On cherche à **trouver la première occurrence** (s'il y en a une) de `pattern` dans `text`.

### Idée de l’algorithme

L’idée de Rabin-Karp repose sur une stratégie rapide mais probabiliste :

1. On **code chaque chaîne de caractères** par une valeur numérique appelée **hachage** (comme une signature numérique).
2. On **calcule le hachage du motif** une seule fois.
3. On **fait glisser une fenêtre de taille `m`** sur le texte et on calcule dynamiquement le **hachage de chaque sous-chaîne**.
4. Si le hachage de la fenêtre courante **correspond à celui du motif**, alors :
   - Il est **probable** que le motif soit trouvé → on vérifie **caractère par caractère** pour confirmer.
   - Il se peut aussi que ce soit une **collision** : deux chaînes différentes mais avec le même hachage (c’est ce qui rend l’algorithme **probabiliste**).

> Le risque de collision est contrôlé par l’utilisation d’un **modulo premier** et d’une **base** adaptée.

### Code et explication

```python
def rabin_karp(text, pattern):
    base = 256            # Base pour le codage (256 pour tous les caractères ASCII)
    mod = 101             # Modulo premier pour limiter la taille des hachages
    n, m = len(text), len(pattern)
    hpat = 0              # Hachage du motif
    htxt = 0              # Hachage de la fenêtre courante du texte
    h = 1                 # Coefficient pour le caractère le plus à gauche (base^(m-1))
```

#### Calcul du coefficient pour le 1er caractère

```python
    for i in range(m - 1):
        h = (h * base) % mod
```

- Ce `h` servira à **"retirer" le caractère de gauche** lors du décalage de la fenêtre (hachage glissant).

#### Calcul initial des hachages du motif et de la première fenêtre du texte

```python
    for i in range(m):
        hpat = (hpat * base + ord(pattern[i])) % mod
        htxt = (htxt * base + ord(text[i])) % mod
```

- `ord(c)` transforme un caractère en entier.
- Le hachage est calculé comme un **nombre en base `base` modulo `mod`**.

#### Parcours du texte avec une fenêtre glissante

```python
    for i in range(n - m + 1):
        if hpat == htxt and text[i:i + m] == pattern:
            return i  # motif trouvé
```

- Si les hachages sont égaux, on vérifie le contenu pour **éviter les faux positifs** (collision).

#### Mise à jour du hachage de la fenêtre

```python
        if i < n - m:
            htxt = (htxt - ord(text[i]) * h) * base + ord(text[i + m])
            htxt %= mod
```

- On **retire le caractère qui sort** de la fenêtre (`text[i]`)
- On **ajoute le caractère suivant** (`text[i + m]`)
- L’opération est faite en **temps constant**.

#### Fin de l’algorithme

```python
    return -1  # motif non trouvé
```

## 5. Exemple : estimation de π (intégration de Monte Carlo)

### Objectif

Estimer la valeur de π sans passer par une formule mathématique, mais simplement par une **expérience aléatoire simulée**.  
C’est un exemple classique de la **méthode de Monte Carlo**, fondée sur la loi des grands nombres.

### Idée

On considère un **carré de côté 1** et le **quart de cercle** inscrit dans ce carré.

- Le carré couvre une surface de `1 × 1 = 1`.
- Le quart de cercle a pour surface : `π × r² / 4 = π / 4` (car `r = 1`).

Si on génère aléatoirement `n` points `(x, y)` uniformément dans le carré `[0, 1] × [0, 1]` :

- La **proportion de points tombant dans le quart de cercle** correspondra approximativement à `π / 4`.
- Donc, on a :
  ```
  π ≈ 4 × (nombre de points dans le cercle) / n
  ```

Plus on génère de points, plus l’approximation est précise (convergence statistique).

### Code Python expliqué

```python
import random

def estimer_pi(n):
    dans_cercle = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            dans_cercle += 1
    return 4 * dans_cercle / n
```

#### Étape par étape

- `random.random()` génère un nombre aléatoire entre 0 et 1.
- On génère `n` couples `(x, y)` dans `[0, 1]²`.
- On vérifie si le point est **dans le quart de cercle** : `x² + y² ≤ 1`
- On compte les points qui satisfont cette condition.
- Enfin, on applique la formule :
  ```
  π ≈ 4 × (nombre de points dans le cercle) / n
  ```

### Exemple d’utilisation

```python
print(estimer_pi(1000000))
```

> Résultat approximatif : `3.1415...` avec un million de points

## 6. Étude de complexité

### Las Vegas

- Ces algorithmes **fournissent toujours un résultat correct**, quel que soit le hasard introduit.
- Leur **temps d'exécution est variable** : il dépend des tirages aléatoires effectués.
- On analyse généralement leur **complexité en espérance** (c’est-à-dire la moyenne sur toutes les exécutions possibles).
- Dans le **pire des cas**, certains Las Vegas peuvent être très lents, mais cela arrive rarement si l'aléa est bien utilisé.

**Exemples :**

- **QuickSort aléatoire** : complexité moyenne `O(n log n)`, pire cas `O(n²)` si les pivots sont mal choisis (peu probable avec randomisation).
- **Algorithme de sélection aléatoire (QuickSelect)** : trouve le k-ième plus petit élément en `O(n)` en moyenne, mais `O(n²)` dans le pire des cas.

### Monte Carlo

- Ces algorithmes ont un **temps d'exécution borné**, souvent très efficace (linéaire, logarithmique...).
- En revanche, le **résultat peut être incorrect**, avec une **probabilité d’erreur connue et maîtrisable**.
- En répétant plusieurs fois l’algorithme, on peut **réduire exponentiellement** la probabilité d'erreur.
- La complexité dépend du **nombre de répétitions** nécessaires pour atteindre un niveau de confiance donné.

**Exemples :**

- **Rabin-Karp** : `O(n + m)` en moyenne, mais `O(nm)` en cas de nombreuses collisions (rare).
- **Miller-Rabin** : `O(k × log³ n)` où `k` est le nombre de répétitions pour atteindre une probabilité d’erreur acceptable.
- **Méthode de Monte Carlo pour π** : `O(n)` pour `n` points simulés, erreur typique en `1/√n`.
