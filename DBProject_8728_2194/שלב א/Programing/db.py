from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://shoham:shoham@localhost:5432/carsDB"

engine = create_engine(DATABASE_URL)