import requests
from bs4 import BeautifulSoup


class Getter:
	def __init__(self):
		print('Hello!')
		self.azlyrics = 'https://www.azlyrics.com'
		self.f = open('lyrics.txt', 'w+')
		self.properlink	= 'https://www.azlyrics.com/l/lilpeep.html'
		self.r = requests.get(self.properlink)
		self.soup = str(BeautifulSoup(self.r.content, 'html.parser'))

	def titles(self):
		self.soup = self.soup[self.soup.find('songlist'):].split('\n')
		self.soup = self.soup[1:]
		self.soup = '\n'.join(self.soup)
		self.soup = self.soup[:self.soup.find(']')].split('\n')
		for i in self.soup:
			i = i[i.find('"')+1:]
			h = i[i.find('h:')+3:]
			h = h[:h.find('html')+4]
			if 'https' not in h:
				h = self.azlyrics + h
			i = i[:i.find('"')]
			print(i, h)
			self.content = i + ' ' + h + '\n'
			self.f.write(self.content)


	def writetest(self):
		self.f.write(self.properlink)
		self.f.write('\nHello!')


def main():
	g = Getter()
	g.titles()
	#g.writetest()


if __name__ == '__main__':
	main()
