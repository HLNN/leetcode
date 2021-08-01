# Note: This is a companion problem to the System Design problem: Design TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# Implement the Solution class:
#
#
# 	Solution() Initializes the object of the system.
# 	String encode(String longUrl) Returns a tiny URL for the given longUrl.
# 	String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
#
#
#  
# Example 1:
#
#
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
#
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after deconding it.
#
#
#  
# Constraints:
#
#
# 	1 <= url.length <= 104
# 	url is guranteed to be a valid URL.
#
#


class Codec:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}
        self.alphabet = "abcdefghijklmnopqrstuvwzyz"

    def encode(self, longUrl):
        while longUrl not in self.long_short:
            code = "".join(choices(self.alphabet, k=6))
            if code not in self.short_long:
                self.short_long[code] = longUrl
                self.long_short[longUrl] = code
        return 'http://tinyurl.com/' + self.long_short[longUrl]

    def decode(self, shortUrl):
        return self.short_long[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
