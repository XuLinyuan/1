import re
import http.client  
import hashlib  
import json  
import urllib  
import random  
import time

class Baidu(): #创建百度翻译类
    def baidu_translate(self,content):  
        appid = '20170622000059949'  
        secretKey = 'V66eNSmKkfDXAKl7YGZv'  
        httpClient = None  
        myurl = '/api/trans/vip/translate'  
        q = content  
        fromLang = 'en' # 源语言  
        toLang = 'zh'   # 翻译后的语言
        salt = random.randint(32768, 65536)  
        sign = appid + q + str(salt) + secretKey  
        sign = hashlib.md5(sign.encode()).hexdigest()  
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(  
                q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(  
                        salt) + '&sign=' + sign  
                
        try:  
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')  
            httpClient.request('GET', myurl)  
            # response是HTTPResponse对象  
            response = httpClient.getresponse()  
            jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式  
            js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构  
            dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果    
            return(dst) # 返回结果
        except Exception as e:  
            print(e)  
        finally:  
            if httpClient:  
                httpClient.close()
                
fanyi=Baidu() # 创建百度翻译类的实体
f=open('LocaleResource_en_US.properties','r') # 读取源文件
f1=open('LocaleResource_zh_CN.properties','w') # 创建待写入的翻译后文件
lines=f.readlines()
for line in lines: # 按行读取源文件
    pattern='(\w+)(\W+)' # 正则表达式，匹配“键 空格 等号”
    match=re.match(pattern,line) 
    if match is not None:
        new_line=line.split(match.group(0)) # 分离等号前后两部分
        content='' 
        content=new_line[1]  # 提取出需要翻译的等号后半部分
        time.sleep(1) # 延长每次循环的时间至1秒。错误码54003，含义：访问频率受限，应降低访问频率
        result=fanyi.baidu_translate(content) # 取得百度翻译结果
        trans=line.replace(new_line[1],result) # 用翻译结果替换等号后半部分
        print(trans)
        f1.writelines(trans+'\n') #写入新文件
f.close() 
f1.close() #关闭两个文件

  
  
  





