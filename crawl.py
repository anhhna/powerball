import os
import time
import pandas as pd
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Setup browser
driver = webdriver.Edge()

# Crawl
start_date = datetime(2021, 6, 12)

all_results = []

date_str = start_date.strftime("%Y-%m-%d")
last_date = date_str
url = f"https://www.powerball.com/draw-result?gc=powerball&date={date_str}"

while True:
    driver.get(url)
    time.sleep(1)  # Let page load a little bit

    draw_date = driver.find_element(By.ID, "DrawDate")
    date_str = draw_date.get_attribute("value")

    # convert to datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    last_date_obj = datetime.strptime(last_date, "%Y-%m-%d")
    if date_obj - last_date_obj > pd.Timedelta(days=7):
        continue

    try:
        # white balls
        white_balls = driver.find_elements(By.CLASS_NAME, "form-control.col.white-balls.item-powerball")
        if not white_balls:
            print(f"No draw found on {date_str}")
            continue  # No results, skip

        numbers = [ball.text for ball in white_balls]

        # power ball
        power_ball = driver.find_element(By.CLASS_NAME, "form-control.col.powerball.item-powerball")
        if not power_ball:
            print(f"No draw found on {date_str}")
            continue  # No results, skip

        numbers = [ball.text for ball in white_balls]
        numbers.append(power_ball.text)

        # powerball
        powerball_winners = 0
        powerball_winners_element = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[2]/div/div/div/table/tbody/tr[1]/td[2]")
        if powerball_winners_element:
            powerball_winners = powerball_winners_element.text

        powerball_price = ''
        powerball_price_element = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/span[2]")
        if powerball_price_element:
            powerball_price = powerball_price_element.text

        powerball_state = ''
        powerball_state_element = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[1]/div[2]/div/div/div[1]/span[3]")
        if powerball_state_element:
            powerball_state = powerball_state_element.text

        all_results.append({
            "date": date_str,
            "numbers": numbers,
            "powerball_winners": powerball_winners,
            "powerball_price": powerball_price,
            "powerball_state": powerball_state
        })
        print(f"{date_str},{numbers},{powerball_winners},{powerball_price},{powerball_state}")

    except NoSuchElementException:
        print(f"No results for {date_str}")
        continue

    card_next = driver.find_elements(By.CLASS_NAME, 'card-next')
    if not card_next:
        break

    url = card_next[0].get_attribute("href")

    last_date = date_str

df = pd.DataFrame(all_results)

file_path = 'powerball.csv'

if not os.path.exists(file_path):
    df.to_csv(file_path, index=False)
else:
    df.to_csv(file_path, mode='a', index=False, header=False)

driver.quit()
