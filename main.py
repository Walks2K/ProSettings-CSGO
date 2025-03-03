"""
Extract and parse table from https://prosettings.net/cs-go-pro-settings-gear-list/ with selenium

Print table
"""

import os
import time
from numpy import dtype

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def get_table(url):
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

    return table


def get_table_data(table):
    """
    Get table data
    """
    table_data = []
    for row in table.find_all("tr"):
        table_data.append([])
        for cell in row.find_all("td"):
            table_data[-1].append(cell.text)

    table_data = [row for row in table_data if row != []]
    return table_data


def get_table_columns(table):
    """
    Get table columns
    """
    table_columns = []
    for row in table.find_all("tr"):
        table_columns.append([])
        for cell in row.find_all("th"):
            table_columns[-1].append(cell.text)

    table_columns = [row for row in table_columns if row != []]
    return table_columns


def print_table(table_data):
    """
    Print table
    """
    for row in table_data:
        print(row)


def main():
    """
    Main function
    """
    url = "https://prosettings.net/cs-go-pro-settings-gear-list/"
    table = get_table(url)
    table_data = get_table_data(table)
    table_columns = get_table_columns(table)

    # Combine table data and columns into one dataframe
    dataframe = pd.DataFrame(table_data, columns=table_columns)

    print(dataframe.describe())
    print(dataframe.dtypes)
    print(dataframe.head())


if __name__ == "__main__":
    main()
