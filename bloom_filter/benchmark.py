import time


def benchmark(bf, data):
    start_insert = time.perf_counter()
    for item in data:
        bf.add(item)
    insert_time = time.perf_counter() - start_insert

    start_lookup = time.perf_counter()
    for item in data:
        bf.contains(item)
    lookup_time = time.perf_counter() - start_lookup

    return insert_time, lookup_time, bf.memory_usage_bytes()
