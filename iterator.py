

class Yes(object):

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes {0}'.format(self.x - 1)
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration


# my_iter1 = Yes(3)
# for i in my_iter1:
#     print(i)

# print('#' * 10)

# my_iter2 = Yes(3)
# while True:
#     try:
#         i = my_iter2.__next__()
#         print(i)
#     except StopIteration:
#         # print('Done from while')
#         break

# print('#' * 10)



# l = [1, 2, 3, 4, 5, 6, 7]


# for i in l:
#     temp = i * i
#     print(temp)

# print('#' * 8)

# iter_obj = l.__iter__()
# while True:
#     try:
#         i = iter_obj.__next__()

#         # Code block
#         temp = i * i
#         print(temp)
#         # End Code block
        
        
#     except StopIteration:
#         break



# rang = range(15)

# for i in rang:
#     print(i)


# # second way via iter and next funcs
# iter_obj = iter(rang)
# while True:
#     try:
#         i = next(iter_obj)
        
#         print(i)
    
#     except StopIteration:
#         break


def gen(n):
    for i in range(n):
        yield i


def gen2(n):
    iter_obj = range(n).__iter__()

    while True:
        try:
            i = iter_obj.__next__()
            
            yield i
            
        except StopIteration:
            break


g = gen(5)
# 1
# r = g.__next__()
# print(r)
# r = g.__next__()
# print(r)
# r = g.__next__()
# print(r)
# r = g.__next__()
# print(r)
# r = g.__next__()
# print(r)
# try:
#     r = g.__next__()
#     print(r)
# except:
#     print('Done')


# 2
# iter_obj = g.__iter__() # generator object technically
# while True:
#     try:
#         i = iter_obj.__next__()
        
#         print(i)
        
#     except StopIteration:
#         break


# 3
for i in g:
    print(i)




# for i in [1, 2, 3]:
#     print(i)
