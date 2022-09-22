import requests
from bs4 import BeautifulSoup


class Getter:
	def __init__(self):
		print('Hello!')
		self.f = open('lyrics.txt', 'w')
		self.properlink	= 'https://www.azlyrics.com/l/lilpeep.html'
		r = requests.get(self.properlink)

	def writetest(self):
		self.f.write(self.properlink)
		self.f.write('\nHello!')


def main():
	g = Getter()
	g.writetest()


if __name__ == '__main__':
	main()
