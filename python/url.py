import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        hash_obj = hashlib.md5(url.encode())
        short = hash_obj.hexdigest()[:6]
        self.url_map[short] = url
        return short

    def retrieve(self, short):
        return self.url_map.get(short, "URL not found")


# Example usage
u = URLShortener()

short = u.shorten("https://www.google.com")
print("Short URL:", short)

original = u.retrieve(short)
print("Original URL:", original)