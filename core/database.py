"""
====================================================
NutriShield
SQLite Database Module
Author : Depi Ginting
====================================================
"""

import sqlite3
from pathlib import Path

# =====================================================
# Lokasi Database
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "nutrishield.db"


class Database:
    """
    SQLite Database Manager
    """

    def __init__(self):

        self.conn = sqlite3.connect(
                DATABASE_FILE,
                check_same_thread=False
            )

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

        self.create_tables()

    # =================================================

    def create_tables(self):
        """
        Membuat tabel jika belum ada.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nik TEXT UNIQUE,

            nama TEXT NOT NULL,

            gender TEXT,

            tanggal_lahir TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_id INTEGER,

            tanggal TEXT,

            umur_bulan REAL,

            berat REAL,

            tinggi REAL,

            bmi REAL,

            z_bbu REAL,

            status_bbu TEXT,

            z_tb REAL,

            status_tb TEXT,

            z_bb REAL,

            status_bb TEXT,

            z_imtu REAL,

            status_imtu TEXT,

            status_gizi TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(patient_id)
                REFERENCES patients(id)

        )
        """)

        self.conn.commit()

    # =================================================

    def add_patient(
        self,
        nik,
        nama,
        gender,
        tanggal_lahir
    ):

        self.cursor.execute("""
        INSERT INTO patients(
            nik,
            nama,
            gender,
            tanggal_lahir
        )

        VALUES(
            ?,?,?,?
        )
        """, (

            nik,
            nama,
            gender,
            tanggal_lahir

        ))

        self.conn.commit()

        return self.cursor.lastrowid

    # =================================================

    def get_patient(self, nik):

        self.cursor.execute("""

        SELECT *

        FROM patients

        WHERE nik=?

        """, (nik,))

        row = self.cursor.fetchone()

        if row:

            return dict(row)

        return None

    # =================================================

    def save_measurement(
        self,
        patient_id,
        result,
        tanggal
    ):

        tb_key = "pbu" if "pbu" in result else "tbu"

        bb_key = "bbpb" if "bbpb" in result else "bbtb"

        measurement = result["measurement"]

        tinggi = measurement.get(
            "height",
            measurement.get("length")
        )

        self.cursor.execute("""

        INSERT INTO measurements(

            patient_id,

            tanggal,

            umur_bulan,

            berat,

            tinggi,

            bmi,

            z_bbu,

            status_bbu,

            z_tb,

            status_tb,

            z_bb,

            status_bb,

            z_imtu,

            status_imtu,

            status_gizi

        )

        VALUES(

            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?

        )

        """, (

            patient_id,

            tanggal,

            result["identity"]["age_month"],

            measurement["weight"],

            tinggi,

            measurement["bmi"],

            result["bbu"]["zscore"],

            result["bbu"]["status"],

            result[tb_key]["zscore"],

            result[tb_key]["status"],

            result[bb_key]["zscore"],

            result[bb_key]["status"],

            result["imtu"]["zscore"],

            result["imtu"]["status"],

            result["summary"]["status_gizi"]

        ))

        self.conn.commit()

    # =================================================

    def get_history(self, patient_id):

        self.cursor.execute("""

        SELECT *

        FROM measurements

        WHERE patient_id=?

        ORDER BY tanggal DESC

        """, (patient_id,))

        rows = self.cursor.fetchall()

        return [dict(i) for i in rows]

    # =================================================

    def delete_patient(self, patient_id):

        self.cursor.execute("""

        DELETE FROM measurements

        WHERE patient_id=?

        """, (patient_id,))

        self.cursor.execute("""

        DELETE FROM patients

        WHERE id=?

        """, (patient_id,))

        self.conn.commit()

    # =================================================

    def close(self):

        self.conn.close()

    
    def get_all_measurements(self):
        """
        Get all measurement history.
        """

        query = """
        SELECT
            m.id,
            p.id AS patient_id,
            p.nik,
            p.nama,
            p.gender,
            p.tanggal_lahir,
            m.tanggal,
            m.weight,
            m.height,
            m.age_month,
            m.wfa_status,
            m.hfa_status,
            m.wfh_status,
            m.bfa_status,
            m.nutrition_status
        FROM measurements m
        JOIN patients p
            ON p.id = m.patient_id
        ORDER BY
            m.tanggal DESC
        """

        cursor = self.conn.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        return [dict(row) for row in rows]
    
    def search_measurements(self, keyword):
        """
        Search measurements by NIK or patient name.
        """

        query = """
        SELECT
            m.*,
            p.nik,
            p.nama
        FROM measurements m
        JOIN patients p
            ON p.id = m.patient_id
        WHERE
            p.nama LIKE ?
            OR
            p.nik LIKE ?
        ORDER BY
            m.tanggal DESC
        """

        cursor = self.conn.cursor()

        keyword = f"%{keyword}%"

        cursor.execute(
            query,
            (
                keyword,
                keyword,
            ),
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]
    
    def filter_measurements(self,start_date, end_date, ):
        """
        Filter measurements by date.
        """

        query = """
        SELECT
            m.*,
            p.nama,
            p.nik
        FROM measurements m
        JOIN patients p
            ON p.id = m.patient_id
        WHERE
            m.tanggal
            BETWEEN ? AND ?
        ORDER BY
            m.tanggal DESC
        """

        cursor = self.conn.cursor()

        cursor.execute(
            query,
            (
                start_date,
                end_date,
            ),
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]
    
    def delete_measurement(self,measurement_id,):
        """
        Delete measurement.
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            DELETE FROM measurements
            WHERE id=?
            """,
            (
                measurement_id,
            ),
        )

        self.conn.commit()

        return cursor.rowcount > 0
    
    def get_statistics(self):
        """
        Get dashboard statistics.
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*) FROM patients
            """
        )

        total_patient = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*) FROM measurements
            """
        )

        total_measurement = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(DISTINCT patient_id)
            FROM measurements
            """
        )

        active_patient = cursor.fetchone()[0]

        return {
            "total_patient": total_patient,
            "total_measurement": total_measurement,
            "active_patient": active_patient,
        }
    
    def today_measurements(self):
        """
        Total measurements today.
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM measurements
            WHERE tanggal = DATE('now','localtime')
            """
        )

        return cursor.fetchone()[0]
    
    def nutrition_percentage(self):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT
                nutrition_status,
                COUNT(*)
            FROM measurements
            GROUP BY nutrition_status
        """)

        rows = cursor.fetchall()

        total = sum(row[1] for row in rows)

        result = {}

        for status, jumlah in rows:

            if total == 0:
                result[status] = 0

            else:
                result[status] = round(
                    jumlah / total * 100,
                    1
                )

        return result