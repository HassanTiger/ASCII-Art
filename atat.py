### 
### Author: Hassan Alnamer
### Description: To defend my cyber space, it became a must to build a powerful
### vehicle that can keep my kingdom safe. Introducing atat the new Ascci armored vehicle.
###
neckLength= int(input('Neck Length:\n'))
bodyHieght= int(input('Body Height:\n'))
LegLength= int(input('Leg Height:\n'))

print('')
  #back
print('''     _,.-Y  |  |  Y-._
 .-~"   ||  |  |  |   "-.''', end='\n')
 #body
print((bodyHieght)*' |______________________|\n',end='')
#print(' |______________________|\n',end='')

#body-neck
print(' |______________________|',end=( (neckLength+4)*' ' + '_____\n'))
#neck
print(' L______________________['+ (neckLength+3) *'-'+'I" .-{"-.')
print('I____________________ [__L]'+neckLength*'_'+'[I_/r(=}=-P')
print("L________________________j~"+" " + neckLength*" " + "'-=c_]/=-^")

#rest of the body
print('\\________________________]')
print('  [___________________]')
print('     I--I"~~"""~~"I--I')

#legs
print((LegLength)*'     |\\n|         |\\n|\n', end='')
print('     ([])         ([])')

#feet
print('    /|..|\\       /|..|\\')
print('   |=}--{=|     |=}--{=|')
print('  .-^--e-^-.   .-^--e-^-.')


