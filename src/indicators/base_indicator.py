# -*- coding: utf-8 -*-
"""
Base Indicator Class

کلاس پایه برای تمام اندیکاتورها
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import pandas as pd
import numpy as np


class BaseIndicator(ABC):
    """Abstract base class for all technical indicators."""
    
    def __init__(self, name: str, short_name: str):
        """Initialize indicator.
        
        Args:
            name: Full indicator name
            short_name: Short name/code for the indicator
        """
        self.name = name
        self.short_name = short_name
        self.params: Dict[str, Any] = {}
    
    @abstractmethod
    def calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate indicator values.
        
        Args:
            data: DataFrame with OHLCV data
            
        Returns:
            DataFrame with calculated indicator values
        """
        pass
    
    def validate_data(self, data: pd.DataFrame) -> bool:
        """Validate input data.
        
        Args:
            data: Input DataFrame
            
        Returns:
            True if data is valid
        """
        required_columns = {"open", "high", "low", "close", "volume"}
        if not required_columns.issubset(set(data.columns)):
            raise ValueError(f"Data must contain columns: {required_columns}")
        return True
