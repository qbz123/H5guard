import execjs
import requests
if __name__ == '__main__':
    js_code = open('mt.js', 'r', encoding='utf-8').read()
    js = execjs.compile(js_code)
    with requests.session() as session:
        session.headers = {
            "dj-token": "",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; MI 6 Build/TQ2A.230405.003.E1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 TitansX/12.9.1 KNB/1.2.0 android/13 mt/com.sankuai.meituan/12.9.404 App/10120/12.9.404 MeituanGroup/12.9.404",
            "Content-Type": "application/json",
            "X-Requested-With": "com.sankuai.meituan",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://market.waimai.meituan.com/",
            "Cookie": ""
        }
        url = 'https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/fetchcoupon?couponReferId=6A6A4BE2942F475D8F916251B3AC247F&geoType=2&gdPageId=492937&pageId=494801&version=1&utmSource=qq&utmCampaign=AgroupBgroupC0D200E0Ghomepage&instanceId=16838781677670.42866282232864470&componentId=16838781677670.42866282232864470'
        data = {"cType": "mtandroid", "fpPlatform": 4, "wxOpenId": "", "appVersion": "12.9.404"}
        req = {
            "url": url,
            "method": "POST",
            "headers": session.headers,
            'data': data
        }
        r = js.call("signReq", req)
        print(r)
        session.headers = r['headers']
        print(session.post(url=url, json=req['data']).text)
