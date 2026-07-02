# -*- coding: utf-8 -*-
"""
Application Settings and Configuration

تنظیمات برنامه
"""

from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings configuration."""
    
    # Application Info
    app_name: str = "Stock Analyzer 1"
    app_version: str = "0.1.0"
    debug: bool = False
    
    # Paths
    base_dir: Path = Path(__file__).parent.parent.parent
    data_dir: Path = Field(default_factory=lambda: Path.home() / ".stock-analyzer1" / "data")
    log_dir: Path = Field(default_factory=lambda: Path.home() / ".stock-analyzer1" / "logs")
    
    # Database
    database_url: str = "sqlite:///./stock_analyzer.db"
    database_echo: bool = False
    
    # Market Settings
    update_interval: int = 5  # seconds
    symbols_count: int = 100
    
    # API Settings (to be configured later)
    api_timeout: int = 30
    api_retry_attempts: int = 3
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    
    # UI Settings
    window_width: int = 1600
    window_height: int = 900
    theme: str = "dark"
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    def __init__(self, **data):
        """Initialize settings and create necessary directories."""
        super().__init__(**data)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)
