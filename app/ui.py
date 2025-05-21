# app/ui.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.recommender import Recommender

# Neo4j connection details
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

st.title("👥 Friend Recommender System")
st.markdown("Get friend suggestions based on mutual connections!")

# Input section
user_id = st.text_input("Enter your User ID", "236")
limit = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Recommend"):
    recommender = Recommender(URI, USER, PASSWORD)
    try:
        recommendations = recommender.recommend_friends(user_id, limit=limit)

        if recommendations:
            st.success(f"Top {limit} friend recommendations for user {user_id}:")
            for rec in recommendations:
                st.write(f"👉 **User ID:** `{rec['recommended_user']}` | 🧩 Mutual Friends: `{rec['mutual_friends']}`")
        else:
            st.warning("No recommendations found. Try another user ID!")

    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        recommender.close()
