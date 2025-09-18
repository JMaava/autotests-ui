import pytest


def test_user_login():
    print("Hello")


def test_greeting():
    greeting = "Hello, world!"
    assert greeting != "Hi, world!"


def test_in_list():
    assert 3 in [1, 2, 3, 4]


# Конструкция with pytest.raises проверяет, что данная ошибка действительно возникла. В результате, тест пройдет
# успешно (статус PASSED), поскольку ошибка является ожидаемым поведением
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# def test_sum():
#     assert 1 + 1 == 3, "Сумма 1 и 1 должна быть 2!"


class TestUserLogin:
    def test1(self):
        ...
