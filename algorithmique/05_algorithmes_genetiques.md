# Algorithmes génétiques

## 1. Introduction

Les **algorithmes génétiques** sont une classe d’**algorithmes évolutionnaires** inspirés du fonctionnement de la **sélection naturelle**.  
Ils permettent de **résoudre des problèmes complexes d’optimisation** en **explorant un espace de solutions** à l’aide de mécanismes biologiques simulés tels que la **mutation**, la **sélection** et le **croisement** (recombinaison).

Ils sont particulièrement utiles lorsque :
- L’espace de recherche est immense
- La solution optimale est inconnue ou difficile à calculer
- Aucune méthode déterministe efficace n’existe



## 2. Principes biologiques simulés

Les algorithmes génétiques modélisent le processus de l'évolution :

- **Population** : ensemble de solutions candidates (appelées individus ou chromosomes)
- **Gènes** : composantes d'une solution (valeurs codées sous forme binaire, numérique ou symbolique)
- **Fitness** : mesure de la qualité d’une solution
- **Sélection** : favorise les meilleurs individus
- **Croisement** : combinaison de gènes entre individus pour créer une descendance
- **Mutation** : modification aléatoire de gènes pour explorer de nouvelles solutions



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



## 4. Exemple simple : maximiser une fonction

### Problème

Maximiser la fonction `f(x) = x²` pour `x` ∈ [0, 31]  
On code `x` comme un chromosome binaire sur 5 bits (par exemple : `x = 19 → "10011"`)



### Étapes de l’algorithme

1. **Population initiale** : ex. 6 individus aléatoires
2. **Fitness** : `f(x) = x²` pour chaque chromosome
3. **Sélection** : roulette ou tournoi
4. **Croisement** : recombinaison de bits entre parents
5. **Mutation** : inversion aléatoire d’un bit
6. **Remplacement** : mise à jour de la population avec les enfants



### Code simplifié en Python

```python
import random

def fitness(x):
    return x * x

def selection(pop):
    return random.choices(pop, weights=[fitness(x) for x in pop], k=2)

def crossover(p1, p2):
    point = random.randint(1, 4)
    mask = (1 << point) - 1
    return (p1 & mask) | (p2 & ~mask)

def mutate(x):
    if random.random() < 0.1:
        bit = 1 << random.randint(0, 4)
        return x ^ bit
    return x

def algo_genetique():
    population = [random.randint(0, 31) for _ in range(6)]
    for generation in range(20):
        new_population = []
        for _ in range(3):
            p1, p2 = selection(population)
            enfant = crossover(p1, p2)
            enfant = mutate(enfant)
            new_population.extend([p1, enfant])
        population = new_population
    return max(population, key=fitness)

print(algo_genetique())
```



## 5. Paramètres importants

- **Taille de la population** : équilibre entre diversité et temps de calcul
- **Taux de mutation** : typiquement faible (~1 % à 10 %)
- **Taux de croisement** : généralement élevé (~60 % à 90 %)
- **Méthode de sélection** : roulette, tournoi, rang, élitisme
- **Critère d’arrêt** : nombre de générations, stagnation, fitness seuil



## 6. Avantages et limites

### Avantages
- Adaptés aux problèmes non différentiables, discontinus ou bruités
- Robustes à la présence de nombreux optima locaux
- Facilement parallélisables
- Approche universelle (boîte noire)

### Limites
- Pas de garantie de convergence optimale
- Dépend fortement du codage et des paramètres
- Temps de calcul parfois long
- Moins précis que des méthodes analytiques quand elles existent



## 7. Applications typiques

- Optimisation de fonctions complexes
- Problèmes de planification et d’ordonnancement
- Conception automatique (architecture, réseaux de neurones)
- Jeux (IA adaptative)
- Apprentissage automatique (feature selection, hyperparamètres)

