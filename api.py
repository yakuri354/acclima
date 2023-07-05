import requests
from datetime import *
import base64
import json

WAQI_TOKEN = "76742416d536bc5630b028a271febc45b02c8f83"

lat, lng = input().split()
ans1 = requests.get(f"https://api.waqi.info/feed/geo:{lat};{lng}?token={WAQI_TOKEN}")
print(json.dumps(ans1.json(), indent=4))

cookies = {
    'ASP.NET_SessionId': 'F5606A7BA4779883278FA318',
}

key = base64.b64encode((str(int(datetime.now(timezone.utc).timestamp() * 1000)) + ';isuckdicks:)').encode('ascii')).decode('utf-8')

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=F5606A7BA4779883278FA318',
    'Referer': 'https://www.lightpollutionmap.info/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

response = requests.get(
    f'https://www.lightpollutionmap.info/QueryRaster/?qk={key}&ql=viirs_2021&qt=point_t&qd={lng},{lat}',
    cookies=cookies,
    headers=headers,
)

print(response.content)
