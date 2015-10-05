"""
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################

# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################

	Recodring class

"""

# Import all files
	# Import the parts we need from SimpleCV
#from SimpleCV import Camera, VideoStream, Display
#import cv2
#import cv
 
	# This import is just to create the video (if you want to do something meanwhile)
from multiprocessing import Process
 
	# To give the correct name to the output file
import time
 
	# Imports to treat command line arguments 
import sys
import getopt

    # ...
from time import gmtime, strftime

# #################################################################################################################################################

"""
    Class 
"""
class recordingClass(object):
    """docstring for recordingClass"""

    bool recordingVideoPart = False

    def __init__(self, arg):
        super(recordingClass, self).__init__()
        self.arg = arg


    def recordingMethod(self):
        if self.recordingVideoPart:
            print "\t Starting ... in time: ", strftime("%a, %d %b %Y %X", gmtime()), "\n"
        


"""
    Function ...
"""
def saveVideoPartToDisk(self, bufferName, outname):
    # construct the encoding arguments
    params = " -i {0} -c:v mpeg4 -b:v 700k -r 24 {1}".format(bufferName, outname)
 
    # run avconv to compress the video since ffmpeg is deprecated (going to be).
    call('avconv'+params, shell=True)


def recordSOd(cameraNumber, ):




"""
if __name__ == '__main__':
    HELP_MSG = '''record.py [options]
 
        -c <cam NR>   If you know which cam you want to use: set it here, else the first camera available is selected 
 
        -x <cam Width>    The width of camera capture. Default is 640 pixels
        --width
 
        -y <cam Height>   The height of camera capture. Default is 480 pixels
        --height
 
        -o <output>       The name of the output file. Default is the timestmp
        --output    
 
        -h <help>     Show this message
        '''
 
 
    camNR = 0
    width = 640
    height = 480
    outname = 'output_{0}.mp4'.format(time.ctime().replace(" ", "_"))     
 
    
 
    # Finally let's start
    main(camNR, width, height, outname)
"""




