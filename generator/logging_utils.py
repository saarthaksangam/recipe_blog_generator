"""
Logging utilities for recipe blog generator.
"""
import logging

def setup_logger() -> logging.Logger:
    """Set up a logger with emoji, timestamp, and process info."""
    logger = logging.getLogger("recipe_blog_generator")
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(process)d] %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
