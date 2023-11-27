"""
File: web_crawler_avg.py
Name:
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html)
	#########################
	tags = soup.find_all('div', {'class': 'sc-e3e7b191-0 jlKVfJ sc-c7e5f54-2 glirPh cli-ratings-container'})
	total = 0
	for tag in tags:
		target = tag.span['aria-label']
		score = float(target.split()[2])
		print(score)
		total += score
	print(total/250)
	#########################


if __name__ == '__main__':
	main()
