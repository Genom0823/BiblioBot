# python3

import requests
from bs4 import BeautifulSoup


def check_updates(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")


def print_res(url):
    res = requests.get(url)
    print(res)


def get_elements_by_class(url, cl):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elements = soup.find_all(class_ = cl)
    return elements


def get_elements_by_tag(url, tag):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elements = soup.find_all(tag)
    return elements