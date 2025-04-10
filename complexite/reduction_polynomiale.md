# Réduction polynomiale

## Pourquoi parle-t-on de réduction polynomiale ?

### Définition intuitive

Lorsqu’on fait face à un problème difficile à résoudre directement, une approche classique consiste à le **transformer** en un autre problème pour lequel on connaît une méthode de résolution efficace. C’est le principe des **réductions polynomiales**.

Une **réduction polynomiale** d’un problème A à un problème B consiste à transformer **chaque instance du problème A** en une **instance équivalente du problème B**, de manière à ce que les réponses soient les mêmes (oui ou non), et que cette transformation soit **effectuée en temps polynomial** par rapport à la taille de l’entrée.

Autrement dit, plutôt que de chercher une solution directe à A, on "traduira" A en B, résoudra B, puis interprètera la solution pour répondre à A.

Cela permet notamment d’**évaluer la difficulté relative** entre deux problèmes. Si on parvient à réduire A à B efficacement, alors **résoudre B permet aussi de résoudre A**.

---

### Définition formelle

On dit qu’un problème A se **réduit en temps polynomial** à un problème B, ce que l’on note **A ≤p B**, s’il existe une **fonction de transformation f**, calculable en temps polynomial, telle que :

- Pour toute instance x de A, f(x) est une instance du problème B ;
- x est une instance dont la réponse est "oui" pour A **si et seulement si** f(x) est une instance dont la réponse est "oui" pour B.

Cette définition implique deux conditions essentielles :

1. **Temps polynomial** : la transformation de x en f(x) doit pouvoir se faire efficacement, c’est-à-dire en un nombre d’étapes borné par un polynôme en la taille de x. Cela garantit que la réduction elle-même ne crée pas un nouveau problème difficile à calculer.

2. **Conservation de la réponse** : il ne suffit pas de transformer le problème ; il faut aussi que la solution soit conservée. La réponse obtenue pour B doit correspondre à la réponse pour A.

Grâce à cette construction, si l'on dispose d'un algorithme pour résoudre B (même si B est un problème complètement différent de A en apparence), on peut **résoudre A en combinant cette transformation et la résolution de B**.

---

### Intuition et intérêt pratique

Ce concept est fondamental en algorithmique, et notamment dans l’étude des problèmes de complexité **NP** et **NP-complets**. Voici pourquoi :

- Une réduction polynomiale permet de montrer que **résoudre un problème A n’est pas plus dur que résoudre un autre problème B**.
- En particulier, si A est un problème pour lequel **on ne connaît pas d’algorithme efficace**, et qu’on parvient à le réduire à un autre problème B qui **est bien connu et supposé difficile**, cela donne **une indication forte sur la complexité de A**.
- C’est ainsi qu’ont été identifiés les **problèmes NP-complets** : ceux vers lesquels on peut réduire en temps polynomial tous les problèmes de NP.

### Notation et vocabulaire

- **A** et **B** désignent des **problèmes de décision** (dont la réponse est "oui" ou "non"), comme par exemple le TSP ou le problème du sac à dos.
- L'écriture **A ≤p B** signifie que **le problème A se transforme en B** en **temps polynomial**.
- Une **réduction polynomiale** garantit que la transformation d’une instance de A en une instance de B se fait en un **temps raisonnable** (borné par un polynôme en fonction de la taille de l’entrée).
- Une réduction est dite **correcte** si l’instance transformée donne **la même réponse** que l’originale : si A répond "oui", alors B aussi.
- Une réduction est dite **complète** si elle peut être appliquée à **tout problème d'une classe de complexité donnée** (comme tous les problèmes de NP).

---

## 2. Intérêt des réductions

Les réductions polynomiales jouent un rôle fondamental en algorithmique et en théorie de la complexité. Elles permettent de relier les problèmes entre eux, de les comparer en termes de difficulté, et de mieux comprendre les limites des algorithmes que nous pouvons concevoir.

Voici les principaux intérêts :

