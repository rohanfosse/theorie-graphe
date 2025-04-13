# Cours – Les Problèmes NP-Complets

## 1. Introduction

Dans le monde des algorithmes, certains problèmes posent un défi particulier :  
on peut **vérifier rapidement** si une solution proposée est correcte,  
mais on **ne sait pas forcément comment la trouver rapidement**.

Ces problèmes appartiennent à une classe appelée **NP** (_Non-déterministe Polynomial_), qui regroupe les problèmes de décision pour lesquels une solution peut être **vérifiée en temps polynomial**, même si la **trouver** peut prendre un temps exponentiel.

Parmi tous les problèmes de NP, il existe une sous-catégorie **cruciale** :  
les **problèmes NP-complets**.  
Ce sont, en quelque sorte, les **problèmes les plus difficiles de NP** : si l’on parvient à en résoudre un efficacement, **tous les autres deviennent également faciles à résoudre**.

> En résumé : Résoudre efficacement un seul problème NP-complet reviendrait à prouver que P = NP.  
> Cela bouleverserait la cryptographie, l’IA, l’optimisation… et toute l’informatique théorique.

## 2. Définitions fondamentales

### 2.1. Qu’est-ce que la classe NP ?

La classe **NP** contient les **problèmes de décision** pour lesquels :

- Une **solution peut être devinée** par une machine non déterministe
- Et **vérifiée efficacement** (en temps polynomial) sur une machine déterministe

Autrement dit, même si on **ne sait pas forcément comment trouver la solution**, on sait **dire rapidement si une proposition est correcte**.

> **Exemple :** le Sudoku (généralisé)  
> On ne sait pas toujours comment résoudre un Sudoku complexe rapidement,  
> mais si on te donne une grille remplie, tu peux vérifier en quelques secondes si c’est une solution valide.

### 2.2. Qu’est-ce qu’un problème NP-complet ?

Un problème est dit **NP-complet** s’il combine deux propriétés clés :

1. Il appartient à **NP** :  
   → donc, une solution peut être **vérifiée rapidement**

2. Il est **au moins aussi difficile** que tous les autres problèmes de NP :  
   → tout problème de NP peut être **transformé (réduit)** en une instance équivalente de ce problème **en temps polynomial**

Ces deux conditions font des problèmes NP-complets des **problèmes centraux** dans l’étude de la complexité algorithmique :

- Si un jour on trouve un algorithme **rapide (temps polynomial)** pour un problème NP-complet, alors **tous les problèmes de NP deviendront "faciles"**.
- Autrement dit, on aurait **P = NP**.

> **Exemple de NP-complet célèbre :** le problème SAT (satisfiabilité booléenne)  
> "Existe-t-il une assignation des variables d’une formule logique qui la rend vraie ?"

## 3. Pourquoi les problèmes NP-complets sont-ils si importants ?

Les **problèmes NP-complets** ne sont pas de simples curiosités théoriques : ils jouent un **rôle central en algorithmique et en informatique théorique**. Voici pourquoi leur étude est essentielle :

### 3.1. Pour comprendre la **difficulté intrinsèque** d’un problème

Lorsqu’on rencontre un nouveau problème algorithmique, on se pose une question cruciale :

> Existe-t-il un algorithme **rapide** (en temps polynomial) pour le résoudre ?

Si le problème est **NP-complet**, cela signifie qu’il est **au moins aussi difficile** que tous les problèmes de NP.  
**Conclusion :** il est **peu probable qu’un algorithme rapide existe**, sauf à prouver que **P = NP**.

### 3.2. Pour servir de **point de comparaison**

Les problèmes NP-complets agissent comme des **références universelles**.  
Si on parvient à **réduire un problème connu NP-complet** à un **nouveau problème**, cela signifie que le nouveau problème est **au moins aussi complexe**.

> C’est un outil fondamental pour **classer et comparer** la difficulté des problèmes.

### 3.3. Pour expliquer la **résistance à l’algorithmique classique**

Beaucoup de problèmes que l’on **rencontre dans la pratique** semblent "simples"... jusqu’à ce qu’on essaie de les programmer :

- Planification de tâches
- Ordonnancement d’examens
- Optimisation de tournées
- Résolution de puzzles ou jeux logiques…

