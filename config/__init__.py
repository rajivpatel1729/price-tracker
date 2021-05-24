import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT_PATH, "data")

if __name__ == "__main__":
    print(PROJECT_ROOT_PATH)
    print(DATA_PATH)
