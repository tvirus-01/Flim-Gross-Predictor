import bs4
import requests
import csv

tr_num = 0
with open("list_movies.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerow(['Movie', 'Production Budget', 'Worldwide Gross'])

for i in range(62):
	if tr_num > 100:
		headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
		url = "https://www.the-numbers.com/movie/budgets/all/"+str(tr_num)

		data = requests.get(url, headers=headers)
		soup = bs4.BeautifulSoup(data.text, "html.parser")

		center = soup.find("center")
	else:
		headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
		url = "https://www.the-numbers.com/movie/budgets/all"

		data = requests.get(url, headers=headers)
		soup = bs4.BeautifulSoup(data.text, "html.parser")

		center = soup.find("center")

	for tr in center.find_all("tr"):
		if tr_num == 0:
			pass
		else:
			td_num = 0
			for td in tr.find_all("td"):
				if td_num == 2:
					a_tag = td.find("a")
					movie_name = a_tag.text
				if td_num == 3:
					prod_budget = td.text.replace("$", "").replace("\xa0", "").replace(",", "")
				if td_num == 5:
					gross_budget = td.text.replace("$", "").replace("\xa0", "").replace(",", "")
				td_num += 1

			with open("list_movies.csv", "a") as f:
				writer = csv.writer(f)
				fields = [movie_name, prod_budget, gross_budget]
				writer.writerow(fields)
			print(fields)

		tr_num += 1
	print("\n")
	print(tr_num)