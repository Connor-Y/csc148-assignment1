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
CheeseView: A visible Cheese.

CheeseView objects are Cheese objects with a visible representation.

Each instance receives a Canvas instance. The Canvas class is a class in the
tkinter framework. The class is used for a place in a window to draw shapes.

CheeseView objects draw themselves as rectangles on the canvas, to represent
side views of rounds of cheese with particular sizes. They can be moved and
highlighted.

CheeseView objects also receive a function to call to report back to a
controller object that the their rectangle was clicked on.
"""

from DomainStools import Cheese
from tkinter import Canvas
from tkinter import Event


class CheeseView(Cheese):
    def __init__(self: 'CheeseView',
                 size: float,
                 click_handler: (lambda Event: None),
                 canvas: Canvas,
                 thickness: float,
                 x_center: float, y_center: float) -> None:
        """
        Initialize a new CheeseView.

        size - horizontal extent of this cheese
        click_handler - function to react to mouse clicks
        canvas - space to draw a representation of this cheese
        thickness - vertical extent of this cheese
        x_center - center of this cheese horizontally
        y_center - center of this cheese vertically
        """

        # Call the superclass constructor appropriately.
        super().__init__(size)

        # Store canvas, thickness, x_center and y_center in instance variables.
        self.canvas = canvas
        self.thickness = thickness
        self.x_center = x_center
        self.y_center = y_center

        self.coordinates = (0, 0, 0, 0)

        # Create a rectangle on the canvas, and record the index that tkinter
        # uses to refer to it.
        self.index = canvas.create_rectangle(0, 0, 0, 0)

        # Initial placement.
        self.place(x_center, y_center)

        # Initially unhighlighted.
        self.highlight(False)

        # Tell the canvas to report when the rectangle is clicked.
        # The report is a call to click_handler, passing it this CheeseView
        # instance so the controller knows which one was clicked.
        self.canvas.tag_bind(self.index,
                             '<ButtonRelease>',
                             lambda _: click_handler(self))

    def highlight(self: 'CheeseView', highlighting: bool) -> None:
        """
        Set this CheeseView's colour to highlighted or not.

        highlighting - whether to highlight
        """

        self.canvas.itemconfigure(self.index,
                                  fill=('red' if highlighting else 'orange'))

    def place(self: 'CheeseView', x_center: float, y_center: float) -> None:
        """
        Used to place "cheese" blocks onto the canvas.
        
        x_center - center of cheese horizontally
        y_center - center of cheese vertically
        """
        # Store x_center and y_center in instance variables.
        self.x_center = x_center
        self.y_center = y_center
        
        # Set the coordinates of the cheese to be placed as an
        # instance variable.
        self.coordinates = (self.x_center - self.size/2, self.y_center
                            + self.thickness/2, self.x_center +
                            self.size/2, self.y_center -
                            self.thickness/2)

        # Positions the "cheese" block onto the canvas.
        self.canvas.coords(self.index, self.coordinates)
