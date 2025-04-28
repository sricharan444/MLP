import sys #sys is used here specifically to access detailed information about the current exception using
from src.logger import logging 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #returns a tuple: (exception type, exception value, traceback).

    file_name=exc_tb.tb_frame.f_code.co_filename #gets the filename from the traceback.

    error_message="error occered!! [{0}] line number[{1}]".format(file_name,exc_tb.tb_lineno) #gets the line number where the exception occurred.
    return error_message

"""
This class inherits from the built-in Exception class.

On initialization:

It calls the base constructor with the error_message.

It then sets a detailed error message using the helper function error_message_detail().

The __str__ method returns the custom error message when the exception is printed or logged
"""
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
"""
try:
    1 / 0
except Exception as e:
    raise CustomException(str(e), sys)
"""