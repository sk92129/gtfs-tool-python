#!/usr/bin/env python
""" This is the class for drop down control """
# coding: utf-8
# final project for Introduction to Python
# Author: Ignatio "Sean" Kang
# AndrewID: ignatiok@andrew.cmu.edu
# Date: Oct 15 24 2019

class TripDropDownItem:
    """ TripDropDownItem """
    def __init__(self, trip_id, headsign):
        """Stores the items as class member"""
        self.trip_id = trip_id
        self.headsign = headsign

    def get_id(self):
        """ return id """
        return self.trip_id

    def get_sign(self):
        """ return the head sign"""
        return self.headsign
