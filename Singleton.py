
class URLFetcherWithout:
    
    def __init__(self):
        self.urls = []
    
    def fetch(self, url):
        print('fetching... {}'.format(url))
        
        urls = self.urls
        urls.append(url)
        self.urls = urls
    
    
f1 = URLFetcherWithout()
f1.fetch('i.ua')

f2 = URLFetcherWithout()
f2.fetch('i.ua')

print("Is these classes the same: ", f1 is f2)




class SingletoneType(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletoneType, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class URLFetcherWith(metaclass=SingletoneType):

    def __init__(self):
        self.urls = []
    
    def fetch(self, url):
        print('fetching... {}'.format(url))
        
        urls = self.urls
        urls.append(url)
        self.urls = urls

