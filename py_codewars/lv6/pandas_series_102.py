"""
Solves the `Pandas Series 102: Max From Common DataFrames` codewars kata
url: https://www.codewars.com/kata/5ea2a798f9632c0032659a75/train/python

Instructions:
Max From Common DataFrames
Input parameters
Two pandas.DataFrame objects

Task
Your function must return a new pandas.DataFrame with the same data and
columns from the first parameter. For common columns in both inputs you
must return the greater value of each cell for that column.

You must not modify the original inputs.

Input DataFrame will never be empty. The number rows of both inputs will
be the same.

Examples
Inputs
   A    B    C
0  2.5  2.0  2.0
1  2.0  2.0  2.0
   C    B    D    E
0  1.0  6.0  7.0  1.0
1  8.5  1.0  9.0  1.0
Output
   A    B    C
0  2.5  6.0  2.0
1  2.0  2.0  8.5
"""
from pandas.core.generic import NDFrame


def max_common(df_a: NDFrame, df_b: NDFrame) -> NDFrame:
    """Return a new NDFrame with the same data and columns from the
    first parameter. For common columns in both inputs you must return the
    greater value of each cell for that column.

    Parameters
    ----------
    df_a : NDFrame
        A NDFrame object.
    df_b : NDFrame
        A NDFrame object.

    Returns
    -------
    NDFrame
        A NDFrame object with the same data and columns from the
        first parameter. For common columns in both inputs you must return the
        greater value of each cell for that column.
    """
    new_df = df_a.copy()
    for column in new_df.columns:
        if column in df_b.columns:
            new_df[column] = new_df[column].where(
                cond=new_df[column] > df_b[column], other=df_b[column]
            )
    return new_df
