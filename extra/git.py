def get_length(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count

print(get_length("1234"))
print(get_length([1, 2, 3, 4]))
print(get_length((1, 2, 3, 4)))
print(get_length({1, 2, 3, 4}))
print(get_length({"a": 1, "b": 2, "c": 3, "d": 4}))
print(get_length(range(1, 5)))
print(get_length(x for x in range(1, 5)))


