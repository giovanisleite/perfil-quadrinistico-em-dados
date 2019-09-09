import hashlib

import pandas as pd


def anonymize(string):
    return hashlib.md5(
        string.encode('utf-8')
    ).hexdigest()


def open_dataframe(filename='dados-completos.csv'):
    return pd.read_csv(filename)


def anonymize_column(dataframe):
    column = 'Quem Indicou'
    dataframe[column] = dataframe[column].apply(anonymize)
    return dataframe


def remove_columns_containing_spoilers(dataframe):
    columns = [
        'Vídeo', 'Indicação genérica', 'Link de identificação', 'Imagem', 'Obs'
    ]
    return dataframe.drop(columns, axis=1)


df = open_dataframe()
clean_df = remove_columns_containing_spoilers(
    anonymize_column(df)
).sort_values('Quem Indicou')
clean_df.to_csv('data.csv', index=False)
