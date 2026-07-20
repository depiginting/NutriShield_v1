from core.loader import WHOLoader
from core.interpolation import Interpolator
from core.zscore import ZScore
from core.classification import Classification
from core.validator import Validator
from core.bmi import BMI
from core.summary import Summary


class Anthropometry:

    def __init__(self):
        self.loader = WHOLoader()

    def calculate(
        self,
        gender,
        age_month,
        weight,
        height=None,
        length=None
    ):
        """
        Perhitungan antropometri WHO.

        Parameters
        ----------
        gender : str
            "L" atau "P"

        age_month : float
            Umur dalam bulan.

        weight : float
            Berat badan (kg).

        height : float, optional
            Tinggi badan (cm) untuk usia >=24 bulan.

        length : float, optional
            Panjang badan (cm) untuk usia <24 bulan.
        """

        # =====================================================
        # VALIDASI
        # =====================================================

        Validator.gender(gender)
        Validator.age(age_month)
        Validator.weight(weight)

        if age_month < 24:

            if length is None:
                raise ValueError(
                    "Panjang badan diperlukan untuk usia <24 bulan."
                )

            Validator.height(length)

            indikator_tb = "pbu"
            indikator_bb = "bbpb"

            ukuran = length
            ukuran_key = "length"

        else:

            if height is None:
                raise ValueError(
                    "Tinggi badan diperlukan untuk usia ≥24 bulan."
                )

            Validator.height(height)

            indikator_tb = "tbu"
            indikator_bb = "bbtb"

            ukuran = height
            ukuran_key = "height"

        # =====================================================
        # LOAD DATASET
        # =====================================================

        df_bbu = self.loader.load(gender, "bbu")
        df_tb = self.loader.load(gender, indikator_tb)
        df_bb = self.loader.load(gender, indikator_bb)

        # =====================================================
        # INTERPOLASI REFERENSI
        # =====================================================

        ref_bbu = Interpolator.interpolate(
            df=df_bbu,
            x_column="umur",
            x_value=age_month
        )

        ref_tb = Interpolator.interpolate(
            df=df_tb,
            x_column="umur",
            x_value=age_month
        )

        kolom = "panjang" if indikator_bb == "bbpb" else "tinggi"

        ref_bb = Interpolator.interpolate(
            df=df_bb,
            x_column=kolom,
            x_value=ukuran
        )

        # =====================================================
        # Z SCORE
        # =====================================================

        z_bbu = ZScore.calculate(
            value=weight,
            reference=ref_bbu
        )

        z_tb = ZScore.calculate(
            value=ukuran,
            reference=ref_tb
        )

        z_bb = ZScore.calculate(
            value=weight,
            reference=ref_bb
        )

        # =====================================================
        # BMI
        # =====================================================

        bmi = BMI.calculate(
            weight=weight,
            height=ukuran
        )

        # =====================================================
        # KLASIFIKASI
        # =====================================================

        status_bbu = Classification.calculate(
            "bbu",
            z_bbu
        )

        status_tb = Classification.calculate(
            indikator_tb,
            z_tb
        )

        status_bb = Classification.calculate(
            indikator_bb,
            z_bb
        )

        # =====================================================
        # HASIL
        # =====================================================

        hasil = {
            "gender": gender,
            "age_month": age_month,
            "weight": weight,
            ukuran_key: ukuran,

            "bbu": {
                "zscore": round(z_bbu, 2),
                "status": status_bbu
            },

            indikator_tb: {
                "zscore": round(z_tb, 2),
                "status": status_tb
            },

            indikator_bb: {
                "zscore": round(z_bb, 2),
                "status": status_bb
            },

            "bmi": round(bmi, 2)
        }

        # =====================================================
        # SUMMARY
        # =====================================================

        try:
            hasil["summary"] = Summary.generate(hasil)
        except Exception:
            # Jika Summary belum final, engine tetap mengembalikan hasil utama.
            pass

        return hasil