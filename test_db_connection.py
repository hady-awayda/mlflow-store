from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import your Base and any models you might need
from config.database import Base
from config.database import DATABASE_URL

# Define a simple test function
def test_db_connection():
    try:
        # Create an engine and session
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = SessionLocal()

        # Try to connect and execute a simple query
        print("Testing database connection...")
        session.execute("SHOW DATABASES;")
        print("Connection successful!")

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        session.close()

if __name__ == "__main__":
    test_db_connection()
