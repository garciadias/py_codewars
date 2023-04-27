import pandas as pd

from py_codewars.lv6.pandas_series_102 import max_common

DATA_A = {"A": [2.5, 2.0], "B": [2.0, 2.0], "C": [2.0, 2.0]}
DATA_B = {"C": [1.0, 8.5], "B": [6.0, 1.0], "D": [7.0, 9.0], "E": [1.0, 1.0]}
DATA_OUTPUT = {"A": [2.5, 2.0], "B": [6.0, 2.0], "C": [2.0, 8.5]}


def test_max_common():
    df_a = pd.DataFrame(DATA_A)
    df_b = pd.DataFrame(DATA_B)
    df_output = pd.DataFrame(DATA_OUTPUT)
    assert max_common(df_a, df_b).equals(df_output)
