import pytest
from os.path import exists
from swapi import BasicApi, Planet, get_page_json


@pytest.fixture()
def test_api():
    return BasicApi('TEST')

@pytest.fixture()
def test_planet():
    mock_planet_dict = {
        'name': 'testname'
    }
    return Planet(mock_planet_dict)


def test_api_attributes(test_api):
    assert test_api.api == 'TEST'
    assert test_api.url == 'https://httpbin.org/get'


def test_cache(test_api):
    get_page_json(test_api.url)
    assert exists('test_cache.sqlite')

# TODO: how to test test_api.get_all_pages()?

def test_planet():
    planet = Planet()
