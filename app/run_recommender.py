# app/run_recommender.py
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.graph_loader import GraphLoader
from app.recommender import Recommender


URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

rec = Recommender(URI, USER, PASSWORD)
recommendations = rec.recommend_friends(0)
for r in recommendations:
    print(f"User {r['recommended_user']} (mutual friends: {r['mutual_friends']})")
rec.close()
