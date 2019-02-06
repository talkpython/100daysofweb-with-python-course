import os
import re
from time import sleep

import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

HOME = 'https://pbreadinglist.herokuapp.com'
FIRST_BOOK = f'{HOME}/books/nHDtDAAAQBAJ'
SECOND_BOOK = f'{HOME}/books/NWqePwAACAAJ'
MY_BOOKS = 'My Books'

# https://pybit.es/pytest-fixtures.html


@pytest.fixture
def driver_home():
    driver = webdriver.Chrome()
    driver.get(HOME)
    # pytest's way of tearDown
    yield driver
    driver.quit()


@pytest.fixture
def driver_first_book():
    driver = webdriver.Chrome()
    driver.get(FIRST_BOOK)
    yield driver
    driver.quit()


@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()

    driver.get(HOME)
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_name('username').send_keys(USERNAME)
    driver.find_element_by_name('password').send_keys(PASSWORD + Keys.RETURN)

    yield driver
    driver.quit()


def test_homepage_title(driver_home):
    expected = "PyBites My Reading List | Because We Love Books"
    assert driver_home.title == expected


def test_number_of_thumbs_homepage(driver_home):
    images = driver_home.find_elements_by_tag_name('img')
    assert len(images) == 100


def test_has_login_link(driver_home):
    try:
        driver_home.find_element_by_link_text('Login')
    except NoSuchElementException:
        pytest.fail('Should have a link called Login')


def test_book_page_title(driver_first_book):
    expected = ("PyBites My Reading List | The Hitchhiker's "
                "Guide to Python")
    assert driver_first_book.title == expected


def test_book_page_meta_data(driver_first_book):
    src = driver_first_book.page_source
    assert "Kenneth Reitz, Tanya Schlusser" in src
    assert "O'Reilly Media, Inc." in src
    assert "338" in src


def test_book_page_has_add_book_link(driver_first_book):
    try:
        driver_first_book.find_element_by_link_text('Add Book')
    except NoSuchElementException:
        pytest.fail('Should have a link called Login')


def test_search_box_auto_direct(driver_first_book):
    text_to_enter = 'Fluent Python'
    searchBox = driver_first_book.find_element_by_name('searchTitles')
    searchBox.send_keys(text_to_enter)
    sleep(2)  # wait for auto-complete (Google books API)
    driver_first_book.find_elements_by_class_name('ac_even')[0].click()

    assert driver_first_book.current_url.endswith('bIZHCgAAQBAJ')
    expected = "PyBites My Reading List | Fluent Python"
    assert driver_first_book.title == expected


def test_login_to_site(driver_login):
    try:
        driver_login.find_element_by_link_text('Logout')
        driver_login.find_element_by_link_text(MY_BOOKS)
        driver_login.find_element_by_link_text('5-Hour Challenge')
    except NoSuchElementException:
        pytest.fail('Missing private links in navbar')

    try:
        driver_login.find_element_by_link_text('Login')
        pytest.fail('Should not have a link called Login when logged in')
    except NoSuchElementException:
        pass


def _get_number_books_read(driver):
    driver.find_element_by_link_text(MY_BOOKS).click()
    stats = driver.find_element_by_class_name('mui--text-subhead')
    return int(re.sub(r'Status: (\d+) books.*', r'\1', stats.text))


def test_add_delete_book(driver_login):
    num_books_read_start = _get_number_books_read(driver_login)

    # adding a book should increase the book counter by 1
    driver_login.get(SECOND_BOOK)
    driver_login.find_element_by_name('bookSubmit').click()
    num_books_after_add = _get_number_books_read(driver_login)
    assert num_books_after_add == num_books_read_start + 1

    # deleting the book should bring the counter back to the initial count
    driver_login.get(SECOND_BOOK)
    driver_login.find_element_by_name('deleteBook').click()
    num_books_after_delete = _get_number_books_read(driver_login)
    assert num_books_after_delete == num_books_read_start


def test_logout(driver_login):
    driver_login.find_element_by_link_text('Logout').click()

    src = driver_login.page_source
    assert "Logged out" in src

    # logged out links
    try:
        driver_login.find_element_by_link_text('Login')
    except NoSuchElementException:
        pytest.fail('Should see Login link in navbar when logged out')

    try:
        driver_login.find_element_by_link_text('Logout')
        driver_login.find_element_by_link_text(MY_BOOKS)
        driver_login.find_element_by_link_text('5-Hour Challenge')
        pytest.fail('Should not show private links when logged out')
    except NoSuchElementException:
        pass
