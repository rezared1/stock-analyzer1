from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="stock-analyzer1",
    version="0.1.0",
    author="rezared1",
    description="تحلیل‌گر حرفه‌ای بازار سهام ایران و رمزارز",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rezared1/stock-analyzer1",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "stock-analyzer1=src.main:main",
        ],
    },
)
