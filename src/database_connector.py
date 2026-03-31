import os

def connect_to_database():
    print("Initiating database connection...")
    # BUG: Missing fallback or try/catch if DB_URL is None
    db_url = os.environ.get("PRODUCTION_DB_URL")
    
    # This will crash with a TypeError if the URL is None
    connection_string = db_url + "?ssl=true"
    print(f"Connected to {connection_string}")
    return True

if __name__ == "__main__":
    connect_to_database()