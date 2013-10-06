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
SolvingController: GUI window for automatically solving Anne Hoy's problems.
"""

from DomainStools import DomainStools
from CheeseView import CheeseView
import tkinter as TI
import time
import math


class SolvingController:
    def __init__(self: 'SolvingController',
                 number_of_cheeses: int,
                 content_width: float, content_height: float,
                 cheese_scale: float, time_delay: float):
        """
        Initialize a new SolvingController.

        number_of_cheeses - number of cheese to tower on the first stool,
                            not counting the bottom cheese acting as stool
        content_width - width in pixels of the working area
        content_height - height in pixels of the working area
        cheese_scale - height in pixels for showing cheese thicknesses,
                       and to scale cheese diameters
        time_delay - number of seconds to pause b/w highlighting a cheese to move and moving it
        """

        self.domain = DomainStools(4)
        self.cheese_to_move = None
        self.blinking = False
        self.cheese_scale = cheese_scale
        self.time_delay = time_delay
        self.number_of_cheeses = number_of_cheeses
        self.root = TI.Tk()        
        #creating variable canvas
        canvas = TI.Canvas(self.root,
                           background="blue",
                           width=content_width, height=content_height)

        canvas.pack(expand=True, fill=TI.BOTH)

        self.moves_label = TI.Label(self.root)
        self.show_number_of_moves()
        self.moves_label.pack()
        #Adding desired number of cheeses to the first stool
        for stool in range(self.domain.number_of_stools()):
            total_size = 0
            for size in range(1 + (number_of_cheeses if stool == 0 else 0)):
                cheese = CheeseView(self.cheese_scale *
                                    (number_of_cheeses + 1 - size),
                                    lambda cheese: self.clicked(cheese),
                                    canvas,
                                    self.cheese_scale,
                                    content_width *
                                    (stool + 1) /
                                    (self.domain.number_of_stools() + 1.0),
                                    content_height - cheese_scale / 2
                                    - total_size)
                self.domain.add(stool, cheese)
                total_size += self.cheese_scale

    def show_number_of_moves(self: 'SolvingController'):
        """Show the number of moves so far."""

        self.moves_label.config(text='Number of moves: ' +
                                str(self.domain.number_of_moves()))

    def clicked(self: 'SolvingController', cheese: CheeseView):
        """React to cheese being clicked: if not in the middle of blinking
           then select cheese for moving, or for moving onto.

           cheese - clicked cheese
        """
        pass

    def select(self: 'SolvingController', cheese: CheeseView):
        """If no cheese is selected to move, select cheese and highlight it.
           Otherwise try moving the currently selected cheese onto cheese:
           if that's not a valid move, blink the currently selected cheese.

           cheese - cheese to select for moving, or to try moving onto.
        """
        #If no cheese is currently selected, select and highlight the 
        #selected cheese
        self.root.update()
        time.sleep(self.time_delay)
        if self.cheese_to_move is None:
            self.cheese_to_move = cheese
            self.cheese_to_move.highlight(True)
        else:
            #If the cheese you are trying to move to is not the selected cheese
            if cheese is not self.cheese_to_move:
                self.domain.move(self.cheese_to_move, cheese)
                self.cheese_to_move.place(cheese.x_center,
                                          cheese.y_center
                                          - self.cheese_scale)
                self.show_number_of_moves()
            self.cheese_to_move.highlight(False)
            self.cheese_to_move = None


def solve(solver: 'SolvingController', 
          n: int, 
          stools: DomainStools,
          inp: int, aux1: int, aux2: int, output: int) -> None:
    """
    Recursive function that determines which moves to make to solve the
    Tower of Anne Hoy (4 stools)
    
    n - Total number of cheeses that are not solved
    stools -  Model Anne Hoy's stools holding cheeses
    inp - input which cheese to be moved
    aux1, aux2 - middle stools used to move cheeses
    output - target goal for cheese
    """ 
    
    if n == 1:
        solver.select(stools.select_top_cheese(inp))
        time.sleep(solver.time_delay)
        solver.select(stools.select_top_cheese(output))
    else:
        i = math.ceil(n/2)
        solve(solver, n-i, stools, inp, aux2, output, aux1)
        tour_of_three_stools(solver, i, stools, inp, aux2, output)
        solve(solver, n-i, stools, aux1, inp, aux2, output)
    return None


def tour_of_three_stools(solver: 'SolvingController', n: int, stools: DomainStools, inp: int, aux: int, output: int) -> None:
    """
    Recursive function that determines which moves to make to solve the
    Tower of Hanoi (3 stools)
    
    n - Total number of cheeses that are not solved
    stools -  Model Anne Hoy's stools holding cheeses
    inp - input which cheese to be moved
    aux1, aux2 - middle stools used to move cheeses
    output     
    """
    if n == 1:
        solver.select(stools.select_top_cheese(inp))
        time.sleep(solver.time_delay)
        solver.select(stools.select_top_cheese(output))
    else:
        tour_of_three_stools(solver, n-1, stools, inp, output, aux)
        tour_of_three_stools(solver, 1, stools, inp, aux, output)
        tour_of_three_stools(solver, n-1, stools, aux, inp, output)
    return None

if __name__ == '__main__':
    f = SolvingController(6, 1024, 320, 20, 1)
    solve(f, f.number_of_cheeses, f.domain, 0, 1, 2, 3)
    TI.mainloop()
