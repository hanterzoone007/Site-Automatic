import requests as r

class User:
    def __init__(self,login,password):
        self._password = password
        self._login = login
        self.session = self.get_session()
        self.header = {}
    
    @property
    def login(self):
        return self._login
    
    @property
    def password(self):
        return self._password
    
    def set_header(self,**args):
        self.header = args
    
    def get_session(self):
        if not self.__dict__.get('header',False):
            self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        sess = r.session()
        sess.headers.update(self.header)
        return sess
    
    def login(self):
        self.session.get('https://hh.ru')
        print(self.session.headers)

