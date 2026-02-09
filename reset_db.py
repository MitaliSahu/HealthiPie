from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['healthify_db']

# 1. WIPE EVERYTHING CLEAN
db.workouts.delete_many({})
db.food_items.delete_many({})
db.users.delete_many({}) # Clears users for a fresh start
db.daily_logs.delete_many({})

print("🧹 Old data wiped.")

# 2. ADD WORKOUTS (Fixes the Dropdown)
workouts = [
    {"name": "Running (Jogging)", "calories": 240, "category": "Cardio"},
    {"name": "Running (Sprint)", "calories": 375, "category": "Cardio"},
    {"name": "Walking (Brisk)", "calories": 130, "category": "Cardio"},
    {"name": "Cycling", "calories": 210, "category": "Cardio"},
    {"name": "Gym: Bench Press", "calories": 150, "category": "Strength"},
    {"name": "Gym: Squats", "calories": 175, "category": "Strength"},
    {"name": "Yoga", "calories": 100, "category": "Flexibility"},
    {"name": "Swimming", "calories": 250, "category": "Cardio"},
    {"name": "Zumba", "calories": 220, "category": "Cardio"},
    {"name": "HIIT", "calories": 300, "category": "Cardio"},
    {"name": "Football", "calories": 290, "category": "Sports"},
    {"name": "Cricket", "calories": 180, "category": "Sports"},
    {"name": "Dancing", "calories": 160, "category": "Activity"},
    {"name": "Cleaning", "calories": 80, "category": "Activity"}
]
db.workouts.insert_many(workouts)
print(f"✅ Added {len(workouts)} Workouts.")

# 3. ADD FOODS (Fixes the Meal Search)
foods = [
    {"name": "Apple", "calories": 95, "protein": 0, "carbs": 25, "fat": 0},
    {"name": "Banana", "calories": 105, "protein": 1, "carbs": 27, "fat": 0},
    {"name": "Chicken Breast (100g)", "calories": 165, "protein": 31, "carbs": 0, "fat": 3},
    {"name": "Rice (1 cup)", "calories": 200, "protein": 4, "carbs": 44, "fat": 0},
    {"name": "Pizza Slice", "calories": 285, "protein": 12, "carbs": 36, "fat": 10},
    {"name": "Egg (Boiled)", "calories": 70, "protein": 6, "carbs": 1, "fat": 5},
    {"name": "Salad (Green)", "calories": 30, "protein": 1, "carbs": 5, "fat": 0},
    {"name": "Milk (1 cup)", "calories": 150, "protein": 8, "carbs": 12, "fat": 8},
    {"name": "Sandwich", "calories": 250, "protein": 10, "carbs": 30, "fat": 8},
    {"name": "Oatmeal", "calories": 150, "protein": 5, "carbs": 27, "fat": 3}
]
db.food_items.insert_many(foods)
print(f"✅ Added {len(foods)} Basic Foods.")