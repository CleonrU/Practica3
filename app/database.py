import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Usa DATABASE_URL de Render para PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://user:password@localhost:5432/practica3")

# Si la URL es de PostgreSQL, crea la conexión sin parámetros adicionales
if DATABASE_URL.startswith("postgres"):
    engine = create_engine(DATABASE_URL)
else:
    # Si alguna vez usas SQLite, este es el caso
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
