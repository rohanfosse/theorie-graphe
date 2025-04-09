import random
import time
import seaborn as sns
import matplotlib.pyplot as plt

class Graphe:
    def __init__(self, matrice_adjacence):
        """
        Initialise un graphe avec une matrice d'adjacence.
        """
        self.matrice_adjacence = matrice_adjacence  # Stocke la matrice d'adjacence
        self.nombre_sommets = len(matrice_adjacence)  # Calcule le nombre de sommets
        self.degres = self.calculer_degres()  # Calcule les degrés des sommets
        self.nombre_aretes = sum(self.degres) // 2  # Calcule le nombre d'arêtes

    def calculer_degres(self):
        """
        Calcule et retourne la liste des degrés de chaque sommet.
        """
        return [sum(ligne) for ligne in self.matrice_adjacence]  # Calcule le degré de chaque sommet

    def a_cycle_eulerien(self):
        """
        Vérifie si le graphe a un cycle eulérien.
        """
        def est_connexe():
            """
            Vérifie si le graphe est connexe.
            """
            def dfs(sommet, visite):
                """
                Parcourt le graphe en profondeur à partir d'un sommet donné.
                """
                visite[sommet] = True  # Marque le sommet comme visité
                for voisin in range(self.nombre_sommets):  # Pour chaque sommet voisin
                    if self.matrice_adjacence[sommet][voisin] > 0 and not visite[voisin]:  # Si une arête existe et que le voisin n'est pas visité
                        dfs(voisin, visite)  # Applique DFS sur le voisin
            
            visite = [False] * self.nombre_sommets  # Initialise les sommets comme non visités
            sommet_depart = -1  # Initialisation du sommet de départ
            for i in range(self.nombre_sommets):
                if self.degres[i] > 0:  # Trouve un sommet avec un degré non nul
                    sommet_depart = i
                    break
            
            if sommet_depart == -1:  # Si aucun sommet avec un degré non nul n'est trouvé
                return False
            
            dfs(sommet_depart, visite)  # Lance DFS à partir du sommet de départ
            
            for i in range(self.nombre_sommets):
                if self.degres[i] > 0 and not visite[i]:  # Si un sommet avec un degré non nul n'est pas visité
                    return False
            return True  # Le graphe est connexe
        
        if not est_connexe():  # Vérifie si le graphe est connexe
            return False
        
        for degre in self.degres:  # Vérifie si chaque sommet a un degré pair
            if degre % 2 != 0:
                return False
        
        return True  # Retourne True si le graphe a un cycle eulérien

    def trouver_cycle_eulerien(self, check=True):
        """
        Trouve et retourne un cycle eulérien dans le graphe si possible.
        """
        if check and not self.a_cycle_eulerien():  # Vérifie d'abord si le graphe a un cycle eulérien
            return None
        
        g = [row[:] for row in self.matrice_adjacence]  # Crée une copie de la matrice d'adjacence
        
        def trouver_cycle(v):
            """
            Trouve un cycle à partir du sommet v en utilisant une pile pour suivre le chemin.
            """
            pile = [v]  # Initialiser la pile avec le sommet de départ
            chemin = []  # Liste pour stocker le chemin du cycle
            
            while pile:  # Tant que la pile n'est pas vide
                u = pile[-1]  # Prend le sommet au sommet de la pile
                arrete_trouvee = False  # Indicateur pour savoir si une arête a été trouvée
                
                for i in range(len(g)):  # Cherche une arête à partir du sommet u
                    if g[u][i] > 0:  # Si une arête existe
                        pile.append(i)  # Ajoute le sommet i à la pile
                        g[u][i] -= 1  # Retire l'arête du graphe
                        g[i][u] -= 1  # Retire l'arête réciproque (car le graphe est non dirigé)
                        arrete_trouvee = True  # Indique qu'une arête a été trouvée
                        break
                
                if not arrete_trouvee:  # Si aucune arête n'a été trouvée
                    chemin.append(pile.pop())  # Ajoute le sommet u au chemin
            
            return chemin  # Retourne le chemin trouvé
        
        sommet_depart = 0  # Trouver un sommet de départ avec un degré non nul
        for i in range(self.nombre_sommets):
            if self.degres[i] > 0:
                sommet_depart = i
                break
        
        cycle = trouver_cycle(sommet_depart)  # Trouve le cycle eulérien à partir du sommet de départ
        
        return cycle[::-1]  # Retourner le cycle en ordre inverse pour obtenir le cycle correct

    @staticmethod
    def generer_graphe_eulerien(n):
        """
        Génère un graphe eulérien aléatoire avec n sommets.
        """
        if n < 3:
            raise ValueError("Le nombre de sommets doit être au moins 3 pour générer un graphe eulérien.")
        
        matrice_adjacence = [[0] * n for _ in range(n)]  # Initialise la matrice d'adjacence

        # Créer un cycle initial
        for i in range(n):
            matrice_adjacence[i][(i + 1) % n] = 1  # Ajoute une arête vers le sommet suivant
            matrice_adjacence[(i + 1) % n][i] = 1  # Ajoute l'arête réciproque
        
        # Ajouter des arêtes pour assurer que chaque sommet a un degré pair
        for i in range(n):
            voisins = [j for j in range(n) if j != i and matrice_adjacence[i][j] == 0]  # Liste des voisins possibles
            while sum(matrice_adjacence[i]) % 2 != 0:  # Tant que le degré du sommet i est impair
                j = random.choice(voisins)  # Choisit un voisin aléatoire
                matrice_adjacence[i][j] += 1  # Ajoute une arête
                matrice_adjacence[j][i] += 1  # Ajoute l'arête réciproque
                voisins.remove(j)  # Retire ce voisin de la liste
        
        return Graphe(matrice_adjacence)  # Retourne un nouveau graphe eulérien

def etude_temps_calcul():
    """
    Étudie le temps de calcul d'un cycle eulérien en fonction de la taille du graphe.
    """
    tailles = list(range(100, 1000, 100))  # Tailles des graphes à tester
    temps_calcul = []

    for taille in tailles:
        g = Graphe.generer_graphe_eulerien(taille)  # Génère un graphe eulérien aléatoire de taille spécifiée
        debut = time.time()  # Enregistre le temps de début
        g.trouver_cycle_eulerien(check=False)  # Calcule le cycle eulérien sans vérification
        fin = time.time()  # Enregistre le temps de fin
        temps_calcul.append(fin - debut)  # Calcule et stocke le temps de calcul

    # Affiche les résultats sous forme de graphique
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=tailles, y=temps_calcul, marker='o')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps de calcul (secondes)')
    plt.title('Temps de calcul d\'un cycle eulérien en fonction de la taille du graphe')
    plt.show()

def main():
    # Exemple d'utilisation
    n = 6  # Nombre de sommets
    g = Graphe.generer_graphe_eulerien(n)
    print("Matrice d'adjacence du graphe eulérien généré :")
    for ligne in g.matrice_adjacence:
        print(ligne)

    print("Nombre de sommets :", g.nombre_sommets)
    print("Nombre d'arêtes :", g.nombre_aretes)
    print("Degrés des sommets :", g.degres)

    cycle = g.trouver_cycle_eulerien()
    if cycle:
        print("Cycle eulérien trouvé:", cycle)
    else:
        print("Aucun cycle eulérien n'existe dans ce graphe.")
    
    # Étude du temps de calcul
    etude_temps_calcul()

if __name__ == '__main__':
    main()
