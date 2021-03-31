import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_imputations(df: pd.DataFrame, column: str, method: str = 'median', **kwargs):
    """
    Grafica la distribucion de una variable antes y despues de imputar
    :param df: DataFrame
    :param column: variable de interes
    :param method: metodo por el que imputa
    :param kwargs:
    :return: NoneType
    """
    plt.subplot(1, 2, 1)
    sns.distplot(df[column], **kwargs)
    plt.subplot(1, 2, 2)
    if method == 'median':
        sns.distplot(df[column].fillna(df[column].fillna(df[column].median())), **kwargs)
    elif method == 'mean':
        sns.distplot(df[column].fillna(df[column].fillna(df[column].mean())), **kwargs)
    else:
        sns.distplot(df[column].fillna(df[column].fillna(df[column].mode())), **kwargs)
    return plt.show()