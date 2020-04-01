import requests,time
import execjs
import re

class tao_sign():
    def __init__(self,cookie,url):
        self.t = int(time.time()) * 1000
        self.cookie = cookie
        #这里要将url的格式进行设置  格式参照淘宝问大家链接参数
        self.url = url

    def get_sign(self):
        tk = re.findall('_m_h5_tk=(.+?)_', self.cookie)[0]
        temp = re.findall('data=(.*)', self.url)[0]
        with open('test.js', encoding='utf-8') as f:
            jsdata = f.read()
        ctx = execjs.compile(jsdata)
        x = tk + "&" + str(t) + "&" + '12574478' + "&" + temp
        sign = ctx.call('h', x)
        return {'sign': sign, 'info': temp}

    def get_info(self):

        head = {
            "authority": "h5api.m.taobao.com",
            "method": "GET",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": self.cookie,
            "referer": "https://h5.m.taobao.com/wendajia/question2017.html?refId=589773891059&pre_item_id=589773891059&ttid=227200%40taobao_android_8.4.0&sourceType=other&suid=c6b1cff4-e094-4993-b346-95f826b4c9fa&ut_sk=1.We7H9xzG%2BAYDACUebBfQq6dp_21646297_1555054673708.Copy.windvane&un=d75c7f4f3565358ee7c4cca5375f99dd&share_crt_v=1&sp_tk=77+lc0l6dWJBeWVjT0Tvv6U=&cpp=1&shareurl=true&spm=a313p.22.u6.1025058449048&short_name=h.eZDBSMw&sm=4ee92f&app=chrome",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }
        c = self.get_sign()
        sign1 = c['sign']
        temp = c['info']
        url2 = f'https://h5api.m.taobao.com/h5/mtop.taobao.social.feed.aggregate/1.0/?jsv=2.4.1&appKey=12574478&t={t}&sign={sign1}&api=mtop.taobao.social.feed.aggregate&v=1.0&ecode=0&timeout=300000&timer=300000&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data={temp}'
        res2 = requests.get(url2, headers=head)
        return res2




