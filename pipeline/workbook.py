from pathlib import Path
from openpyxl import Workbook, load_workbook
from config import OUTPUT_SUFFIX
from logger import get_logger

logger = get_logger(__name__)

def open_workbook(file_path: str) -> Workbook:
    logger.info(f"Opening workbook: {file_path}")

    try:
        workbook = load_workbook(file_path)

        logger.info("Workbook opened successfully.")

        return workbook
    
    except Exception:
        logger.exception(
            f"Failed to open workbook: {file_path}"
        )
        raise

def generate_output_path(file_path: str) -> Path:
    path = Path(file_path)

    output_directory = Path("output")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = output_directory / (
        f"{path.stem}{OUTPUT_SUFFIX}{path.suffix}"
    )

    logger.info(f"Generated output path: {output_path}")

    return output_path

def save_workbook(workbook: Workbook, output_path: Path) -> None:
    logger.info(f"Saving workbook: {output_path}")

    try:
        workbook.save(output_path)
        
        logger.info("Workbook saved successfully.")

    except Exception:
        logger.exception(
            f"Failed to save workbook: {output_path}"
        )
        raise
