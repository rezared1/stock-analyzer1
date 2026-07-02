# -*- coding: utf-8 -*-
"""
Helper Functions and Utilities

توابع کمکی و ابزارها
"""

from typing import List, Dict, Any
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


def get_date_range(days: int = 365) -> tuple[datetime, datetime]:
    """Get date range for data fetching.
    
    Args:
        days: Number of days to look back
        
    Returns:
        Tuple of (start_date, end_date)
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return start_date, end_date


def format_number(value: float, decimals: int = 2) -> str:
    """Format number with Persian locale.
    
    Args:
        value: Number to format
        decimals: Number of decimal places
        
    Returns:
        Formatted string
    """
    return f"{value:,.{decimals}f}"


def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculate percentage change.
    
    Args:
        current: Current value
        previous: Previous value
        
    Returns:
        Percentage change
    """
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100


def is_market_open() -> bool:
    """Check if market is currently open.
    
    Returns:
        True if market is open, False otherwise
    """
    from config.constants import TSE_MARKET_OPEN, TSE_MARKET_CLOSE
    
    now = datetime.now()
    if now.weekday() > 4:  # Friday or Saturday
        return False
    
    market_open = datetime.strptime(TSE_MARKET_OPEN, "%H:%M").time()
    market_close = datetime.strptime(TSE_MARKET_CLOSE, "%H:%M").time()
    
    return market_open <= now.time() <= market_close
