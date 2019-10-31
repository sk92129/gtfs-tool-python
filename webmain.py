#!/usr/bin/env python
""" This is the main web controller or entry points """
# coding: utf-8
#
# final project for Introduction to Python
# Author: Ignatio "Sean" Kang
# AndrewID: ignatiok@andrew.cmu.edu
# Date: Oct 15 24 2019

from flask import Flask, render_template, request
from routes import Routes
from realtimevehicle import RealTimeVehicle
from tripdropdownitem import TripDropDownItem

import os

WEBAPP = Flask(__name__)

ROUTES = Routes()


def read_all_static_files():
    cwd = os.getcwd()
    print(cwd)
    """ Read all the static GTFS files """
    if not ROUTES.is_read():
        print("reading set up data.")
        ROUTES.read(cwd)
        print("finished reading set up data")
    else:
        print("already read the static files")




@WEBAPP.route("/")
def web_start():
    """ The entry point for the main web site """
    return render_template("index.html", message="Hello MBTA User!")


@WEBAPP.route("/allroutes")
def all_routes():
    """ entry point to display all the routes"""
    all_route_data = ROUTES.get_all()
    return render_template("allroutes.html", message="", all_routes=all_route_data)


@WEBAPP.route("/map")
def show_map():
    """ entry point to display all running vehicles on map"""
    real_time = RealTimeVehicle()
    all_cars = real_time.get_all_routes()
    return render_template("map.html", message="", all_vehicles=all_cars)


@WEBAPP.route("/tripform")
def trip_form():
    """ entry point to display a form. """
    trip_id_list = []
    trip_id_list.append(TripDropDownItem("41894177", "Harvard"))
    trip_id_list.append(TripDropDownItem("42011779", "Ruggles"))

    return render_template("tripform.html", message="", all_trips=trip_id_list)


@WEBAPP.route("/findtrip", methods=['POST'])
def find_trip():
    """ entry point for the form action """
    try:
        request_trip_id = request.form['tripid']
        search_response = ROUTES.find_trip_data(request_trip_id)
        return render_template("tripsearch.html", message="", trip_data=search_response)
    except Exception as ex:
        print(ex)

@WEBAPP.route("/gettrip", methods=['GET'])
def get_trip():
    """ entry point for GET on the trip """
    try:
        request_trip_id = request.args.get('tripid')
        search_response = ROUTES.find_trip_data(request_trip_id)
        return render_template("tripsearch.html", message="", trip_data=search_response)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    read_all_static_files()
    WEBAPP.run()

# when this is run from the FLASK script, the __name__ is not main
read_all_static_files()
