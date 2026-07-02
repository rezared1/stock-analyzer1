# -*- coding: utf-8 -*-
"""
Logging Configuration

تنظیمات ثبت اطلاعات
"""

import sys
from pathlib import Path
from loguru import logger

from config.settings import Settings


def setup_logger(name: str) -> logger:
    """Setup and configure logger.
    
    Args:
        name: Logger name (typically __name__)
        
    Returns:
        Configured logger instance
    """
    settings = Settings()
    
    # Remove default handler
    logger.remove()
    
    # Add console handler
    logger.add(
        sys.stdout,
        format=settings.log_format,
        level=settings.log_level,
        colorize=True,
    )
    
    # Add file handler
    log_file = settings.log_dir / "stock_analyzer.log"
    logger.add(
        str(log_file),
        format=settings.log_format,
        level=settings.log_level,
        rotation="500 MB",
        retention="7 days",
    )
    
    return logger.bind(name=name)
