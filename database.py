from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://root:password@localhost:5432/fast_api_db"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)