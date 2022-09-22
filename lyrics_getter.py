import requests, re
from bs4 import BeautifulSoup


class Getter:
	def __init__(self):
		print('Hello!')
		self.f = open('lyrics.txt', 'w')
		self.properlink	= 'https://www.azlyrics.com/l/lilpeep.html'
		self.r = requests.get(self.properlink)
		self.soup = str(BeautifulSoup(self.r.content, 'html.parser')).split('\n')

	def titles(self):
		for i in self.soup:
			if 'div class="listalbum-item"><a href="/lyrics/lilpeep' in i:
				print(i[38:])
				self.f.write(i[38:] + '\n')


	def writetest(self):
		self.f.write(self.properlink)
		self.f.write('\nHello!')


def main():
	g = Getter()
	g.titles()
	#g.writetest()


if __name__ == '__main__':
	main()
