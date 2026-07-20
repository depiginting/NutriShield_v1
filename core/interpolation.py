"""
====================================================
NutriShield
Interpolation Module
====================================================
"""

import pandas as pd


class Interpolator:
    """
    Linear interpolation pada dataset WHO.
    """

    @staticmethod
    def interpolate(df: pd.DataFrame,
                    x_column: str,
                    x_value: float):
        """
        Mengembalikan satu baris hasil interpolasi.

        Parameters
        ----------
        df : DataFrame
        x_column : umur / tinggi / panjang
        x_value : nilai yang dicari
        """

        df = df.sort_values(x_column).reset_index(drop=True)

        # tepat berada pada tabel
        exact = df[df[x_column] == x_value]

        if not exact.empty:
            return exact.iloc[0]

        # batas bawah
        lower = df[df[x_column] < x_value]

        # batas atas
        upper = df[df[x_column] > x_value]

        if lower.empty:
            return upper.iloc[0]

        if upper.empty:
            return lower.iloc[-1]

        lower = lower.iloc[-1]
        upper = upper.iloc[0]

        ratio = (
            (x_value - lower[x_column])
            /
            (upper[x_column] - lower[x_column])
        )

        result = {}

        result[x_column] = x_value

        for col in df.columns:

            if col == x_column:
                continue

            result[col] = (
                lower[col]
                +
                ratio
                *
                (upper[col] - lower[col])
            )

        return pd.Series(result)