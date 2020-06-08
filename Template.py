"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from graphics import*
from dog import Dog
from msdie import MSDie
def main():
    '''
    fileHandle = open("sample.txt", "a")
    print()
    #print(fileHandle)
    readRetrun = fileHandle.real()


    #7-2 problem 3
    print(5*'All that ')
    print()
    '''
    # section1
    '''
    win = GraphWin("demo", 1000, 1000)
    myCircle = Circle(Point(500, 500), 200)
    myCircle.setFill("greem")
    myCircle.draw(win)
    win.getMouse()
    '''
    # section2
    '''
    d = Dog("samantha")
    print(d)
    print(d.getName())
    d.setName("Godzilla")
    print(d.getName())

    d.bark()
    '''
    # section 3
    die = MSDie(6)
    print("number of sides", die.getSides())
    print("value:", die.getValue)
    die.setValue(5)
    print("value:", die.getValue())
    die.setValue(12)
    print("value:", die.getValue())

    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())


main()
