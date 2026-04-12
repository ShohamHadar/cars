from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://ori:ori@localhost:5432/carsDB"

engine = create_engine(DATABASE_URL)