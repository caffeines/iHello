from marshmallow import ValidationError


def str_min_length(min_length, field="String"):
    def validate(s):
        if len(s) >= min_length:
            return s
        raise ValidationError(
            f"{field.capitalize()} must be at least {min_length} characters long"
        )

    return validate
