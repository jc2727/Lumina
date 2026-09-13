import pandas as pd
def cargar_datos(ruta_archivo, tipo ='csv'):
    """
    Carga los datos desde un archivo CSV o Excel y devuelve un DataFrame de pandas.
    
    Parámetros:
    ruta_archivo (str): La ruta del archivo CSV o excel a cargar.
    tipo (str): El tipo de archivo a cargar. Puede ser 'csv' o 'excel'. Por defecto es 'csv'.
    
    Retorna:
    pd.DataFrame: Un DataFrame que contiene los datos cargados.
    """
    tipo = tipo.lower()
    try:
        if tipo == 'csv':
            df = pd.read_csv(ruta_archivo)
        elif tipo == 'excel':
            df = pd.read_excel(ruta_archivo)
        else:
            raise ValueError("El tipo de archivo debe ser 'csv' o 'excel'.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {ruta_archivo} no se encontró.")

    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError(f"El archivo {ruta_archivo} está vacío.")
    except pd.errors.ParserError:
        raise pd.errors.ParserError(f"Hubo un error al parsear el archivo {ruta_archivo}.")
        