import random


def get_one_value_no_dplc(lst):
    seen = set()
    while True:
        random.shuffle(lst)
        for item in lst:
            if item not in seen:
                seen.add(item)
                yield item
        seen.clear()

def get_one_value(lst):
    while True:
        random.shuffle(lst)
        for item in lst:
            yield item

lst = [2, 4, 5, 2]
gen = get_one_value(lst)
gen2 = get_one_value_no_dplc(lst)

for _ in range(10):
    print(next(gen))
print("-"*24)
for _ in range(10):
    print(next(gen2))