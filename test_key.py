import google.generativeai as genai
import os

# 1. PASTE YOUR REAL KEY HERE (No dots! No spaces!)
MY_KEY = "AIzaSyDMbUGjb6EBhA0b6BB8NGK9qloIexqO1T0"

print(f"Testing Key: {MY_KEY[:10]}... (Length: {len(MY_KEY)})")

try:
    genai.configure(api_key=MY_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say hello")
    print("✅ SUCCESS! The key works.")
    print("Response:", response.text)
except Exception as e:
    print("\n❌ FAILURE. The key is wrong.")
    print("Error details:", e)