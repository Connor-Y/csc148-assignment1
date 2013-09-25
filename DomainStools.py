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
    def __init__(self: 'DomainStools', num_of_stools: int) -> None:
        self.num_of_stools = num_of_stools
        self.num_of_moves = 0
        self.stool_list = []
        for x in range(self.num_of_stools):
            self.stool_list.append([])

    def number_of_stools(self: 'DomainStools') -> int:
        """Returns the number of stools in DomainStools."""
        return self.num_of_stools

    def add(self: 'DomainStools', stool, cheese):
        self.stool_list[stool].append(cheese)

    def number_of_moves(self: 'DomainStools'):
        return self.num_of_moves

    def move(self: 'DomainStools', cheese_to_move: 'CheeseView', cheese: 'CheeseView') -> None:
        self.num_of_moves += 1
        #check that cheese_to_move is on the top of its current stool
        stool_of_cheese_to_move = -1
        for stool_index, stool in enumerate(self.stool_list):
            if cheese_to_move is stool[-1]:
                stool_of_cheese_to_move = stool_index
        if stool_of_cheese_to_move == -1:
            print("cheese_to_move is not on top")
            raise Exception

        #check that cheese is on the top of its current stool
        stool_of_cheese = -1
        for stool_index, stool in enumerate(self.stool_list):
            if cheese is stool[-1]:
                stool_of_cheese = stool_index
        if stool_of_cheese == -1:
            print("cheese to move onto is not on top")
            raise Exception

        #check if size of cheese_to_move is smaller than cheese
        if cheese_to_move.size > cheese.size:
            print("cheese size is incorrect")
            raise Exception


        #finally, move cheese
        self.stool_list[stool_of_cheese].append(self.stool_list[stool_of_cheese_to_move][-1])
        del self.stool_list[stool_of_cheese_to_move][-1]



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
