# Bin Packing Problem

## Introduction

Le **Bin Packing Problem (BPP)** est un **problème fondamental d’optimisation combinatoire**, apparu dès les années 1970.  
Il modélise des situations où l’on cherche à **organiser efficacement l’espace ou les ressources** en regroupant des éléments dans des conteneurs de capacité limitée.

Ce problème est **NP-difficile**, c’est-à-dire qu’il n’existe **aucun algorithme connu capable de le résoudre de manière exacte en temps polynomial** pour tous les cas généraux. Cela en fait un excellent candidat pour l’étude d’**algorithmes approximatifs**, **probabilistes** ou **hybrides**.

### Problème de base

On dispose de :

- Un ensemble d’objets `O = {o₁, o₂, ..., oₙ}`, où chaque objet `oᵢ` a une taille `sᵢ` comprise dans `(0, 1]`
- Des bacs (ou conteneurs) de **capacité fixe**, généralement `1.0`
- Un **nombre illimité de bacs** à disposition

> L’objectif est de **placer tous les objets dans des bacs** sans dépasser la capacité maximale de chaque bac, en **utilisant le moins de bacs possible**.

### Contraintes

- La somme des tailles des objets dans un bac donné ne doit **jamais excéder 1.0**
- Chaque objet doit être placé **dans un seul et unique bac**
- On cherche à **minimiser le nombre total de bacs utilisés**

### Illustration

Prenons l’exemple suivant :

```txt
Objets : [0.4, 0.3, 0.6, 0.5, 0.2]
Capacité des bacs : 1.0
```

Une solution possible est :

- Bac 1 : 0.6 + 0.4 = 1.0 ✅
- Bac 2 : 0.5 + 0.3 = 0.8 ✅
- Bac 3 : 0.2 ✅

→ **Nombre total de bacs : 3**

Cette solution est **optimale** : aucun arrangement ne permet de réduire le nombre de bacs.

### Variantes

Le BPP se décline en plusieurs variantes, selon les contraintes ou objectifs :

- **Bin Packing multidimensionnel** : les objets ont plusieurs dimensions (volume, poids, etc.)
- **Bin Packing en ligne (online)** : les objets arrivent un par un, sans connaître à l’avance les suivants
- **Bin Packing avec bacs de capacités différentes**
- **Bin Packing avec priorité ou coût associé aux objets**
- **Bin Packing avec fragmentation possible (Split Packing)**

### Domaines d’application

Ce problème apparaît dans de nombreux contextes réels :

- **Logistique** : chargement de conteneurs, camions ou palettes
- **Systèmes d’exploitation** : allocation de mémoire ou de ressources CPU
- **Découpe industrielle** : découpage de matériaux (bois, tissu, métal) sans gaspillage
- **Cloud computing** : placement de machines virtuelles sur des serveurs physiques
- **Streaming média** : regroupement de morceaux audio/vidéo dans des blocs de taille fixe

### Pourquoi ce problème est difficile ?

Même s’il est facile à comprendre, le BPP est **combinatoirement explosif** :

- Pour `n` objets, le nombre de façons de les répartir dans des bacs peut être **exponentiel**.
- Il n’existe **pas d’algorithme exact efficace** connu pour le résoudre dans le cas général.
- Les meilleures approches sont souvent **approchées ou heuristiques**, ou utilisent **du hasard contrôlé** pour trouver de **bonnes solutions rapidement**.

Voici la suite enrichie et complète de la section **3. Algorithmes classiques (déterministes)** :

## Algorithmes classiques (déterministes)

### First Fit (FF)

- Parcourt les objets un à un dans l’ordre donné.
- Pour chaque objet, il cherche **le premier bac** dans lequel l’objet peut être placé sans dépasser la capacité.
- Si aucun bac existant ne convient, **un nouveau bac est ouvert**.

> Complexité : `O(n × m)` où `m` est le nombre de bacs ouverts à l’instant `n`,  
> ou `O(n log n)` avec une structure de données efficace pour trier les bacs.

**Avantages** :

- Très rapide et facile à implémenter
- Donne souvent une solution acceptable dans la pratique

**Inconvénients** :

- L’ordre des objets impacte fortement le résultat
- Peut laisser beaucoup d’espace inutilisé si les objets sont petits ou mal agencés

### Best Fit (BF)

- Pour chaque objet, parcourt tous les bacs déjà ouverts.
- Il le place dans **le bac dans lequel il reste le moins d’espace après insertion**, à condition que l’objet tienne.
- Si aucun bac ne convient, **un nouveau bac est ouvert**.

> Complexité similaire à FF avec des structures adaptées (`O(n log n)`)

**Avantages** :

- Cherche à **minimiser le vide** dans les bacs
- Moins de "gaspillage d’espace" que First Fit dans certains cas

**Inconvénients** :

