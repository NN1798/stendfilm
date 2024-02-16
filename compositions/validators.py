from django.core.validators import RegexValidator


year_validator = RegexValidator(
    regex='^[1-9][0-9]{3}$',
    message='Введите год, состоящий из 4 цифр'
)

budget_validator = RegexValidator(
    regex='^[1-9]\d*|0$',
    message='Введите неотрицательное число'
)
