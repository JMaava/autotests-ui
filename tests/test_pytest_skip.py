import pytest


@pytest.mark.skip(reason="Фича в разаботке")
def test_feature_in_dev():
    ...


@pytest.mark.skip(reason="Фича в разаботке")
class TestSuiteSkip:
    def test_feature_in_dev_1(self):
        ...

    def test_feature_in_dev_2(self):
        ...
