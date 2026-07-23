from openpyxl.styles import PatternFill
from config.config import ERROR_FILL_COLOR

ERROR_FILL = PatternFill(
    fill_type="solid",
    fgColor=ERROR_FILL_COLOR
)