from pprint import pprint
from core.anthropometry import Anthropometry

engine = Anthropometry()

# ==============================
# TEST 1 : Laki-laki 18 bulan
# ==============================
print("=" * 70)
print("TEST 1 - Laki-laki 18 bulan")
print("=" * 70)

hasil = engine.calculate(
    gender="L",
    age_month=18,
    weight=10.8,
    length=80.3
)

pprint(hasil)

# ==============================
# TEST 2 : Perempuan 36 bulan
# ==============================
print("\n")
print("=" * 70)
print("TEST 2 - Perempuan 36 bulan")
print("=" * 70)

hasil = engine.calculate(
    gender="P",
    age_month=36,
    weight=13.5,
    height=95.6
)

pprint(hasil)