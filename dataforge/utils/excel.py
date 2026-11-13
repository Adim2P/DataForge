from pathlib import Path

from openpyxl.styles import Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.worksheet import Worksheet

def data_paths() -> tuple[Path, Path]:

    input_dir = Path.cwd() / "data" / "input"
    output_dir = Path.cwd() / "data" / "output"

    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    return input_dir, output_dir

def format_worksheet(ws: Worksheet) -> None:

    if ws.max_row < 2:
        raise ValueError(
            "The worksheet needs a header row and at least one data row."
        )

    if not ws.tables:
        headers = [
            ws.cell(1, col).value
            for col in range(1, ws.max_column + 1)
        ]
        if not all(isinstance(h, str) and h.strip() for h in headers):
            raise ValueError(
                "An excel table needs nonempty, unique text headers in row 1."
            )

        if len({h.casefold() for h in headers if isinstance(h, str)}) != len(headers):
            raise ValueError(
                "An excel table needs nonempty, unique text headers in row 1."
            )

        workbook = ws.parent

        if workbook is None:
            raise ValueError("The worksheet must belong to a workbook.")

        used_names = {
            name
            for sheet in workbook.worksheets
            for name in sheet.tables
        }

        number = 1

        while f"DataForgeTable{number}" in used_names:
            number += 1

        table = Table(
            displayName=f"DataForgeTable{number}",
            ref=ws.dimensions
        )

        table.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium2",
            showRowStripes=True,
        )

        ws.add_table(table)

    thin = Side(style="thin", color="B7C2CC")

    border = Border(
        left=thin,
        right=thin,
        top=thin,
        bottom=thin,
    )

    for column in ws.iter_cols():
        max_len = max(
            (
                len(str(cell.value))
                for cell in column
                if cell.value is not None
            ),
            default = 0,
        )

        column_index = column[0].column

        if column_index is None:
            raise ValueError("The cell does not have a column index.")

        letter = get_column_letter(column_index)

        ws.column_dimensions[letter].width = min(
            max(max_len + 2, 12),
            60,
        )

        for cell in column:
            cell.border = border
