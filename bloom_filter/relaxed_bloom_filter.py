import mmh3
from bitarray import bitarray

class RelaxedBloomFilter:
    """
    Relaxed Bloom Filter inspired by:
    'Extending the Applicability of Bloom Filters by Relaxing their Parameter Constraints'
    """

    def __init__(self, size, num_hashes):
        self.size = size                  # bit array size (m)
        self.num_hashes = num_hashes      # relaxed k
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        for i in range(self.num_hashes):
            yield mmh3.hash(item, i) % self.size

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def contains(self, item):
        return all(self.bit_array[h] for h in self._hashes(item))

    def memory_usage_bytes(self):
        return self.bit_array.buffer_info()[1]
