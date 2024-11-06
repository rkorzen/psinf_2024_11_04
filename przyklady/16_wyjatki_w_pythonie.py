
class MyException(Exception):
    pass


try:

    raise MyException("Jakis error")
    1/0
except ZeroDivisionError as e:
    print("nie dziel przez 0")
    print(e)
except MyException:
    1/0
    print("Obluga wyjatku My Exception")
finally:
    print("Coś tam")

#
# try:
#     1/0
# except:
#
#     pass