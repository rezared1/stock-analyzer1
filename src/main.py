#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Analyzer 1 - Main Entry Point

تحلیل‌گر حرفه‌ای بازار سهام ایران و رمزارز
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import Settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


def main():
    """Main entry point for the application."""
    try:
        logger.info("Starting Stock Analyzer 1...")
        settings = Settings()
        logger.info(f"Configuration loaded: {settings.app_name}")
        logger.info("Application initialized successfully")
        
        # TODO: Initialize UI and start application
        logger.info("UI initialization pending...")
        
    except Exception as e:
        logger.error(f"Error starting application: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
