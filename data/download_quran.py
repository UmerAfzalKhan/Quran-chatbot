import requests
import json

# Al-Quran Cloud API (Most Reliable)
url = "https://api.alquran.cloud/v1/quran/en.pickthall"

print("📥 Downloading Quran data...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Save to file
    with open('quran.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✅ Downloaded successfully!")
    print(f"📊 Total Surahs: {len(data['data']['surahs'])}")
else:
    print(f"❌ Error: {response.status_code}")