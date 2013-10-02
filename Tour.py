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
from DomainStools import DomainStools
from DomainStools import Cheese
import math


def tour_of_four_stools(n: int, stools: DomainStools) -> None:
    """Move an n cheese tower from the first stool in stools to the fourth.

       n - number of cheeses on the first stool of stools
       stools - a DomainStools with a tower of cheese on the first stool
                and three other empty stools
    """
    tour_helper(n, stools, 0, 1, 2, 3)


def tour_helper(n: int, stools: DomainStools, input: int, aux1: int, aux2: int, output: int) -> None:
    if n == 1:
        stools.move(stools.select_top_cheese(input), stools.select_top_cheese(output))
    else:
        i = math.ceil(n/2)
        tour_helper(n-i, stools, input, aux2, output, aux1)
        tour_of_three_stools(i, stools, input, aux2, output)
        tour_helper(n-i, stools, aux1, input, aux2, output)


def tour_of_three_stools(n: int, stools: DomainStools, input: int, aux: int, output: int) -> None:
    if n == 1:
        stools.move(stools.select_top_cheese(input), stools.select_top_cheese(output))
    else:
        tour_of_three_stools(n-1, stools, input, output, aux)
        tour_of_three_stools(1, stools, input, aux, output)
        tour_of_three_stools(n-1, stools, aux, input, output)

if __name__ == '__main__':
    four_stools = DomainStools(4)
    for s in range(7, 0, -1):
        four_stools.add(0, Cheese(s))
    tour_of_four_stools(7, four_stools)
    print(four_stools.number_of_moves())

    #three_stools = DomainStools(3)
    #for s in range(15, 0, -1):
    #    three_stools.add(0, Cheese(s))
    #tour_of_three_stools(15, three_stools, 0, 1, 2)
    #print(three_stools.number_of_moves())

