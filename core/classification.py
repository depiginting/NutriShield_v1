"""
====================================================
NutriShield
WHO Classification
====================================================
"""


class Classification:

    @staticmethod
    def calculate(indicator: str, zscore: float) -> str:

        indicator = indicator.lower()

        # ============================================
        # BB/U
        # ============================================

        if indicator == "bbu":

            if zscore < -3:
                return "Berat Badan Sangat Kurang"

            elif zscore < -2:
                return "Berat Badan Kurang"

            elif zscore <= 1:
                return "Berat Badan Normal"

            return "Risiko Berat Badan Lebih"

        # ============================================
        # PB/U atau TB/U
        # ============================================

        elif indicator in ("pbu", "tbu"):

            if zscore < -3:
                return "Sangat Pendek"

            elif zscore < -2:
                return "Pendek (Stunting)"

            elif zscore <= 3:
                return "Normal"

            return "Tinggi"

        # ============================================
        # BB/PB atau BB/TB
        # ============================================

        elif indicator in ("bbpb", "bbtb"):

            if zscore < -3:
                return "Gizi Buruk"

            elif zscore < -2:
                return "Gizi Kurang"

            elif zscore <= 1:
                return "Gizi Baik"

            elif zscore <= 2:
                return "Berisiko Gizi Lebih"

            elif zscore <= 3:
                return "Gizi Lebih"

            return "Obesitas"

        # ============================================
        # IMT/U
        # ============================================

        elif indicator == "imtu":

            if zscore < -3:
                return "Gizi Buruk"

            elif zscore < -2:
                return "Gizi Kurang"

            elif zscore <= 1:
                return "Normal"

            elif zscore <= 2:
                return "Berisiko Gizi Lebih"

            elif zscore <= 3:
                return "Gizi Lebih"

            return "Obesitas"

        # ============================================

        raise ValueError(
            f"Indikator '{indicator}' tidak dikenali."
        )