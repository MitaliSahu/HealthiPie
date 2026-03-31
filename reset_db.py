import csv
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# 1. .env file se Cloud URL load karein
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("❌ Error: MONGO_URI not found in .env file!")
    exit()

print("🔌 Connecting to MongoDB Cloud...")
client = MongoClient(MONGO_URI)
db = client['healthipie']  # Apne database ka sahi naam daalein

print("⏳ Cleaning old database lists...")
# Hum sirf food aur workouts wipe kar rahe hain, users aur logs nahi (taaki aapka purana data na ude)
db.food_items.delete_many({})
db.workouts.delete_many({})
print("🧹 Old foods and workouts wiped.")

# 1. LOAD FOODS FROM CSV
foods_list = []
try:
    with open('food.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            foods_list.append({
                "name": row.get('name', 'Unknown Food'),
                "serving_size": row.get('serving_size', '100g'),
                "calories": float(row.get('calories', 0) or 0),
                "protein": float(row.get('protein', 0) or 0),
                "carbs": float(row.get('carbs', 0) or 0),
                "fat": float(row.get('fat', 0) or 0),
                "category": "CSV Data"
            })
            
    if foods_list:
        db.food_items.insert_many(foods_list)
        print(f"✅ Successfully loaded {len(foods_list)} food items from food.csv!")
except FileNotFoundError:
    print("❌ food.csv file not found in the folder.")

# 2. LOAD WORKOUTS FROM CSV
workouts_list = []
try:
    with open('workouts.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming workouts.csv has 'name', 'calories', 'category'
            workouts_list.append({
                "name": row.get('name', 'Unknown Workout'),
                "calories": float(row.get('calories', 0) or 0),
                "category": row.get('category', 'Activity')
            })
            
    if workouts_list:
        db.workouts.insert_many(workouts_list)
        print(f"✅ Successfully loaded {len(workouts_list)} workouts from workouts.csv!")
except FileNotFoundError:
    print("❌ workouts.csv file not found in the folder.")

print("🎉 Database is now fully updated with your CSV data!")