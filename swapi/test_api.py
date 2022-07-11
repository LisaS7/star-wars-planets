from datetime import timedelta
import os
import pytest
from os.path import exists
from swapi import BasicApi, Planet, get_page_json, create_planets, set_timedelta

CACHE = 'test_cache.sqlite'
GET_URL = 'https://httpbin.org/get'

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


@pytest.fixture(autouse=True, scope='session')
def test_suite_cleanup():
    # insert setup code here if required
    yield
    os.remove(CACHE)


@pytest.fixture()
def test_api():
    return BasicApi('TEST')


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


def test_set_timedelta():
    assert set_timedelta(None, 'hours') is None
    assert set_timedelta(12, 'days') == timedelta(days=12)
    assert set_timedelta(20, 'hours') == timedelta(hours=20)


@pytest.mark.xfail(raises=TypeError)
def test_fail_timedelta():
    set_timedelta('12', 'days')


def test_api_attributes(test_api):
    assert test_api.api == 'TEST'
    assert test_api.url == GET_URL


def test_cache(test_api):
    get_page_json(test_api.url)
    assert exists(CACHE)


# TODO: how to test test_api.get_all_pages()?

def test_planet_int_method(test_planet):
    assert test_planet.int_from_key('rotation_period') == 12
    assert test_planet.int_from_key('name') is None


def test_planet_split_string_method(test_planet):
    assert test_planet.list_from_string('climate') == ['arid', 'dry']
    assert test_planet.list_from_string('name') == ['testname']


def test_planet_attributes(test_planet):
    assert test_planet.name == 'testname'
    assert test_planet.day_length == timedelta(hours=12)
    assert test_planet.year_length == timedelta(days=50)
    assert test_planet.climate == ['arid', 'dry']
    assert test_planet.terrain == ['grasslands', 'mountains']
    assert test_planet.surface_water == 60
    assert test_planet.population == 10000
    assert test_planet.gravity == '1 standard'
