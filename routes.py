#!/usr/bin/env python
""" This is the class for handling all static files """
# coding: utf-8
#
# final project for Introduction to Python
# Author: Ignatio "Sean" Kang
# AndrewID: ignatiok@andrew.cmu.edu
# Date: Oct 15 24 2019

import csv
from tripdata import TripData
from tripdropdownitem import TripDropDownItem

class Routes:
    """ Route """
    def __init__(self):
        """Stores the base path as class member"""
        self.all_routes = []
        self.all_known_route_id = set()
        self.finished = False
        self.all_stoptimes = {}
        self.all_stops = {}
        self.all_trips = {}
        self.trip_drop_down_list = []

    def read(self, base_path):
        """Stores the base path as class member"""
        with open(base_path + "/GTFS-files/routes.txt", "r") as csv_routes_file_hanlder:
            route_reader = csv.reader(csv_routes_file_hanlder, delimiter=",")
            next(route_reader)
            for row in route_reader:
                self.all_routes.append(row)
                self.all_known_route_id.add(row[0])

        with open(base_path + "/GTFS-files/stop_times.txt", "r") as csv_stoptimes_file_hanlder:
            stoptime_reader = csv.reader(csv_stoptimes_file_hanlder, delimiter=",")
            next(stoptime_reader)
            for row in stoptime_reader:
                trip_id = row[0]
                if trip_id in self.all_stoptimes:
                    # already exists
                    my_list = self.all_stoptimes[trip_id]
                    my_list.append(row)
                else:
                    my_list = []
                    my_list.append(row)
                    self.all_stoptimes[trip_id] = my_list

        with open(base_path + "/GTFS-files/stops.txt", "r") as csv_stops_file_hanlder:
            stops_reader = csv.reader(csv_stops_file_hanlder, delimiter=",")
            next(stops_reader)
            for row in stops_reader:
                stop_id = row[0]
                if stop_id in self.all_stops:
                    # already exists
                    print("THIS SHOULD NOT HAPPEN")
                else:
                    self.all_stops[stop_id] = row


        with open(base_path + "/GTFS-files/trips.txt", "r") as trips_file_hanlder:
            trips_reader = csv.reader(trips_file_hanlder, delimiter=",")
            next(trips_reader)
            for row in trips_reader:
                trip_id = row[2]
                if trip_id in self.all_trips:
                    # already exists
                    print("THIS SHOULD NOT HAPPEN")
                else:
                    self.all_trips[trip_id] = row
                    self.trip_drop_down_list.append(TripDropDownItem(trip_id, row[3]))


        self.finished = True

    def is_read(self):
        """ Returns True if all the static files were read successfully """
        return self.finished

    def get_all_trip_id(self):
        """ Return all the trip defined into dropdown item format."""
        return self.trip_drop_down_list

    def display_id(self):
        """ Prints all the routes of their ID """
        for route in self.all_routes:
            print("routeId: "+route[0])

    def display_all(self):
        """ print all the route """
        for route in self.all_routes:
            print("routeId: "+route)

    def route_exists(self, route_id):
        """ Return True when the route ID exists in the static data files."""
        return route_id in self.all_known_route_id


    def print_route_data_from_route_tables(self, route_id):
        """ Print the route data specified by the route ID """
        for route in self.all_routes:
            if route[0] == route_id:
                print(route)

    def print_route_data(self, route_id):
        """ Print the route data specified by the route ID """
        self.print_route_data_from_route_tables(route_id)
        print("Printing data about route")

    def get_all(self):
        """ Return all the route data """
        return self.all_routes

    def find_trip_data(self, trip_id):
        """ Return  trip data from the trip id """
        try:
            my_list = self.all_stoptimes[trip_id]
            stoptime_record = my_list[0] # just get the first one for now
            stop_id = stoptime_record[3]
            stop_record = self.all_stops[stop_id]
            stop_name = stop_record[2]
            stop_lat = stop_record[6]
            stop_lon = stop_record[7]
            trip_record = self.all_trips[trip_id]
            route_id = trip_record[0]
            headsign = trip_record[3]

            trip_data = TripData(trip_id, stop_name, stop_lat, stop_lon, route_id, headsign)

            return trip_data
        except KeyError:
            trip_data2 = TripData("", "Missing", "", "", "Missing", "Missing")
            return trip_data2
