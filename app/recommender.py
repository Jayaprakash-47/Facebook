# app/recommender.py

from neo4j import GraphDatabase

class Recommender:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def recommend_friends(self, user_id, limit=5):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (u:Person {id: $user_id})-[:FRIEND]->(:Person)-[:FRIEND]->(fof)
                WHERE NOT (u)-[:FRIEND]->(fof) AND u <> fof
                RETURN fof.id AS recommended_user, COUNT(*) AS mutual_friends
                ORDER BY mutual_friends DESC
                LIMIT $limit
            """, user_id=user_id, limit=limit)
            return result.data()

