import requests,re
from sys import stdout
s=requests.session()
url='http://one.zju.edu.cn/pass_code/zx'
h="""Host: one.zju.edu.cn
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=7192890D64313FBFD611B3FEF41706F0.TomcatB; sm=1; _ga=GA1.3.1041695605.1589297255; sudy_ck=750C517DB9011185DD60ABC21A9A6EF23ECB9D9F17242D70C671993600F46CEF79C04EE1F8B856CA45C44BEB78785C2A33B67384ABB72210827D6CA57108C1F8A6F41B61A1DF1F9D0D0CDF7B3B97DF85; prev_choosen_tag=%22%E5%85%A8%E9%83%A8%22; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh; FILTER_NOT_FOUND_IMG=%7B%22T0028%3A%E5%AD%A6%E7%94%9F%E8%BF%94%E6%A0%A1%E7%99%BB%E8%AE%B0%22%3Atrue%2C%22T0029%3A%E5%AD%A6%E7%94%9F%E8%BF%94%E6%A0%A1%E7%99%BB%E8%AE%B0%EF%BC%88%E7%AC%AC%E5%8D%81%E6%89%B9%EF%BC%89%22%3Atrue%2C%22Z1722%3A%E7%A0%94%E7%A9%B6%E7%94%9F%E7%A6%BB%E6%A0%A1%E7%94%B3%E8%AF%B7%E6%B5%81%E7%A8%8B%22%3Atrue%2C%22Z1606%3A%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E5%9C%A8%E6%A0%A1%E5%AD%A6%E7%94%9F%E7%8E%B0%E5%AE%9E%E8%A1%A8%E7%8E%B0%E8%AF%81%E6%98%8E%22%3Atrue%2C%22T0025%3A%E5%AD%A6%E7%94%9F%E8%BF%9B%E5%87%BA%E6%A0%A1%E5%9B%AD%E7%94%B3%E8%AF%B7%22%3Atrue%2C%22T0027%3A%E6%98%A5%E5%AD%A3%E6%AF%95%E4%B8%9A%E7%94%9F%E8%BF%94%E6%A0%A1%E7%94%B3%E8%AF%B7%22%3Atrue%2C%22%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%94%9F%E8%AF%B7%E5%81%87%22%3Atrue%2C%22T0006%3A%E5%85%AC%E5%85%B1%E5%9C%BA%E9%A6%86%E7%94%B3%E8%AF%B7%22%3Atrue%2C%22T0026%3A%E5%AD%A6%E7%94%9F%E8%BF%9B%E5%87%BA%E6%A0%A1%E5%9B%AD%E6%8A%A5%E5%A4%87%22%3Atrue%7D; _pc0=FeadZzuYZwXol4z00uqiy56nBdvsxDJ8Tam82Py722U%2BagDxeCPTtHXizpwrs2gb; _csrf=S8mwplVi9KWoF2WQ0TlCeGxe3nU0shf90DiDXBjPjm8%3D; _pf0=fXG9bPud0V0bPq9bUC4JG07jTMyQ8q65tBeY6cJz5ow%3D; _pv0=IHmAEoKtbVvOlOdA%2BThuI7AdMA3RmHc%2BNnUgs%2FL5V7xSPT7BEsR3u9UvNGJ4%2BOggAUcecYJHxfZRE1oedypKkT5yoQQjMTinfERNJgAo%2F6fN5J9IKjFUAz%2FzmZPvIIDN3lUus7yURDm5yDjtW2EC4xqe8OT4r6ZijcURg6mCiKxcUibxKTbIYt5X1Wcd%2FlUykMFbhG8AnGrMTv%2FHlxUbWARRCIANPauRdGoLq%2FlkfhmPesd7FxSdyxcRGYLefUU02SGUhaHkjEqfjmv6Dfc1k469yUU9%2FBzW5DA1gY%2BA9Ig0ZpXuD9cFVUZT8RG78BcVsjVjBlE%2F7WdJJrRjyLm6lpTuWKbtjSWk09c0yHLclvEpM5whGnQJhdb0W398WQGvCL%2B75L57L3m7ceuli3zmbjysp9dXRJbz7M7H5ACwfc4%3D
"""
header={}
# print(h.split('\n'))
for item in h.split('\n'):
    if ':' in item:
        header[item.split(':')[0]]=item.split(':')[1].strip()
# print(header)
p=s.get(url,headers=header)
# print(header)
# print(p.text)

text=p.text
pattern=re.compile("text\t: '(.+?)',")
m=pattern.findall(text)
print(m[0])
stdout.flush()
