import time

from Pages.Base_Page import Page
from selenium.webdriver.common.by import By


class SearchPage(Page):
    SELECT_FROM_YEAR= (By.CLASS_NAME, '[name="search-filters-from-years"]')

    def select_date(self, from_year):
        self.select_dropdown_by_value(*self.SELECT_FROM_YEAR, value=from_year)