- Plus lent que FF si aucune structure de tri n’est utilisée
- Sensible à l’ordre d’arrivée des objets

### First Fit Decreasing (FFD)

- **Trie d’abord** les objets **par taille décroissante**
- Puis applique l’algorithme **First Fit** sur cette liste triée

> Complexité : `O(n log n)` (pour le tri)  
> Garantie d’approximation : **`FFD(I) ≤ (11/9 × OPT) + 1`** où `OPT` est le nombre optimal de bacs

**Avantages** :

- Une des heuristiques les plus efficaces et connues pour le BPP
- Facile à implémenter
- Offre **une borne supérieure proche de l’optimal**

**Inconvénients** :

- Le tri initial peut être coûteux pour des très grandes instances
- Le résultat reste une approximation, pas garanti optimal

### Best Fit Decreasing (BFD)

- Variante de FFD utilisant **Best Fit** après tri décroissant.

> Performances souvent comparables à FFD

### Worst Fit (WF) _(moins courant)_

- Place chaque objet dans le bac avec **le plus d’espace libre** (le plus vide).
- Objectif : répartir les objets de façon équilibrée.

> Rarement meilleur que FF/BF en pratique.

### Algorithmes exacts (brute force, backtracking)

- On peut théoriquement **explorer toutes les répartitions possibles** des objets dans des bacs, pour trouver la solution exacte.
- Cela devient rapidement **intraitable** : le nombre de configurations possibles croît **exponentiellement** (`O(kⁿ)` avec `k` bacs).

> Utilisé uniquement pour **des instances très petites** ou pour comparer les performances des heuristiques.

## Algorithmes probabilistes pour le Bin Packing

Lorsque les méthodes exactes deviennent inapplicables à cause de la **taille du problème** ou que les heuristiques classiques donnent des résultats insatisfaisants, les **algorithmes probabilistes** apportent une alternative efficace pour :

- Explorer **rapidement** un **grand espace de solutions**
- Trouver des **solutions approchées** de bonne qualité
- Éviter les pièges des **pires cas déterministes**
- Répondre à des contraintes de **temps réel ou de ressources limitées**

Ces algorithmes reposent sur l’introduction de **hasard contrôlé** dans le processus de résolution.  
On distingue deux grandes approches : les méthodes de type **Las Vegas** (résultat exact mais variable) et les méthodes **Monte Carlo** (temps fixe, résultat approximatif).

### Las Vegas : bin packing avec randomisation des ordres

Il s’agit de versions probabilistes des algorithmes **First Fit** ou **Best Fit**, où l’on introduit de l’aléa **dans l’ordre de traitement des objets**. Le reste de l’algorithme reste inchangé.

- Chaque exécution est **valide** (aucune contrainte violée).
- Le résultat (nombre de bacs utilisés) peut **varier d’une exécution à l’autre**.
- En répétant plusieurs fois, on **garde la meilleure solution trouvée**.

#### Exemple de stratégie

```txt
1. On mélange aléatoirement la liste des objets
2. On applique First Fit ou Best Fit
3. On répète cela plusieurs fois
4. On conserve la solution la plus économique (moins de bacs)
```

#### Avantages

- Très simple à implémenter à partir d’un code existant
- Peu coûteux si le nombre d’itérations reste modéré
- Efficace pour échapper aux mauvaises configurations

#### Inconvénients

- Pas de garantie de performance (même après 1000 essais, on peut rester loin de l’optimum)
- Nécessite de fixer un nombre d’itérations maximal
- Sensible à la qualité de la fonction de randomisation

### Monte Carlo : heuristiques stochastiques

Ici, on accepte que la solution puisse être **approximative**, en échange d’un **temps d’exécution borné et prévisible**.  
Ces algorithmes visent à **explorer l’espace des répartitions** à l’aide de mécanismes inspirés de la nature, de la physique ou du vivant.

Parmi les approches les plus connues :

- **Recuit simulé (Simulated Annealing)** : métaphore du refroidissement d’un métal
- **Algorithmes évolutionnaires / génétiques** : inspirés de la sélection naturelle
- **Recherche tabou avec aléa** : exploration des voisins avec mémoire

Ces méthodes sont particulièrement adaptées à des problèmes où la fonction de coût est **complexe, non linéaire** ou où **de nombreuses solutions proches coexistent**.

#### Exemple : recuit simulé

**Principe général** :

1. On part d’une solution initiale (souvent générée par FFD ou BF)
2. On génère un **voisin** de cette solution en modifiant légèrement la répartition (déplacement, échange)
3. On **accepte ou rejette** ce voisin selon une **fonction de probabilité** dépendant d’une **température T**
4. La température décroît au fil des itérations → l’algorithme devient progressivement plus **conservateur**

> Cela permet d’**accepter des solutions moins bonnes temporairement**, pour **éviter les minima locaux** et atteindre un meilleur compromis global.

