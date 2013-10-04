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
import sys

class DomainStools:
    """Model Anne Hoy's stools holding cheese.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    # TODO: See Steps 2 and 3 of the handout.
    def __init__(self: 'DomainStools', num_of_stools: int) -> None:
        """
        Initialize a new DomainStools.

        num_of_stools - the number of stools desired in the version of Anne
        Hoy's problem.
        """

        # Store num_of_stools in an instance variable.
        self.num_of_stools = num_of_stools

        # Create two instance variables for accumulation; one for the
        # number of moves performed in the problem and one for
        # the stools of cheese.
        self.num_of_moves = 0
        self.stool_list = []
        
        # Update stool_list to include nested lists refering to each
        # stool along with the base cheeses on each.
        for x in range(self.num_of_stools):
            self.stool_list.append([])
        for stool in range(self.num_of_stools):
            self.stool_list[stool].append(Cheese(sys.maxsize))

    def number_of_stools(self: 'DomainStools') -> int:
        """
        Returns the number of stools in DomainStools.
        """
        return self.num_of_stools

    def num_of_cheese_on_stool(self: 'DomainStools', stool_num: int) -> int:
        """
        Returns the number of cheese blocks on the specified stool number.

        stool_num - A stool in DomainStools.
        """
        return len(self.stool_list[stool_num])

    def add(self: 'DomainStools', stool, cheese) -> None:
        """
        Adds an additional cheese to a desired stool.

        stool - a stool in DomainStools
        cheese - a block of cheese
        """
        self.stool_list[stool].append(cheese)
        return None

    def number_of_moves(self: 'DomainStools'):
        """
        Returns the number of moves performed on the Anne Hoy problem.
        """
        return self.num_of_moves

    def move(self: 'DomainStools', cheese_to_move: 'CheeseView', cheese: 'CheeseView') -> None:
        """
        Move a cheese from a selected stool onto a target stool.

        cheese_to_move - the cheese that is selected to move
        cheese - the top cheese on the target stool
        """
        
        #check that cheese_to_move is on the top of its current stool
        stool_of_cheese_to_move = -1
        for stool_index, stool in enumerate(self.stool_list):
            if cheese_to_move is stool[-1]:
                stool_of_cheese_to_move = stool_index
        if stool_of_cheese_to_move == -1:
           # print("cheese_to_move is not on top")
            raise Exception

        #check that cheese is on the top of its current stool
        stool_of_cheese = -1
        for stool_index, stool in enumerate(self.stool_list):
            if cheese is stool[-1]:
                stool_of_cheese = stool_index
        if stool_of_cheese == -1:
         #   print("cheese to move onto is not on top")
            raise Exception

        #check if size of cheese_to_move is smaller than cheese
        if cheese_to_move.size > cheese.size:
         #   print("cheese size is incorrect")
            raise Exception

        #finally, move cheese
        self.stool_list[stool_of_cheese].append(self.stool_list[stool_of_cheese_to_move][-1])
        del self.stool_list[stool_of_cheese_to_move][-1]
        self.num_of_moves += 1

    def select_top_cheese(self: 'DomainStools', stool_idx: int):
        """
        Returns the top cheese on a desired stool.

        stool_idx - the index of the stool with the cheese desired
        """
        return self.stool_list[stool_idx][-1]

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
