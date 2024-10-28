import random


def get_one_value(lst):
    seen = set()
    index = 0
    random.shuffle(lst)
    while True:
        if lst[index] not in seen:
            seen.add(lst[index])
            yield lst[index]
        index = (index + 1) % len(lst)
        if index == 0:
            seen.clear()
            random.shuffle(lst)


lst = [2, 4, 5, 1]
gen = get_one_value(lst)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
