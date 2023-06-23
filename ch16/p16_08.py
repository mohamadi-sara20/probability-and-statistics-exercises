import numpy as np
import collections


def wilxoc_test(A, mu, direction='two.sided'):
    ds = np.subtract(A, mu)
    ds.sort()
    ds_freq = collections.Counter(ds)

    abs_ds = np.abs(ds)
    abs_sort = np.sort(abs_ds)
    abs_sort = abs_sort[abs_sort != 0]
    abs_ranks = dict({})
    freq = dict({})

    for i in range(len(abs_sort)): 
        if abs_sort[i] in abs_ranks:
            freq[abs_sort[i]] += 1
            abs_ranks[abs_sort[i]] += i+1
        else:
            abs_ranks[abs_sort[i]] = i+1
            freq[abs_sort[i]] = 1
    
    ranks = dict({})
    for i in range(len(ds)):
        if ds[i] != 0:
            ranks[ds[i]] = abs_ranks[abs(ds[i])]
    for k in ranks:
        if freq[abs(k)] > 1:
            ranks[k] = ranks[abs(k)] / freq[abs(k)]
        

    wp = 0
    wn = 0
    for i in ranks:
        if i > 0:
            wp += ds_freq[i] * ranks[i]
        else:
            wn += ranks[i] * ds_freq[i]

    if direction == 'less':
        # -
        return wn
    elif direction == 'greater':
        # +
        return wp
    elif direction == 'two.sided':
        # equal (min(w-, w+))
        return min(wp, wn)
    return


if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 
    time = np.array([17, 15, 20, 20, 32, 28, 12, 26, 25, 25, 35, 24])
    wval = wilxoc_test(time, 20)
    print(wval)