Et pourtant, aucun algorithme efficace ne semble fonctionner **dans tous les cas**.  
→ Cela s’explique souvent par le fait que le problème est **NP-complet**, donc **fondamentalement difficile** à résoudre dans le pire des cas.

### 3.4. Parce qu’ils sont **partout en informatique**

Les problèmes NP-complets ne sont pas rares ni artificiels.  
On les retrouve dans **presque tous les domaines de l'informatique** :

| Domaine                   | Exemple de problème NP-complet              |
| ------------------------- | ------------------------------------------- |
| Optimisation              | Sac à dos, voyageur de commerce (TSP)       |
| Réseaux                   | Clique, couverture de sommets, coloration   |
| Logique                   | SAT, 3-SAT                                  |
| Intelligence artificielle | Planification d’actions, jeux combinatoires |
| Bioinformatique           | Alignement multiple, structures d’ARN       |
| Bases de données          | Requêtes optimales, jointures complexes     |
| Sécurité                  | Détection d’attaques par contraintes        |

## 4. Le premier problème NP-complet : **SAT** et le théorème de Cook

### 4.1. Le problème SAT

Le **problème SAT** (pour _Satisfiability_, ou **satisfiabilité**) est l’un des problèmes les plus fondamentaux de l’informatique théorique.

> **Énoncé** : Étant donnée une **formule logique** (composée de variables, ET, OU, NON...), existe-t-il une assignation de valeurs (vrai ou faux) aux variables qui **rend la formule vraie** ?

**Exemple** :

```text
(x ∨ y) ∧ (¬x ∨ z)
```

Est-elle satisfiable ? Oui, par exemple si `x = false, y = true, z = true`.

### 4.2. Pourquoi SAT est central ?

- **SAT est le premier problème** pour lequel on a démontré qu’il est **NP-complet**
- C’est à partir de SAT que **tous les autres problèmes NP-complets** ont été construits, par réduction polynomiale
- SAT est devenu un **point de départ historique** dans l’étude de la complexité algorithmique

### 4.3. Le théorème de Cook (1971)

Le **théorème de Cook**, démontré par **Stephen Cook** (et indépendamment par **Leonid Levin**), affirme que :

> **SAT est NP-complet**

Ce résultat a ouvert la voie à **l’étude systématique des problèmes difficiles**, et a introduit la notion même de **problème NP-complet**.

**Ce que Cook a prouvé :**

- SAT appartient à NP (on peut **vérifier** une solution rapidement)
- Tout problème de NP peut être **réduit à SAT en temps polynomial**

### 4.4. Formes usuelles de SAT

#### • SAT (forme générale)

Formules booléennes quelconques avec conjonctions (∧), disjonctions (∨) et négations (¬).

#### • CNF-SAT (forme normale conjonctive)

Forme standardisée où la formule est une **conjonction de clauses**, chaque clause étant une **disjonction de littéraux**.

**Exemple** :

```text
(¬x ∨ y ∨ z) ∧ (x ∨ ¬y)
```

#### • 3-SAT

Version de CNF-SAT où chaque clause contient exactement **3 littéraux**.  
→ Cette version **reste NP-complete**, même avec cette restriction !

### 4.5. Conséquence du théorème de Cook

> SAT est devenu **le "problème pivot"** de la complexité de type NP.  
> Tout nouveau problème pour lequel on soupçonne une complexité élevée est comparé à SAT.

C’est à partir de SAT qu’on a pu démontrer que des **centaines d’autres problèmes** sont NP-complets : TSP, CLIQUE, coloration de graphe, sac à dos...

### 4.6. En pratique

- SAT est **au cœur des SAT-solvers**, utilisés en :
  - **vérification de programmes**
  - **raisonnement automatique**
  - **cybersécurité**
  - **résolution de puzzles (ex : Sudoku)**
- Il existe aujourd’hui des outils capables de **résoudre efficacement des instances très complexes**, même si le problème reste NP-complet en théorie.

## 5. Comment prouver qu’un problème est NP-complet ?

Lorsqu’on soupçonne qu’un nouveau problème est aussi difficile que ceux de NP, on peut chercher à montrer qu’il est **NP-complet**.  
Cela se fait en deux étapes **essentielles et complémentaires** :

### Étape 1 : Montrer que le problème est dans NP

> Autrement dit, **peut-on vérifier rapidement (en temps polynomial) qu’une solution proposée est correcte ?**

