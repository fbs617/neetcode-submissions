import heapq

class Twitter:

    def __init__(self):
        # key is userId, value is tweetIds
        self.tweets = {}
        # key is userId, value is all of their followers (including themself)
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
            self.following[userId] = set([userId])
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        for following in self.following[userId]:
            if following in self.tweets:
                out += self.tweets[following]
        out.sort(key=lambda x:x[0], reverse=True)
        out = out[:10]
        for i, (t, n) in enumerate(out):
            out[i] = n
        return out
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set([followerId])
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
