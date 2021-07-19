class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_d = defaultdict(set)
        self.tweet_d = defaultdict(list)
        self.tweet_id = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweet_d[userId].append((tweetId, self.tweet_id))
        self.tweet_id += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user_list = self.user_d[userId]
        tweet_list = self.tweet_d[userId][:]
        for user_id in user_list:
            tweet_list.extend(self.tweet_d[user_id])
        tweet_list = sorted(tweet_list, key=lambda x:x[1], reverse=True)
        res = [tweet_id for tweet_id, _ in tweet_list]
        return res[:10] if len(res) >= 10 else res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_d[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.user_d:
            if followeeId in self.user_d[followerId]:
                self.user_d[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)