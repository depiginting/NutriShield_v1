"""
====================================================
Test Database NutriShield
====================================================
"""

from pprint import pprint

from core.database import Database
from core.anthropometry import Anthropometry

# =====================================================
# Inisialisasi
# =====================================================

db = Database()
engine = Anthropometry()

print("=" * 60)
print("DATABASE BERHASIL DIBUAT")
print("=" * 60)

# =====================================================
# Tambah pasien
# =====================================================

nik = "1201010101010001"

patient = db.get_patient(nik)

if patient is None:

    patient_id = db.add_patient(
        nik=nik,
        nama="Andi Saputra",
        gender="L",
        tanggal_lahir="2025-01-15"
    )

    print("\nPasien baru ditambahkan.")
    print("Patient ID :", patient_id)

else:

    patient_id = patient["id"]

    print("\nPasien sudah ada.")
    print("Patient ID :", patient_id)

# =====================================================
# Ambil data pasien
# =====================================================

print("\nDATA PASIEN")

patient = db.get_patient(nik)

pprint(patient)

# =====================================================
# Hitung antropometri
# =====================================================

print("\nHASIL ANTROPOMETRI")

hasil = engine.calculate(
    gender="L",
    age_month=18,
    weight=10.8,
    length=80.3
)

pprint(hasil)

# =====================================================
# Simpan hasil
# =====================================================

db.save_measurement(
    patient_id=patient_id,
    result=hasil,
    tanggal="2026-07-20"
)

print("\nHASIL BERHASIL DISIMPAN")

# =====================================================
# Tampilkan riwayat
# =====================================================

print("\nRIWAYAT PEMERIKSAAN")

history = db.get_history(patient_id)

for item in history:

    pprint(item)

# =====================================================
# Tutup koneksi
# =====================================================

db.close()

print("\nSELESAI")