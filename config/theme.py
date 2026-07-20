"""
=========================================================
NutriShield
Smart Child Nutrition Assessment System Based on WHO Standards

File    : theme.py
Author  : Depi Ginting
Version : 1.0.0
=========================================================
"""

# ==========================================================
# COLOR PALETTE
# ==========================================================

PRIMARY_COLOR = "#1565C0"
SECONDARY_COLOR = "#42A5F5"

SUCCESS_COLOR = "#2E7D32"
WARNING_COLOR = "#EF6C00"
DANGER_COLOR = "#C62828"
INFO_COLOR = "#0288D1"

BACKGROUND_COLOR = "#F5F7FA"
CARD_COLOR = "#FFFFFF"

TEXT_COLOR = "#263238"
TEXT_SECONDARY_COLOR = "#607D8B"

BORDER_COLOR = "#E0E0E0"

# ==========================================================
# TYPOGRAPHY
# ==========================================================

FONT_FAMILY = "Inter"

TITLE_SIZE = "28px"
SUBTITLE_SIZE = "20px"
TEXT_SIZE = "15px"
SMALL_TEXT_SIZE = "13px"

# ==========================================================
# LAYOUT
# ==========================================================

SIDEBAR_WIDTH = 260

CARD_RADIUS = 12

BUTTON_RADIUS = 8

CARD_PADDING = 16

PAGE_PADDING = 20

# ==========================================================
# ICONS
# ==========================================================

ICON_DASHBOARD = "dashboard"
ICON_MEASUREMENT = "straighten"
ICON_HISTORY = "history"
ICON_GRAPH = "monitoring"
ICON_REPORT = "description"
ICON_SETTINGS = "settings"
ICON_ABOUT = "info"

# ==========================================================
# STATUS COLORS
# ==========================================================

STATUS_COLOR = {
    "Normal": SUCCESS_COLOR,
    "Gizi Baik": SUCCESS_COLOR,
    "Risiko": WARNING_COLOR,
    "Gizi Kurang": WARNING_COLOR,
    "Gizi Lebih": WARNING_COLOR,
    "Stunting": DANGER_COLOR,
    "Severely Stunted": DANGER_COLOR,
    "Gizi Buruk": DANGER_COLOR,
    "Obesitas": DANGER_COLOR,
}

# ==========================================================
# CHART COLORS
# ==========================================================

CHART_COLORS = [
    PRIMARY_COLOR,
    SUCCESS_COLOR,
    WARNING_COLOR,
    DANGER_COLOR,
    INFO_COLOR,
]