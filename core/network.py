from core.layer import Layer
from math_ops.losses import LossFunction

class Network:
    """
    Classe principale représentant le perceptron multicouche (MLP).
    Utilise la Composition : un réseau contient une liste de couches (Layer)
    et une fonction de perte (LossFunction).
    """
    def __init__(self):
        """Initialise un réseau vide."""
        self.layers = []  # Liste d'objets Layer
        self.loss_function = None

    def add(self, layer: Layer):
        """Ajoute une couche au réseau."""
        pass

    def compile(self, loss_strategy: LossFunction):
        """Configure la fonction de perte du réseau."""
        pass

    def forward(self, input_data):
        """Fait passer les données à travers toutes les couches."""
        pass

    def fit(self, x_train, y_train, epochs: int, learning_rate: float):
        """
        Entraîne le réseau de neurones sur un jeu de données.
        (Boucle sur les époques, calcul du forward, du loss, puis du backward).
        """
        pass

    def predict(self, x_test):
        """Prédit les sorties pour un jeu de données de test."""
        pass

    def save(self, filepath: str):
        """
        Sauvegarde l'architecture et les poids du réseau dans un fichier JSON.
        (Figure imposée : Lecture/écriture de fichiers).
        """
        pass

    def load(self, filepath: str):
        """
        Charge l'architecture et les poids depuis un fichier JSON.
        """
        pass