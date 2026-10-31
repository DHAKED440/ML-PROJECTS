import sys
from types import ModuleType
from src.logger import logging

def error_message_detail(error, error_detail: ModuleType):
    _,_,exc_tb= error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message= f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    else:
        error_message= f"Error occured: {str(error)}"

    return error_message

class CustomException(Exception):
     def __init__(self, error_message, error_detail: ModuleType):

        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail
        )

     def __str__(self):
        return self.error_message

