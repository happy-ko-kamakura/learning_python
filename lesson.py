print('hello world')

num = 1
print(num)

name = 'happy-ko'
print(name)

print(num, type(num))
print(num, type(name))

is_ok = True
print(is_ok, type(is_ok))

name = '1'
new_num = int(name)
print(new_num, type(new_num))

num: int = 1
name: str = '1'
num = name
print(num, type(num))

print('hi', 'world', sep=',')
print('hi', 'world', sep=',', end='')
print('hi', 'world', sep=',', end='\n')

print('hi', 'world', sep=',', end='\n')
print('hi', 'world', sep=',', end='.\n')


print(2+2)

import math
result = math.sqrt(25)
print(result)

result = math.log2(10)
print(result)

import math
print(help(math))

s = 'My name is sachiko. '
is_start = s.startswith('My')
print(is_start)
s = 'ahaha'
is_start = s.startswith('My')
print(is_start)

s = 'My name is sachiko. '
print(s.find('sachiko'))
print(s.rfind('sachiko'))

s = 'My name is sachiko. Call me sachiko.'
print(s.rfind('sachiko'))

print(s.count('sachiko'))

name = 'sachiko'
print(name.capitalize())

print(s.title())

print(name.upper())
print(name.lower())

print(s.replace('sachiko', 'happy'))
