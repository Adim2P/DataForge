from logger import get_logger

from pipeline.engine import ValidationEngine
from pipeline.workbook import (
    generate_output_path,
    open_workbook,
    save_workbook
)
from validators.registry import VALIDATORS
from pipeline.file_dialog import select_workbook

logger = get_logger(__name__)

def main():

    print("DataForge v0.1")
    print("Excel Validation Utility")

    print("\n1. Validate Workbook")
    print("2. Exit\n")

    print("\nChoose an option:")

    choice = input("> ").strip()

    if choice != '1':
        print("\nGoodbye!")
        return
    
    file_path = select_workbook()

    if not file_path:
        print("\nNo workbook selected.")
        return
    
    logger.info(f"Workbook selected: {file_path}")

    workbook = open_workbook(file_path)
    engine = ValidationEngine(VALIDATORS)
    results = engine.run(workbook)

    output_path = generate_output_path(file_path)
    save_workbook(workbook, output_path)

    print("\nValidation Complete")
    print(f"Issues Found : {len(results)}")

if __name__ == "__main__":
    main()
