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


def boxplot(data: pd.DataFrame, column: str, label: str = None, **kwargs):
    if label is None:
        return sns.catplot(data=data, y=column, kind='box', **kwargs)
    else:
        return sns.catplot(data=data, x=column, y=label, kind='box', **kwargs)


def histogram(data: pd.DataFrame, column: str, **kwargs):
    return sns.distplot(a=data[column], **kwargs)


def scatterplot(data: pd.DataFrame, x: str, y: str, **kwargs):
    return sns.relplot(x=x, y=y, data=data, kind="scatter", **kwargs)