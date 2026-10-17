import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для автоматического логирования выполнения функций.

    Логирует успешное завершение выполнения или возникающие ошибки.
    При указании filename логирует в файл, иначе выводит в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = (
                    f"{func.__name__} error: {error_type}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(log_message, filename)
                raise e

        return wrapper

    if callable(filename):
        func = filename
        filename = None
        return decorator(func)

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """Вспомогательная функция для записи сообщений в файл или в консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)