- **Identifier des problèmes NP-complets**  
  Lorsqu'on arrive à réduire un problème connu pour être difficile (déjà prouvé NP-complet) à un nouveau problème, cela permet de montrer que ce dernier est **au moins aussi difficile**. Si le nouveau problème est aussi dans la classe NP, on peut alors conclure qu’il est **NP-complet**. Ce mécanisme a permis, à partir du premier problème NP-complet (SAT, via le théorème de Cook), d’identifier des dizaines d’autres problèmes tout aussi complexes.

- **Prouver qu’un problème n’a probablement pas d’algorithme efficace**  
  Si un problème peut être réduit à un autre problème NP-complet, cela suggère qu’il est **peu probable qu’il puisse être résolu en temps polynomial**, à moins que P = NP. C’est un **argument indirect**, mais très puissant, pour **démontrer la difficulté d’un problème**. Cela évite de passer du temps à chercher un algorithme rapide là où il est très probable qu’aucun n’existe.

- **Trouver des stratégies de résolution indirectes**  
  Parfois, au lieu d’inventer un nouvel algorithme pour un problème donné, il est plus judicieux de le reformuler (par une réduction) en un problème pour lequel il existe déjà des outils efficaces ou bien étudiés. Cela permet d’**exploiter les algorithmes existants** pour résoudre indirectement le problème initial.

- **Utiliser les réductions dans des raisonnements par l’absurde**  
  Les réductions sont souvent utilisées dans des **preuves par contradiction**. Par exemple, si on suppose qu’un problème A peut être résolu efficacement (en temps polynomial), alors, par réduction, on pourrait aussi résoudre un problème B que l’on sait être difficile (comme un problème NP-complet). Cette contradiction indique que notre hypothèse de départ est probablement fausse. Autrement dit, si résoudre A permettrait de résoudre un problème réputé difficile, alors A est lui aussi difficile.

---

## 3. Exemple simple : réduction du **problème de la clique** au **problème de la couverture de sommets**

Pour bien comprendre l’intérêt et le fonctionnement d’une réduction polynomiale, prenons un exemple classique : la réduction du problème de la **clique** à celui de la **couverture de sommets** (*Vertex Cover*).

### Description des deux problèmes

- **Problème de la clique** : étant donné un graphe non orienté G = (V, E) et un entier k, existe-t-il un sous-ensemble de k sommets dans G formant une **clique** ?  
  Autrement dit, peut-on trouver k sommets tels que **chaque paire de sommets de cet ensemble soit reliée par une arête** dans G ?

- **Problème de la couverture de sommets** (*Vertex Cover*) : étant donné un graphe G = (V, E) et un entier k, existe-t-il un ensemble de k sommets qui **touche toutes les arêtes du graphe** ?  
  Autrement dit, peut-on choisir k sommets tels que **chaque arête du graphe ait au moins un de ses deux sommets dans cet ensemble** ?

### Objectif de la réduction

Nous allons montrer que si nous savons résoudre efficacement le problème de la couverture de sommets, alors nous pouvons aussi résoudre efficacement le problème de la clique, grâce à une réduction polynomiale.

### Principe de la réduction

L’idée est de transformer une instance du problème de la clique en une instance équivalente du problème de la couverture de sommets, de manière à ce que **la réponse "oui" à l’un implique une réponse "oui" à l’autre**.

Voici les grandes étapes de la transformation :

1. On part d’un graphe G = (V, E) et d’un entier k (la taille de la clique recherchée).
2. On construit le **complémentaire** de G, noté G’, c’est-à-dire un graphe qui a les **mêmes sommets**, mais où une arête est présente dans G’ si et seulement si elle **n’est pas présente dans G**.
3. On cherche alors une **couverture de sommets** de taille **|V| - k** dans G’.

Pourquoi cela fonctionne-t-il ? Car une **clique de taille k dans G** correspond à un ensemble de **k sommets totalement non connectés dans G’** (puisque les arêtes de G y sont absentes). Les **arêtes restantes dans G’** (celles entre les sommets non inclus dans la clique) doivent alors être couvertes par les **|V| - k** autres sommets.

### Justification de la correspondance

