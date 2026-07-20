"""
====================================================
NutriShield
Anthropometry Engine
Author : Depi Ginting
====================================================
"""

from core.loader import WHOLoader
from core.validator import Validator
from core.interpolation import Interpolator
from core.zscore import ZScore
from core.classification import Classification
from core.bmi import BMI
from core.summary import Summary


class Anthropometry:
    """
    Engine utama perhitungan antropometri WHO.
    """

    def __init__(self):
        self.loader = WHOLoader()

    def _reference(self, df, x_column, x_value):
        return Interpolator.interpolate(df, x_column, x_value)

    def _result(self, indicator, value, ref):

        z = float(round(ZScore.calculate(value, ref), 2))

        return {
            "value": float(value),
            "zscore": z,
            "status": Classification.calculate(indicator, z)
         }

    def calculate(
        self,
        gender,
        age_month,
        weight,
        height=None,
        length=None
    ):

        gender = Validator.gender(gender)
        age_month = Validator.age(age_month)
        weight = Validator.weight(weight)

        if age_month < 24:
            if length is None:
                raise ValueError(
                    "Panjang badan diperlukan untuk usia <24 bulan."
                )
            measurement = Validator.height(length)
            tb_indicator = "pbu"
            bb_indicator = "bbpb"
            xcol = "panjang"
            measurement_name = "length"
        else:
            if height is None:
                raise ValueError(
                    "Tinggi badan diperlukan untuk usia ≥24 bulan."
                )
            measurement = Validator.height(height)
            tb_indicator = "tbu"
            bb_indicator = "bbtb"
            xcol = "tinggi"
            measurement_name = "height"

        df_bbu = self.loader.load(gender, "bbu")
        df_tb = self.loader.load(gender, tb_indicator)
        df_bb = self.loader.load(gender, bb_indicator)
        df_imtu = self.loader.load(gender, "imtu")

        ref_bbu = self._reference(df_bbu, "umur", age_month)
        ref_tb = self._reference(df_tb, "umur", age_month)
        ref_bb = self._reference(df_bb, xcol, measurement)

        bmi = BMI.calculate(weight, measurement)
        ref_imtu = self._reference(df_imtu, "umur", age_month)

        result = {
            "identity": {
                "gender": gender,
                "age_month": age_month,
            },
            "measurement": {
                "weight": weight,
                measurement_name: measurement,
                "bmi": bmi,
            },
            "bbu": self._result("bbu", weight, ref_bbu),
            tb_indicator: self._result(tb_indicator, measurement, ref_tb),
            bb_indicator: self._result(bb_indicator, weight, ref_bb),
            "imtu": self._result("imtu", bmi, ref_imtu),
        }

        result["summary"] = Summary.generate(result)

        return result
