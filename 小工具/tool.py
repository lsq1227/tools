import requests,json
from lxml import etree

def get_ip(url,Agreement='https',choice=False):
    """
    Add function for agent.
    Any agent can, just add your connection at the URL
    :param choice: Whether to switch new agents
            Agreement:Select a protocol. It defaults to HTTPS and can be modified to http
            url:Fill in the proxy access address you purchased
    :return: Example{'https': '58.218.214.140:4296'}
    """
    with open('./ip_pool.txt','r+',encoding='utf-8') as f:
        c = f.read()
        if len(c) == 0 or choice == True:
            res = requests.get(url).text
            with open('./ip_pool.txt', 'w', encoding='utf-8') as f:
                f.write(res)
            res = json.loads(res)
            return {Agreement: res['data'][0]['ip']+':'+str(+res['data'][0]['port'])}
        else:
            temp = json.loads(c)
            return {Agreement: temp['data'][0]['ip']+":"+str(temp['data'][0]['port'])}


def en_de(data,choice,code='utf-8'):
    """
    Use the interface of other websites to encrypt and decode URL encoding
    (multiple encryptions or decryptions are allowed)
    :param data: String to encrypt
    :param choice: EN is encryption and De is decryption
    :param code: Encoding format. Default to UTF-8
    :return: string -> Result
    """
    url = 'http://tool.chinaz.com/tools/urlencode.aspx'
    data = {
        'content': data,
        'charsetSelect': code,
    }
    if choice == 'en':
        data['en'] = 'UrlDecode编码'
    elif choice == 'de':
        data['de'] = 'UrlDecode解码'

    head = {
       'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    res = requests.post(url,headers=head,data=data).text
    div = etree.HTML(res)
    try:
        content = div.xpath('//div[@class="pr"]/textarea/text()')[0]
        return content
    except:
        print('节点选取错误')
        return


def get_page(page,dic):  # 分页器
    """
    :param page: page -- int or str num
    :param dic:  dic --  list
    :return: list  -- Paged list
    """
    page = int(page) - 1
    limit = int(page) * 10
    if len(dic) < 10:
        return dic
    try:
        a = dic[limit:limit + 10]
    except:
        a = dic[limit:limit + len(dic) - limit]
    return a



def che_get_img(url,img_name,path):
    """
    Download the component, fill in the response parameters,
    and write the IMG file in the relative path
    :param url:  Picture url to download
    :param img_name: Picture name to store
    :param path: File storage path
    :return: None
    -----------    Be  tb_img_che()  called ------------------
    """
    try:
        r = requests.get(url,stream=True)
    except requests.exceptions.MissingSchema:
        r = requests.get('http:'+url,stream=True)
    print(f'now ruequests{img_name}')
    print(r.status_code)
    name = img_name.replace('/','-').replace('【','').replace('】','').replace('<','').replace('>','')
    if r.status_code == 200:
        try:
            open(f'{path}\{name}.png', 'wb').write(r.content)
        except:
            open(f'{path}\{"untitled"+str(random.randint(10000))}.png', 'wb').write(r.content)




def tb_img_che(key,head):
    """
    Input the keywords to be searched in TaoBao and TianMao to download the through train pictures。
    :param key: search key -- string
    :return: None
    """
    path = os.getcwd() + '\\' + f'{key}_train'
    url = f'https://s.taobao.com/search?q={key}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc'
    res = requests.get(url,headers=head).text
    try:
        img = re.findall('"pic_url":"(.*?)",',res)
        shop_name = re.findall('"nick":"(.*?)",',res)
        id = re.findall('"nid":"(.*?)",',res)
        err = re.findall('"nid":"(.*?)",',res)[0]
    except:
        print('Please change the cookie')
        head['cookie'] = input('string --> Enter cookies here: ')
        res = requests.get(url, headers=head).text
        img = re.findall('"pic_url":"(.*?)",', res)
        shop_name = re.findall('"nick":"(.*?)",', res)
        id = re.findall('"nid":"(.*?)",', res)
    mkdir(path)
    for i in range(0,len(img)):
        che_get_img('http:'+img[i],shop_name[i]+'-'+str(id[i]),path)
        print(shop_name[i])








