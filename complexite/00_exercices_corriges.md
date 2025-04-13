# Exercices sur la complexité algorithmique

## Niveau 1 — Compréhension intuitive

### **Exercice 1 — Comptage de boucles simples**

```python
for i in range(n):
    print(i)
```

**Question** : Quelle est la complexité en temps de ce code ?

**Correction** :

- La boucle s’exécute `n` fois.
- L’instruction dans la boucle est `O(1)` → coût constant.
- Donc **complexité** : `O(n)`

### **Exercice 2 — Boucle imbriquée**

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

**Question** : Quelle est la complexité temporelle ?

**Correction** :

- La boucle intérieure s’exécute `n` fois pour **chaque** itération de la boucle extérieure (qui s’exécute aussi `n` fois).
- Donc total : `n × n = n²`
- **Complexité** : `O(n²)`

### **Exercice 3 — Logarithmique**

```python
i = 1
while i < n:
    print(i)
    i *= 2
```

**Question** : Quelle est la complexité en temps ?

**Correction** :

- À chaque itération, `i` double → `i = 1, 2, 4, 8, ..., ≤ n`
- Il faut environ `log₂(n)` étapes avant que `i ≥ n`
- **Complexité** : `O(log n)`

## Niveau 2 — Analyse de cas intermédiaires

### **Exercice 4 — Complexité mixte**

```python
for i in range(n):
    for j in range(1, n, 2):
        print(i, j)
```

**Question** : Quelle est la complexité ?

**Correction** :

- La boucle extérieure : `n` itérations
- La boucle intérieure saute de 2 en 2 → ≈ `n/2` itérations
- Total ≈ `n × (n/2) = O(n²)`

### **Exercice 5 — Cas avec dépendance**

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

**Question** : Quelle est la complexité ?

**Correction** :

- Pour `i = 0` → 0 itérations
- Pour `i = 1` → 1
- ...
- Total = `0 + 1 + 2 + ... + (n-1)` = `n(n-1)/2`
- Donc **complexité** : `O(n²)`

## Niveau 3 — Fonctions récursives

### **Exercice 6 — Récursion simple**

```python
def f(n):
    if n == 0:
        return
    f(n - 1)
```

**Question** : Combien d’appels récursifs sont faits ? Complexité ?

**Correction** :

- La fonction s'appelle elle-même `n` fois avant d’atteindre le cas de base.
- Chaque appel prend `O(1)`
- **Complexité** : `O(n)`

### **Exercice 7 — Récursion double (exponentielle)**

```python
def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 2)
```

**Question** : Quelle est la complexité ?

**Correction** :

- C’est la définition naïve de Fibonacci.
- L’arbre d’appel contient environ `2^n` appels → croissance exponentielle.
- **Complexité** : `O(2^n)`

### **Exercice 8 — Récursion logarithmique**

```python
def f(n):
    if n == 0:
        return
    f(n // 2)
```

**Question** : Combien d’appels récursifs sont effectués ?

**Correction** :

- À chaque appel, `n` est divisé par 2
- Nombre d’appels ≈ `log₂(n)`
- **Complexité** : `O(log n)`

## Niveau 4 — Bonus de réflexion

### **Exercice 9 — Analyse amortie**

```python
arr = []
for i in range(n):
    arr.append(i)
```

**Question** : En Python, `append()` peut parfois causer une reallocation mémoire. Quelle est la complexité **amortie** de cet algorithme ?

**Correction** :

- `append()` est généralement `O(1)` **amorti** (même si reallocation coûte `O(n)` ponctuellement).
- Donc sur `n` appels : **O(n)** en **temps amorti**

### **Exercice 10 — Code mélangeant plusieurs types de complexité**

```python
for i in range(n):
    j = 1
    while j < n:
        j *= 2
        print(i, j)
```

**Question** : Complexité en temps ?

**Correction** :

- La boucle `while` est `O(log n)` (j double à chaque fois)
- Elle est répétée `n` fois (dans la boucle `for`)
- Donc **complexité totale** : `O(n log n)`
