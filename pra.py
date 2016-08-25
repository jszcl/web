import os

import urllib.request



def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    
    a = html.find('\"200\"')
    while a!=-1:
        b = html.find ('.jpg',a ,a+255)
        if b!= -1:
            img_addrs.append(html[a+14:b+4])
        else:
            b=a+14
        a=html.find('\"200\"',b)
    for each in img_addrs:
        print(each)
    return img_addrs

    
def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img=url_open(each)
            f.write(img)

def download_lady(folder='lady' ,pages=10):  
    os.mkdir(folder)
    os.chdir(folder)
    url= 'http://tu.fengniao.com/'
    page_num = 9
    for i in range(pages):
        page_num += i
        page_url = url + str(page_num)
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_lady()
    
    
