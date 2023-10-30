# R-4.1

# the alg
# both time and space usage are O(n)
def rec_find_max(S, index):
    if index == len(S)-1:
        return S[index]
    return max(S[index], rec_find_max(S, index+1))

def find_max(S):
    return rec_find_max(S, 0)

#print(find_max([1,2,774,5,6,7,8]))

# R-4.2

'''def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)'''
"""
arrows would trace downwards for the call, and upwards for the returns

power(2, 5) --> reuturn 2 * 16 ==> 32 <- the result
    ->
        power(2, 4) --> return 2 * 8
            ->      
                power(2, 3) --> return 2 * 4
                    ->
                        power(2, 2) --> return 2 * 2
                            ->
                                power(2, 1) --> returns 2 * 1
                                    ->
                                        power(2, 0) --> base condition met, return 1"""
# print(power(2, 5))

# R-4.3
def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result

print(power(2, 18))
"""
arrows would trace downwards for the calls; upwards for the returns
power(2, 18) n is even; returns 512*512
    power(2, 9) n is odd; returns 2*(16*16)
        power(2, 4) n is even; returns (4*4)
            power(2, 2) n is even; returns (2*2)
                power(2, 1) n is odd; returns 2*(1*1)
                    power(2, 0) -> returns 1"""


# R-4.4
def reverse(S, start, stop):
    if start < stop -1: # if at least 2 elements
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

# S = [4, 3, 6, 2, 6]
# reverse(S, 0, 5)
# print(S)

"""
did this on already reversed array; nothing changes just the numbers, the alg is explained correctly

we start the reversing from the middle moving outwards, getting pairs of already swapped numbers into sooner calls, then combining them

reverse(S, 0, 5) swap: [4, 3, 6, 2, 6]
    reverse(S, 1, 4) swap: [_,3,6,2,_]
        reverse(S, 2, 3) -> base condition (2 is not smaller than 3-1); the number 6 in the middle does not get swapped->
                                                                        there is nothing to swap it with"""

# R-4.5
# PuzzleSolve(3, S, U)
# S is empty, U = {a, b, c ,d}

def solves(S):
    #Note, this is a random solution to the pseudoproblem
    return S == ['d','b','c']


def PuzzleSolver(k, S, U):
    for e in sorted(U).copy():
        S.append(e)
        U.remove(e)
        if k==1:
            print(S)
            if solves(S):
                print( f'Solution found: {S}')
        else:
            PuzzleSolver(k-1, S, U)
        U.add(S.pop())  #removes the last item of an array

PuzzleSolver(3, [], {'a','b','c','d'})