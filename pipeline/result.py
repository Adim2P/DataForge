from dataclasses import dataclass
from openpyxl.cell.cell import Cell

@dataclass
class ValidationResult:
    validator: str
    message: str

@dataclass
class CellValidation:
    cell: Cell
    result: ValidationResult