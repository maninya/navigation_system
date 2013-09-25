import scipy as sp
from scipy.misc import imread, imresize, imshow         
from scipy.signal.signaltools import correlate2d as c2d
import sys

#region 1, region 2, region 3, region 4

region1 = ['xerox room','CEEMS','Ceems lab','Library','Library seat','Libraryseats','Libraryseat','Ceems','near ceems','Staircase','Near ceems']
region2 = ['Data centre','Datacentre','Labs','Datacentreseat','oslab','Staircase','Research scholar rooms','Classroom 204','Elevator','Open Systems Lab','Information systems Lab','Information Systems Lab RC','Computational Lab',
'Data centre','Labs entrance','Wireless Networks Lab','Classroom 204']
region3 = ['faculty cubicles','Restrooms','Elevator','Faculty cubicles']
pics1 = ['near_xerox','front_xerox','Library','Library_seat','a_wall','me','Staircase']
pics2 = ['Staircase','Faculty_side','Library_side','Railing','me','a_wall','Library','Research_scholar_room','Comp_Lab']
pics3 = ['Restroom','cab','Faculty_cubicles','a_wall','me','faculty_cubicles']
pics = []
piclen = 0


def choose(wire_loc):
    global pics1,pics2,pics3,pics,piclen,region1,region2,region3
    if wire_loc in region1:
        pics = list(pics1)
    elif wire_loc in region2:
        pics = list(pics2)
    elif wire_loc in region3: 
        pics = list(pics3)    
    piclen = len(pics)

def get(pics,i):
    #global pics
    # get JPG image as Scipy array, RGB (3 layer)
    data = imread('%s%d.jpeg' %(pics,i))
    data = imresize(data,0.4)   
    #im2 = imresize(im22,0.5)
    #im3 = imresize(im33,0.5)
    # convert to grey-scale using W3C luminance calc
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    # normalize as in http://en.wikipedia.org/wiki/Cross-correlation
    return (data - data.mean()) / data.std()

def compare(INPUTFILE,wire_loc):
    global pics,piclen
    test = imread(INPUTFILE)
    test = imresize(test,0.4)
    test = sp.inner(test, [299, 587, 114]) / 1000.0
    test = (test - test.mean()) / test.std()
    choose(wire_loc)
    if not pics:
        print "I cannot recognise what is in front of me"   
        return 
    for a in range (0,piclen):
        for b in range(1,4):
            im1 = get(pics[a],b)
            com = c2d(im1, test, mode='same')
            #print '%s%d' %(pics[a],b)
            #print com.max()
            if com.max() > 7000:
                pics[a] = pics[a].replace("_", " ")
                print '%s' %pics[a]
                return
    print "I cannot recognise what is in front of me"   
 
            

if __name__ == "__main__":
    wire_loc = sys.argv[2]
    #print wire_loc
    loc = sys.argv[1]
    compare(loc,wire_loc)
    #print 'Done comparing images'

#print c23.max()

#(42105.00000000259, 39898.103896795357, 16482.883608327804, 15873.465425120798)
