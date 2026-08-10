from collections import defaultdict, OrderedDict


class LFUCache(object):

    def __init__(self, capacity):

        self.capacity = capacity

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        self.freq = defaultdict(OrderedDict)

        # Minimum frequency currently present
        self.min_freq = 0

    def get(self, key):

        if key not in self.cache:
            return -1

        value, frequency = self.cache[key]

        # Remove from old frequency bucket
        del self.freq[frequency][key]

        # If bucket becomes empty
        if not self.freq[frequency]:

            del self.freq[frequency]

            if self.min_freq == frequency:
                self.min_freq += 1

        # Increase frequency
        frequency += 1

        self.cache[key] = [value, frequency]

        # Add to new frequency bucket
        self.freq[frequency][key] = None

        return value

    def put(self, key, value):

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:

            _, frequency = self.cache[key]

            # Remove old frequency
            del self.freq[frequency][key]

            if not self.freq[frequency]:

                del self.freq[frequency]

                if self.min_freq == frequency:
                    self.min_freq += 1

            # Increase frequency
            frequency += 1

            self.cache[key] = [value, frequency]

            self.freq[frequency][key] = None

            return

        # Cache is full
        if len(self.cache) >= self.capacity:

            # Get least frequently used bucket
            keys = self.freq[self.min_freq]

            # First key = least recently used
            old_key, _ = keys.popitem(last=False)

            del self.cache[old_key]

            if not keys:
                del self.freq[self.min_freq]

        # Insert new key
        self.cache[key] = [value, 1]

        self.freq[1][key] = None

        self.min_freq = 1