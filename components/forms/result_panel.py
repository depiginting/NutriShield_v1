import streamlit as st


def result_panel(result: dict | None):
    """Tampilkan hasil analisis antropometri."""
    st.subheader("Hasil Analisis")

    if result is None:
        st.info("Silakan lakukan pengukuran terlebih dahulu.")
        return

    tb_key = "pbu" if "pbu" in result else "tbu"
    bb_key = "bbpb" if "bbpb" in result else "bbtb"

    metrics = [
        ("BB/U", result["bbu"]),
        ("PB/U" if tb_key == "pbu" else "TB/U", result[tb_key]),
        ("BB/PB" if bb_key == "bbpb" else "BB/TB", result[bb_key]),
        ("IMT/U", result["imtu"]),
    ]

    for label, item in metrics:
        st.metric(label, item["status"], f'Z = {item["zscore"]:.2f}')

    summary = result["summary"]
    st.success(f'Status Gizi: **{summary["status_gizi"]}**')

    recommendations = summary.get("recommendation", [])
    if recommendations:
        st.info("\n".join(f"• {item}" for item in recommendations))
