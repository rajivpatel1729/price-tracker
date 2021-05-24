import os
from config import DATA_PATH

DATABASE_FILE_PATH = os.path.join(DATA_PATH, "pricetracker.db")
PRICETRACKER_DB_SQLITE_PATH = f"sqlite:///{DATABASE_FILE_PATH}"

if __name__ == "__main__":
    print(DATABASE_FILE_PATH)
    print(PRICETRACKER_DB_SQLITE_PATH)
