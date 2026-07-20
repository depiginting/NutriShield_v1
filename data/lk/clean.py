df.columns = df.columns.str.strip().str.lower()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace('"', "", regex=False)
        )

        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass