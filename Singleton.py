
class URLFetcherWithout:
    
    def __init__(self):
        self.urls = []
    
    def fetch(self, url):
        print('fetching... {}'.format(url))
        
        urls = self.urls
        urls.append(url)
        self.urls = urls

    def show_urls(self):
        print(self.urls)
    
    
f1 = URLFetcherWithout()
f1.fetch('i.ua')
f1.show_urls()

f2 = URLFetcherWithout()
f2.fetch('google.com')
f2.show_urls()

print("Is these classes the same: ", f1 is f2)

print('=='*30)
print(' '*12,' SingletoneType ')
print('=='*30)


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

    def show_urls(self):
        print(self.urls)


fw1 = URLFetcherWith()
fw1.fetch('i.ua')
fw1.show_urls()

fw2 = URLFetcherWith()
fw2.fetch('google.com')
fw2.show_urls()

print("Is these classes the same: ", fw1 is fw2)
