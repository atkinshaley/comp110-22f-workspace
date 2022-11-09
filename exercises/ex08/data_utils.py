"""Dictionary related utility functions."""

__author__ = "730480669"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(constant: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new table with only N rows of data."""
    i: int = 0
    new_dict: dict[str, list[str]] = {}
    for column in constant:
        new_values: list[str] = []
        while i < N: 
            new_values.append(column)
            i += 1
        new_dict = [constant[column], new_values]
    return new_dict


def select(constant: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns a subset of the original dictionary."""
    new_dict: dict[str, list[str]] = {}
    for x in constant:
        new_dict[x] = constant[columns]
    return new_dict


def concat(constant: dict[str, list[str]], constant_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a new column-based table withtwocolumn-based tables combined."""
    table: dict[str, list[str]] = {}
    return table


def count(counter: list[str]) -> dict[str, int]:
    """Produces a dictionary and counts the times a value appears in the given list."""
    new_dict: dict[counter: list[str], int] = {}
    for item in counter:
        if item in counter:
            new_dict[counter] += 1
        else:
            new_dict[counter] = 1
    return new_dict