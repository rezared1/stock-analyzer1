# -*- coding: utf-8 -*-
"""
Application Constants

ثوابت برنامه
"""

# Indicators
INDICATORS = [
    "RSI",
    "MACD",
    "EMA",
    "SMA",
    "VWAP",
    "ATR",
    "Bollinger Bands",
    "Ichimoku",
    "SuperTrend",
]

# Timeframes
TIMEFRAMES = {
    "1m": 60,
    "5m": 300,
    "15m": 900,
    "30m": 1800,
    "1h": 3600,
    "4h": 14400,
    "1d": 86400,
    "1w": 604800,
    "1M": 2592000,
}

# Signal Levels
SIGNAL_LEVELS = {
    "strong_buy": (92, 100),
    "buy": (75, 91),
    "neutral": (40, 74),
    "sell": (25, 39),
    "strong_sell": (0, 24),
}

# Colors (for charts and UI)
COLORS = {
    "bullish": "#00FF00",
    "bearish": "#FF0000",
    "neutral": "#FFFF00",
    "strong_buy": "#00AA00",
    "strong_sell": "#AA0000",
}

# Default Settings
DEFAULT_RSI_PERIOD = 14
DEFAULT_MACD_FAST = 12
DEFAULT_MACD_SLOW = 26
DEFAULT_MACD_SIGNAL = 9
DEFAULT_BOLLINGER_PERIOD = 20
DEFAULT_BOLLINGER_STD = 2

# Market
TSE_MARKET_OPEN = "08:00"
TSE_MARKET_CLOSE = "12:30"
CRYPTO_MARKET_ALWAYS_OPEN = True
