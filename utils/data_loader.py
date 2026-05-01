class MNISTLoader:
    """
    Classe utilitaire pour charger et pré-traiter les données MNIST.
    """
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self):
        """Charge le CSV ou les binaires MNIST."""
        pass

    def normalize(self, data):
        """Normalise les valeurs des pixels (ex: entre 0 et 1)."""
        pass

    def to_categorical(self, labels):
        """Transforme les labels en vecteurs one-hot encoding (One-Hot)."""
        pass