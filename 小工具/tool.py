import requests,json

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
            return {Agreement:res['data'][0]['ip']+':'+str(+res['data'][0]['port'])}
        else:
            temp = json.loads(c)
            return {Agreement:temp['data'][0]['ip']+":"+str(temp['data'][0]['port'])}
















