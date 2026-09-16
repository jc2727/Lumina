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


def split_x_y(df, target_column):
    """
    Esta funcion divide un DataFrame en características (X) y variable objetivo (y).

    Parametros:
    df: DataFrame a dividir
    target_column: columna objetivo

    Retorna:
    X: DataFrame con las características
    y: Serie con la variable objetivo

    """
    x = df.drop(columns=[target_column])
    y = df[target_column]
    return x, y


def create_model(numeric_columns,categorical_columns,model_name):
    """
    Esta funcion crea  un modelo de machine learning.

    Parametros:
    numeric_columns: lista de columnas numéricas
    categorical_columns: lista de columnas categóricas
    model_name: nombre del modelo de machine learning a crear

    Retorna:
    model: Receta de Modelo de ML

    """
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.linear_model import LinearRegression, Lasso
    from sklearn.ensemble import RandomForestRegressor
    from xgboost import XGBRegressor
    
    
    if model_name == 'linear_regression':

        preprocessor = pre_process_data(
                     numeric_columns,
                     categorical_columns,
                     scale_numeric = True 
         )
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', LinearRegression())
        ])

    elif model_name == 'lasso':

        preprocessor = pre_process_data(
                     numeric_columns,
                     categorical_columns,
                     scale_numeric = True 
         )
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', Lasso())
        ])

    elif model_name == 'random_forest':

        preprocessor = pre_process_data(
                     numeric_columns,
                     categorical_columns,
                     scale_numeric = False
         )
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor())
        ])
    elif model_name == 'xg_boost':

        preprocessor = pre_process_data(
                     numeric_columns,
                     categorical_columns,
                     scale_numeric = False
         )
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', XGBRegressor())
        ])
    else:
        raise ValueError(f"Modelo no soportado: {model_name}")
    return model


def validate_model(model, x_train,y_train):
    """
    Esta funcion valida un modelo de machine learning utilizando datos de train 
    usaremos cross validation para hacer la validación temporal.

    Parametros:
    model: Receta de Modelo de ML
    x_train: DataFrame con las características de entrenamiento
    y_train: Serie con la variable objetivo de entrenamiento

    Retorna:
    results: resultado de métricas de validación cross-validation temporal

    """
    from sklearn.model_selection import TimeSeriesSplit, cross_validate

    tscv = TimeSeriesSplit(n_splits=5)

    results = cross_validate(model, x_train, y_train, cv=tscv, 
                             scoring= {'mae' : 'neg_mean_absolute_error',
                                       'rmse' : 'neg_root_mean_squared_error',
                                       'mape' : 'neg_mean_absolute_percentage_error',
                                       'r2' : 'r2'}

                            )

    mae = abs(results['test_mae']).mean()
    rmse = abs(results['test_rmse']).mean()
    mape = abs(results['test_mape']).mean()*100
    r2 = results['test_r2'].mean()

    metrics = {
        'mae': mae,
        'rmse': rmse,
        'mape': mape,
        'r2': r2
    }
    
    return  metrics


    