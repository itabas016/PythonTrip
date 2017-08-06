#coding:utf-8
 
import scrapy
import os
import urllib
import zlib
from bs4 import Beautifulsoup
 

SITE_NAME = 'http://www.xeall.com'
KEY_WORD = 'shenshi'

class Comics(scrapy.Spider):
 
    name = "comics"
 
    def start_requests(self):
        urls = [ SITE_NAME + '/' + KEY_WORD ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        content = response.body
        if not content:
            self.log('parse body error.')
            return

        # use beautifulsoup instead of lxml
        soup = Beautifulsoup(content, "html5lib")

        # get tags contain comics
        listcon_tag = soup.find('ul', class_='listcon')
        if len(listcon_tag) < 1:
            self.log('extract comics list error.')
            return

        # get <a> in each tag list
        com_a_list = listcon_tag.find_all('a', attrs={ 'href': True })
        if len(com_a_list) < 1:
            self.log('can not find <a> that contain href arrtibute.')
            return

        # append each comics url to array
        comics_url_list = []
        for tag_a in com_a_list:
            url = SITE_NAME + tag_a['href']
            comics_url_list.append(url)


        print('\n>>>>>>>>>>>>>>>>>>> current page comics list <<<<<<<<<<<<<<<<<<<<')
        print(comics_url_list)

        # handle each page comic
        for url in comics_url_list:
            print('>>>>>>>>  parse comics:' + url)
            yield scrapy.Request(url=url, callback=self.comics_parse)

        # if just crawl current one page execute return
        #return

        # get all pages and each for this
        page_tag = soup.find('ul', class_="pagelist")
        if len(page_tag) < 1:
            self.log('extract page list error.')
            return

        # get next page url
        page_a_list = page_tag.find_all('a', attrs={ 'href': True })
        if len(page_a_list) < 2:
            self.log('extract page tag a error.')
            return

        #check current page is or not last page by select control
        select_tag = soup.find('select', attrs={ 'name': 'sldd' })
        option_list = select_tag.find_all('option')

        # verify current page is last by attribute selected in option tage
        last_option = option_list[-1]
        current_option = select_tag.find('option', attrs={ 'selected': True })

        # check is or not last page
        is_last = (last_option.string == current_option.string)
        if not is_last:
            next_page = SITE_NAME + '/' + KEY_WORD + '/' + page_a_list[-2]['href']
            if next_page is not None:
                print('\n------ parse next page --------')
                print(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
                pass
        else:
            print('========= Last page ==========')


    def comics_parse(self, response):
        content = response.body
        if not content:
            self.log('parse comics body error.')
            return

        soup = Beautifulsoup(content, "html5lib")

        page_list_tag = soup.find('ul', class_='pagelist')

        current_li = page_list_tag.find('li', class_='thisclass')
        page_num = current_li.string
        self.log('current page = ' + page_num)

        # display current page img tag
        li_tag = soup.find('li', id='imgshow')
        img_tag = li_tag.find('img')

        # current img url
        img_url = img_tag['src']
        self.log('img url: ' + img_url)

        # comics title
        title = img_tag['alt']

        # save img to local
        self.save_img(page_num, title, img_url)

        # next page url, when the href attribute is # so that signed the last page
        a_tag_list = page_list_tag.find_all('a')
        next_page = a_tag_list[-1]['href']
        if next_page == '#':
            self.log('parse comics: ' + title + ' finished.')
        else:
            next_page = SITE_NAME + '/' + KEY_WORD + '/' + next_page
            yield scrapy.Request(next_page, callback=self.comics_parse)


    def save_img(self, img_num, title, img_url):
        self.log('saving pic: ' + img_url)

        # save comics folder
        document = ''

        # each comic file name by title
        comics_path = document + '/' + title
        exists = os.path.exists(comics_path)
        if not exists:
            self.log('create document: ' + title)
            os.makedirs(comics_path)

        # each img name by title_page_num
        pic_name = comics_path + '/' + title + '_' + img_num + '.jpg'

        # check img exist in the local, if yes then pass
        exists = os.path.exists(pic_name)
        if exists:
            self.log('pic exists: ' + pic_name)
            return

        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = { user_agent }

            req = urllib.request.Request(img_url, headers = headers)
            response = urllib.request.urlopen(req, timeout = 30)

            # request the response data
            data = response.read()

            # if data is zip or gzip
            if response.info().get('Content-Encoding') == 'gzip':
                data = zlib.decompress(data, 16 + zlib.MAX_WBITS)

            # img save local
            fp = open(pic_name, "wb")
            fp.write(data)
            fp.close

            self.log('save image finished: ' + pic_name)
        except Exception as e:
            self.log('save image eror.')
            self.log(e)