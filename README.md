# 📖 Quranic Chatbot

<div align="center">
  <img src="screenshots/1.png" alt="Quranic Chatbot" width="800"/>
  <br>
  <p>
    <strong>An AI-powered chatbot that answers Islamic questions using Quranic verses with RAG (Retrieval-Augmented Generation)</strong>
  </p>
  <br>
</div>

## 🚀 Live Demo

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://your-app-url.streamlit.app)
[![GitHub Repo](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/quran-chatbot)

---

## 📸 Screenshots

<div align="center">
  <h3>🏠 Home Page</h3>
  <img src="screenshots/1.png" alt="Home" width="700"/>
  <br><br>
  
  <h3>💬 Chat Interface</h3>
  <img src="screenshots/2.png" alt="Chat" width="700"/>
  <br><br>
  
  <h3>📚 Quran References</h3>
  <img src="screenshots/3.png" alt="References" width="700"/>
  <br><br>
  
  <h3>📖 Surah Explanation</h3>
  <img src="screenshots/4.png" alt="Surah Explanation" width="700"/>
  <br><br>
  
  <h3>💡 Answer with References</h3>
  <img src="screenshots/5.png" alt="Answer with References" width="700"/>
</div>

---

## ✨ Features

- 🤖 **AI-Powered Answers** - Uses Groq's LLM (Llama 3.1 8B) for accurate responses
- 📖 **Quranic References** - Every answer includes Surah and Ayah numbers
- 🔍 **RAG Architecture** - Retrieves relevant verses before generating answers
- 💬 **Chat Interface** - Smooth conversation flow with history
- ⚡ **Fast Search** - FAISS vector database for quick retrieval (2-3 seconds after first load)
- 📱 **Responsive** - Works on desktop and mobile
- 🕌 **Islamic Content** - Specialized for Quranic questions

---

## 🛠️ Tech Stack

<div align="center">
  <table>
    <tr>
      <td><strong>Frontend</strong></td>
      <td>Streamlit</td>
    </tr>
    <tr>
      <td><strong>AI/LLM</strong></td>
      <td>Groq (Llama 3.1 8B)</td>
    </tr>
    <tr>
      <td><strong>RAG Framework</strong></td>
      <td>LangChain</td>
    </tr>
    <tr>
      <td><strong>Vector Database</strong></td>
      <td>FAISS</td>
    </tr>
    <tr>
      <td><strong>Embeddings</strong></td>
      <td>Sentence Transformers (all-MiniLM-L6-v2)</td>
    </tr>
    <tr>
      <td><strong>Data Source</strong></td>
      <td>Al-Quran Cloud API</td>
    </tr>
  </table>
</div>

---

## 🏗️ Architecture

The chatbot follows a **RAG (Retrieval-Augmented Generation)** architecture:
User Question
↓
[Query Embedding]
↓
[FAISS Vector Search] ← Quran Verses (Embedded)
↓
[Retrieved Context]
↓
[Groq LLM] ← Prompt Template
↓
[AI Response] + [References]


### How it works:

1. **User Question** - User asks any Islamic question
2. **Query Embedding** - The question is converted into a vector (embedding)
3. **FAISS Vector Search** - Searches for similar Quranic verses in the vector database
4. **Retrieved Context** - Top 5 relevant verses are retrieved
5. **Groq LLM** - AI model generates answer based on context
6. **Response + References** - Answer with Surah and Ayah references

---

## 📥 Installation

### Prerequisites

- Python 3.10+
- Groq API Key ([Get it here](https://console.groq.com/))

### Steps

```bash
# 1. Clone repository
git clone https://github.com/yourusername/quran-chatbot.git
cd quran-chatbot

# 2. Create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 5. Download Quran data
cd data
python download_quran.py
cd ..

# 6. Run app
streamlit run src/app.py

🔑 Environment Variables
Create .env file:GROQ_API_KEY=your_groq_api_key_here

📁 Project Structure
text
quran-chatbot/
├── data/
│   ├── quran.json          # Quran data (114 Surahs, 6236 Ayahs)
│   └── download_quran.py   # Data download script
│
├── src/
│   ├── app.py              # Streamlit main app
│   ├── data_loader.py      # Quran data loader
│   ├── vector_store.py     # FAISS vector store
│   └── rag_chain.py        # RAG chain with Groq
│
├── screenshots/            # App screenshots
│   ├── 1.png               # Home page
│   ├── 2.png               # Chat interface
│   ├── 3.png               # References
│   ├── 4.png               # Surah explanation
│   └── 5.png               # Answer with references
│
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── requirements.txt        # Python dependencies
└── README.md               # This file
📊 Data
114 Surahs loaded from Al-Quran Cloud API

6,236 Ayahs processed and embedded

6,465 chunks created for retrieval

2-3 minutes initial loading time (cached after first run)

💬 Sample Questions
Category	Question
🕌 Beliefs	"What does Quran say about Allah?"
🤲 Prayer	"What does Quran say about Salah?"
💝 Morals	"What does Quran say about patience?"
📖 Surah	"Explain Surah Al-Fatiha"
🌍 Creation	"What are the signs of Allah's existence?"
👨‍👩‍👧‍👦 Social	"What does Quran say about parents?"
💰 Wealth	"What does Quran say about charity?"
🛠️ Troubleshooting
Common Issues
1. ModuleNotFoundError
pip install -r requirements.txt
2. Model Decommissioned
Update src/rag_chain.py:

python
model="llama-3.1-8b-instant"
3. Memory Error
Reduce chunk size in src/vector_store.py:

python
chunk_size=300  # Instead of 500
4. Slow Loading First Time
Cache is created on first run. Subsequent runs will be fast (2-3 seconds).

🤝 Contributing
Fork the repository

Create feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add some AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is for educational purposes. Quranic text and translations are from public sources.

🙏 Acknowledgments
Al-Quran Cloud API for Quran data

Groq for LLM services

LangChain for RAG framework

Streamlit for web interface

📬 Contact
Email: uafzalk@gmail.com
LinkedIn: www.LinkedIn.com/In/UmerAfzalKhan

⭐ Star Us!
If you found this project useful, please give it a star! 🌟

<div align="center"> Made with ❤️ using Python, Streamlit, and Groq </div> ```