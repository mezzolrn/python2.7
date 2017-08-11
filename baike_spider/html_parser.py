

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		#/
		links = soup.find_all('a', href=re.compile(r"/item/"))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, page_url, soup):
		res_data = {}

		#url
		res_data['url'] = page_url

		#class="lemmaWgt-lemmaTitle-title"
		title_node = soup.find('dd', attrs={'class',"lemmaWgt-lemmaTitle-title"}).find('h1')
		res_data['title'] = title_node.get_text()

		#class="lemma-summary"
		if soup.find('div', attrs={'class',"lemma-summary"}):
			summary_node = soup.find('div', attrs={'class',"lemma-summary"})
			res_data['summary'] = summary_node.get_text()
		else:
			res_data['summary'] = ''

		return res_data

	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data