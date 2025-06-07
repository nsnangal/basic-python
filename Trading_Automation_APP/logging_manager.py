import logging
from logging.handlers import RotatingFileHandler
import os
import functools
import inspect

class LoggerManager:
    
    def __init__(self,name="AppLogger" ,log_dir="logs", max_bytes=2_000_000, backup_count=5):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Capture all levels
              
        # Prevent duplicate handlers if reloaded
        if not self.logger.handlers:
            self._add_handler("info.log", logging.INFO)
            self._add_handler("warning.log", logging.WARNING)
            self._add_handler("error.log", logging.ERROR)
            self._add_handler("debug.log", logging.DEBUG)
            self._add_console_handler()

    
    def _add_handler(self, filename, level):
        handler = RotatingFileHandler(
            os.path.join(self.log_dir, filename),
            maxBytes=2_000_000,
            backupCount=2
        )
        handler.setLevel(level)
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def _add_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
    
    @staticmethod
    def log_function_call(level=logging.DEBUG):
     """
     Decorator to log function entry and exit using the logger of the instance.
     """
     def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            class_name = ''
            logger = logging.getLogger("AppLogger") # fallback
            
            try:
                if len(args) > 0 and hasattr(args[0], '__class__'):
                    class_name = args[0].__class__.__name__ + '.'
                    if hasattr(args[0], 'logger'):
                        logger = args[0].logger  # use logger of calling class
            except Exception as e:
                pass  # Silent fail-safe

            logger.log(level, f" {class_name}{func_name} started")
            result = func(*args, **kwargs)
            logger.log(level, f" {class_name}{func_name} completed")
            return result
        return wrapper
     return decorator

