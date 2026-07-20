from core.loader import WHOLoader
from core.interpolation import Interpolator

loader = WHOLoader()

# contoh BBTB laki-laki
df = loader.load("L", "bbtb")

# tinggi yang tidak ada di tabel
tinggi = 80.3

hasil = Interpolator.interpolate(
    df=df,
    x_column="tinggi",
    x_value=tinggi
)

print("=" * 50)
print(f"Tinggi : {tinggi} cm")
print("=" * 50)

for k, v in hasil.items():
    print(f"{k:12}: {v}")