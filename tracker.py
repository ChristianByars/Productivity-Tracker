from backend.activity import run_tracker
from backend.createDB import create_db

def main():
    run_tracker()
    create_db()
    

if __name__ == "__main__":
    main()