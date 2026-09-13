def pre_process_data(numeric_columns, categorical_columns,scale_numeric=True):
    """

    Esta funcion pre procesa los datos, aplicando escalado a las columnas numéricas y codificación one-hot a las columnas categóricas.

    Parametros:
    numeric_columns: lista de columnas numéricas
    categorical_columns: lista de columnas categóricas
    scale_numeric: booleano que indica si se debe escalar las columnas numéricas (por defecto True)

    Retorna:
    preprocessor: objeto ColumnTransformer que aplica las transformaciones especificadas a las columnas correspondientes.

    La idea de esta función es que se pueda usar para cualquier modelo de machine learning que requiera preprocesamiento de datos.

    """

    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline

    if scale_numeric:
        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])
    else:
        numeric_transformer = 'passthrough'

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore', drop='if_binary'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_columns),
            ('cat', categorical_transformer, categorical_columns)
        ])

    return preprocessor


def split_temporal(df, date_column,train_size=.8):
    """
    Esta funcion divide un DataFrame en conjuntos de entrenamiento y prueba de manera temporal, basándose en una columna de fecha.

    Parametros:
    df: DataFrame a dividir
    date_column: columna de fecha para ordenar los datos
    train_size: proporción de datos para el conjunto de entrenamiento (por defecto 0.8)

    Retorna:
    train_df: DataFrame de entrenamiento
    test_df: DataFrame de prueba

    """

    df = df.sort_values(by=date_column).reset_index(drop=True)
    train_index = int(len(df) * train_size)
    train_df = df.iloc[:train_index]
    test_df = df.iloc[train_index:]
    return train_df, test_df