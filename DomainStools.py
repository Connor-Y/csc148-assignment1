# Copyright 2013 Gary Baumgartner
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
DomainStools:  Model Anne Hoy's stools holding cheeses.
Cheese:   Model a cheese with a given size
"""


class DomainStools:
    """Model Anne Hoy's stools holding cheese.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    # TODO: See Steps 2 and 3 of the handout.
    def __init__(self: 'DomainStools', number_of_stools: int) -> None:
        self.number_of_stools = number_of_stools

    def number_of_stools() -> int:
        """Returns the number of stools in DomainStools."""
        return self.number_of_stools

    def add(stool, cheese):
        pass

    def number_of_moves():
        pass

    def move(cheese_to_move, cheese):
        pass
    pass


class Cheese:
    def __init__(self: 'Cheese', size: float) -> None:
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """

        self.size = size
