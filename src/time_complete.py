#! /usr/bin/python3
"""
Module calculate elapsed time
"""
import time

def complete_time(start, end):
    """
    function that gives the time duration in hours minutes and seconds
    Arguments : 
    	start : 
	end : 
    """
    total = end - start
    hrs = total // 3600
    minu = (total % 3600) // 60
    sec = (total % 3600) % 60
    if total < 60:
        return "{:2.0f} sec".format(sec)
    elif total < 3600:
        return "{:2.0f} min {:2.0f} sec".format(minu, sec)
    else:
        return "{:3.0f} h {:2.0f} min {:2.0f} sec".format(hrs, minu, sec)

if __name__ == "__main__":
	import time_complete
	print(help(time_complete))
