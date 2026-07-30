from collections import OrderedDict, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        
        self.key_val = {}   
        self.key_freq = {}  
        self.freq_list = defaultdict(OrderedDict)  

    def _update_freq(self, key: int) -> None:
        """Bump the frequency of an existing key by 1, moving it between freq buckets."""
        freq = self.key_freq[key]
        val = self.freq_list[freq].pop(key)
        
        if not self.freq_list[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        new_freq = freq + 1
        self.key_freq[key] = new_freq
        self.freq_list[new_freq][key] = val  

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        
        self._update_freq(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_val:
            self.key_val[key] = value
            self._update_freq(key)
            return
        
        if self.size >= self.capacity:
            evict_key, _ = self.freq_list[self.min_freq].popitem(last=False)
            del self.key_val[evict_key]
            del self.key_freq[evict_key]
            self.size -= 1
        
        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_list[1][key] = value
        self.min_freq = 1  
        self.size += 1