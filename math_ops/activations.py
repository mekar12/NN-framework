from abc import ABC, abstractmethod

class ActivationFunction(ABC):
    """
    Classe abstraite pour le pattern Strategy des fonctions d'activation.
    """
    @abstractmethod
    def compute(self, x):
        pass

    @abstractmethod
    def derivative(self, x):
        pass


class ReLU(ActivationFunction):
    """Fonction d'activation Rectified Linear Unit."""
    def compute(self, x):
        pass

    def derivative(self, x):
        pass


class Sigmoid(ActivationFunction):
    """Fonction d'activation Sigmoïde."""
    def compute(self, x):
        pass

    def derivative(self, x):
        pass


class ActivationLayer(Layer):
    """
    Couche qui applique une fonction d'activation aux données.
    Hérite de Layer et utilise la Composition avec ActivationFunction.
    """
    def __init__(self, activation_strategy: ActivationFunction):
        super().__init__()
        self.activation = activation_strategy

    def forward(self, input_data):
        pass

    def backward(self, output_gradient, learning_rate):
        pass