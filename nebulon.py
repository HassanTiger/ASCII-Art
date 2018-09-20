largeLayers= int(input('Large Layers on bottom:\n'))
mediumLayers= int(input('Medium Layers on bottom:\n'))
smallLayers= int(input('Small Layers on bottom\n'))
frontLength= int(input('Front length:\n'))
middleBody= int(input('Middle length:\n'))
backBody= int(input('Back length:\n'))
#.........................................
print('')
largelength= frontLength-3
mediumLength= round(frontLength/2 + 0.1)
smalllength= int(frontLength/3)
print( '  /=' + frontLength*'-'+ '\\' + 8*' ' +middleBody*' '+ ' /'+ backBody*'-'   + '|\n',end='')
print( ' /==' + frontLength*'/'+ '==\\\     '  +middleBody*' '+ '|' +(backBody+1)*'='+ '|\n',end='')
print( '|==-' + frontLength*'\\'+'======\--'  +middleBody*'='+ '=' +(backBody+1)*'='+ '|\n',end='')
print( ' \==' + frontLength*'=' +'==-------'  +middleBody*'-'+ '-' +(backBody+1)*'-'+ '|\n',end='')

#largeLayers
print(largeLayers*('   /' + (largelength) *'-' +'|\n'+ '   \\'+(largelength)*'='+'|\n'), end='')


#mediumLayers
print(mediumLayers*( (  mediumLength  )* ' '+'/' + ( mediumLength ) *'+' +'|\n'+ 
( mediumLength )*' '+'\\'+( mediumLength )*'-'+'|\n', end='')

#smallLayers
print(smallLayers*( ( smalllength )* ' ' +'\\' + ( smalllength ) *'<' +'|\n'+
( smalllength )*' '+ '  ' +( smalllength )*'<'+'|\n'), end='')
 