import matplotlib.pyplot as plt
from relaxed_bloom_filter import RelaxedBloomFilter
from data_gen import generate_data
from benchmark import benchmark

DATA_SIZE = 10000
BIT_ARRAY_SIZE = 200000
hash_counts = [2, 4, 6, 8, 10]

insert_times = []
lookup_times = []
memory_usage = []

data = generate_data(DATA_SIZE)

for k in hash_counts:
    bf = RelaxedBloomFilter(BIT_ARRAY_SIZE, k)
    ins_t, look_t, mem = benchmark(bf, data)

    insert_times.append(ins_t)
    lookup_times.append(look_t)
    memory_usage.append(mem / 1024)  # KB

# Insert Time Graph
plt.figure()
plt.plot(hash_counts, insert_times, marker='o')
plt.xlabel("Number of Hash Functions (k)")
plt.ylabel("Insert Time (seconds)")
plt.title("Insert Time vs Hash Functions")
plt.grid(True)
plt.show()

# Lookup Time Graph
plt.figure()
plt.plot(hash_counts, lookup_times, marker='o')
plt.xlabel("Number of Hash Functions (k)")
plt.ylabel("Lookup Time (seconds)")
plt.title("Lookup Time vs Hash Functions")
plt.grid(True)
plt.show()

# Memory Usage Graph
plt.figure()
plt.plot(hash_counts, memory_usage, marker='o')
plt.xlabel("Number of Hash Functions (k)")
plt.ylabel("Memory Usage (KB)")
plt.title("Memory Usage (Constant Space)")
plt.grid(True)
plt.show()
