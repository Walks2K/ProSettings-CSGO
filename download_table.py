"""
Downloads the table of data from https://prosettings.net/cs-go-pro-settings-gear-list/
"""

import os
import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_table(url="https://prosettings.net/cs-go-pro-settings-gear-list/"):
    """
    Get table from url
    """
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # Initialize WebDriver
    driver = webdriver.Chrome(
        executable_path=os.path.abspath("chromedriver"), options=chrome_options
    )
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