- Si G contient une clique de taille k, alors il existe un ensemble de |V| - k sommets qui couvrent toutes les arêtes de G’.
- Inversement, si G’ possède une couverture de sommets de taille |V| - k, alors les k sommets restants forment une clique dans G.

Ainsi, résoudre le problème de Vertex Cover sur G’ avec le paramètre |V| - k revient à résoudre le problème de la clique sur G avec le paramètre k.

### Conclusion

Cette transformation est efficace (elle peut être effectuée en temps polynomial), et elle préserve la réponse (oui ou non) du problème initial. Il s’agit donc bien d’une **réduction polynomiale**.

---

## 4. Exemple : réduction du **problème du voyageur de commerce (TSP)** au **problème du cycle hamiltonien**

Cet exemple permet d’illustrer comment un problème d’optimisation (le TSP) peut être relié à un problème de décision bien connu : l’existence d’un **cycle hamiltonien**. Cela nous montre également comment adapter les instances et les paramètres pour qu’une solution de l’un fournisse une solution de l’autre.

### Présentation des deux problèmes

- **Problème du voyageur de commerce (TSP)** : on dispose d’un graphe complet pondéré (chaque arête a un coût). Le but est de trouver un cycle (appelé "tournée") qui passe une seule fois par chaque sommet (ville), revient au point de départ, et dont le **coût total est inférieur ou égal à une borne k**. C’est un problème d’optimisation, mais il peut être formulé comme un **problème de décision** : "Existe-t-il un cycle hamiltonien de coût total inférieur ou égal à k ?"

- **Problème du cycle hamiltonien** : étant donné un graphe non pondéré, peut-on trouver un cycle simple qui **passe une et une seule fois par chaque sommet**, et revient au point de départ ? Il s’agit d’un **problème de décision** classique, connu pour être NP-complet.

### Objectif de la réduction

Nous allons montrer comment transformer une instance du problème du cycle hamiltonien en une instance du TSP, de manière à ce que **résoudre le TSP permette de répondre à la question du cycle hamiltonien**. Autrement dit, on veut prouver que **le problème du cycle hamiltonien se réduit en temps polynomial au TSP**.

### Construction de la réduction

1. **On part d’un graphe non pondéré G = (V, E)**, qui représente une instance du problème du cycle hamiltonien. Le graphe peut être quelconque, et toutes les arêtes ont le même "coût implicite" (disons 1).

2. **On construit un graphe complet G’ = (V, E’)**, c’est-à-dire un graphe contenant **toutes les arêtes possibles** entre les sommets de G. Ce graphe sera l’entrée de notre instance du TSP.

3. On assigne un **poids aux arêtes** dans G’ :
   - Si une arête existe déjà dans le graphe original G, alors elle garde un poids **égal à 1**.
   - Si une arête n’existe pas dans G, c’est-à-dire qu’elle a été ajoutée dans G’ pour le compléter, alors on lui assigne un **poids de 2** (ou un poids supérieur à 1 en général).

4. **On fixe la borne k à n**, où **n est le nombre de sommets du graphe**. Cette valeur correspond au coût total d’un cycle qui n’utilise que des arêtes de poids 1 (celles qui existaient dans le graphe initial).

### Justification de la réduction

- Si **G possède un cycle hamiltonien**, alors ce cycle est constitué uniquement d’arêtes de poids 1 dans G’. Il correspond donc à une solution au TSP de coût total exactement égal à n.

- Si **G ne possède pas de cycle hamiltonien**, alors **toute tournée passant par tous les sommets** dans G’ devra nécessairement inclure au moins une arête de poids 2. Le coût total de cette tournée sera alors **strictement supérieur à n**.

Ainsi, **résoudre le TSP avec la borne k = n** dans ce graphe G’ revient à **répondre à la question du cycle hamiltonien dans G**. La transformation du graphe G en G’, et l’affectation des poids, se fait en **temps polynomial**, ce qui en fait bien une réduction polynomiale.

### Conclusion

