import base64

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        return base64.encodestring(longUrl)
    

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """

        return base64.decodestring(shortUrl)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

#this site used for reference: https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
