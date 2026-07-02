# -*- coding: utf-8 -*-
"""
Database Models

مدل‌های دیتابیس
"""

from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Symbol(Base):
    """Symbol model."""
    __tablename__ = "symbols"
    
    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    market = Column(String(50))  # TSE, Crypto, etc.
    last_price = Column(Float)
    last_update = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    ohlcv_data = relationship("OHLCV", back_populates="symbol")
    scores = relationship("AIScore", back_populates="symbol")


class OHLCV(Base):
    """OHLCV data model."""
    __tablename__ = "ohlcv"
    
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey("symbols.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    timeframe = Column(String(10))  # 1m, 5m, 1h, 1d, etc.
    
    # Relationship
    symbol = relationship("Symbol", back_populates="ohlcv_data")


class AIScore(Base):
    """AI Analysis Score model."""
    __tablename__ = "ai_scores"
    
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey("symbols.id"), nullable=False)
    score = Column(Float, nullable=False)  # 0-100
    signal = Column(String(50))  # buy, sell, hold, etc.
    confidence = Column(Float)  # 0-1
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    symbol = relationship("Symbol", back_populates="scores")
