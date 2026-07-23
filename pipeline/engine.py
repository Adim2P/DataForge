from openpyxl import Workbook
from logger import get_logger
from pipeline.result import CellValidation
from pipeline.styles import ERROR_FILL
from config.config import VALIDATE_FORMULAS

logger = get_logger(__name__)

class ValidationEngine:

    def __init__(self, validators: list):
        self.validators = validators

    def run(self, workbook: Workbook):
        results = []

        logger.info("Starting Validation pipeline.")

        for worksheet in workbook.worksheets:
            logger.info(f"Scanning worksheet: {worksheet.title}")

            for row in worksheet.iter_rows():
                for cell in row:
                    if cell.data_type == "f" and not VALIDATE_FORMULAS:
                        continue

                    if cell.value is None:
                        continue

                    if not isinstance(cell.value, str):
                        continue

                    if not cell.value.strip():
                        continue

                    for validator in self.validators:
                        result = validator.validate(cell.value)

                        if result:
                            logger.info(
                                f"[{validator.name}] "
                                f"{worksheet.title}!{cell.coordinate} "
                                f"-> {cell.value}"
                            )

                            cell.fill = ERROR_FILL

                            results.append(
                                CellValidation(
                                    cell=cell,
                                    result=result
                                )
                            )
        logger.info(
            f"Validation completed. {len(results)} issue(s) found."
        )

        return results
        