import random
import sys
for i in  [1,2,3,4,5]:
    if i == 3:
      print('there is an element 3 in the list Break...')
      break
else:
     print('when not equal to 3')

for i in range(5):
    print(random.randint(1,50))

""" while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed {}'.format(response))
 """
def hello(name):
    print('Hello {}'.format(name))
    