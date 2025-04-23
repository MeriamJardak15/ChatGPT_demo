# 💬 MiniChat – Flask Chatbot with OpenAI GPT

MiniChat is a lightweight web application built with Flask that integrates OpenAI's GPT-3.5-turbo API to generate intelligent responses to user queries. The application allows users to submit questions through a web interface and receive dynamic, AI-generated replies in real time.

## 🚀 Features

- Simple and clean Flask backend.
- Uses OpenAI GPT-3.5-turbo via `openai.ChatCompletion`.
- Renders responses in a user-friendly HTML interface.
- Handles 404 errors with a custom page.
- Secure API key configuration using environment-based settings.

## 🗂️ Project Structure

```
.
├── app.py             # Main Flask application
├── aiapi.py           # Handles OpenAI API interaction
├── config.py          # Configuration management
├── templates/
│   ├── index.html     # Homepage template
│   └── 404.html       # Custom 404 error page
```

## 🧠 How It Works

1. Users access the homepage served by Flask (`index.html`).
2. They enter a question and submit the form.
3. The Flask backend sends the question to the OpenAI API via `aiapi.generateChatResponse`.
4. The response is returned in JSON format and rendered on the page.

## ⚙️ Configuration

The API key and other settings are managed in `config.py`. Here's an example:

```python
class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = "your-openai-key-here"
```

> 🔐 **Important**: Never expose your API keys in public repositories. Use environment variables or a `.env` file in production.

## 🧪 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/minichat-flask.git
cd minichat-flask
```

### 2. Install dependencies

```bash
pip install flask openai
```

### 3. Set your OpenAI API key

Edit `config.py` or use an environment variable setup.

### 4. Run the app

```bash
python app.py
```

The app will be accessible at: `http://localhost:8888/`

## 🧩 Requirements

- Python 3.7+
- Flask
- OpenAI Python SDK
