###
### Author: Hassan Alnamer
### Course: CSc 110
### Description: This is a program to make different shapes by using different functions
###
def main():
    myChar=''
    myHeight=0
    while True:
        shape= str(input('Enter shape to display:\n'))
        myChar= input('Enter arrow character:\n')
        myHeight=int(input('Enter row-area height:\n'))
        Nshape= shape.lower()
        if Nshape=='hourglass':
            hourGlass(myChar, myHeight)
            break

        elif Nshape=='plumbbob':
            plumbBob(myChar, myHeight)
            break

        elif Nshape=='house':
            house(myChar, myHeight)
            break
        else:
            print('!!! Enter a different shape !!!')



def hourGlass(arrowChar, height):
    print('')
    counter=0
    while counter<height:
        print( '|---------|\n',end='' )
        counter+=1

    rows=6
    spaces=0
    arrow=11
    while rows>0:
        #print spaces
        sCounter=0
        while sCounter<spaces:
            print(' ',end='')
            sCounter+=1
        spaces+=1
        #print the character
        aCounter=0
        while aCounter<arrow:
            print(arrowChar,end='')
            aCounter+=1
        arrow-=2
        print(sep='\n')
        rows-=1
      
    #flipped  
    rows=6
    spaces=5
    arrow=1
    while rows>0:
        sCounter=0
        while sCounter<spaces:
            print(' ',end='')
            sCounter+=1
        spaces-=1
        aCounter=0
        while aCounter<arrow:
            print(arrowChar,end='')
            aCounter+=1
        arrow+=2
        print(sep='\n')
        rows-=1
    counter=0
    while counter<height:
        print( '|---------|\n',end='' )
        counter+=1


def plumbBob(arrowChar, height):
    print('')
    rows=6
    spaces=5
    arrow=1
    while rows>0:
        sCounter=0
        while sCounter<spaces:
            print(' ',end='')
            sCounter+=1
        spaces-=1
        aCounter=0
        while aCounter<arrow:
            print(arrowChar,end='')
            aCounter+=1
        arrow+=2
        print(sep='\n')
        rows-=1
    counter=0
    while counter<height:
        print( '|---------|\n',end='' )
        counter+=1
        
   
    rows=6
    spaces=0
    arrow=11
    while rows>0:
        #print spaces
        sCounter=0
        while sCounter<spaces:
            print(' ',end='')
            sCounter+=1
        spaces+=1
        #print the character
        aCounter=0
        while aCounter<arrow:
            print(arrowChar,end='')
            aCounter+=1
        arrow-=2
        print(sep='\n')
        rows-=1




def house(arrowChar, height):
    print('')
    rows=6
    spaces=5
    arrow=1
    while rows>0:
        sCounter=0
        while sCounter<spaces:
            print(' ',end='')
            sCounter+=1
        spaces-=1
        aCounter=0
        while aCounter<arrow:
            print(arrowChar,end='')
            aCounter+=1
        arrow+=2
        print(sep='\n')
        rows-=1
    counter=0
    while counter<height:
        print( '|---------|\n',end='' )
        counter+=1

   


main()