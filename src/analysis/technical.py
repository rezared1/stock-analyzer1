# -*- coding: utf-8 -*-
"""
Technical Analysis Engine

موتور تحلیل تکنیکال
"""

from typing import Dict, List, Any
import pandas as pd

from indicators.rsi import RSI
from utils.logger import setup_logger

logger = setup_logger(__name__)


class TechnicalAnalyzer:
    """Technical analysis engine for market symbols."""
    
    def __init__(self):
        """Initialize technical analyzer."""
        self.indicators = {
            "RSI": RSI(),
        }
    
    def analyze(self, data: pd.DataFrame, symbol: str) -> Dict[str, Any]:
        """Perform technical analysis on symbol data.
        
        Args:
            data: OHLCV data
            symbol: Symbol code
            
        Returns:
            Analysis results dictionary
        """
        logger.debug(f"Analyzing {symbol}")
        
        results = {"symbol": symbol, "indicators": {}}
        
        for name, indicator in self.indicators.items():
            try:
                analyzed_data = indicator.calculate(data)
                results["indicators"][name] = analyzed_data.iloc[-1].to_dict()
            except Exception as e:
                logger.error(f"Error calculating {name}: {e}")
        
        return results
