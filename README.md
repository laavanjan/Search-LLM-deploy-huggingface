
# 🔎 Search-LLM-Deploy-HuggingFace


![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-brightgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Groq API](https://img.shields.io/badge/Groq-API-purple)
![Hugging Face Space](https://img.shields.io/badge/HuggingFace-Space-blue)

A chatbot that leverages Large Language Models (LLMs) to perform real-time web searches using LangChain, Groq API, and various search tools. This project is deployed on **Hugging Face Spaces**.

## 🚀 Live Demo

Try the chatbot here: **[Search Engine LLM](https://huggingface.co/spaces/Laavanjan/Search_Engine_llm)**

## 🛠 Features

- 🌐 **Web Search**: Retrieves up-to-date information from the web using DuckDuckGo.
- 📚 **Arxiv & Wikipedia Support**: Fetches relevant academic papers and Wikipedia summaries.
- 🤖 **LLM-Powered Responses**: Uses Groq's `qwen-2.5-32b` model for intelligent responses.
- 🔄 **Chat History**: Maintains session history for a better user experience.
- 📊 **LangSmith Tracing**: Enables tracking and debugging of LangChain interactions.
- 📂 **Deployed on Hugging Face Spaces**: Easily accessible without setup.

## 🏗️ Tech Stack

- **Python** 🐍
- **Streamlit** 🎈
- **LangChain & LangSmith** 🔗
- **Groq API** 🚀
- **DuckDuckGo Search API** 🔎
- **Arxiv & Wikipedia API** 📖

## 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/laavanjan/Search-LLM-deploy-huggingface.git
   cd Search-LLM-deploy-huggingface
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file and add your API keys:

   ```bash
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_PROJECT="Chatbot with webSearch"
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## 🖼️ Demo Images

*(Screenshots of the chatbot in action will be added here)*

## 📝 License

This project is licensed under the **GPL License**.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, make changes, and submit a pull request.

---

⭐ **Star this repo** if you find it useful!
