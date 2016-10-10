import requests, bs4, re, os
from multiprocessing import Pool

def getPayload(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    #print(soup)
    tinfos = soup.find_all('div', class_='tinfo')
    #print(tinfos)
    for tinfo in tinfos:
        href = tinfo.a['href']
        if (href != 'http://www.xunleigang.com'):
            #downloadTorrent
            href = dict(i.split('=') for i in tinfo.a['href'].split('&'))
            title = tinfo.a['title']
            id = href['id']
            uhash = href['uhash']
            payload = {'action':'download', 'imageField.x':'66', 'imageField.y':'40', 'id':id, 'uhash':uhash}
            title = title.replace('.', '_').replace('/', '_')
            #print(title)
            r = requests.post('http://www.bttiantang.com/download2.php', data = payload)
            with open(title + '.torrent', 'wb+') as f:
                f.write(r.content)

def downloadTorrent(payload):
    '''kw = 'action=download&id=27442&uhash=9c608887ce5de16995467b53&imageField.x=66&imageField.y=40'
    payload = dict(i.split('=') for i in kw.split('&'))
    print(payload)'''
    href = payload['href']
    href = dict(i.split('=') for i in href.split('&'))
    title = payload['name']
    #title.replace(' ', '')
    id = href['id']
    uhash = href['uhash']
    payload = {'action':'download', 'imageField.x':'66', 'imageField.y':'40', 'id':id, 'uhash':uhash}
    #print(payload)
    title = title.replace('.', '_').replace('/', '_')
    #print(title)
    r = requests.post('http://www.bttiantang.com/download2.php', data = payload)
    with open(title + '.torrent', 'wb+') as f:
        f.write(r.content)

def getUrls(i):
    url = 'http://www.bttiantang.com/?PageNo=' + str(i)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    #print(soup)
    urllist = []
    urls = soup.find_all('p', class_="tt cl")
    for i in urls:
        #print('http://www.bttiantang.com/%s, %s'%(i.a['href'],i.b.text))
        url = 'http://www.bttiantang.com/' + i.a['href']
        #print(url)
        urllist.append(url)
    return urllist

def main():
    if(os.path.exists('torrent')):
        os.chdir('torrent')
    else:
        os.mkdir('torrent')
        os.chdir('torrent')

    for i in range(678, 703):
        urllist = getUrls(i)
        print(urllist)
        #urllist  = getUrls()
        p = Pool(4)
        p.map(getPayload, urllist)
        p.close()
        p.join()








if __name__ == '__main__':
    main()