Cela signifie que si quelqu’un nous donne une solution possible (un "certificat"), nous devons être capables de :

- Vérifier que cette solution est **valide**,
- Et le faire en **temps polynomial**, par exemple à l’aide d’un algorithme simple.

**Exemples :**

- Pour le problème du **sac à dos** (version décision) : si on propose une sélection d’objets, il suffit de **vérifier leur poids et leur valeur totale**.
- Pour le **problème de la clique** : si on donne un sous-ensemble de sommets, on peut vérifier **en combien de temps ?** → En `O(k²)` si la clique a k sommets.

### Étape 2 : Réduire un problème NP-complet connu au nouveau problème

> C’est le cœur de la démonstration : on **transforme une instance** d’un problème déjà connu comme étant NP-complet en **une instance équivalente** du nouveau problème, en **temps polynomial**.

Cette transformation doit répondre à deux critères :

- **Fidélité** : l’instance transformée donne une réponse "oui" si et seulement si l’instance d’origine donnait aussi "oui".
- **Efficacité** : la transformation doit être **polynomiale**, c’est-à-dire réalisable en un nombre raisonnable d’étapes selon la taille de l’entrée.

### Schéma général de la preuve

```text
SAT  ≤p  PROBLÈME NOUVEAU
```

- On part d’un problème **déjà connu comme NP-complet** (souvent SAT, 3-SAT, CLIQUE…),
- On le **réduit** à votre nouveau problème `P` en \*\*temps polynomial`,
- Et on montre que **toute solution pour P résout le problème d’origine**.

> Ainsi, si on parvient à résoudre P, alors on pourrait résoudre tous les autres problèmes de NP → donc P est NP-complet.

### Exemple simplifié

Prenons un exemple pédagogique :

- On veut prouver que le problème du **Vertex Cover** est NP-complet.
- On procède comme suit :
  1. On montre qu’un **candidat pour Vertex Cover peut être vérifié rapidement** → il est dans NP.
  2. On **réduit le problème de CLIQUE** (déjà connu comme NP-complet) à Vertex Cover.
     - On construit le **graphe complémentaire**,
     - Et on montre qu’une **clique de taille k** dans le graphe d’origine correspond à une **couverture de sommets de taille |V| - k** dans le graphe complémentaire.

## 6. Exemples de problèmes NP-complets

### Problèmes logiques et booléens

| Problème                 | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **SAT**                  | Formule booléenne satisfiable ?                     |
| **3-SAT**                | SAT restreint à des clauses de 3 littéraux          |
| **Clique**               | Existe-t-il une clique de taille k dans un graphe ? |
| **Coloration de graphe** | Peut-on colorier un graphe avec k couleurs ?        |

### Problèmes d’optimisation et combinatoires

| Problème                                     | Description                                                            |
| -------------------------------------------- | ---------------------------------------------------------------------- |
| **Problème du sac à dos** (version décision) | Peut-on atteindre une valeur au moins V sans dépasser une capacité W ? |
| **Voyageur de commerce (TSP)**               | Existe-t-il un circuit passant par toutes les villes de coût ≤ k ?     |
| **Partition**                                | Peut-on diviser un ensemble en deux sous-ensembles de sommes égales ?  |
| **Vertex Cover**                             | Existe-t-il un ensemble de k sommets couvrant toutes les arêtes ?      |

### Jeux, IA, planification

- Sudoku (généralisé)
- Sokoban (généralisé)
- Planification de tâches avec contraintes

## 8. Résolution pratique des problèmes NP-complets

### 8.1. Solutions exactes (mais lentes)

- **Backtracking** / Brute force : parcourt toutes les possibilités
- **Branch & Bound**
- **Programmation dynamique (cas limités)**

### 8.2. Solutions approchées ou heuristiques

- **Algorithmes gloutons**
- **Recuit simulé, génétiques, colonies de fourmis…**
- **Algorithmes d’approximation** (ex : 2-approximation pour Vertex Cover)

### 8.3. Méthodes modernes

- **SAT-solvers**
- **ILP (Programmation linéaire en nombres entiers)**
- **Méthodes hybrides ou méta-heuristiques**

## 9. Implications du problème P = NP

La question **P = NP ?** est l’une des plus profondes et célèbres de l’informatique théorique. Elle interroge un point fondamental :

> **Est-ce que tous les problèmes dont on peut vérifier une solution rapidement peuvent également être résolus rapidement ?**

Autrement dit : si une machine peut **vérifier** une réponse en temps polynomial, peut-elle aussi **trouver** cette réponse en temps polynomial ?

### Si **P = NP**

Cela signifierait que tous les problèmes NP, y compris les problèmes NP-complets, **auraient une solution efficace**. Les conséquences seraient majeures dans plusieurs domaines :

#### Cryptographie

La plupart des systèmes de cryptographie actuels (RSA, courbes elliptiques, etc.) reposent sur des problèmes supposés **inextricables à résoudre**, mais faciles à vérifier.  
Si P = NP, ces problèmes deviendraient solvables rapidement, ce qui **remettrait en cause la sécurité des communications numériques**, des données bancaires ou des systèmes d'identification.

#### Intelligence artificielle

De nombreuses tâches en planification automatique, raisonnement logique, diagnostic ou jeu relèvent de problèmes NP.  
Un algorithme efficace pour ces problèmes ouvrirait la voie à des **capacités de raisonnement automatisé** très avancées.

#### Optimisation

Dans les domaines de la logistique, de la gestion de ressources, de la production, de la bioinformatique ou de la finance, on traite souvent de problèmes NP-complets.  
Si P = NP, il deviendrait possible de **trouver directement les meilleures solutions**, là où aujourd’hui on se contente d’approximations.

#### Sciences et ingénierie

De nombreuses simulations (en biologie, en chimie, en physique des matériaux…) nécessitent de résoudre des problèmes combinatoires complexes.  
L’existence d’un algorithme efficace pourrait transformer la modélisation scientifique.

### Si **P ≠ NP**

C’est aujourd’hui l’hypothèse la plus largement admise. Elle signifie qu’il **existe des problèmes pour lesquels la solution est vérifiable rapidement, mais introuvable efficacement** dans le pire des cas.  
Cela justifie les efforts actuels dans :

- Le développement d’**heuristiques**, qui donnent de "bonnes" solutions sans garantie d’optimalité.
- Les **algorithmes d’approximation**, qui garantissent une solution proche de l’optimum.
- L’utilisation de **SAT-solvers**, de méthodes **probabilistes**, de **métaheuristiques** (algorithmes génétiques, recuit simulé...), etc.

Cela implique également qu’**aucun algorithme rapide universel** ne pourra résoudre tous les problèmes de NP, et que le travail du concepteur d’algorithmes reste central.

## Le statut de problème du millénaire

En l’an 2000, le **Clay Mathematics Institute** a sélectionné **sept grands problèmes non résolus** en mathématiques, connus sous le nom de **Problèmes du millénaire**. Chacun est assorti d’une récompense d’un million de dollars pour une démonstration rigoureuse.

Voici la liste de ces sept problèmes :

| Numéro | Problème                                                         | Domaine                         | Statut actuel |
| ------ | ---------------------------------------------------------------- | ------------------------------- | ------------- |
| 1      | **P = NP ?**                                                     | Informatique théorique          | Non résolu    |
| 2      | L'hypothèse de Riemann                                           | Théorie des nombres             | Non résolu    |
| 3      | La conjecture de Hodge                                           | Géométrie algébrique            | Non résolu    |
| 4      | L'existence et la régularité des solutions de Navier-Stokes      | Physique mathématique           | Non résolu    |
| 5      | La conjecture de Birch et Swinnerton-Dyer                        | Théorie des nombres             | Non résolu    |
| 6      | La conjecture de Poincaré (résolue en 2003 par Grigori Perelman) | Topologie                       | **Résolu**    |
| 7      | L'hypothèse de Yang-Mills                                        | Physique quantique mathématique | Non résolu    |

**Remarque :** seul le problème de la **conjecture de Poincaré** a été résolu à ce jour, mais son auteur a refusé le prix.

La question **P = NP ?** dépasse largement le cadre académique. Elle interroge les **limites fondamentales du calcul**, de la sécurité informatique, de l’intelligence artificielle et de la recherche opérationnelle.  
Qu’elle soit un jour résolue ou non, elle nous pousse à mieux comprendre :

- Ce qu’un algorithme peut faire efficacement,
- Ce qu’il ne pourra jamais faire dans des délais raisonnables,
- Et comment, malgré tout, on peut **concevoir des outils performants** pour approcher la complexité.
