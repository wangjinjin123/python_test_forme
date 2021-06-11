import requests

#将get和post方法封装成request方法
class HttpRequest:
    def request(self,url,method,**kwargs):#
        if method.lower() == 'get':
            res = requests.get(url,**kwargs)
        else:
            res = requests.post(url,**kwargs)
        return res

