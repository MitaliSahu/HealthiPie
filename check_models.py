import google.generativeai as genai

# I put your exact key from the screenshot here:
KEY = "AIzaSyDMbUGjb6EBhA0b6BB8NGK9qloIexqO1T0"
genai.configure(api_key=KEY)

print("🔍 Asking Google for available models...")
try:
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ AVAILABLE: {m.name}")
            available_models.append(m.name)
            
    if not available_models:
        print("❌ No models found. The Key works, but the Project has no API access enabled.")
except Exception as e:
    print(f"❌ CONNECTION ERROR: {e}")