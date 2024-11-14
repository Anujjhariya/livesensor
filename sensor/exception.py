
'''
In this file, we typically define custom exceptions. 
This means we’re creating special types of errors that are specific to our program, 
rather than using Python’s default errors. 
By doing this, we can:
>>Give more meaningful error messages.
>>Include details like the file name and 
>>line number where the error occurred, 
which makes it much easier to track down issues.
'''

import sys
import os



def error_message_detail(error,error_detail:sys):
    # exc.info :- returs three value but we need only 3rd value and we stored it in "exc_tb"
    _,_,exc_tb = error_detail.exc_info()
    fielname = exc_tb.tb_frame.f_code.co_filename

    error_message="error occured and the file name is [{0}] and the line number is [{1}] and error is [{2}]".format(
    fielname,exc_tb.tb_lineno,str(error))
    return error_message


'''this class raise the proper error means:
-->in which file,
-->in which line and 
-->what is the error'''

class SensorException(Exception):

    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)


        self.error_message =  error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message