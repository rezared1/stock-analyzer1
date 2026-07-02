# -*- coding: utf-8 -*-
"""
Database Manager

مدیریت دیتابیس
"""

from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config.settings import Settings
from utils.logger import setup_logger
from .models import Base

logger = setup_logger(__name__)


class DatabaseManager:
    """Database connection and management."""
    
    def __init__(self, database_url: Optional[str] = None):
        """Initialize database manager.
        
        Args:
            database_url: Database connection URL
        """
        settings = Settings()
        self.database_url = database_url or settings.database_url
        
        # Create engine
        self.engine = create_engine(
            self.database_url,
            echo=settings.database_echo,
        )
        
        # Create tables
        self.create_tables()
        
        # Create session factory
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
        )
        
        logger.info(f"Database initialized: {self.database_url}")
    
    def create_tables(self) -> None:
        """Create all database tables."""
        Base.metadata.create_all(bind=self.engine)
        logger.info("Database tables created")
    
    def get_session(self) -> Session:
        """Get a database session.
        
        Returns:
            Database session
        """
        return self.SessionLocal()
    
    def close(self) -> None:
        """Close database connection."""
        self.engine.dispose()
        logger.info("Database connection closed")


# Global database manager instance
_db_manager: Optional[DatabaseManager] = None


def get_db_manager() -> DatabaseManager:
    """Get the global database manager instance.
    
    Returns:
        Database manager instance
    """
    global _db_manager
    if _db_manager is None:
        _db_manager = DatabaseManager()
    return _db_manager
