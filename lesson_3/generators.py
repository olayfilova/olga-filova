# for i in range(1, 20, 2):
#     print(i)


def some_generator():
    print("start")
    yield 1
    print("after yield 1")


def some_generator_infinite():  # no StopIteration
    while True:  # requirements-task
        print("start")
        yield 2
        print("after yield 1")


# val = some_generator_infinite()
# val = some_generator()
# print(next(val))
# print(next(val))


def some_range(start, end, step):
    current_val = start
    while current_val<end:
        yield current_val
        current_val += step


def some_range_reversed(start, end, step):
    current_val = start
    while end < current_val:
        yield current_val
        current_val -= step



for i in some_range(20, 10, 2):
    print(i)


def complex_generator(limit):
    counter = 0
    while counter<=limit:
        print("action before yield1")
        yield "welcome"
        print("action after yield1")
        print("action before yield2")
        yield "how are you"
        print("action after yield2")
        counter +=1


for i in complex_generator(20):
    print(f"{i}")


# #Minimal test
#
# def test_file():
#     create file()
#     yield
#     delete file()
#
#
#
# def my_test(test_file):
#     test_file()
#     print("test")
# ##for i in complex_generator(20):
# ##    print(f"{i}")
##