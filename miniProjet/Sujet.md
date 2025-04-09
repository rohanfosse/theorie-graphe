# Sujet de Mini Projet : Optimisation de Parcours de Drones pour la Surveillance d'une Zone

## Contexte

Vous êtes responsable de la planification des parcours de drones pour couvrir des points d'intérêt spécifiques dans une zone définie. Vous devez modéliser ce problème sous forme de graphe et implémenter différentes stratégies pour trouver le parcours optimal. Vous trouverez le graphe dans le fichier `graph_data.json`.

## Objectifs du Projet

1. **Modélisation du Problème** : Représentez les points d'intérêt et les chemins possibles sous forme de graphe.
2. **Algorithmes de Parcours de Graphe** :
   - Implémentez une solution en **brute force**.
   - Implémentez une solution **greedy**.
   - Implémentez un algorithme de parcours de graphe de votre choix (ex: Dijkstra).
3. **Analyse de Complexité** :
   - Analysez la complexité de chaque algorithme.
   - Comparez les performances en termes de temps de calcul et longueur du chemin.

## Instructions Détaillées

### Étape 1 : Préparation

- Installez Python et la librairie NetworkX : `pip install networkx`.
- Créez un fichier Python principal pour organiser votre code (ex : `drone_surveillance.py`).

### Étape 2 : Modélisation du Graphe

- Utilisez NetworkX pour créer un graphe représentant les points d'intérêt et les chemins possibles.

### Étape 3 : Implémentation des Algorithmes

1. **Brute Force** : Explorez toutes les permutations possibles pour trouver le chemin le plus court.
2. **Greedy** : Utilisez une approche gourmande pour choisir le chemin le plus court à chaque étape.
3. **Algorithme de Parcours** : Implémentez Dijkstra pour trouver le chemin le plus court.

### Étape 4 : Analyse de Complexité

- Analysez la complexité en termes de temps et espace pour chaque algorithme. Justifiez vos résultats.
- Comparez les résultats obtenus (temps de calcul et longueur du chemin).

## Squelette de Code

```python
import networkx as nx
import itertools
import time

# Modélisation du graphe
def create_graph():
    G = nx.Graph()
    # Ajoutez ici les nœuds et les arêtes avec leurs poids
    return G

# Brute Force
def brute_force_tsp(G):
    # Implémentez l'algorithme de brute force pour le TSP
    return None, None

# Greedy Algorithm
def greedy_tsp(G, start_node):
    # Implémentez l'algorithme greedy pour le TSP
    return None, None

# Dijkstra Algorithm
def dijkstra_tsp(G, start_node):
    # Implémentez l'algorithme de Dijkstra pour le TSP
    return None, None

# Main Function
def main():
    G = create_graph()
    
    print("Brute Force:")
    start = time.time()
    path, length = brute_force_tsp(G)
    end = time.time()
    print(f"Path: {path}, Length: {length}, Time: {end - start:.4f} seconds")

    print("\nGreedy:")
    start = time.time()
    path, length = greedy_tsp(G, 'A')
    end = time.time()
    print(f"Path: {path}, Length: {length}, Time: {end - start:.4f} seconds")

    print("\nDijkstra:")
    start = time.time()
    path, length = dijkstra_tsp(G, 'A')
    end = time.time()
    print(f"Path: {path}, Length: {length}, Time: {end - start:.4f} seconds")

if __name__ == "__main__":
    main()
```

## Analyse de Complexité

- **Brute Force** : O(n!), car toutes les permutations sont explorées.
- **Greedy** : O(n^2), car pour chaque nœud, on cherche le plus proche parmi les n-1 restants.
- **Dijkstra** : O(n log n), car l'algorithme utilise une file de priorité.

## Livrables

- **Code Python** : Incluez toutes les implémentations et testez avec différents graphes.
- **Rapport d'Étude** :
  - Description du problème et de la modélisation.
  - Explication des algorithmes.
  - Analyse de complexité.
  - Comparaison des résultats.

## Ressources

- [NetworkX Documentation](https://networkx.org/documentation/stable/index.html)
- [Complexity Analysis](https://en.wikipedia.org/wiki/Time_complexity)
- [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Greedy Algorithms](https://en.wikipedia.org/wiki/Greedy_algorithm)