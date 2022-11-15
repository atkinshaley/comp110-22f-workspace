"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730480669"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, another: Point) -> float:
        length: float = sqrt((self.x - another.x)**2 + (self.y - another.y)**2)
        return length

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        self.location = self.location.add(self.direction)

    def contract_disease(self) -> None:
        """Assigns INFECTED state to Cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Tests non-sickness of Cell."""
        return self.sickness == constants.VULNERABLE

    def is_infected(self) -> bool:
        """Tests sickness of Cell."""
        return self.sickness == constants.INFECTED

    def color(self) -> str:
        """Determines color of Cell based on sickness."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "pink"

    def contact_with(self, another: Cell) -> None:
        if self.is_vulnerable and another.is_infected:
                self.contract_disease()
        if self.is_infected and another.is_vulnerable:
                another.contract_disease()

        



class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infection_count: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infection_count <= 0:
            raise ValueError("Initial cell infection population must be greater than zero!")
        if infection_count > cells:
            raise ValueError("Infected cell count cannot exceed cell population.")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infection_count:
                cell.contract_disease()
            self.population.append(cell)
        

    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0* pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
            i: int = 0
            j: int = 0
            while i < len(self.population):
                j = i + 1
                while j < len(self.population):
                    if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                        self.population[i].contact_with(self.population[j])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False