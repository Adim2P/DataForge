from pipeline.result import ValidationResult

class BaseValidator:
    
    name = "Base Validator"

    def validate(self, value: str) -> ValidationResult | None:
        raise NotImplementedError