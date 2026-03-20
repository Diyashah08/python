import sys
import logging
def error_message_detail(error:Exception , error_details: sys) -> str:
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"File:[{file_name}] at line number [{line_number}]: {str(error)}"
    logging.error(error_message)
class MyException(Exception):
    def __init__(self,error_message:str,error_details:sys):
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message,error_details)
        def __str__(self)->str:
            return self.error_message