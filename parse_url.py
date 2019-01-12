import requests
from retrying import retry


headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; \
            .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"
           }


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    # print('*'*30)
    if method == 'POST':
        response = requests.post(url, headers=headers, data=data, proxies=proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method='GET', data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(parse_url(url))







