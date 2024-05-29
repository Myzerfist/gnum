# Author: Myzerfist

# Credits: jfs on stackoverflow.com, https://stackoverflow.com/users/4279/jfs
def random(seed=None, a=0, b=10, N=10**12, integer=True):
    '''Pass a seed to generate new sequence, otherwise next value is returned.'''
    if seed is not None:
        # print("Starting new sequence.")
        global _rand_generator 
        if integer: 
            hash_plus = lambda j: int(a + (b - a) * (abs(hash(str(hash(str(seed) + str(j + 1))))) % 10**13) / 10**13)
        else:
            hash_plus = lambda j: a + (b - a) * (abs(hash(str(hash(str(seed) + str(j + 1))))) % 10**13) / 10**13
        _rand_generator = (hash_plus(j) for j in range(N))
    try:
        return next(_rand_generator)
    except StopIteration:
        # print("Random seed required.")
        return None

def gnumint(max):
    return random(seed=42, b=max)
    # print(random())
