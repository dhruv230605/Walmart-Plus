# scrapers/google_trends.py
from pytrends.request import TrendReq

def fetch_trending_searches(region='united_states'):
    pytrends = TrendReq()
    trending_searches = pytrends.trending_searches(pn=region)
    return trending_searches 