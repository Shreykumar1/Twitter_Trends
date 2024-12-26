from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from datetime import datetime
import time
import random
import requests
from src.config import Config

def get_proxy():
    # Create a dictionary of proxy settings
    proxy_settings = {
        "http": f"http://{Config.PROXYMESH_USERNAME}:{Config.PROXYMESH_PASSWORD}@us-ca.proxymesh.com:31280",
        "https": f"http://{Config.PROXYMESH_USERNAME}:{Config.PROXYMESH_PASSWORD}@us-ca.proxymesh.com:31280",
    }
    return proxy_settings

def test_proxy(proxies):
    try:
        # Test the proxy by fetching the public IP
        response = requests.get('https://api.ipify.org?format=json', proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.json().get("ip", "Unknown IP")
    except requests.RequestException as error:
        print(f"Proxy test failed: {error}")
        return None

def fetch_trending_topics():
    # Initialize the Edge WebDriver
    driver = webdriver.Edge()

    driver.get('https://twitter.com/login')
    try:
        _  = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
    except:
        print("Timeout: Page did not load in time.")
        driver.quit()

    # Log in to Twitter
    username_field = driver.find_element(By.NAME, "text")
    username_field.send_keys(Config.TWITTER_USERNAME)

    next_btn = driver.find_element(By.XPATH, "//span[text()='Next']/ancestor::button")
    next_btn.click()
    time.sleep(2)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(Config.TWITTER_PASSWORD)
    password_field.send_keys(Keys.RETURN)
    time.sleep(10)

    # Fetch trending topics
    trend_elements = driver.find_elements(By.XPATH,"//div[@aria-label='Timeline: Trending now']//div[contains(@class,'css-175oi2r')]//span[starts-with(text(), '#')]")
    trending_topics = [trend.text for trend in trend_elements if trend.text]

    # if len(trending_topics) < 3:
    #     print("Could not fetch trending topics.")

    driver.quit()  
    return trending_topics

def store_in_mongo(trending_topics, ip_address):
    # Connect to MongoDB and store the trending topics
    mongo_client = MongoClient(Config.MONGO_URI)
    db = mongo_client['twitter_trends_db']
    collection = db['trends']

    unique_id = f"trend_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"
    document = {
        "_id": unique_id,
        "trends": trending_topics,
        "timestamp": datetime.now(),
        "ip_address": ip_address
    }

    collection.insert_one(document)
    return document

def run_script():
    # Main function to execute the script
    proxies = get_proxy()
    ip_address = test_proxy(proxies)
    if not ip_address:
        print("Exiting due to proxy issues.")
        return {"error": "Proxy issues, unable to fetch IP address"}

    trending_topics = fetch_trending_topics()
    if trending_topics:
        document = store_in_mongo(trending_topics, ip_address)
        print(f"Stored document: {document}")
        return document
    else:
        print("No trends found.")
        return {"error": "No trends found"}