**Avantages** :

- Capable de s’approcher de l’optimal même sur de très grandes instances
- Très flexible (on peut adapter la fonction d’énergie, la structure de voisinage, etc.)
- Applicable à des variantes du bin packing (multidimensionnel, capacitaire, etc.)

**Inconvénients** :

- Nécessite de **régler finement** les paramètres (température initiale, taux de décroissance…)
- La qualité finale dépend fortement de ces réglages
- Peut être lent à converger si mal paramétré

## Exemple : randomized First Fit

### Objectif

Mettre en œuvre une **stratégie simple et probabiliste** basée sur l’algorithme **First Fit**, mais en explorant différents **ordres aléatoires** des objets.

Cette approche permet de **trouver de meilleures solutions** qu’un unique passage déterministe, en évitant les mauvaises configurations dues à un ordre initial défavorable.

### Stratégie

1. Mélanger la liste des objets de manière aléatoire
2. Appliquer l’algorithme **First Fit**
3. Répéter ce processus plusieurs fois (`trials`)
4. Conserver la **meilleure solution trouvée** (c’est-à-dire le plus petit nombre de bacs)

### Code Python

```python
import random

def first_fit(objects):
    bins = []
    for obj in objects:
        placed = False
        for b in bins:
            if sum(b) + obj <= 1.0:
                b.append(obj)
                placed = True
                break
        if not placed:
            bins.append([obj])
    return bins

def randomized_bin_packing(objects, trials=100):
    best_bins = None
    for _ in range(trials):
        shuffled = objects[:]
        random.shuffle(shuffled)
        bins = first_fit(shuffled)
        if best_bins is None or len(bins) < len(best_bins):
            best_bins = bins
    return best_bins
```

### Exemple d'utilisation

```python
objs = [0.4, 0.3, 0.6, 0.5, 0.2]
solution = randomized_bin_packing(objs, trials=1000)
print(f"Nombre de bacs utilisés : {len(solution)}")
```

> En répétant l’algorithme 1000 fois, on obtient souvent une solution très proche de l’**optimum minimal**, sans garantie mais avec une probabilité élevée de succès.

## Complexité

### Algorithmes déterministes

- **First Fit** et **Best Fit** : `O(n × m)` ou `O(n log n)` avec structures triées
- **First Fit Decreasing (FFD)** :
  - Tri initial : `O(n log n)`
  - Placement : `O(n log n)`
  - **Garantie d’approximation** : `FFD(I) ≤ (11/9 × OPT) + 1`

→ Très efficaces dans la pratique pour des instances moyennes.

### Algorithmes Las Vegas

- Exemple : Randomized First Fit
- Complexité : `O(trials × n log n)` (si le placement est optimisé)
- Résultat **toujours valide**
- Qualité de la solution dépend du **nombre d’essais** et de la **chance**

→ On peut fixer une limite de temps ou de tentatives, et ajuster dynamiquement.

### Algorithmes Monte Carlo

- Exemple : Recuit simulé, algorithmes génétiques
- Complexité typique : `O(k × n)` pour `k` itérations
- Résultat **non garanti exact** mais souvent **très bon**
- Probabilité d’erreur ou de sous-optimisation **contrôlable** via les paramètres

→ Approprié pour les **grandes instances**, les systèmes **en ligne**, ou les **problèmes multidimensionnels** où les heuristiques classiques échouent.

## Applications du Bin Packing

Le **Bin Packing Problem** a de très nombreuses applications concrètes, dans des domaines où il faut **optimiser l’utilisation d’une ressource finie** :

### Informatique

- **Allocation mémoire** : regrouper des blocs mémoire dans des pages physiques
- **Cloud computing** : placer des machines virtuelles sur des serveurs physiques avec capacité fixe
- **Gestion de bande passante** : répartir des flux dans des canaux de capacité limitée

### Logistique et transport

- **Chargement de conteneurs** : optimiser l’espace dans des camions, avions, cargos
- **Stockage d’objets** dans des entrepôts avec volumes limités
- **Planification de livraisons** en regroupant des colis par poids/volume

### Industrie

- **Découpe de matériaux** : textile, verre, bois, métal (version "Cutting Stock Problem")
- **Production industrielle** : regroupement de lots de production pour éviter les pertes

### Publicité et multimédia

- **Placement d’annonces** : regrouper des publicités dans des emplacements de taille fixe
- **Encodage vidéo** : empaquetage de fragments dans des segments limités en taille

### Autres

- **Ordonnancement de tâches** : allouer des tâches sur des machines avec capacité CPU/temps
- **Planification de ressources** : dans les jeux, l’éducation, ou les événements

> Le Bin Packing est donc **à la fois théorique et profondément appliqué**, ce qui en fait un excellent exemple pour introduire **les méthodes heuristiques et probabilistes** en algorithmique.
