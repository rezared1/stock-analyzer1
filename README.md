# Stock Analyzer 1 - تحلیل‌گر حرفه‌ای بازار

یک نرم‌افزار تحلیل بازار سهام ایران و رمزارز با هوش مصنوعی و معماری استاندارد شرکت‌های نرم‌افزاری

## 🎯 اهداف پروژه

- 📊 تحلیل حرفه‌ای بدون محدودیت API
- 🤖 هوش مصنوعی برای اولویت‌بندی فرصت‌ها
- 📈 یکپارچگی کامل داده‌ها
- 🔄 بروزرسانی خودکار هر 5 ثانیه
- 📊 گزارشات جامع و تفصیلی
- ~200 فایل و ~25,000 خط کد با استاندارد بالا

## 🏗️ معماری پروژه

```
stock-analyzer1/
├── src/
│   ├── ui/                    # رابط کاربری (PyQt6)
│   ├── data/                  # منابع داده (provider.py)
│   ├── indicators/            # موتور اندیکاتورها
│   ├── analysis/              # تحلیل‌ها
│   ├── database/              # مدیریت دیتابیس
│   ├── config/                # تنظیمات
│   ├── utils/                 # ابزار کمکی
│   └── main.py
├── tests/
├── assets/
├── docs/
├── config/
├── requirements.txt
├── setup.py
└── README.md
```

## 📋 مراحل توسعه

### ✅ مرحله اول - هفته اول
- رابط کاربری حرفه‌ای (Desktop)
- دیتابیس محلی
- فایل تنظیمات
- موتور نمودارها
- موتور اندیکاتورها

### ⏳ مرحله‌های بعدی
- انتخاب منبع داده
- هوش مصنوعی و تحلیل‌های پیشرفته

## 📦 نصب و راه‌اندازی

```bash
git clone https://github.com/rezared1/stock-analyzer1.git
cd stock-analyzer1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## 🤝 مشارکت‌کنندگان

- **rezared1** - توسعه‌دهنده اصلی

## 📄 لایسنس

MIT License
