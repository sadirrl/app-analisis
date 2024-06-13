# data_handler.py
import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        """Carga los datos del archivo CSV en un DataFrame de pandas."""
        self.data = pd.read_csv(self.file_path)
    
    def preview_data(self):
        """Muestra las primeras 10 filas del DataFrame."""
        if self.data is not None:
            return self.data.head(10)
        else:
            return "No data loaded. Please load a CSV file first."
    
    def calculate_statistics(self):
        """Calcula y devuelve estadísticas descriptivas de las columnas numéricas."""
        if self.data is not None:
            stats = self.data.describe().loc[['mean', '50%', 'std']]
            stats.rename(index={'50%': 'mediana'}, inplace=True)
            stats.rename(index={'mean': 'media'}, inplace=True)
            stats.rename(index={'std': 'desviacion estandar'}, inplace=True)
            return stats
        else:
            return "No data loaded. Please load a CSV file first."
