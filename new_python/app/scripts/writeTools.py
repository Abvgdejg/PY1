import time
import sys

def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"

def SetupWriting(collection=None):
    global start_time
    global progression
    global collection_to_write

    start_time = time.time()
    progression = 0
    collection_to_write = collection

def WriteConsole(title, is_last=False):
    global start_time
    global progression
    global collection_to_write

    if is_last != True:
        progression += 1 

    tmp_time = time.time()
    sys.stdout.write("\r" + title + ": " + str(progression) + ("/" + str(len(collection_to_write)) + " " if collection_to_write != None else " ")  + "(" + toFixed(progression / (tmp_time - start_time)) + " Frames/s)" + ("\n" if is_last else ""))
    sys.stdout.flush()