from tkinter import Tk
from tkinter.filedialog import askopenfilename

from logger import get_logger

logger = get_logger(__name__)

def select_workbook() -> str:

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    file_path = askopenfilename(
        title="Select an Excel Workbook",
        filetypes=[
            ("Excel Workbook", "*.xlsx *.xlsm *.xltx *.xltm"),
            ("All Files", "*.*")
        ]
    )

    root.destroy()

    if file_path:
        logger.info(f"Workbook selected: {file_path}")
    else:
        logger.info("Workbook selection cancelled.")

    return file_path
