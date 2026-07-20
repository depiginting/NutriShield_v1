from core.loader import WHOLoader

loader = WHOLoader()

print("=" * 60)
print("TEST WHO LOADER")
print("=" * 60)

for gender in ["L", "P"]:
    print(f"\nGender : {gender}")

    for indikator in [
        "bbu",
        "pbu",
        "tbu",
        "bbpb",
        "bbtb",
        "imtu"
    ]:

        try:
            df = loader.load(gender, indikator)

            print(
                f"✓ {indikator.upper():5} | "
                f"Baris: {len(df):3} | "
                f"Kolom: {len(df.columns)} | "
                f"Kolom pertama: {df.columns[0]}"
            )

            # cek tipe data
            print(df.dtypes)

            # tampilkan 3 data pertama
            print(df.head(3))

            print("-" * 60)

        except Exception as e:
            print(f"✗ {indikator.upper()} -> {e}")