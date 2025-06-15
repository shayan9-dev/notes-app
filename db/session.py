from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://fast_owner:npg_d4ZLzxj1FPkX@ep-noisy-star-a1mlvxvs-pooler.ap-southeast-1.aws.neon.tech/fast?sslmode=require"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
