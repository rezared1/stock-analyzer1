# -*- coding: utf-8 -*-
"""
Data Provider - Central Data Source

تمام برنامه از این فایل داده می‌گیرد.
اگر API تغییر کند، فقط این فایل تغییر می‌یابد.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime
import pandas as pd

from utils.logger import setup_logger

logger = setup_logger(__name__)


class BaseDataProvider(ABC):
    """Abstract base class for data providers."""
    
    @abstractmethod
    def get_symbols(self) -> List[str]:
        """Get list of available symbols."""
        pass
    
    @abstractmethod
    def get_ohlcv(self, symbol: str, timeframe: str = "1d") -> pd.DataFrame:
        """Get OHLCV data for a symbol."""
        pass
    
    @abstractmethod
    def get_ticker(self, symbol: str) -> Dict[str, Any]:
        """Get current ticker data for a symbol."""
        pass
    
    @abstractmethod
    def get_order_book(self, symbol: str) -> Dict[str, Any]:
        """Get order book data for a symbol."""
        pass


class MockDataProvider(BaseDataProvider):
    """Mock data provider for testing and development."""
    
    def __init__(self):
        """Initialize mock provider."""
        logger.info("Initializing MockDataProvider")
        self.symbols = self._generate_sample_symbols()
    
    def _generate_sample_symbols(self) -> List[str]:
        """Generate sample symbols for testing.
        
        Returns:
            List of sample symbol codes
        """
        return [
            "Fملی",
            "وبملت",
            "شپنا",
            "فارابی",
            "سپاهان",
        ]
    
    def get_symbols(self) -> List[str]:
        """Get list of available symbols.
        
        Returns:
            List of symbol codes
        """
        return self.symbols
    
    def get_ohlcv(self, symbol: str, timeframe: str = "1d") -> pd.DataFrame:
        """Get mock OHLCV data for a symbol.
        
        Args:
            symbol: Symbol code
            timeframe: Time frame (default: 1d)
            
        Returns:
            DataFrame with OHLCV data
        """
        logger.debug(f"Fetching OHLCV data for {symbol} ({timeframe})")
        # TODO: Implement actual data fetching
        return pd.DataFrame()
    
    def get_ticker(self, symbol: str) -> Dict[str, Any]:
        """Get current ticker data for a symbol.
        
        Args:
            symbol: Symbol code
            
        Returns:
            Dictionary with ticker data
        """
        logger.debug(f"Fetching ticker data for {symbol}")
        # TODO: Implement actual data fetching
        return {}
    
    def get_order_book(self, symbol: str) -> Dict[str, Any]:
        """Get order book data for a symbol.
        
        Args:
            symbol: Symbol code
            
        Returns:
            Dictionary with order book data
        """
        logger.debug(f"Fetching order book for {symbol}")
        # TODO: Implement actual data fetching
        return {}


# Global provider instance
_provider: Optional[BaseDataProvider] = None


def get_provider() -> BaseDataProvider:
    """Get the global data provider instance.
    
    Returns:
        Data provider instance
    """
    global _provider
    if _provider is None:
        _provider = MockDataProvider()
    return _provider


def set_provider(provider: BaseDataProvider) -> None:
    """Set the global data provider instance.
    
    Args:
        provider: Data provider instance
    """
    global _provider
    _provider = provider
    logger.info(f"Data provider set to {type(provider).__name__}")
