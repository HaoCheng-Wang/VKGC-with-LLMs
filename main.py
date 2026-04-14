import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from config import neo4jconfig
from src.kg_writer import Neo4jWriter
def main():
    writer = Neo4jWriter(neo4jconfig.URL,neo4jconfig.USERNAME,neo4jconfig.PASSWORD)
    writer.create_constraints()

if __name__ == "__main__":
    main()