from abc import ABC, abstractmethod

class LossFunction(ABC):
    """
    Classe abstraite pour le pattern Strategy des fonctions de coût.
    """
    @abstractmethod
    def calculate(self, y_true, y_pred):
        pass

    @abstractmethod
    def derivative(self, y_true, y_pred):
        pass

class MSE(LossFunction):
    """Erreur Quadratique Moyenne (Mean Squared Error)."""
    def calculate(self, y_true, y_pred):
        pass

    def derivative(self, y_true, y_pred):
        pass