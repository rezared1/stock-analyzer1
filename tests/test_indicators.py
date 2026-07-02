# -*- coding: utf-8 -*-
"""
Tests for Technical Indicators

تست‌های اندیکاتورها
"""

import pytest
import pandas as pd
import numpy as np

from src.indicators.rsi import RSI


@pytest.fixture
def sample_data():
    """Create sample OHLCV data for testing."""
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
    data = pd.DataFrame({
        "date": dates,
        "open": np.random.randn(100).cumsum() + 100,
        "high": np.random.randn(100).cumsum() + 105,
        "low": np.random.randn(100).cumsum() + 95,
        "close": np.random.randn(100).cumsum() + 100,
        "volume": np.random.randint(1000, 10000, 100),
    })
    return data


class TestRSI:
    """Tests for RSI indicator."""
    
    def test_rsi_calculation(self, sample_data):
        """Test RSI calculation."""
        rsi = RSI(period=14)
        result = rsi.calculate(sample_data)
        
        assert "RSI" in result.columns
        assert result["RSI"].notna().sum() > 0
    
    def test_rsi_range(self, sample_data):
        """Test RSI is within valid range."""
        rsi = RSI(period=14)
        result = rsi.calculate(sample_data)
        
        valid_rsi = result["RSI"].dropna()
        assert (valid_rsi >= 0).all()
        assert (valid_rsi <= 100).all()
