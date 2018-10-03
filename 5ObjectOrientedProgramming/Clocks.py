# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:08:15 2017

@author: Batuhan Akar
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
        # time != self.time (aka Clock.time)

clock = Clock('5:30')
# time = 5:30
# self.time = 5:30
clock.print_time()
# time = 6:30 BUT
# self.time = 5:30 BECAUSE TIME HAS NOT BEEN ASSIGNED TO THE INSTANCE.
# EVEN IF time = 6:30 IT DOES NOT MATTER.


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)

clock = Clock('5:30')
# time = 5:30
# self.time = 5:30
clock.print_time('10:30')
# time = 10:30 (NEW ASSIGNMENT)
# self.time is not referenced


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
# time = 5:30
# self.time = 5.30
paris_clock = boston_clock
# BEWARE!!! PARIS IS A REFERENCE TO BOSTON
# paris_clock and boston_clock IS THE SAME OBJECT
paris_clock.time = '10:30'
# paris-->boston: self.time = 10:30
boston_clock.print_time()
