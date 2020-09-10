import random
import string
import pickle
def randomString(stringLength = 5):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(stringLength))
def generator(keys,numbers):
    numbers = numbers[0:len(keys)]
    return dict(zip(keys,numbers))

keys = []
numbers = [random.randint(0,100) for i in range(0,5)]
for i in range(0,5):
    keys.append(randomString())

with open('dict.data','wb') as f:
    pickle.dump(generator(keys,numbers),f)

with open('dict.data','rb') as f:
    data = pickle.load(f)
    print(data)
# print(keys)
# print(numbers)
# print(generator(keys,numbers))