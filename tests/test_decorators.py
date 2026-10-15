from typing import Any

import pytest

from src.decorators import log


def test_log_console_success(capsys: Any) -> None:
    """Проверка логирования успешного выполнения функции в консоль."""

    @log
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


def test_log_console_error(capsys: Any) -> None:
    """Проверка логирования ошибки в консоль при вызове без параметров."""

    @log
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert (
        "divide error: ZeroDivisionError. Inputs: (1, 0), {}"
        in captured.out
    )


def test_log_file_success(tmp_path: Any) -> None:
    """Проверка логирования успешного выполнения в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    result = multiply(3, 4)

    assert result == 12
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok\n" in content


def test_log_file_error(tmp_path: Any) -> None:
    """Проверка логирования исключения в файл."""
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def raise_value_error() -> None:
        raise ValueError("Invalid value")

    with pytest.raises(ValueError):
        raise_value_error()

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert (
        "raise_value_error error: ValueError. Inputs: (), {}"
        in content
    )


@pytest.mark.parametrize(
    "a, b, expected_result, expected_log",
    [
        (10, 2, 5.0, "calc ok"),
        (100, 4, 25.0, "calc ok"),
    ],
)
def test_log_parametrized(
    capsys: Any, a: int, b: int, expected_result: float, expected_log: str
) -> None:
    """Параметризованный тест логирования вызовов с пустой скобкой @log()."""

    @log()
    def calc(x: int, y: int) -> float:
        return x / y

    res = calc(a, b)
    captured = capsys.readouterr()

    assert res == expected_result
    assert expected_log in captured.out