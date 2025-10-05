import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number_i', [1, 2,-1 , 3])
def test_numbers(number_i: int):
    print(f'Number: {number_i}')
    assert number_i > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperation:
    @pytest.mark.parametrize('account', ['Credit', 'Debit'])
    def test_user_with_operation(self, user: str, account: str):
        ...

    def test_user_without_operation(self, user: str):
        ...


users = {
    '+700000000011':'User with money',
    '+700000000022': 'User without money'
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
                         )
def test_identifiers(phone_number: str):
    ...

