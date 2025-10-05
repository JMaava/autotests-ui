import pytest

SYS_VER = "1.2.0"


@pytest.mark.skipif(
    SYS_VER == "1.3.0",
    reason="Тест не может быть запущен на версии 1.3.0"
)
def test_system_ver_val():
    ...


@pytest.mark.skipif(
    SYS_VER == "1.2.0",
    reason="Тест не может быть запущен на версии 1.2.0"
)
def test_system_ver_invalid():
    ...
