
def incr_by_2(x, step=2):
    return x + step

def incr_by_12(x, step=12):
    return x + step



def incr_factory(step=1):

    def func(x):
        return x + step

    return func


incr_by_2 = incr_factory(2)
incr_by_12 = incr_factory(12)


print(incr_by_2(1))
print(incr_by_2(12))