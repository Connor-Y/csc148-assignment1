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
ManualController: GUI window for manually solving Anne Hoy's problems.
"""

from DomainStools import DomainStools
from CheeseView import CheeseView
import tkinter as TI
import time


class ManualController:
    def __init__(self: 'ManualController',
                 number_of_cheeses: int, number_of_stools: int,
                 content_width: float, content_height: float,
                 cheese_scale: float):
        """
        Initialize a new ManualController.

        number_of_cheeses - number of cheese to tower on the first stool,
                            not counting the bottom cheese acting as stool
        number_of_stools - number of stools, to be shown as large cheeses
        content_width - width in pixels of the working area
        content_height - height in pixels of the working area
        cheese_scale - height in pixels for showing cheese thicknesses,
                       and to scale cheese diameters
        """

        self.domain = DomainStools(number_of_stools)

        self.cheese_to_move = None
        self.blinking = False

        self.cheese_scale = cheese_scale

        self.root = TI.Tk()
        canvas = TI.Canvas(self.root,
                           background="blue",
                           width=content_width, height=content_height)
        canvas.pack(expand=True, fill=TI.BOTH)

        self.moves_label = TI.Label(self.root)
        self.show_number_of_moves()
        self.moves_label.pack()

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

    def show_number_of_moves(self: 'ManualController'):
        """Show the number of moves so far."""

        self.moves_label.config(text='Number of moves: ' +
                                str(self.domain.number_of_moves()))

    def clicked(self: 'ManualController', cheese: CheeseView):
        """React to cheese being clicked: if not in the middle of blinking
           then select cheese for moving, or for moving onto.

           cheese - clicked cheese
        """
        if not self.blinking:
            self.select(cheese)

    def select(self: 'ManualController', cheese: CheeseView):
        """If no cheese is selected to move, select cheese and highlight it.
           Otherwise try moving the currently selected cheese onto cheese:
           if that's not a valid move, blink the currently selected cheese.

           cheese - cheese to select for moving, or to try moving onto.
        """

        if self.cheese_to_move is None:
            self.cheese_to_move = cheese
            self.cheese_to_move.highlight(True)
        else:
            if cheese is not self.cheese_to_move:
                try:
                    self.domain.move(self.cheese_to_move, cheese)
                    self.cheese_to_move.place(cheese.x_center,
                                              cheese.y_center
                                              - self.cheese_scale)
                    self.show_number_of_moves()
                except:
                    self.blinking = True
                    for i in range(10):
                        self.cheese_to_move.highlight(i % 2 != 0)
                        self.root.update()
                        time.sleep(0.1)
                    self.blinking = False
            self.cheese_to_move.highlight(False)
            self.cheese_to_move = None

if __name__ == '__main__':
    ManualController(5, 4, 1024, 320, 20)
    TI.mainloop()
