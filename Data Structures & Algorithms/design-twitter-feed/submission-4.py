class Twitter:
    def __init__(self):
        self.posts = defaultdict(list)  # Stores tweets for each user
        self.follows = defaultdict(set)  # Stores follow relationships
        self.timestamp = 0  # Tracks the order of tweets globally

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet with a timestamp for sorting
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.follows and userId not in self.posts:
            return []  # Return an empty list if the user doesn't exist

        # Create a min-heap to store the 10 most recent tweets
        min_heap = []

        # Include the user's own tweets
        for tweet in self.posts[userId]:
            heapq.heappush(min_heap, tweet)
            if len(min_heap) > 10:
                heapq.heappop(min_heap)

        # Include tweets from followees
        for followeeId in self.follows[userId]:
            for tweet in self.posts[followeeId]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        # Extract tweets from the heap, sorted by most recent
        return [tweetId for _, tweetId in sorted(min_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # Users can't follow themselves
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)