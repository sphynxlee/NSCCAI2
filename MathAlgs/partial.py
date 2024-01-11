import timeit
from functools import partial

def mylen(list):
    len = 0
    for i in list:
        len += 1
    return len

mylen_timeing = partial(mylen, range(1,1000000))
len_timeing = partial(len, range(1,1000000))

runtime = timeit.timeit(len_timeing, number=1000)
print(f'Time for len: {runtime} seconds')

runtime2 = timeit.timeit(mylen_timeing, number=1000)
print(f'Time for mylen: {runtime2} seconds')