Cette réduction permet de montrer que **le problème du cycle hamiltonien se réduit au TSP**, ce qui signifie que **TSP est au moins aussi difficile**. Comme le problème du cycle hamiltonien est NP-complet, cela contribue à montrer que **TSP est lui aussi NP-complet** (dans sa version de décision). Cette démarche est une des méthodes classiques pour établir la complexité d’un nouveau problème à partir d’un problème déjà connu.
---

## 5. Exemple : réduction du **problème de la somme des sous-ensembles (Subset Sum)** au **problème du sac à dos (Knapsack)**

Cet exemple illustre comment un problème d’arithmétique simple peut être transformé en une version plus générale, ici le problème bien connu du sac à dos. L’objectif est de montrer que **résoudre le problème du sac à dos permet de résoudre Subset Sum**, à travers une réduction polynomiale.

### Présentation des deux problèmes

- **Problème de la somme des sous-ensembles (Subset Sum)** : étant donné un ensemble d’entiers positifs et une valeur cible T, existe-t-il un **sous-ensemble de ces entiers dont la somme est exactement égale à T** ?  
  C’est un problème de décision classique : la réponse est "oui" s’il existe un tel sous-ensemble, "non" sinon.

- **Problème du sac à dos (Knapsack)** : on dispose d’un ensemble d’objets, chacun avec un **poids** et une **valeur**. On fixe une capacité maximale du sac (W) et une valeur minimale cible (V). Le problème est de savoir s’il existe un sous-ensemble d’objets **dont la somme des poids n’excède pas W** et **dont la somme des valeurs est au moins V**.

Dans sa version de décision, Knapsack pose la question suivante : *Existe-t-il un sous-ensemble d’objets dont le poids total ≤ W et la valeur totale ≥ V ?*

### Objectif de la réduction

Nous cherchons à **transformer une instance de Subset Sum en une instance équivalente de Knapsack**, afin que résoudre le second revienne à répondre à la question du premier. L’objectif est de construire cette transformation de manière simple et efficace (en temps polynomial).

### Construction de la réduction

Soit une instance de Subset Sum donnée par :

- Un ensemble d’entiers positifs : {a₁, a₂, ..., aₙ}
- Une valeur cible T

Pour obtenir une instance équivalente du problème du sac à dos, on procède comme suit :

1. On considère que chaque entier aᵢ représente à la fois le **poids** et la **valeur** d’un objet dans Knapsack.
   - Poids de l’objet i : wᵢ = aᵢ
   - Valeur de l’objet i : vᵢ = aᵢ

2. On fixe la **capacité maximale du sac** à **T** : W = T

3. On fixe également la **valeur minimale souhaitée** à **T** : V = T

L’instance de Knapsack ainsi construite pose alors la question suivante : *Existe-t-il un sous-ensemble d’objets dont la somme des poids est ≤ T et la somme des valeurs est ≥ T ?*

Mais puisque poids = valeur pour tous les objets, cela revient à demander s’il existe un sous-ensemble d’entiers dont **la somme est exactement égale à T**.

### Justification de la réduction

- Si la réponse à Subset Sum est "oui", alors il existe un sous-ensemble d’entiers dont la somme est T. Ce même sous-ensemble correspond à des objets dont le poids total est ≤ T (exactement T) et la valeur totale est ≥ T (exactement T), donc c’est une solution valide pour Knapsack.

- Si la réponse à Knapsack est "oui" dans cette configuration, alors le sous-ensemble sélectionné a poids total ≤ T et valeur ≥ T. Puisque poids = valeur, cela implique que la somme est exactement T, donc c’est aussi une solution pour Subset Sum.

La transformation est donc correcte, et comme elle ne fait qu’associer chaque entier à une paire (poids, valeur), elle est **réalisable en temps polynomial**. Il s’agit bien d’une **réduction polynomiale**.

### Conclusion

Cette réduction montre que **Subset Sum est un cas particulier du problème du sac à dos**. Elle permet d’utiliser les résultats connus sur Knapsack (par exemple, sa NP-complétude) pour en déduire des résultats sur Subset Sum. Cela illustre comment, en complexité algorithmique, des problèmes différents en apparence peuvent être **profondément liés** par des transformations simples mais puissantes.
