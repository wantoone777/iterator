


class Yes(object):

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
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



l = ['12', 'fdsa', 505, 'alex', 'Moscow']



for i in l:
    print(i)



iter_obj = l.__iter__()
while True:
    try:
        i = iter_obj.__next__()

        # Code block
        print(i)
        # End Code block
        
        
    except StopIteration:
        break



