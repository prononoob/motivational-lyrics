import requests, random
from bs4 import BeautifulSoup


class Getter:
	def __init__(self):
		print('Hello!')
		self.azlyrics = 'https://www.azlyrics.com'
		self.f = open('lyrics.txt', 'w+')
		self.properlink	= 'https://www.azlyrics.com/l/lilpeep.html'
		self.r = requests.get(self.properlink)
		self.soup = str(BeautifulSoup(self.r.content, 'html.parser'))
		self.soup = self.soup[self.soup.find('songlist'):].split('\n')
		self.soup = self.soup[1:]
		self.soup = '\n'.join(self.soup)
		self.soup = self.soup[:self.soup.find(']')].split('\n')
		self.maxRange = len(self.soup)

	def getTitles(self):
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

	def randomTitle(self):
		self.x = random.randint(0, self.maxRange)
		self.link = self.soup[self.x]
		self.link = self.link[self.link.find('h:')+3:]
		self.link = self.link[:self.link.find('html')+4]
		if 'https' not in self.link:
			self.link = self.azlyrics + self.link
		print(self.link)

	def randomLyrics(self):
		self.r2 = requests.get(self.link)
		self.lyrics = str(BeautifulSoup(self.r2.content, 'html.parser'))
		self.lyrics = self.lyrics[self.lyrics.find('Sorry about that')+23:]
		self.lyrics = self.lyrics[:self.lyrics.find('</div>')-1]
		self.lyrics = self.lyrics.split('\n')
		self.maxLyrRange = random.randint(0, len(self.lyrics))
		self.lyrics = self.lyrics[self.maxLyrRange]
		self.lyrics = self.lyrics.strip('<br/>')
		print(self.lyrics)

	def lirycs(self):
		pass


	def writetest(self):
		self.f.write(self.properlink)
		self.f.write('\nHello!')


def main():
	g = Getter()
	g.randomTitle()
	g.randomLyrics()
	#g.writetest()


if __name__ == '__main__':
	main()
