"""
355. 设计推特

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，
能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。
推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户

示例:
Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);
"""


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tuser = {}
        self.tposted = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if self.tuser.get(userId, 0) == 0:
            self.tuser[userId] = set([userId])
        self.tposted.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user
        followed or by the user herself.
        Tweets must be ordered from most recent to least recent.

        :type userId: int
        :rtype: List[int]
        """
        result = []
        if userId in self.tuser:
            followlist = self.tuser[userId]
            pl = len(self.tposted)
            for i in range(pl - 1, -1, -1):
                t = self.tposted[i]
                if t[0] in followlist:
                    result.append(t[1])
            return result[:10]
        else:
            return []

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid,
        it should be a no-op.

        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if self.tuser.get(followerId, 0) == 0:
            self.tuser[followerId] = set([followerId])

        if self.tuser.get(followeeId, 0) == 0:
            self.tuser[followeeId] = set([followeeId])

        self.tuser[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid,
        it should be a no-op.

        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if self.tuser.get(followerId, 0) == 0:
            self.tuser[followerId] = set([followerId])

        if self.tuser.get(followeeId, 0) == 0:
            self.tuser[followeeId] = set([followeeId])

        if followeeId in self.tuser[followerId] and followeeId != followerId:
            self.tuser[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 3)
obj.postTweet(1, 101)
obj.postTweet(1, 13)
obj.postTweet(1, 10)
obj.postTweet(1, 2)
obj.postTweet(1, 94)
obj.postTweet(1, 505)
obj.postTweet(1, 333)
obj.postTweet(1, 22)
obj.postTweet(1, 11)
print(obj.getNewsFeed(1))
# print(obj.tuser)
# print(obj.tposted)
