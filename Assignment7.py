#An Nguyen
#CMSC403
#Input : Command line argument for text file which contains dimensions of a canvas and rectangles
#Ouput: Packs rectangles into the canvas and displays a window representing the output

from tkinter import *
from rectpack import *

#creates Canvas object
class CustomCanvas:
    def __init__(self, aHeight, aWidth):
        #self.height = height
        #self.width = width
        self.master = Tk()
        #self.master.geometry('300x300')
        self.myCanvas = Canvas(self.master, height=aHeight, width=aWidth, bg='white')
        self.myCanvas.pack()
        #self.master.mainloop()

#creates Rectangle object
class Rectangle:
    def __init__(self,height,width): #constructor
        self.height=height
        self.width=width
        x=0
        y=0

    def setPos(self, x, y): #set position of rectangle
        self.x=x
        self.y=y

#https://github.com/secnot/rectpack
#packs allRect into the canvas
def pack (allRect, canvasSize):

    #pack rectangles
    packer = newPacker()
    for rectangle in allRect:
        packer.add_rect(rectangle.width,rectangle.height)
    packer.add_bin(int(canvasSize[0]), int(canvasSize[1]))
    packer.pack()

    #add rectangles to canvas
    all_rects = packer.rect_list()

    return all_rects

def main():
    #read file line by line
    filepath = sys.argv[1]
    # This opens a handle to your file, in 'r' read mode
    file_handle = open(filepath, 'r')
    # Read in all the lines of your file into a list of lines
    lines_list = file_handle.readlines()
    # Extract dimensions from first line.
    canvasSize = lines_list[0].split(',')

    #iterate thru for rectangles
    i=1
    rectangleList=[]
    line=lines_list[i] #first rectangle
    while True:
        lineAsList = line.split(',')
        rectangleList.append(Rectangle(int(lineAsList[0]),int(lineAsList[1])))
        i+=1
        if (i<len(lines_list)):
            line=lines_list[i] #get next rectangle
        else:
            break

    #pack the rectangles and get their coordinates
    all_rects = pack(rectangleList, canvasSize)
    #create canvas
    window = CustomCanvas(int(canvasSize[0]), int(canvasSize[1]))

    #display all rectangles
    for r in all_rects:
        window.myCanvas.create_rectangle(r[1], r[2], r[1]+r[3],r[2]+r[4], fill='blue', outline='black')
        #print(r[0], r[1], r[0]+r[2],r[1]+r[3])


    #display filled canvas
    window.myCanvas.pack()
    window.master.mainloop()

if __name__ == '__main__':
    main()
