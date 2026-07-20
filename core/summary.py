"""
====================================================
NutriShield
Summary Module
Author : Depi Ginting
====================================================
"""


class Summary:

    @staticmethod
    def generate(result: dict) -> dict:
        """
        Membuat kesimpulan status gizi berdasarkan
        hasil seluruh indikator.
        """

        summary = {

            "stunting": False,
            "underweight": False,
            "wasting": False,
            "overweight": False,
            "obesity": False,

            "status_gizi": "Normal",

            "recommendation": []
        }

        # =====================================
        # STUNTING
        # =====================================

        tb = result.get("tbu") or result.get("pbu")

        if tb:

            if "Pendek" in tb["status"] \
               or "Sangat Pendek" in tb["status"]:

                summary["stunting"] = True

        # =====================================
        # UNDERWEIGHT
        # =====================================

        bbu = result.get("bbu")

        if bbu:

            if "Kurang" in bbu["status"] \
               or "Sangat" in bbu["status"]:

                summary["underweight"] = True

        # =====================================
        # WASTING
        # =====================================

        bb = result.get("bbtb") or result.get("bbpb")

        if bb:

            if "Gizi Buruk" in bb["status"] \
               or "Gizi Kurang" in bb["status"]:

                summary["wasting"] = True

        # =====================================
        # OVERWEIGHT
        # =====================================

        if bb:

            if "Berisiko" in bb["status"] \
               or "Gizi Lebih" in bb["status"]:

                summary["overweight"] = True

        # =====================================
        # OBESITAS
        # =====================================

        if bb:

            if "Obesitas" in bb["status"]:

                summary["obesity"] = True

        # =====================================
        # STATUS AKHIR
        # =====================================

        if summary["obesity"]:

            summary["status_gizi"] = "Obesitas"

        elif summary["overweight"]:

            summary["status_gizi"] = "Gizi Lebih"

        elif summary["wasting"]:

            summary["status_gizi"] = "Wasting"

        elif summary["underweight"]:

            summary["status_gizi"] = "Underweight"

        elif summary["stunting"]:

            summary["status_gizi"] = "Stunting"

        else:

            summary["status_gizi"] = "Normal"

        # =====================================
        # REKOMENDASI
        # =====================================

        if summary["stunting"]:

            summary["recommendation"].append(
                "Lakukan pemantauan tinggi badan secara berkala."
            )

        if summary["underweight"]:

            summary["recommendation"].append(
                "Evaluasi kecukupan asupan energi dan protein."
            )

        if summary["wasting"]:

            summary["recommendation"].append(
                "Segera konsultasikan ke tenaga kesehatan."
            )

        if summary["overweight"]:

            summary["recommendation"].append(
                "Atur pola makan dan tingkatkan aktivitas fisik."
            )

        if summary["obesity"]:

            summary["recommendation"].append(
                "Lakukan evaluasi gizi secara menyeluruh."
            )

        if summary["status_gizi"] == "Normal":

            summary["recommendation"].append(
                "Pertahankan pola makan seimbang dan pemantauan rutin."
            )

        return summary