

def moj_generator():
    i = 1
    while True:
        yield i
        i += 1




mgen = moj_generator()




# for i in mgen:
#     print(i)

print(next(mgen))

print(next(mgen))

print(next(mgen))