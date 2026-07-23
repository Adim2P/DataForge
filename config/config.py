from pathlib import Path
from configparser import ConfigParser
import os

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE =  BASE_DIR / "config.ini"

config = ConfigParser()

def load_config():

    if not os.path.exists(CONFIG_FILE):
        print("[INFO] config.ini was not found, creating new one")

        config["Fill Color"] = {
            "error_fill": "FFF383FF"
        }

        config["Font Color"] = {
            "error_color": "9C0006"
        }

        config["Cell Formula"] = {
            "validate_formula": "False"
        }

        config["Append"] = {
            "output": "_validated"
        }

        with open(CONFIG_FILE, "w") as f:
            config.write(f)

    else:
        config.read(CONFIG_FILE)

load_config()

# Fill Color

ERROR_FILL_COLOR = (
    config["Fill Color"]["error_fill"]
)

# Font Color

ERROR_FONT_COLOR = (
    config["Font Color"]["error_color"]
)

# Cell Formula

VALIDATE_FORMULAS = config.getboolean(
    "Cell Formula",
    "validate_formulas"
)

# Append (Suffixes/Prefixes)

OUTPUT_SUFFIX = (
    config["Append"]["output"]
)