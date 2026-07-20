"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : settings.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

from pathlib import Path

# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "NutriShield"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Smart Child Nutrition Assessment System Based on WHO Standards"
AUTHOR = "Depi Ginting"
ORGANIZATION = "Politeknik Aceh Selatan"

# ==========================================================
# PROJECT DIRECTORY
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"
CONFIG_DIR = BASE_DIR / "config"
CORE_DIR = BASE_DIR / "core"
DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "database"
PAGES_DIR = BASE_DIR / "pages"
REPORT_DIR = BASE_DIR / "reports"
SERVICES_DIR = BASE_DIR / "services"
UTILS_DIR = BASE_DIR / "utils"
COMPONENTS_DIR = BASE_DIR / "components"

# ==========================================================
# DATABASE
# ==========================================================

DATABASE_NAME = "nutrishield.db"
DATABASE_PATH = DATABASE_DIR / DATABASE_NAME

# ==========================================================
# ASSETS
# ==========================================================

LOGO_PATH = ASSETS_DIR / "logo.png"
FAVICON_PATH = ASSETS_DIR / "favicon.ico"
CSS_PATH = ASSETS_DIR / "css" / "custom.css"

# ==========================================================
# REPORT
# ==========================================================

REPORT_PREFIX = "Laporan_Gizi"

# ==========================================================
# STREAMLIT
# ==========================================================

PAGE_TITLE = APP_NAME
PAGE_ICON = str(FAVICON_PATH)
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# ==========================================================
# DATE FORMAT
# ==========================================================

DATE_FORMAT = "%d-%m-%Y"
DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"

# ==========================================================
# CREATE REQUIRED DIRECTORY
# ==========================================================

for directory in [
    DATA_DIR,
    DATABASE_DIR,
    REPORT_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)