#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
from selenium.webdriver import FirefoxOptions
import requests
import sys
import os
import time
from threading import Thread
from queue import Queue
import argparse
import binascii
import json


import subprocess
import datetime

import shutil


opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts, executable_path=r'/e/geckodriver/geckodriver.exe')
driver.get('https://www.facebook.com/khema.thiri.7/posts/734912143563512')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.find('div', attrs={'class': '_5pbx userContent _3576'}))