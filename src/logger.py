import logging
import os
from logging.handlers import RotatingFileHandler

# Create a logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Define log file path
LOG_FILE = os.path.join(LOG_DIR, "project.log")

def get_logger(name):
    """Returns a configured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Capture all levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

    # Prevent duplicate handlers
    if not logger.handlers:
        # File handler with log rotation (max 5MB per file, keeps last 5 logs)
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Define log format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # Avoid duplicate logs in Jupyter Notebooks
        logger.propagate = False

    return logger

# Default logger instance
logger = get_logger(__name__)
