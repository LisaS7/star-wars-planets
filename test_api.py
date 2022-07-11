from datetime import timedelta
import os
import pytest
from os.path import exists
from swapi import BasicApi, Planet, get_page_json

CACHE = 'test_cache.sqlite'
GET_URL = 'https://httpbin.org/get'


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
    mock_planet_dict = {
        'name': 'testname',
        'rotation_period': '12',
        'orbital_period': '50',
    }
    return Planet(mock_planet_dict)


def test_get_page_from_json():
    response = get_page_json(GET_URL)
    assert response['url'] == GET_URL


def test_api_attributes(test_api):
    assert test_api.api == 'TEST'
    assert test_api.url == GET_URL


def test_cache(test_api):
    get_page_json(test_api.url)
    assert exists(CACHE)


# TODO: how to test test_api.get_all_pages()?


def test_planet_attributes(test_planet):
    assert test_planet.name == 'testname'
    assert test_planet.day_length == timedelta(hours=12)
    assert test_planet.year_length == timedelta(days=50)
