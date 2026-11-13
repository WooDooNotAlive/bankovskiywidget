from unittest.mock import MagicMock, patch

from src.file_readers import read_csv_file, read_excel_file


@patch("src.file_readers.Path.exists")
@patch("pandas.read_csv")
def test_read_csv_file_success(
    mock_read_csv: MagicMock, mock_exists: MagicMock
) -> None:
    """Тест успешного считывания CSV-файла."""
    mock_exists.return_value = True
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.fillna.return_value = mock_df
    mock_df.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED", "amount": "100.00"}
    ]
    mock_read_csv.return_value = mock_df

    result = read_csv_file("data/transactions.csv")
    assert result == [{"id": 1, "state": "EXECUTED", "amount": "100.00"}]
    mock_read_csv.assert_called_once()


@patch("src.file_readers.Path.exists")
def test_read_csv_file_not_found(mock_exists: MagicMock) -> None:
    """Тест отсутствия CSV-файла."""
    mock_exists.return_value = False
    result = read_csv_file("invalid_path.csv")
    assert result == []


@patch("src.file_readers.Path.exists")
@patch("pandas.read_csv")
def test_read_csv_file_exception(
    mock_read_csv: MagicMock, mock_exists: MagicMock
) -> None:
    """Тест обработки ошибки при чтении CSV."""
    mock_exists.return_value = True
    mock_read_csv.side_effect = Exception("CSV Read Error")

    result = read_csv_file("data/corrupted.csv")
    assert result == []


@patch("src.file_readers.Path.exists")
@patch("pandas.read_excel")
def test_read_excel_file_success(
    mock_read_excel: MagicMock, mock_exists: MagicMock
) -> None:
    """Тест успешного считывания Excel-файла."""
    mock_exists.return_value = True
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.fillna.return_value = mock_df
    mock_df.to_dict.return_value = [
        {"id": 2, "state": "CANCELED", "amount": "250.00"}
    ]
    mock_read_excel.return_value = mock_df

    result = read_excel_file("data/transactions_excel.xlsx")
    assert result == [{"id": 2, "state": "CANCELED", "amount": "250.00"}]
    mock_read_excel.assert_called_once()


@patch("src.file_readers.Path.exists")
def test_read_excel_file_not_found(mock_exists: MagicMock) -> None:
    """Тест отсутствия Excel-файла."""
    mock_exists.return_value = False
    result = read_excel_file("invalid_path.xlsx")
    assert result == []


@patch("src.file_readers.Path.exists")
@patch("pandas.read_excel")
def test_read_excel_file_exception(
    mock_read_excel: MagicMock, mock_exists: MagicMock
) -> None:
    """Тест обработки ошибки при чтении Excel."""
    mock_exists.return_value = True
    mock_read_excel.side_effect = Exception("Excel Read Error")

    result = read_excel_file("data/corrupted.xlsx")
    assert result == []
