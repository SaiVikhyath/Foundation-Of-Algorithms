# Author: Sai Vikhyath K
# Date: 15 November, 2022


"""
Description:
Given a list of items that will be requested and a cache of certain size,
Find the optimal replacement strategy of replacing the items in the cache to minimize overall cache misses.
"""

class OptimalOfflineCaching:
    """ 
    Given a list of items that will be requested and a cache of certain size,
    If cache has the requested item, it's a cache hit.
    Else if cache can accomodate the item, insert into cache.
    Else if the cache is full and the item requested is not in cache, replace the item that will be used the farthest in the future.
    """

    def __init__(self, numberOfItems: int, sizeOfCache: int) -> None:
        """
        Maintain a list of items that will be requested.
        """
        
        self.numberOfItems = numberOfItems
        self.sizeOfCache = sizeOfCache
        self.itemsInCache = []

        for i in range(numberOfItems):
            self.itemsInCache.append(input("Enter item " + str(i + 1) + " to request: "))


    def findFarthestAccessed(self, cache: list, itemsInCache: list) -> str:
        """ Given the cache and the future item requests,
            Return the item that will be accessed the farthest in future.
        """
        
        c = cache.copy()
        
        for i in range(len(itemsInCache)):
            if len(c) == 1:
                return c[0]
            if itemsInCache[i] in c:
                c.remove(itemsInCache[i])
        
        return -1
            



    def farthestInFuture(self) -> None:
        """ Given a list of requested items and the size of the cache,
            Obtain the number of cache hits and cache misses using the optimal caching strategy.
        """

        numberOfCacheMisses = 0
        numberOfCacheHits = 0
        cache = list()

        for i in range(self.numberOfItems):
            if self.itemsInCache[i] in cache:
                numberOfCacheHits += 1
                continue
            elif len(cache) < self.sizeOfCache:
                numberOfCacheMisses += 1
                cache.append(self.itemsInCache[i])
            else:
                numberOfCacheMisses += 1
                farthest = self.findFarthestAccessed(cache, self.itemsInCache[i + 1:])
                if farthest == -1:
                    cache.pop()
                else:
                    cache.remove(farthest)
                cache.append(self.itemsInCache[i])
            
        print("Number of cache hits:", numberOfCacheHits)
        print("Number of cache misses:", numberOfCacheMisses)



if __name__ == "__main__":
    numberOfItems = int(input("Enter the number of items to be requested: "))
    sizeOfCache = int(input("Enter the size of the cache: "))
    ooc = OptimalOfflineCaching(numberOfItems, sizeOfCache)
    ooc.farthestInFuture()