import re
from logger import get_logger
from pipeline.result import ValidationResult
from validators.base import BaseValidator

logger = get_logger(__name__)

class NonLatinValidator(BaseValidator):
    
    name = "Non-Latin Validator"

    PATTERN = re.compile(
        r"[^A-Za-zÀ-ÿ0-9 .,&'()\/+_*\-\":!@]"
    )

    def validate(self, value: str):
        if self.PATTERN.search(value):

            logger.debug(
                f"Foreign characters detected: {value}"
            )

            return ValidationResult(
                validator=self.name,
                message="Contains non-Latin characters."
            )
        
        return None