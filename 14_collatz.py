from math import log, ceil
log_2 = log(2)
known_lengths = {0:0,1:1}

def is_power_of_2(num):
   return num != 0 and ((num & (num - 1)) == 0)



def len_of_collatz(n):

    if n in known_lengths:
        return known_lengths[n]

    if is_power_of_2(n):
        result = 1 + int(log(n)/log_2)
    elif ceil(n/2.0) == n/2.0:
        result = 1 + len_of_collatz(n/2)
    else:
        result = 1 + len_of_collatz(3 * n + 1)


    known_lengths[n] = result

    return result




def get_number_with_longest_chain(m=1000000):
    longest, n = 0, 0
    for i in xrange(1, m+1, 2):
        l = len_of_collatz(i)
        if l > longest:
            longest = l
            n = i
    return n
print get_number_with_longest_chain()
