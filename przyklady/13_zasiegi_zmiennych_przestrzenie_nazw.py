print(dir())
a = 1


def foo():
    # global a
    # a = 3
    b = 4

    def bar():
        global b
        b = 10
        # print("xxx", globals())
        print("xxx", locals())
        print(b)
    bar()

    # print("aaa", globals())
    print("aaa", locals())

    print("a w foo", a)

# print(globals())
print(locals())

print("a przed foo", a)
foo()
print("a po foo", a)

# przestrzen builtins

# przestrzen globalna

# przestrzen nielokalna - domykajaca

# przestrzen lokalna