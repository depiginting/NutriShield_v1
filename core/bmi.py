"""
====================================================
NutriShield
Body Mass Index (BMI)
Author : Depi Ginting
====================================================
"""


class BMI:
    """
    Menghitung Body Mass Index (BMI) / Indeks Massa Tubuh (IMT)
    """

    @staticmethod
    def calculate(weight: float, height: float) -> float:
        """
        Menghitung BMI.

        Parameters
        ----------
        weight : float
            Berat badan (kg)

        height : float
            Tinggi/Panjang badan (cm)

        Returns
        -------
        float
            Nilai BMI
        """

        weight = float(weight)
        height = float(height)

        if weight <= 0:
            raise ValueError(
                "Berat badan harus lebih dari 0 kg."
            )

        if height <= 0:
            raise ValueError(
                "Tinggi/Panjang badan harus lebih dari 0 cm."
            )

        height_meter = height / 100

        bmi = weight / (height_meter ** 2)

        return round(bmi, 2)