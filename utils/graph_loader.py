import os
from neo4j import GraphDatabase

class GraphLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_data(self, folderpath):
        with self.driver.session() as session:
            for file in os.listdir(folderpath):
                if file.endswith(".edges"):
                    full_path = os.path.join(folderpath, file)
                    with open(full_path, "r") as f:
                        for line in f:
                            u, v = line.strip().split()
                            session.run(
                                "MERGE (a:Person {id: $u}) "
                                "MERGE (b:Person {id: $v}) "
                                "MERGE (a)-[:FRIEND]->(b)",
                                u=u, v=v
                            )
        print("✅ All .edges files loaded into Neo4j")
        return True