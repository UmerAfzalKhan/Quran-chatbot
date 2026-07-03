import json
import os
from typing import List, Dict
from langchain_core.documents import Document

def load_quran_data():
    """Load Quran data from JSON file"""
    data_path = os.path.join(os.path.dirname(__file__), '../data/quran.json')
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Quran data not found at {data_path}")
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'data' in data and 'surahs' in data['data']:
        return data['data']['surahs']
    elif 'surahs' in data:
        return data['surahs']
    else:
        return data

def prepare_documents(surahs: List[Dict]):
    """Convert Quran data into LangChain documents"""
    documents = []
    
    for surah in surahs:
        surah_name = surah.get('name', 'Unknown')
        surah_english = surah.get('englishName', '')
        ayahs = surah.get('ayahs', [])
        
        for ayah in ayahs:
            ayah_num = ayah.get('numberInSurah', '')
            arabic = ayah.get('text', '')
            
            translation = ''
            if 'translation' in ayah:
                translation = ayah['translation']
            elif 'editions' in ayah and ayah['editions']:
                translation = ayah['editions'][0].get('text', '')
            
            text = f"""Surah {surah_name} ({surah_english}) - Ayah {ayah_num}
Arabic: {arabic}
English: {translation}"""
            
            metadata = {
                'surah': surah_name,
                'surah_number': surah.get('number', ''),
                'ayah_number': ayah_num
            }
            
            documents.append(Document(page_content=text, metadata=metadata))
    
    return documents