import streamlit as st
from core.anthropometry import Anthropometry
from core.database import Database
from services.measurement_service import MeasurementService
from components.forms.patient_form import patient_form
from components.forms.measurement_form import measurement_form
from components.forms.result_panel import result_panel
if "measurement_result" not in st.session_state: st.session_state.measurement_result=None
service=MeasurementService(Database(), Anthropometry())
st.title("Pengukuran Status Gizi"); c1,c2,c3=st.columns([1.2,1,1.2])
with c1: patient=patient_form()
with c2: measurement=measurement_form()
if measurement["calculate"]:
    try:
        args={"gender":patient["gender"],"age_month":patient["umur_bulan"],"weight":measurement["weight"]}
        args["length" if patient["umur_bulan"]<24 else "height"]=measurement["height"]
        st.session_state.measurement_result=service.calculate(**args)
    except ValueError as err: st.session_state.measurement_result=None; st.error(str(err))
with c3: result_panel(st.session_state.measurement_result)
if measurement["save"]:
    if st.session_state.measurement_result is None: st.error("Hitung status gizi terlebih dahulu sebelum menyimpan.")
    elif not patient["nik"] or not patient["nama"]: st.error("NIK dan nama lengkap wajib diisi sebelum menyimpan.")
    else:
        old=service.get_patient(patient["nik"])
        pid=old["id"] if old else service.create_patient(patient["nik"],patient["nama"],patient["gender"],patient["tanggal_lahir"].isoformat())
        service.save_measurement(pid,st.session_state.measurement_result,measurement["tanggal"].isoformat()); st.success("Data berhasil disimpan.")
if measurement["reset"]: st.session_state.measurement_result=None; st.rerun()
service.close()
