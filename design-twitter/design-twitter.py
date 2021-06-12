class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 1
        self.follow_dict = defaultdict(set)
        self.tweet_dict = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweet_dict[userId].append((tweetId, self.time))
        self.time += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = self.tweet_dict[userId].copy()
        for user_id in self.follow_dict[userId]:
            news.extend(self.tweet_dict[user_id])
        news = [i for i, _ in sorted(news, key=lambda x: x[1], reverse=True)][:10]
        
        return news
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_dict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)