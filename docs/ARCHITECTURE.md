# Stock Analyzer 1 - Architecture

## System Architecture

### Overview

Stock Analyzer 1 is a professional market analysis platform with modular architecture.

### Core Components

#### 1. Data Layer (`src/data/`)
- **provider.py**: Central data source (all data flows through this)
- **cache.py**: Caching mechanism for performance

#### 2. Indicators Layer (`src/indicators/`)
- Base indicator class
- RSI, MACD, EMA, SMA, VWAP, ATR, Bollinger Bands, Ichimoku, SuperTrend

#### 3. Analysis Layer (`src/analysis/`)
- Technical analysis engine
- Tape reading analysis
- AI scoring system
- Market scanner

#### 4. Database Layer (`src/database/`)
- SQLAlchemy models
- Database manager
- SQL migrations

#### 5. UI Layer (`src/ui/`)
- PyQt6 components
- Dashboard
- Market watcher
- Portfolio manager
- Alerts system

### Design Principles

1. **Modularity**: Each component is independent and testable
2. **Single Responsibility**: Each module has one clear purpose
3. **DRY (Don't Repeat Yourself)**: Centralized data management
4. **Testability**: Unit tests for all critical components

### Data Flow

```
UI → Analysis → Indicators → Data → Provider → API/Database
```

### Key Design Decision: Single Data Provider

All data enters through `data/provider.py`. This ensures:
- Easy API switching
- Consistent data format
- Simple caching strategy
- Minimal coupling between components
