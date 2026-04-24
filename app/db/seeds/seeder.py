import json
from pathlib import Path

import app.db.database as db_module
from app.services.profile_service import ProfileService
from app.schemas.profile import ProfileCreate
from app.core.settings import BASE_DIR

BASE_DIR = Path(__file__).resolve().parent
SEED_FILE = Path("seed_profiles.json")
SEED_PATH = f"{BASE_DIR}/{SEED_FILE}"
print(SEED_FILE)
print(BASE_DIR)
print(SEED_PATH)

def seed_profiles():
    db_module.init_db()
    
    db = db_module.SessionLocal()   # type: ignore

    try:
        with open(SEED_PATH, "r", encoding="utf-8") as f:
            raw = json.load(f)

            data = raw.get("profiles")

        for item in data:
            try:
                profile = ProfileCreate(**item)
                created = ProfileService.create_profile(db, profile)
                print(f"Created: {created.id}")
            except Exception as e:
                print(f"Skipped: {item.get('name')} → {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_profiles()