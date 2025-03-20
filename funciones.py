def cargar_dataset(archivo):
    import pandas as pd
    import os
    #Si se desea agregar un input se coloca:
#   archivo=input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.html':
        df= pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"Hola, acabas de ingresar un documento que desconozco, con extensión: {extension}")
    


def sustituir_nulos(df):
   
    import numpy as np
    primos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}  # Lista de índices primos hasta 30 para simplificar
    
    for col_index, col in enumerate(df.columns):
        if df[col].dtype in [np.int64, np.float64]:
            df[col].fillna(1111111 if col_index in primos else 1000001, inplace=True)
        else:
            df[col].fillna("Valor Nulo", inplace=True)
    
    return df


def identificar_nulos(df):
   
    nulos_por_columna = df.isnull().sum()
    total_nulos = df.isnull().sum().sum()
    
    return nulos_por_columna, total_nulos


def identificar_y_sustituir_atipicos(df):
    import numpy as np
    for col in df.select_dtypes(include=['float', 'float64', 'int', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        Limite_Inferior_iqr = Q1 - 1.5 * IQR
        Limite_Superior_iqr = Q3 + 1.5 * IQR
        df.loc[(df[col] < Limite_Inferior_iqr) | (df[col] > Limite_Superior_iqr), col] = "Valor Atípico"
    
    return df
