"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730480669"


class Simpy:
    """A class that is based off of the NumPy library."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the values of the Simpy object to the arguments passed in."""
        self.values = values

    def __repr__(self) -> str:
        """Returns a str representation of a Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, numbs: float, how_many: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        j: int = 0
        self.values = []
        while j < how_many:
            self.values.append(numbs)
            j += 1
        return f"Simpy({self.values})"

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values in a Simpy object with a range in terms of floats."""
        j: int = start
        assert step != 0.0
        while abs(j) < abs(stop):
            if j == start:
                self.values.append(start)
                j += step
            else:
                start += step
                self.values.append(start)
                j += step
        return f"Simpy({self.values})"

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute of a Simpy object."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Produces a new Simpy object where each item corresponds to the original Simpy object."""
        new_simp: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                new_simp.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                new_simp.values.append(self.values[i] + rhs)
                i += 1
        return new_simp

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Produces a new Simpy object where each item corresponds to the original Simpy object exponentially."""
        new_simp: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                new_simp.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                new_simp.values.append(self.values[i] ** rhs)
                i += 1
        return new_simp

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines if a Simpy object is equal to another Simpy object or float value."""
        i: int = 0
        new_list: list[bool] = []
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                new_list.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                new_list.append(self.values[i] == rhs)
                i += 1
        return new_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines if a value of a Simpy is greater than another Simpy or a float."""
        i: int = 0
        new_list: list[bool] = []
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                new_list.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                new_list.append(self.values[i] > rhs)
                i += 1
        return new_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns either a float or a Simpy thorugh subscription."""
        subval: float
        new_simp: Simpy = []
        i: int = 0
        if isinstance(rhs, int):
            subval = self.values[rhs]
            return subval
        else:
            while i < len(rhs):
                if rhs[i]:
                    new_simp.append(self.values[i])
                i += 1
            return f"Simpy({new_simp})"