# Projet ADEME – Partie 2 : Optimisation logistique avec contraintes de chargement (Bin Packing Problem)

## Contexte général

Dans le cadre de l’appel à manifestation d’intérêt lancé par l’ADEME (Agence de la Transition Écologique), la structure CesiCDP poursuit son engagement pour proposer des solutions concrètes et innovantes visant à améliorer les performances environnementales et économiques des systèmes de transport.

La première phase du projet, déjà menée par vos équipes, s’est concentrée sur la problématique du **voyageur de commerce (TSP)** : optimiser les tournées de livraison afin de minimiser les distances parcourues. Cette approche permet de réduire les émissions de CO₂ liées aux trajets, en s’attaquant au problème du parcours optimal sur un réseau routier.

Cependant, dans une logique industrielle réaliste, d’autres contraintes s’imposent. L’enjeu n’est plus uniquement de réduire les distances, mais aussi de **réduire le nombre de véhicules nécessaires**. Cela suppose une meilleure organisation des chargements. Chaque véhicule ayant une capacité limitée, il devient indispensable de répartir efficacement les livraisons afin d’**éviter des trajets inutiles** tout en respectant les contraintes physiques.

Ce volet du projet s’inscrit donc dans un **cadre logistique** : optimiser la mutualisation des ressources (camions) tout en tenant compte des capacités de chargement. Cette réflexion est au cœur des problématiques actuelles de la logistique verte, de l’optimisation des tournées urbaines, de la livraison du dernier kilomètre, ou encore du ramassage de déchets en milieu urbain.

## Problématique de cette seconde phase

Cette deuxième phase du projet s’intéresse spécifiquement à une problématique bien connue en algorithmique et en recherche opérationnelle : le **Bin Packing Problem**.

Ce problème se formule ainsi : un ensemble de colis, chacun caractérisé par un volume, doit être réparti dans des conteneurs (ou des véhicules) de capacité fixe. L’objectif est de minimiser le nombre de véhicules utilisés, tout en respectant strictement la contrainte de capacité de chacun.

Dans un contexte réel, cela signifie :

- Réduire le nombre de camions mis en circulation.
- Optimiser les tournées en amont, en regroupant intelligemment les colis compatibles.
- Diminuer les coûts d’exploitation tout en réduisant l’impact environnemental du transport.