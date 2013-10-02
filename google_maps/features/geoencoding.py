__author__ = 'arobres'

import json

import requests
from lettuce import *
from lettuce import step
from commons import Commons

GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json?'


@before.each_scenario
def setUp(scenario):

    world.utils = Commons()

@step('Given a (.*) name')
def city_name(step, city):
    world.city = city


@step('I request the geoencoding of the city')
def geocode(step):
    payload = {'address':world.city ,'sensor': 'false'}
    world.r = requests.get(GEOCODE_BASE_URL, params=payload)
    assert world.r.ok
    world.result = json.loads(world.r.content)


@step('When I request the geoencoding without (.*) or (.*)')
def geocode(step,sensor, city):
    if sensor == 'null':
        payload = {'address':world.city}
    elif city == 'null':
        payload = {'sensor': sensor}
    else:
        payload = payload = {'address':world.city,'sensor': sensor}

    world.r = requests.get(GEOCODE_BASE_URL, params=payload)



@step('I obtain the (.*) name with the (.*)')
def assert_country_code(step, city, country_code):

    assert world.r.ok
    world.address_components = world.result['results'][0]['address_components']
    assert world.address_components[len(world.address_components)-1]['short_name'] == country_code, \
        "Error: Expected value is: " + country_code + " and the obtanined value is: " +  \
        world.address_components[len(world.address_components)-1]['short_name']


@step('I obtain a response with status "(.*)"')
def assert_zero_results(step, message):
    assert world.r.ok
    assert world.result['status'] == message


@step('I obtain an (.*)')
def assert_error(step, error_code):
    world.r.status_code == error_code