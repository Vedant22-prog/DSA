import heapq
from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):

        self.tweets[userId].append(
            (self.time, tweetId)
        )

        self.time += 1

        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId):

        users = self.following[userId] | {userId}

        heap = []

        for user in users:

            if self.tweets[user]:

                index = len(self.tweets[user]) - 1

                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        while heap and len(result) < 10:

            _, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            index -= 1

            if index >= 0:

                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)