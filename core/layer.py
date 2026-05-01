from abc import ABC, abstractmethod

class Layer(ABC):
    """
    Classe abstraite représentant une couche générique du réseau de neurones.
    Toutes les couches doivent implémenter une propagation avant et arrière.
    """
    def __init__(self):
        self.input_data = None
        self.output_data = None

    @abstractmethod
    def forward(self, input_data):
        """Calcule la sortie de la couche en fonction de l'entrée."""
        pass

    @abstractmethod
    def backward(self, output_gradient, learning_rate):
        """
        Calcule le gradient par rapport à l'entrée et met à jour
        les paramètres de la couche si nécessaire.
        """
        pass


class Dense(Layer):
    """
    Couche complètement connectée (Fully Connected Layer).
    Hérite de Layer.
    """
    def __init__(self, input_size: int, output_size: int):
        """
        Initialise les poids et les biais de manière aléatoire.
        """
        super().__init__()
        self.weights = None  # Sera une matrice numpy
        self.bias = None     # Sera un vecteur numpy

    def forward(self, input_data):
        pass

    def backward(self, output_gradient, learning_rate):
        pass