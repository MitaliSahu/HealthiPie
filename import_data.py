import csv
import os
from pymongo import MongoClient

# Files
FOOD_FILE = 'food.csv'
WORKOUT_FILE = 'workouts.csv'

# Database
client = MongoClient('mongodb://localhost:27017/')
db = client['healthify_db']

def import_foods():
    if not os.path.exists(FOOD_FILE):
        print(f"❌ Error: {FOOD_FILE} not found.")
        return

    # WIPE OLD DATA
    deleted = db.food_items.delete_many({})
    print(f"🧹 Removed {deleted.deleted_count} old food items.")
    
    batch = []
    with open(FOOD_FILE, 'r', encoding='utf-8-sig') as f: 
        reader = csv.DictReader(f)
        reader.fieldnames = [name.lower().strip() for name in reader.fieldnames]
        
        for row in reader:
            try:
                batch.append({
                    "name": row.get('name', 'Unknown'),
                    "serving_size": row.get('serving_size', '1 serving'),
                    "calories": int(float(row.get('calories', 0))),
                    "protein": int(float(row.get('protein', 0))),
                    "carbs": int(float(row.get('carbs', 0))),
                    "fat": int(float(row.get('fat', 0)))
                })
            except ValueError: continue 

    if batch:
        db.food_items.insert_many(batch)
        print(f"✅ Success! Imported {len(batch)} Food items.")

def import_workouts():
    if not os.path.exists(WORKOUT_FILE): return
    db.workouts.delete_many({})
    batch = []
    with open(WORKOUT_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [name.lower().strip() for name in reader.fieldnames]
        for row in reader:
            try:
                batch.append({
                    "name": row.get('name', 'Exercise'),
                    "calories": int(float(row.get('calories', 0))),
                    "category": row.get('category', 'General')
                })
            except ValueError: continue
    if batch:
        db.workouts.insert_many(batch)
        print(f"✅ Success! Imported {len(batch)} Workouts.")

if __name__ == "__main__":
    import_foods()
    import_workouts()