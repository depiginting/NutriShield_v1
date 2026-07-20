"""
====================================================
NutriShield
Age Calculation Module
Author : Depi Ginting
====================================================
"""

from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Age:

    @staticmethod
    def _to_date(value):
        """
        Mengubah string YYYY-MM-DD atau datetime menjadi date.
        """

        if isinstance(value, date):
            return value

        if isinstance(value, datetime):
            return value.date()

        return datetime.strptime(value, "%Y-%m-%d").date()

    # ======================================================

    @staticmethod
    def calculate(date_of_birth, tanggal=None):
        """
        Menghitung umur berdasarkan tanggal lahir dan
        tanggal pengukuran.

        Parameters
        ----------
        date_of_birth : date | str
        tanggal : date | str

        Returns
        -------
        dict
        """

        dob = Age._to_date(date_of_birth)

        if tanggal is None:
            tanggal = date.today()

        measure = Age._to_date(tanggal)

        if measure < dob:
            raise ValueError(
                "Tanggal pengukuran tidak boleh lebih kecil dari tanggal lahir."
            )

        delta = relativedelta(measure, dob)

        total_days = (measure - dob).days

        total_months = (
            delta.years * 12
            + delta.months
            + (delta.days / 30.4375)
        )

        return {

            "years": delta.years,

            "months": delta.months,

            "days": delta.days,

            "total_days": total_days,

            "total_months": round(total_months, 2)

        }