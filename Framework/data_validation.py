def validate_data(df,target, fecha):
    """
    Esta función Valida los datos proporcionados cumpliendo con ciertos criterios como
    Duplicados, Valores nulos, Tipos de datos y Formato de fecha.


    Parameters:
       Fecha: Que Columna tiene el tipo de fecha
       Target: Variable objetivo que se quiere predecir
       df: DataFrame de pandas que contiene los datos a validar.


    Returns:
        un resumen que contiene Información: 
        Cuantas columnas y filas, cuantos valores nulos, cuántos duplicados, tipos de datos
    """
#Este bloque de código valida si la columna objetivo y la columna de fecha existen en el DataFrame.
    if fecha not in df.columns:
        raise ValueError(f"La columna de fecha '{fecha}' no se encuentra en el DataFrame.")
    if target not in df.columns:
        raise ValueError(f"La columna objetivo '{target}' no se encuentra en el DataFrame.")

#Este bloque imprime información sobre el DataFrame, incluyendo el número de filas y columnas, los tipos de datos de cada columna, la cantidad de valores nulos y duplicados.
    print("Información del DataFrame:")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

    print("Tipos de datos:")
    print(df.dtypes)

    print("Valores nulos:")
    print(df.isnull().sum())

    print("Duplicados:")
    print(df.duplicated().sum())
