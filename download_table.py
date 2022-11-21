"""
Downloads the table of data from https://prosettings.net/cs-go-pro-settings-gear-list/
"""
import os
import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver


def get_table(url="https://prosettings.net/cs-go-pro-settings-gear-list/"):
    """
    Get table from url
    """
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
    driver.implicitly_wait(5)
    driver.get(url)
    driver.maximize_window()

    time.sleep(5)

    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    # Save table to file
    with open("table.html", "w", encoding="utf-8") as file:
        file.write(str(table))

    dataframe = pd.read_html(table.prettify())[0]
    dataframe = dataframe.dropna(how="all")

    return dataframe


if __name__ == "__main__":
    get_table()
