import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.graph_loader import GraphLoader
from app.recommender import Recommender

# Replace with your actual credentials
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

DATA_PATH = "data/facebook"

def main():
    # Step 1: Load Graph Data
    loader = GraphLoader(URI, USER, PASSWORD)
    loader.load_data(DATA_PATH)
    loader.close()
    print("✅ Graph data loaded successfully into Neo4j!")

    # Step 2: Friend Recommendations
    recommender = Recommender(URI, USER, PASSWORD)
    
    user_id = "236"  # Replace with a valid ID from your dataset
    recommendations = recommender.recommend_friends(user_id, limit=5)

    print(f"\n👥 Top friend recommendations for user {user_id}:")
    for rec in recommendations:
        print(f"  👉 User ID: {rec['recommended_user']} (Mutual Friends: {rec['mutual_friends']})")

    recommender.close()

if __name__ == "__main__":
    main()
