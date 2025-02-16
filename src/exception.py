import sys
import os
import logging

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the logger from src (ensure it exists in src/logger.py)
from src.logger import logger

class DataScienceException(Exception):
    """Base exception class for the data science project"""

    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.message = DataScienceException.get_error_message(message, error_detail)
        logger.error(self.message)

    @staticmethod
    def get_error_message(message, error_detail: sys):
        """Extract error details"""
        exc_type, exc_obj, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error in {file_name} at line {line_number}: {message}"

    def __str__(self):
        return self.message


# Custom Exception Classes
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


# **Test the Exception Handling**
if __name__ == '__main__':
    try:
        a = 1 / 0
    except Exception as e:
        logger.info("Attempted division by zero.")
        raise DataScienceException("Division by zero error", sys)
