"""
====================================================
NutriShield Loader WHO Dataset
Author : Depi Ginting
====================================================
"""

from pathlib import Path
import pandas as pd

from core.config import (
    LK_DIR,
    PR_DIR,
    INDICATORS,
    GENDER,
    SD_COLUMNS
)


class WHOLoader:
    """
    Loader dataset WHO.
    """

    def __init__(self):
        self._cache = {}

    def load(self, gender: str, indicator: str) -> pd.DataFrame:
        """
        Membaca dataset WHO berdasarkan jenis kelamin
        dan indikator.

        Parameters
        ----------
        gender : str
            L / P / LK / PR

        indicator : str
            bbu
            pbu
            tbu
            bbpb
            bbtb
            imtu
        """

        gender = gender.upper()

        if gender not in GENDER:
            raise ValueError(
                f"Gender '{gender}' tidak dikenali."
            )

        gender_folder = GENDER[gender]

        indicator = indicator.lower()

        if indicator not in INDICATORS:
            raise ValueError(
                f"Indikator '{indicator}' tidak tersedia."
            )

        key = (gender_folder, indicator)

        if key in self._cache:
            return self._cache[key]

        folder = LK_DIR if gender_folder == "lk" else PR_DIR

        file_path = folder / f"{indicator}.csv"

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        df = pd.read_csv(file_path)

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        for col in df.columns:

            if df[col].dtype == object:

                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(",", ".", regex=False)
                )

                try:
                    df[col] = pd.to_numeric(df[col])
                except:
                    pass

        for col in SD_COLUMNS:

            if col not in df.columns:
                raise ValueError(
                    f"Kolom '{col}' tidak ditemukan "
                    f"pada {file_path.name}"
                )

        self._cache[key] = df

        return df

    def clear_cache(self):
        """
        Menghapus cache dataset.
        """
        self._cache.clear()