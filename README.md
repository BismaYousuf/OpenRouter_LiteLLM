# 🤖 Bisma's AI Agent Playground

Today, I learned how to use **OpenRouter** and **LiteLLM** to create intelligent agents using the `openai-agents` framework. Say hello to `Bisma_Agent`! 💬✨

---

## 🌐 OpenRouter Integration

With OpenRouter, I used the `deepseek-chat` model to power an assistant that can understand and respond intelligently.

🔑 Make sure you have your `OPENROUTER_API_KEY` stored safely in a `.env` file.

📂 Code is in: `app.py`

---

## ⚡ LiteLLM + Gemini Integration

I also experimented with **LiteLLM** to use Google's Gemini model through the same agent structure.

🔑 Use your `GEMINI_API_KEY` in the `.env` file.

📂 Code is in: `main.py`

💡 Tip: Don't forget to install support with:
```bash
uv pip install "openai-agents[litellm]"
🔐 Environment Setup
Create a .env file in your root directory with:

env
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key
GEMINI_API_KEY=your_gemini_api_key
🧠 What I Learned
Loading API keys securely with dotenv

Using different models with the same agent structure

Understanding the difference between OpenRouter and LiteLLM as model providers

Running agents synchronously using Runner.run_sync

🛠️ Requirements
Python 3.10+

openai-agents package

uv or pip for installing packages

.env file with your API keys

🧪 Output Sample
Each agent replies to:

"I am Bisma, Who are You?"

With a helpful and friendly AI-generated response. 🧸

