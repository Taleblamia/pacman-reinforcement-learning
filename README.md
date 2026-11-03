# Pacman — Apprentissage par renforcement

Projet académique consacré à l'apprentissage par renforcement dans les environnements Gridworld et Pacman.

## Objectif

Étudier comment un agent choisit ses actions pour maximiser ses récompenses : se déplacer dans une grille, collecter la nourriture et éviter les fantômes dans Pacman.

## Méthodes étudiées

- **Value Iteration** : calcul des valeurs et d'une politique à partir du modèle de l'environnement.
- **Q-learning** : apprentissage des valeurs des actions par interaction avec l'environnement.
- **Q-learning approximatif** : estimation des valeurs avec des caractéristiques telles que la proximité des fantômes et la distance à la nourriture.
- **Deep Q-Network (DQN)** : exploration d'un agent utilisant un réseau de neurones convolutif et une mémoire d'expériences.

## Organisation

- `RL_defi_Python3/reinforcement_Python3/` : agents classiques, environnements Gridworld et Pacman, notebooks et visualisations.
- `PacmanDQN)/PacmanDQN/` : implémentation DQN, paramètres et exemples de démonstration.
- `codePython_3.0/` : fichiers complémentaires du simulateur.
- Les fichiers PDF contiennent les sujets, les documents de travail et le rapport du projet.

## Technologies

Python, NumPy, TensorFlow et Jupyter Notebook.

## Exécution

Depuis `RL_defi_Python3/reinforcement_Python3/`, exemple d'utilisation de l'agent Q-learning :

```bash
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
```

Depuis `PacmanDQN)/PacmanDQN/`, exemple fourni par le projet DQN :

```bash
python pacman.py -p PacmanDQN -n 6000 -x 5000 -l smallGrid
```

Le code DQN utilise une ancienne API TensorFlow (`tf.Session`, `tf.placeholder`). Un environnement compatible ou une adaptation est nécessaire. Ces commandes n'ont pas été validées dans l'environnement actuel.

## Crédits et conditions de diffusion

Le framework pédagogique Pacman provient des projets d'intelligence artificielle de l'UC Berkeley, notamment de John DeNero et Dan Klein. La base DQN provient de PacmanDQN de Tycho van der Ouderaa et du travail de Tejas Kulkarni.

Les en-têtes du code Berkeley demandent de ne pas distribuer ni publier les solutions pédagogiques. Conserver ces mentions et tenir compte de cette restriction avant toute diffusion. Ce dépôt ne présente pas les frameworks tiers comme des créations originales.
