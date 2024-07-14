import numpy as np
import pandas as pd
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = WD.Chrome()
driver.get('https://freesearchigrservice.maharashtra.gov.in/')
elem = driver.find_element(By.NAME, "ddlFromYear")

elem.clear()

elem.send_keys(Keys.RETURN)

