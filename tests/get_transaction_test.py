import db

if __name__ == "__main__":
    results = db.get_transaction()
    print("\n".join(results))
