class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id = 1
        self.tweets = defaultdict(list)
        self.follow_dict = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((tweetId, self.id))
        self.id += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        subs = [userId, *list(self.follow_dict[userId])]
        tweets = []
        for user_id in subs:
            tweets.extend(self.tweets[user_id][-10:])
        tweets.sort(key=lambda x: -x[1])
        return [tweet_id for tweet_id, _ in tweets[:10]]
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_dict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follow_dict:
            self.follow_dict[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)