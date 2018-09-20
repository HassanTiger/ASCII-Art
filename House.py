my_spaces= int(input('Enter your width:'))
print('''
 ___^___
/       \\
|   H   |
|   H   |
''')
print(' '+ (my_spaces*'_') +'^'+ (my_spaces*'_'))
print('/'+' '*my_spaces+' '+' '*my_spaces+'\\')
print('|'+' '*my_spaces+'H'+' '*my_spaces+'|')
print('|'+'_'*my_spaces+'H'+'_'*my_spaces+'|')