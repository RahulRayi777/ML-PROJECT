import sys
import os 
import logging
 

class DataScienceException(Exception):
    """Base exception class for the data science project"""
    
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.message = DataScienceException.get_error_message(message, error_detail)
        logger.error(self.message)

    @staticmethod
    def get_error_message(message, error_detail: sys):
        """Extract error details"""
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error in {file_name} at line {line_number}: {message}"

    def __str__(self):
        return self.message

# Specific Exceptions
class DataLoadingError(DataScienceException):
    """Exception raised when there is an error loading data"""
    pass

class DataProcessingError(DataScienceException):
    """Exception raised when there is an error processing data"""
    pass

class ModelTrainingError(DataScienceException):
    """Exception raised when there is an error during model training"""
    pass

class ModelPredictionError(DataScienceException):
    """Exception raised when there is an error making predictions"""
    pass
