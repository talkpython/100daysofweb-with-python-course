import os
import re
from time import sleep

import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

load_dotenv()

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

HOME = 'https://pybitesbooks.com'
FIRST_BOOK = f'{HOME}/books/nHDtDAAAQBAJ'
SECOND_BOOK = f'{HOME}/books/NWqePwAACAAJ'
MY_BOOKS = 'My Books'

# https://pybit.es/pytest-fixtures.html


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    # teardown code
    driver.quit()


@pytest.fixture
def driver_home(driver):
    driver.get(HOME)
    yield driver


@pytest.fixture
def driver_first_book(driver):
    driver.get(FIRST_BOOK)
    yield driver


@pytest.fixture
def driver_login(driver):
    driver.get(HOME)
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_name('username').send_keys(USERNAME)
    driver.find_element_by_name('password').send_keys(PASSWORD + Keys.RETURN)
    yield driver


def test_homepage_title(driver_home):
    pass


def test_number_of_thumbs_homepage(driver_home):
    pass


def test_has_login_link(driver_home):
    pass


def _get_number_books_read(driver):
    pass


def test_book_page_title(driver_first_book):
    pass


def test_book_page_meta_data(driver_first_book):
    pass


def test_book_page_has_add_book_link(driver_first_book):
    pass


def test_search_box_auto_direct(driver_first_book):
    pass


def test_login_to_site(driver_login):
    pass


def test_add_delete_book(driver_login):
    pass


def test_logout(driver_login):
    pass
