# Tutoriel sur les Algorithmes de Brute Force et Greedy

## Introduction

Les algorithmes de brute force et les algorithmes gloutons (greedy) sont deux approches différentes pour résoudre des problèmes d'optimisation et de recherche.

- **Brute Force** : Cette approche consiste à explorer toutes les solutions possibles pour trouver la meilleure solution. Bien que simple et universelle, elle est souvent inefficace pour les problèmes de grande taille en raison de sa complexité exponentielle.

### Algorithme Greedy (Glouton)

L'algorithme glouton (ou greedy) est une méthode de résolution de problèmes qui construit progressivement une solution en prenant à chaque étape la meilleure décision locale possible, sans se préoccuper des conséquences à long terme. Cette approche peut être très efficace pour certains types de problèmes, bien qu'elle ne garantisse pas toujours une solution optimale globale.
Principe de base

L'idée principale derrière l'algorithme greedy est de choisir à chaque étape l'option qui semble la meilleure sur le moment. Cela signifie que pour chaque étape du processus de construction de la solution, on sélectionne l'élément qui offre le gain le plus élevé ou le coût le plus bas, selon le problème traité.

#### Étapes de l'algorithme Greedy

- Initialisation : Commencer avec une solution vide ou partielle.
- Sélection : À chaque étape, choisir l'option qui semble la meilleure selon un critère spécifique (par exemple, le coût minimal ou le profit maximal).
- Validation : Vérifier si l'option choisie peut être ajoutée à la solution sans violer les contraintes du problème.
- Itération : Répéter les étapes de sélection et de validation jusqu'à ce que la solution soit complète.
- Terminaison : Lorsque plus aucune option ne peut être ajoutée à la solution, l'algorithme s'arrête.

### Exemples d'utilisation de l'algorithme de Brute Force

1. **Trouver la plus longue sous-chaîne sans caractères répétés** :

   - **Problème** : Étant donné une chaîne de caractères, trouver la plus longue sous-chaîne qui ne contient pas de caractères répétés.

2. **Problème du sous-ensemble à somme donnée (Subset Sum Problem)** :

   - **Problème** : Étant donné un ensemble d'entiers, déterminer si un sous-ensemble existe dont la somme est égale à une valeur cible donnée.

3. **Problème des paires de mots (Word Pair Problem)** :
   - **Problème** : Trouver toutes les paires de mots dans une liste qui sont des anagrammes.

### Exemples d'utilisation de l'algorithme Greedy

1. **Problème de la monnaie (Coin Change Problem)** :

   - **Problème** : Trouver le nombre minimal de pièces nécessaires pour atteindre un montant donné à partir d'un ensemble de pièces de différentes valeurs.

2. **Problème du sac à dos fractionnaire (Fractional Knapsack Problem)** :

   - **Problème** : Maximiser la valeur des objets dans un sac à dos de capacité limitée en choisissant des fractions d'objets.

3. **Problème de l'intervalle de sélection (Interval Scheduling Problem)** :
   - **Problème** : Étant donné un ensemble d'intervalles de temps, sélectionner le plus grand nombre possible d'intervalles non chevauchants.

Voyons ces deux types d'algorithmes en détail avec des exemples en Python.

---

## Algorithme de Brute Force

### Exemple : Trouver la plus longue sous-chaîne sans caractères répétés

**Problème** : Étant donné une chaîne de caractères, trouvez la plus longue sous-chaîne qui ne contient pas de caractères répétés.

**Solution par Brute Force** : Générer toutes les sous-chaînes possibles et vérifier si elles contiennent des caractères répétés. Garder la plus longue sous-chaîne sans répétition.

### Implémentation en Python

```python
def longest_unique_substring(s):
    n = len(s)
    max_length = 0
    max_substring = ""

    # Générer toutes les sous-chaînes possibles
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]  # Extraire la sous-chaîne de i à j
            if len(substring) == len(set(substring)):  # Vérifie si tous les caractères sont uniques
                if len(substring) > max_length:
                    max_length = len(substring)  # Mettre à jour la longueur maximale
                    max_substring = substring  # Mettre à jour la sous-chaîne maximale

    return max_substring, max_length

# Exemple d'utilisation
s = "abcabcbb"
longest_substring, length = longest_unique_substring(s)
print(f"Plus longue sous-chaîne sans caractères répétés: '{longest_substring}' avec une longueur de {length}")
```

### Exemple de résultat

```plaintext
Plus longue sous-chaîne sans caractères répétés: 'abc' avec une longueur de 3
```

---

## Algorithme Greedy (Glouton)

### Exemple : Problème de la Monnaie (Coin Change Problem)

**Problème** : On dispose d'un ensemble de pièces de monnaie de différentes valeurs. Le but est de faire une somme spécifique avec le minimum de pièces possible.

**Solution Gloutonne** : À chaque étape, on choisit la plus grande pièce qui ne dépasse pas la somme restante.

### Implémentations en Python

```python
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Trie les pièces par ordre décroissant
    count = 0
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin  # Réduit le montant restant de la valeur de la pièce
            count += 1  # Augmente le nombre de pièces utilisées
            result.append(coin)  # Ajoute la pièce à la liste des résultats

    if amount != 0:
        return -1, []  # Indique qu'il n'est pas possible de faire la somme exacte avec les pièces données
    return count, result

# Exemple d'utilisation
coins = [1, 5, 10, 25]
amount = 63
count, result = coin_change_greedy(coins, amount)
if count != -1:
    print(f"Nombre minimal de pièces: {count}")
    print(f"Pièces utilisées: {result}")
else:
    print("Il n'est pas possible de faire la somme exacte avec les pièces données")
```

### Explication de l'exemple

- Tri des pièces : Les pièces sont triées par ordre décroissant de leur valeur pour toujours essayer de prendre la pièce la plus grande possible en premier.
- Sélection des pièces : Pour chaque pièce, on la prend autant de fois que possible sans dépasser le montant restant.
- Réduction du montant : À chaque fois qu'une pièce est prise, le montant restant à atteindre est réduit de la valeur de cette pièce.
- Terminaison : Si à la fin, le montant restant est zéro, l'algorithme a réussi. Sinon, il est impossible d'atteindre exactement le montant donné avec les pièces disponibles.

### Exemple de résultats

```plaintext
Nombre minimal de pièces: 6
Pièces utilisées: [25, 25, 10, 1, 1, 1]
```

---

## Conclusion

Les algorithmes de brute force et gloutons ont chacun leurs avantages et inconvénients :

- **Brute Force** : Facile à implémenter et garantit une solution optimale, mais inefficace pour les grands problèmes.
- **Greedy** : Rapide et efficace pour certains problèmes spécifiques, mais ne garantit pas toujours une solution optimale.

En fonction du problème et de ses contraintes, il est crucial de choisir la bonne approche pour obtenir des solutions optimales dans des délais raisonnables.
