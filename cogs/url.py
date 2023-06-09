# python3

import requests
from bs4 import BeautifulSoup

parser = "lxml" #"html.parser"

def get_html(url):
    res = requests.get(url)
    return res


def check_updates(befor, after):
    if befor == after:
        return False

    else:
        return True


def print_res(url):
    res = requests.get(url)
    print(res)


def get_element_by_class(url, cl):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, parser)
    elements = soup.find(class_ = cl)
    return elements


def get_elements_by_class(url, cl):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, parser)
    elements = soup.find_all(class_ = cl)
    return elements


def get_elements_by_tag(url, tag):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, parser)
    elements = soup.find_all(tag)
    return elements


def soup(res):
    soup = BeautifulSoup(res.text, parser)
    return soup