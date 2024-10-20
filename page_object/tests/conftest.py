from selenium import webdriver
import pytest
from page_object.data import Data


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Data.site_url)
    yield driver
    driver.quit()