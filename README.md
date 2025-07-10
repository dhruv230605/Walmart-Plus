# Walmart Hackathon Inventory AI

## Overview
This project is an AI-powered inventory management system that scrapes live data from Google Trends, Amazon Best Sellers, and other sources (excluding Walmart). It uses a Retrieval-Augmented Generation (RAG) pipeline to provide actionable stocking insights, factoring in holidays and regional events (like natural disasters).

## Features
- Scrape trending products and topics from multiple sources
- Store and process data in a local database
- AI-powered recommendations for inventory stocking
- (Optional) Dashboard for visualization

## Tech Stack
- Python (FastAPI/Flask)
- Scraping: pytrends, requests, BeautifulSoup, Selenium
- Database: SQLite/Postgres
- RAG: OpenAI/HuggingFace + FAISS/ChromaDB
- (Optional) Streamlit/React frontend

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the backend: `python api/main.py`
4. (Optional) Run the frontend: `streamlit run frontend/app.py`

## Folder Structure
- `scrapers/` - Web scraping modules
- `rag/` - Retrieval-Augmented Generation pipeline
- `db/` - Database models and setup
- `api/` - API endpoints
- `frontend/` - (Optional) Frontend app
- `utils/` - Utility functions
- `data/` - Data storage 