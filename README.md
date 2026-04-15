# 🔗 URL Shortener API

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)

A production-ready URL shortener API that converts long URLs into short, shareable links with automatic redirects and click tracking analytics.

##  Features

-  Shorten any URL to a 6-character unique code
-  Automatic HTTP redirects (302) to original URLs
-  Click tracking with real-time analytics
-  Custom aliases support (e.g., `/myresume`)
-  Interactive API documentation (Swagger UI)
-  In-memory storage (ready for database integration)

##  Tech Stack

- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server for high performance
- **Pydantic** - Data validation

## Quick Start

### Prerequisites
- Python 3.12 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/omm-sahoo-codes/url-shortener-api.git
cd url-shortener-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload