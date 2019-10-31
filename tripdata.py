#!/usr/bin/env python
""" This is the class for the real time trip data """
# coding: utf-8
# final project for Introduction to Python
# Author: Ignatio "Sean" Kang
# AndrewID: ignatiok@andrew.cmu.edu
# Date: Oct 15 24 2019

class TripData:
    """ TripData """

    def __init__(self, trip_id, stop_name, stop_lat, stop_lon, route_id, headsign):
        """Stores the search results as class member"""
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.trip_id = trip_id
        self.route_id = route_id
        self.headsign = headsign

    def get_stop_name(self):
        """ get the stop name """
        return self.stop_name

    def get_stop_lat(self):
        """ get stop latitude """
        return self.stop_lat

    def get_stop_lon(self):
        """ get stop longitude """
        return self.stop_lon

    def get_trip_id(self):
        """ get the trip id """
        return self.trip_id

    def get_route_id(self):
        """ get the route id """
        return self.route_id

    def get_headsign(self):
        """ get the head sign"""
        return self.headsign
