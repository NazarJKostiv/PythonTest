import random


def get_one_value(lst):
    while True:
        random.shuffle(lst)
        for item in lst:
            yield item



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
