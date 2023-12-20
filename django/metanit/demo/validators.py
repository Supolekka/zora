from django.core.exceptions import ValidationError
def validate_pasword_len(password):
    if len(password) < 8:
        raise ValidationError('Длина пароля не может быть меньше 8 символов')