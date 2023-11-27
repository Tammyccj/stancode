import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html, features='html.parser')
	tags = soup.find_all('div', {'class': 'sc-c7e5f54-7 bVlcQU cli-title-metadata'})
	d = {}
	for tag in tags:
		year = tag.text[:4]
		if year not in d:
			d[year] = 1
		else:
			d[year] += 1
	for year, count in sorted(d.items(), key=lambda t: t[1]):
		print(year, count)


if __name__ == '__main__':
	main()
