import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

def scrape_first_time():
	article_list = scrape(50)
	df = pd.DataFrame(article_list)
	return df

def scrape_update():
	article_list = scrape(5)
	df = pd.DataFrame(article_list)
	return df

def scrape(num_faceplates):

	url = "https://www.reddit.com/r/tech/"
	geckodriver_path = "/usr/local/bin/geckodriver"
	service=Service(executable_path=geckodriver_path)
	driver=webdriver.Firefox(service=service)

	driver.get(url)

	time.sleep(5)

	main_container = driver.find_element(By.CLASS_NAME, "main-container")
	first_three_articles = main_container.find_elements(By.TAG_NAME, "article")

	article_list = []

	for article in first_three_articles:
		article_dict = {}
		shreddit_post = article.find_element(By.TAG_NAME, "shreddit-post")
		id_value = shreddit_post.get_attribute("id")
		article_dict['id'] = id_value
		for tag in article.find_elements(By.CSS_SELECTOR, "*"):
				if tag.text:
					article_dict[tag.tag_name] = tag.text
		article_list.append(article_dict)


	time.sleep(5)

	last_height = driver.execute_script("return document.body.scrollHeight")
	scroll_distance = 1000

	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight + arguments[0]);", scroll_distance)
		time.sleep(2)
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break 
		
		faceplate_elements = main_container.find_elements(By.TAG_NAME, "faceplate-batch")
		if len(faceplate_elements)>=num_faceplates:
			break
			
		last_height = new_height


	faceplates = main_container.find_elements(By.TAG_NAME, "faceplate-batch")

	for faceplate in faceplates:

		articles = faceplate.find_elements(By.TAG_NAME, "article")
		
		for article in articles:
			article_dict = {}
			shreddit_post = article.find_element(By.TAG_NAME, "shreddit-post")
			id_value = shreddit_post.get_attribute("id")
			article_dict['id'] = id_value
			for tag in article.find_elements(By.CSS_SELECTOR, "*"):
					if tag.text:
						article_dict[tag.tag_name] = tag.text
			article_list.append(article_dict)

	driver.quit()
	
	return article_list


    


