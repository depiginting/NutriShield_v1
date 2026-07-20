"""
====================================================
NutriShield
WHO Z Score
====================================================
"""


class ZScore:

    @staticmethod
    def calculate(value, ref):
        """
        value = nilai anak

        ref = hasil interpolasi
        """

        m3 = ref["sd_min3"]
        m2 = ref["sd_min2"]
        m1 = ref["sd_min1"]

        med = ref["median"]

        p1 = ref["sd_plus1"]
        p2 = ref["sd_plus2"]
        p3 = ref["sd_plus3"]

        # ===== Median sampai +1 SD =====

        if med <= value <= p1:

            return (value-med)/(p1-med)

        # ===== +1 SD sampai +2 SD =====

        if p1 < value <= p2:

            return 1 + (value-p1)/(p2-p1)

        # ===== +2 SD sampai +3 SD =====

        if p2 < value <= p3:

            return 2 + (value-p2)/(p3-p2)

        # ===== > +3 SD =====

        if value > p3:

            return 3 + (value-p3)/(p3-p2)

        # ===== Median sampai -1 SD =====

        if m1 <= value < med:

            return -(med-value)/(med-m1)

        # ===== -1 SD sampai -2 SD =====

        if m2 <= value < m1:

            return -1 - (m1-value)/(m1-m2)

        # ===== -2 SD sampai -3 SD =====

        if m3 <= value < m2:

            return -2 - (m2-value)/(m2-m3)

        # ===== < -3 SD =====

        return -3 - (m3-value)/(m2-m3)