class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.dict = {}
              

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dict[tokenId] = currentTime + self.time_to_live       

    def renew(self, tokenId: str, currentTime: int) -> None:
        time = self.dict.get(tokenId)
        if time and time > currentTime:
            self.dict[tokenId] = currentTime + self.time_to_live    

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key in self.dict:
            if self.dict[key] > currentTime:
                count += 1
        return count
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)