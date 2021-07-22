class Codec:
    
    alphabet = string.ascii_letters + "0123456789"
    
    def __init__(self):
        
        self.url_code = {}
        self.code_url = {}
        self.base_url = "https://my-tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        while longUrl not in self.url_code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code_url:
                self.code_url[code] = longUrl
                self.url_code[longUrl] = code
        return self.base_url + self.url_code[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split('/')[3]
        return self.code_url.get(code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))