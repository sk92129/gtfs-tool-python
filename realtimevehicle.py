#!/usr/bin/env python
""" This is the class for handling real time data """
# coding: utf-8
# final project for Introduction to Python
# Author: Ignatio "Sean" Kang
# AndrewID: ignatiok@andrew.cmu.edu
# Date: Oct 15 24 2019

import urllib
import urllib.request
from google.transit import gtfs_realtime_pb2


class RealTimeVehicle:
    """  Main class for handling real time vehicles in the system """


    def __init__(self):
        """Stores the  as class member"""
        self.my_url = "https://cdn.mbta.com/realtime/VehiclePositions.pb"

    def get_all_entities(self, routeid):
        """ Return all the vehicle entities"""
        my_data = []
        feed = gtfs_realtime_pb2.FeedMessage()
        with urllib.request.urlopen(self.my_url) as url_gtfs:
            stream_data = url_gtfs.read()
            #print(s)
            feed.ParseFromString(stream_data)
            for entity in feed.entity:
                if entity.HasField('vehicle'): #and entity.vehicle.trip.routeid == routeid:
                    vehicle = entity.vehicle
                    if vehicle.HasField('trip'):
                        trip = vehicle.trip
                        if trip.HasField('route_id'):
                            if routeid == trip.route_id:
                                my_data.append(entity)
        return my_data

    def get_all_routes(self):
        """ return all the routes """
        my_data = []
        feed = gtfs_realtime_pb2.FeedMessage()
        with urllib.request.urlopen(self.my_url) as url_gtfs:
            stream_data = url_gtfs.read()
            feed.ParseFromString(stream_data)
            #print(feed.entity)
            for entity in feed.entity:
                if entity.HasField('vehicle'):
                    vehicle = entity.vehicle
                    if vehicle.HasField('trip'):
                        trip = vehicle.trip
                        if trip.HasField('route_id'):
                            my_data.append(entity)
        return my_data


    def print_vehicle_by_route(self, route_id):
        """ print all the vehicle by the route id """
        entity_for_route = self.get_all_entities(route_id)
        for entity in entity_for_route:
            print(entity)

    def display_all_routes_names(self):
        """ print all the running vehicles """
        route_entities = self.get_all_routes()
        for entity in route_entities:
            print(entity)
