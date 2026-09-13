def numeric_summary(df):
    """
    Genera un summary estadístico de las columnas numéricas de un DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: Un DataFrame con el summary estadístico.
    """
    numeric_df = df.select_dtypes(include=['number'])
    summary = numeric_df.describe()
    return summary

def target_over_time(df, target_column, time_column, freq = 'W'):
    """
    Genera un gráfico de línea que muestra la evolución de la variable objetivo a lo largo del tiempo.

    Parameters:
    df (pd.DataFrame): El input DataFrame.
    target_column (str): Nombre de columna objetivo.
    time_column (str): Columna de tiempo
    freq (str): Frecuencia de agrupación para el tiempo. Por defecto es semanal ('W').
    Returns:
    None
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    # Agrupa por la columna de tiempo y suma  la variable objetivo
    grouped = ( 
        df.groupby(pd.Grouper(key=time_column, freq=freq))[target_column]
        .sum()
        .reset_index()      
    )



    # Crea el gráfico de línea
    sns.lineplot(data=grouped, x=time_column, y=target_column)
    plt.title(f'Evolución de {target_column} a lo largo del tiempo')
    plt.xlabel(time_column)
    plt.ylabel(target_column)
    plt.tight_layout()
    plt.show()


def analisis_pairwise(df, columns=None,hue=None):
    """
    Genera un gráfico de pairplot para las columnas especificadas del DataFrame.

    Parameters:
    df (pd.DataFrame): El input DataFrame.
    columns (list): Lista de columnas a incluir en el pairplot. Si es None, se incluyen todas las columnas numéricas.

    Returns:
    None
    """
    import seaborn as sns
    import matplotlib.pyplot as plt

    if columns is None:
        columns = df.select_dtypes(include=['number']).columns.tolist()

    sns.pairplot(data = df,
                 vars=columns,
                 hue=hue)
    plt.show()

def matrix_correlation(df, columns=None):
    """
    Genera un heatmap de la matriz de correlación para las columnas especificadas del DataFrame.

    Parameters:
    df (pd.DataFrame): El input DataFrame.
    columns (list): Lista de columnas a incluir en la matriz de correlación. Si es None, se incluyen todas las columnas numéricas.

    Returns:
    None
    """
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np

    if columns is None:
        columns = df.select_dtypes(include=['number']).columns.tolist()

    corr_matrix = df[columns].corr()

    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', mask=mask)
    plt.title('Matriz de correlación')
    plt.tight_layout()
    plt.show()