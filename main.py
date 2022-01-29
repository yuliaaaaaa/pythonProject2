# contrl+alt+l
'''
write a program which accepts 2 float arg. calculates sum, -, /, * there
the output should contains the f string with formatted data
if the sum of all calculations is less than fifty you should ask to provide data again

'''
num_1, num_2 = float(input('input 2 numbers')), float(input())
print(f'num 1 = {num_1}, num 2 = {num_2}')
suma = num_1 + num_2
product = num_1 * num_2
dividation = num_1 / num_2
subs = num_1 - num_2
print('sum = {},product = {}, product = {}, subs = {}'.format(suma, product, dividation, subs))

The_whole_sum = suma + product + dividation + subs
print(f'your the whole sum is: {The_whole_sum}')

if The_whole_sum < 50:
    print('you got the num less than 50')
else:
    print('you got the num bigger than 50')
