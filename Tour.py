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


def tour_of_four_stools(n: int, stools: DomainStools) -> None:
    """Move an n cheese tower from the first stool in stools to the fourth.

       n - number of cheeses on the first stool of stools
       stools - a DomainStools with a tower of cheese on the first stool
                and three other empty stools
    """
    if n > 1:
        i = 1
        tour_of_four_stools(n-i, stools)
        tour_of_three_stools(i, stools)
        


def tour_of_three_stools(n: int, stools: DomainStools) -> None:
    print("Tour of stools called")
    while stools.num_of_cheese_on_stool(2) != n+1:
        if n%2==0:
            try:
                stools.move(stools.select_top_cheese(0), stools.select_top_cheese(1))
            except:
                stools.move(stools.select_top_cheese(1), stools.select_top_cheese(0))
            try:
                stools.move(stools.select_top_cheese(0), stools.select_top_cheese(2))
            except:
                stools.move(stools.select_top_cheese(2), stools.select_top_cheese(0))
            try:
                stools.move(stools.select_top_cheese(1), stools.select_top_cheese(2))
            except:
                stools.move(stools.select_top_cheese(2), stools.select_top_cheese(1))
        else:
            try:
                stools.move(stools.select_top_cheese(0), stools.select_top_cheese(2))
            except:
                stools.move(stools.select_top_cheese(2), stools.select_top_cheese(0))
            if stools.num_of_cheese_on_stool(2) == n+1:
                break
            try:
                stools.move(stools.select_top_cheese(0), stools.select_top_cheese(1))
            except:
                stools.move(stools.select_top_cheese(1), stools.select_top_cheese(0))
            try:
                stools.move(stools.select_top_cheese(2), stools.select_top_cheese(1))
            except:
                stools.move(stools.select_top_cheese(1), stools.select_top_cheese(2))
    print("tower of hanoi completed.")
    print("Stool 1, number of cheeses: " + str(stools.num_of_cheese_on_stool(0)))
    print("Stool 2, number of cheeses: " + str(stools.num_of_cheese_on_stool(1)))
    print("Stool 3, number of cheeses: " + str(stools.num_of_cheese_on_stool(2)))


if __name__ == '__main__':
    #four_stools = DomainStools(4)
    #for s in range(5, 0, -1):
    #    four_stools.add(0, Cheese(s))
    #tour_of_four_stools(5, four_stools)
    #print(four_stools.number_of_moves())

    three_stools = DomainStools(3)
    for s in range(15, 0, -1):
        three_stools.add(0, Cheese(s))
    tour_of_three_stools(15, three_stools)
    print(three_stools.number_of_moves())

