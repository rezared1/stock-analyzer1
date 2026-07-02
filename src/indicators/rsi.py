# -*- coding: utf-8 -*-
"""
Relative Strength Index (RSI) Indicator

اندیکاتور قدرت نسبی
"""

import pandas as pd
import numpy as np

from .base_indicator import BaseIndicator
from config.constants import DEFAULT_RSI_PERIOD


class RSI(BaseIndicator):
    """Relative Strength Index indicator."""
    
    def __init__(self, period: int = DEFAULT_RSI_PERIOD):
        """Initialize RSI indicator.
        
        Args:
            period: Period for RSI calculation (default: 14)
        """
        super().__init__("Relative Strength Index", "RSI")
        self.params = {"period": period}
    
    def calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate RSI.
        
        Args:
            data: DataFrame with OHLCV data
            
        Returns:
            DataFrame with RSI values
        """
        self.validate_data(data)
        
        df = data.copy()
        period = self.params["period"]
        
        # Calculate price changes
        delta = df["close"].diff()
        
        # Separate gains and losses
        gains = delta.where(delta > 0, 0)
        losses = -delta.where(delta < 0, 0)
        
        # Calculate average gains and losses
        avg_gains = gains.rolling(window=period).mean()
        avg_losses = losses.rolling(window=period).mean()
        
        # Calculate RS and RSI
        rs = avg_gains / avg_losses
        df["RSI"] = 100 - (100 / (1 + rs))
        
        return df
