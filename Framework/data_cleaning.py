import pandas as pd
def convertir_tipos(df, fecha, convertir=None):


    """
    Convierte la columna de fecha a tipo datetime.
    Cambia el tipo de datos de las columnas que el usuario indique 

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna de fecha.
        fecha(str): Nombre de la columna de fecha.
        convertir (Dict): Indica si una columna deber convertirse a un tipo especifico y especifica en dict a que tipo

    Returns:
        pd.DataFrame: DataFrame con la columna de fecha convertida a tipo datetime.
    """
    df[fecha] = pd.to_datetime(df[fecha])

    if convertir is not None:
        for columna, tipo in convertir.items():
            df[columna] = df[columna].astype(tipo)

    return df


def eliminar_duplicados(df):
    """
    Elimina filas duplicadas del DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que puede contener filas duplicadas.

    Returns:
        pd.DataFrame: DataFrame sin filas duplicadas.
    """
    filas_antes = df.shape[0]
    df = df.drop_duplicates()
    filas_despues = df.shape[0]
    print(f"Se eliminaron {filas_antes - filas_despues} filas duplicadas.") 
    return df



def limpiar_nulos(df,tratamiento):
    """
    Limpia los valores nulos en las columnas especificadas del DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que puede contener valores nulos.
        tratamiento (dict): Diccionario que especifica el método de limpieza para cada columna.
        return regresa el DataFrame con los valores nulos tratados según el método especificado.

    """
    for columna, metodo in tratamiento.items():
        print(columna, metodo)
        if metodo == 'eliminar':
            df = df.dropna(subset=[columna])
        elif metodo == 'media':
            df[columna] = df[columna].fillna(df[columna].mean())
        elif metodo == 'mediana':
            df[columna] = df[columna].fillna(df[columna].median())
        elif metodo == 'interpolar':
            df[columna] = df[columna].interpolate()
        else:
            raise ValueError(f"Método de limpieza no válido para la columna {columna}: {metodo}")

    return df