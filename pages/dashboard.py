import pandas as pd
import streamlit as st

from services.service_container import services
from components.cards.metric_card import metric_card


# =====================================
# TITLE
# =====================================

st.title("Dashboard")

# =====================================
# LOAD DATA
# =====================================

stats = services.dashboard.get_statistics()

# =====================================
# METRIC CARD
# =====================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    metric_card(
        "Total Anak",
        stats["total_patient"]
    )

with col2:
    metric_card(
        "Pengukuran",
        stats["total_measurement"]
    )

with col3:
    metric_card(
        "Hari Ini",
        stats["today"]
    )

with col4:

    normal = stats["percentage"].get(
        "Normal",
        0
    )

    metric_card(
        "Normal",
        f"{normal}%"
    )



chart = pd.DataFrame(...)

st.bar_chart(chart)

# =====================================
# DISTRIBUSI STATUS GIZI
# =====================================

st.subheader("Distribusi Status Gizi")

for status, jumlah in stats["nutrition"].items():
    st.write(f"{status} : {jumlah}")

# =====================================
# PENGUKURAN TERAKHIR
# =====================================

latest = services.dashboard.latest_measurements()

if latest:

    df = pd.DataFrame(latest)

    columns = [
        "nama",
        "tanggal",
        "weight",
        "height",
        "nutrition_status",
    ]

    df = df[columns]

    df.columns = [
        "Nama",
        "Tanggal",
        "BB (kg)",
        "TB (cm)",
        "Status Gizi",
    ]

    st.subheader("Pengukuran Terakhir")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )


    latest = services.dashboard.latest_measurements()

...

st.dataframe(df)

risk = services.dashboard.risk_children()

if risk:

    df = pd.DataFrame(risk)

    st.dataframe(df)