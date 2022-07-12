from datetime import timedelta
import os
import pytest
from os.path import exists
from swapi.swapi import BasicApi, Planet, get_page_json, create_planets, list_from_string

GET_URL = 'https://httpbin.org/get'
CACHE_EXPIRY_DAYS = 1
CONTENT_LABEL = 'content'
NEXT_URL_LABEL = 'next'

mock_planet_dict = {
    'name': 'testname',
    'rotation_period': '12',
    'orbital_period': '50',
    'climate': 'arid, dry',
    'terrain': 'grasslands, mountains',
    'surface_water': '60',
    'population': '10000',
    'gravity': '1 standard',
}


@pytest.fixture()
def test_api():
    api = BasicApi('TEST')
    api.url = GET_URL
    return api


@pytest.fixture()
def test_planet():
    return Planet(mock_planet_dict)


def test_get_page_from_json():
    response = get_page_json(GET_URL)
    assert response['url'] == GET_URL


def test_create_planets_from_data():
    mock_data = [mock_planet_dict, mock_planet_dict, mock_planet_dict]
    planet_list = create_planets(mock_data)
    assert len(planet_list) == 3
    assert all(isinstance(planet, Planet) for planet in planet_list)


def test_split_string_method(test_planet):
    assert list_from_string(test_planet.climate) == ['arid', 'dry']
    assert list_from_string(test_planet.name) == ['testname']


def test_api_attributes(test_api):
    assert test_api.api == 'TEST'
    assert test_api.url == GET_URL


# TODO: how to test test_api.get_all_pages()?

def test_planet_int_method(test_planet):
    assert test_planet.int_from_key('rotation_period') == 12
    assert test_planet.int_from_key('name') is None


def test_planet_attributes(test_planet):
    assert test_planet.name == 'testname'
    assert test_planet.day_length == 12
    assert test_planet.year_length == 50
    assert test_planet.climate == 'arid, dry'
    assert test_planet.terrain == 'grasslands, mountains'
    assert test_planet.surface_water == 60
    assert test_planet.population == 10000
    assert test_planet.gravity == '1 standard'
