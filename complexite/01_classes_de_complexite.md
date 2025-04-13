# Cours : Introduction à la Complexité Algorithmique et aux Problèmes NP-Complets

---

## Table des matières

1. [Introduction aux Problèmes Algorithmiques](#1-introduction-aux-problèmes-algorithmiques)
2. [Problèmes de Décision et d’Optimisation](#2-problèmes-de-décision-et-doptimisation)
3. [La Machine de Turing](#3-la-machine-de-turing)
4. [Classes de Complexité](#4-classes-de-complexité)
5. [Réduction Polynômiale](#5-réduction-polynômiale)
6. [Théorème de Cook](#6-théorème-de-cook)
7. [Exemple : Problème du Voyageur de Commerce (TSP)](#7-exemple-problème-du-voyageur-de-commerce-tsp)
8. [Questions de Validation](#8-questions-de-validation)
9. [Exemples Supplémentaires](#9-exemples-supplémentaires)
10. [Conclusion](#10-conclusion)

---

## 1. Introduction aux Problèmes Algorithmiques

**Définition d’un problème algorithmique :**
Un problème algorithmique est composé de deux éléments principaux :

- **Format des données d’entrée :** Les données sont codées généralement en binaire (parfois en unaire pour les problèmes pseudo-polynômiaux) et définissent un ensemble de définitions pour chaque donnée.
- **Question posée :** Une question spécifique sur ces données.

**Exemple :**

- **Problème du tri :** Comment réorganiser une liste de nombres dans l'ordre croissant ?
- **Format des données d'entrée :** Une liste de nombres entiers.
- **Question posée :** Quelle est l'ordre croissant des nombres dans la liste ?

**Instance de problème :**
Une instance est un ensemble de valeurs respectant le format de données. Par exemple, pour le problème du cycle eulérien, une instance serait un graphe avec un sommet de départ.

## 2. Problèmes de Décision et d’Optimisation

**Problème de décision :**
Un problème algorithmique dont la question admet comme réponse soit « oui », soit « non ».

**Exemple :**

- **Problème de décision pour le tri :** Existe-t-il une permutation de la liste qui est dans l'ordre croissant ?

**Problème d’optimisation associé à un problème de décision :**
Pour convertir un problème d’optimisation en un problème de décision, on associe une condition de limite. Par exemple, pour le problème du plus court chemin :

- **Problème de décision :** Étant donné un graphe G, deux sommets u et v de G, et un entier k, existe-t-il un chemin de u vers v, de taille inférieure ou égale à k ?
- **Problème d’optimisation :** Quelle est la plus petite valeur de k pour laquelle la réponse est « oui » ?

**Exemple :**

- **Problème d'optimisation :** Trouver le chemin le plus court entre deux points dans un graphe.

## 3. La Machine de Turing

**Définition :**
Proposée par Alan Turing, une machine de Turing est un modèle mathématique de calculateur défini par :

- Un ensemble fini d’états possibles.
- Un alphabet de symboles incluant le symbole vide.
- Une fonction de transition associant à chaque couple (état, symbole) un triplet (état, symbole, sens de déplacement).
- L’ensemble des états acceptants.
- Un état initial.

**Fonctionnement :**
À chaque étape, la machine lit le symbole sur la bande, applique la fonction de transition, change d’état, écrit un nouveau symbole, et se déplace sur la bande.

**Exemple :**

- **Machine de Turing pour l'incrémentation :** Une machine de Turing qui lit une représentation binaire d'un nombre, l'incrémente de 1, et écrit le résultat sur la bande.

## 4. Classes de Complexité

### Classe P

**Définition :**
La classe P regroupe les problèmes de décision qui peuvent être résolus en temps polynomial par une machine de Turing déterministe. En d'autres termes, il existe un algorithme qui résout le problème en un temps O(p(n)), où p est un polynôme et n la taille de l'entrée.

**Caractéristiques :**

- **Problèmes faciles :** Considérés comme "faciles" ou "tractables" car ils peuvent être résolus en un temps raisonnable même pour des entrées de grande taille.
- **Exemples :** Tri de nombres (quicksort, mergesort), recherche dans un tableau trié (recherche dichotomique), le problème du plus court chemin (algorithme de Dijkstra).

### Classe NP

**Définition :**
La classe NP (Non-déterministe Polynomial) regroupe les problèmes de décision pour lesquels une solution candidate peut être vérifiée en temps polynomial par une machine de Turing déterministe. Cela signifie qu’il existe un algorithme qui peut vérifier la validité d'une solution donnée en temps polynomial.

**Caractéristiques :**

- **Certificat vérifiable en temps polynomial :** Une solution proposée (certificat) peut être vérifiée rapidement, même si trouver cette solution peut être difficile.
- **Exemples :** Problème du voyageur de commerce (TSP), problème de la clique, problème de la satisfiabilité (SAT).

### Classe co-NP

**Définition :**
La classe co-NP regroupe les problèmes de décision dont le complément est dans NP. Autrement dit, un problème est dans co-NP si, lorsqu’une solution n'existe pas, il est possible de vérifier cette non-existence en temps polynomial.

**Caractéristiques :**

- **Vérification de la non-solution :** Pour les problèmes de co-NP, il est possible de vérifier rapidement qu'une solution n'existe pas.
- **Exemples :** Non-primalité d’un nombre (vérifier qu’un nombre est composé).

### Classe NP-Complet

**Définition :**
Un problème est NP-Complet s’il est dans NP et qu'il est aussi difficile que tout autre problème dans NP. Autrement dit, tout problème dans NP peut être réduit en temps polynomial à ce problème.

**Caractéristiques :**

- **Difficile à résoudre et à vérifier :** Les problèmes NP-Complets sont les plus difficiles à résoudre au sein de NP. S’il existe un algorithme en temps polynomial pour l’un de ces problèmes, alors tous les problèmes dans NP peuvent être résolus en temps polynomial (ce qui impliquerait que P=NP).
- **Exemples :** Problème SAT, problème du voyageur de commerce (TSP), problème du sac à dos.

### Classe NP-Difficile

**Définition :**
Un problème est NP-Difficile s’il est au moins aussi difficile que les problèmes dans NP. Contrairement aux problèmes NP-Complets, un problème NP-Difficile n’a pas besoin d’être dans NP, ce qui signifie qu'il peut ne pas être un problème de décision.

**Caractéristiques :**

- **Réduction polynomiale :** Tout problème dans NP peut être réduit en temps polynomial à un problème NP-Difficile.
- **Exemples :** Problèmes d’optimisation associés aux problèmes NP-Complets, tels que trouver le tour le plus court dans le TSP.

### Classe co-NP-Complet

**Définition :**
Un problème est co-NP-Complet s’il est dans co-NP et qu’il est aussi difficile que tout autre problème dans co-NP.

**Caractéristiques :**

- **Difficile à vérifier l'absence de solution :** Les problèmes co-NP-Complets sont les plus difficiles à vérifier l'absence de solution au sein de co-NP.
- **Exemples :** Complément des problèmes NP-Complets, tels que le problème UNSAT (vérifier qu’aucune assignation ne satisfait une formule logique).

### Résumé Visuel des Relations

- P ⊆ NP
- P ⊆ co-NP
- NP ∩ co-NP (les problèmes qui sont à la fois dans NP et co-NP)
- NP ⊆ NP-Difficile
- NP-Complète ⊆ NP ⊆ NP-Difficile

## 5. Réduction Polynômiale

**Définition :**
Une réduction polynômiale permet de transformer une instance d’un problème en une instance d’un autre problème en temps polynomial, tout en conservant la réponse. Si un problème A se réduit en temps polynomial à un problème B, alors A est au moins aussi difficile à résoudre que B.

**Exemple :**

- **Réduction du problème de la clique au problème de la couverture de sommets :** On peut montrer que trouver une clique de taille k dans un graphe est aussi difficile que trouver une couverture de sommets de taille |V| - k.

**Propriétés :**

- Si A peut être résolu en temps polynomial et que A se réduit à B, alors B peut être résolu en temps polynomial.
- Si B ne peut pas être résolu en temps polynomial et que A se réduit à B, alors A ne peut pas être résolu en temps polynomial.

**Processus de Réduction :**

1. **Transformation des Données d’Entrée :**

   - Convertir une instance du problème A en une instance du problème B.
   - Cette transformation doit se faire en temps polynomial par rapport à la taille de l’instance de A.

2. **Transformation de la Solution :**
   - Si on trouve une solution pour l’instance du problème B, cette solution doit être convertible en une solution valide pour l’instance du problème A.
   - Cette transformation doit également se faire en temps polynomial.

**Exemple de Réduction :**

**Problème de la Couverture de Sommets (Vertex Cover) :**

- **Problème A (Vertex Cover) :** Trouver un ensemble de sommets de taille k tels que chaque arête du graphe est incidente à au moins un sommet de cet ensemble.
- **Problème B (Clique) :** Trouver un sous-graphe complet de taille k (c'est-à-dire une clique de k sommets).

**Réduction :**

- Transformer une instance du problème de la clique en une instance du problème de la couverture de sommets :
  1. Complémenter le graphe : Construire un graphe complémentaire où les arêtes sont celles qui ne sont pas présentes dans le graphe original.
  2. Si le graphe original a une clique de taille k, alors son complémentaire a une couverture de sommets de taille |V| - k.

**Exemple concret :**

- Soit un graphe G avec les sommets {A, B, C, D} et les arêtes {AB, BC, CD}.
- Le graphe complémentaire G' aura les arêtes {AC, AD, BD}.
- Si le graphe G a une clique de taille 2 (disons {A, B}), alors le graphe complémentaire G' a une couverture de sommets de taille 2 (les sommets restants C et D).

## 6. Théorème de Cook

Le théorème de Cook démontre que le problème SAT (satisfiabilité) est NP-Complet, établissant la base pour prouver que d’autres problèmes sont NP-Complets.

**Exemple :**

- **Problème SAT :** Étant donné une formule logique, existe-t-il une assignation des variables qui rend la formule vraie ?

## 7. Exemple : Problème du Voyageur de Commerce (TSP)

**Définition :**
Le problème du TSP consiste à trouver le chemin le plus court permettant de visiter un ensemble de villes une seule fois et de revenir au point de départ.

**Problème de décision associé :**
Existe-t-il un cycle hamiltonien de longueur inférieure ou égale à k ?

**Optimisation :**
Trouver la plus petite valeur de k pour laquelle la réponse est « oui ».

**Exemple :**

- **Problème de décision TSP :** Étant donné un ensemble de villes et une distance k, existe-t-il un tour complet passant par chaque ville exactement une fois et ayant une longueur totale inférieure ou égale à k ?
- **Problème d'optimisation TSP :** Trouver le tour le plus court possible passant par toutes les villes une seule fois.

\*\*

Complexité :\*\*
Le TSP est NP-Complet. Cela signifie que, sauf si P=NP, il est improbable de trouver une solution optimale en temps polynomial.

## 8. Questions de Validation

1. **Que signifie NP ?**

   - Non déterministe Polynomial.

2. **Direction de la réduction pour prouver qu’un problème est NP-Complet :**

   - Transformez une instance du problème NP-Complet connu en une instance du problème à prouver.

3. **Problème de décision NP-Complet initial :**

   - Le problème SAT.

4. **Problème de décision associé à un problème d’optimisation avec un nombre exponentiel de solutions :**

   - Non nécessairement NP-Complet.

5. **Le problème de la n-coloration de graphe est-il dans NP ?**
   - Oui, vérifiable en temps polynomial.

---

## 9. Exemples Supplémentaires

- **Problème des dames :** Placer 8 dames sur un échiquier de 8x8 de manière à ce qu'aucune dame ne puisse en attaquer une autre. Le problème de décision serait de demander si une configuration donnée est correcte. Le problème d'optimisation pourrait être de trouver le placement optimal pour n dames sur un échiquier n x n.

- **Problème du sac à dos :** Remplir un sac à dos avec des objets de manière à maximiser la valeur totale sans dépasser la capacité. Le problème de décision demande si une certaine valeur peut être atteinte sans dépasser la capacité. Le problème d'optimisation cherche à maximiser cette valeur.

- **Problème du coloriage de graphe :** Colorier les sommets d'un graphe avec le minimum de couleurs, de manière à ce que deux sommets adjacents n'aient pas la même couleur. Le problème de décision serait de vérifier si un graphe peut être colorié avec k couleurs. Le problème d'optimisation consiste à trouver le nombre minimal de couleurs nécessaires.

## 10. Conclusion

**Implications :**
La résolution de problèmes NP-Complets en temps polynomial semble improbable, ce qui entraîne souvent l'utilisation d'heuristiques ou d'algorithmes d'approximation pour des solutions sous-optimales en pratique.

**Hypothèse P=NP :**
Si un jour on prouve que P=NP, cela signifierait que tous les problèmes NP-Complets peuvent être résolus en temps polynomial. Cependant, des solutions pratiques peuvent rester complexes en fonction du degré du polynôme et des constantes associées.
