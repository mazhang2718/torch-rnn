from bs4 import BeautifulSoup
import urllib
import csv



numPages = 73
frameworks = []

for page in range(1,numPages+1):
	link = "https://www.javascripting.com/?p=" + str(page)
	r = urllib.urlopen(link).read()
	soup = BeautifulSoup(r, "lxml")

	numChild = 17

	if (page==73):
		numChild = 13

	for child in range(1,numChild+1):
		selection = "#item-list > li:nth-of-type(" + str(child) + ") > div > h3 > a"
		framework = soup.select(selection)[0].string
		frameworks.append(framework)


file = open('frameworks.txt', 'w')
file.write('framework\n')

for framework in frameworks:
	file.write(framework + '\n')

file.close()

