from django.core.exceptions import ValidationError


def check_raiting(value):
    if value > 10 or value < 1:
        raise ValidationError('Рейтинг выставляется от 1 до 10')


def check_phonenum(phone):
    if len(phone) != 13 or phone[0] != '+':
        raise ValidationError('Сheck if the dialed number is correct ')


def check_year_of_foundation(year):
    if year > 2022 or year < 1900:
        raise ValidationError(
            "Year couldn't be less than 1900 and more than 2022.Сheck if the dialed year is correct ")
