# 🍳 Video Subtitles to Recipe Blog Generator

A lightweight tool that automatically generates clean, structured Markdown recipe blog posts from YouTube videos using OpenAI’s GPT-4.1 API.

Originally built for the food blog [**Platin' It with Wendy**](https://www.youtube.com/@PlatinItWithWendy), this project is adaptable for any cooking or content creation workflow that starts with spoken video transcripts.

---

## 🚀 Features

- 🧠 Converts YouTube transcripts into warm, engaging recipe blog posts using GPT-4.1
- ✍️ Uses OpenAI's chat format with separate **system** and **user** prompts
- 📄 Markdown-based template files (no prompt logic in code!)
- 📂 Organizes blog posts by recipe title and creation date
- 🔐 Uses a `.env` file to securely load your OpenAI API key
- 🖥️ Modern React frontend for easy blog generation

---

## 📦 Requirements

- Python **3.10 or higher**
- Node.js **18+** and npm (for frontend)
- An OpenAI API key (requires a paid OpenAI account)

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/recipe_blog_generator.git
cd recipe_blog_generator
```

### 2. Backend Setup (FastAPI)

#### a. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### b. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### c. Environment Setup

Create a `.env` file in the root of the repo:

```bash
touch .env
```

Add your OpenAI API key:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

#### d. Run the Backend API

```bash
cd backend
uvicorn main:app --reload
```

The backend will be available at: [http://localhost:8000](http://localhost:8000)

---

### 3. Frontend Setup (React + Vite)

The React frontend is in the `frontend/` directory.

#### a. Install Node.js dependencies

```bash
cd frontend
npm install
```

#### b. Start the development server

```bash
npm run dev
```

The frontend will be available at: [http://localhost:5173](http://localhost:5173)

---

### 4. Local Development Workflow

- **Start the backend** (see above)
- **Start the frontend** (see above)
- Open [http://localhost:5173](http://localhost:5173) in your browser
- The frontend will communicate with the backend API at [http://localhost:8000](http://localhost:8000)

---

## 📂 Project Structure

```
recipe_blog_generator/
├── backend/                # FastAPI backend (all Python code)
│   ├── main.py             # FastAPI entrypoint
│   ├── agents/             # LLM agent definitions (e.g., blog_agent)
│   ├── clients/            # API clients (OpenAI, etc.)
│   ├── middleware/         # FastAPI middleware (logging, CORS, etc.)
│   ├── router/             # FastAPI route definitions (API endpoints)
│   ├── schemas/            # Pydantic models for API responses
│   ├── services/           # Core business logic and utilities
│   │   ├── llm/            # LLM call wrappers
│   │   ├── prompt_builders/# Functions to build prompt messages
│   │   ├── prompts/        # Prompt templates (system/user)
│   │   ├── tools/          # Tool functions (e.g., generate_blog_from_youtube)
│   │   └── youtube_utils/  # YouTube metadata/subtitle extraction utilities
│   └── utils/              # General-purpose utilities (logging, helpers)
├── frontend/               # React + Vite frontend
│   ├── src/                # React source code
│   └── ...
├── config.py               # Project-wide config (blog name, model, etc.)
├── requirements.txt        # Python dependencies
├── README.md
└── ...
```

### Backend Overview

- **Agents**: The main agent (blog_agent) orchestrates the process of generating a recipe blog post from a YouTube URL. It uses tools to fetch video metadata, transcript, and thumbnail, and then builds prompts for the LLM.
- **Tools**: The backend/services/tools/ directory contains tool functions (e.g., generate_blog_from_youtube) that the agent can call. These tools use the youtube_utils module to extract video details and subtitles.
- **YouTube Utils**: The backend/services/youtube_utils/ folder provides helper functions for extracting the video title, upload date, thumbnail, and transcript using yt-dlp.
- **Prompt Builders & Templates**: Prompt templates (Markdown) live in backend/services/prompts/. Prompt builder functions fill in these templates with video-specific data.
- **API**: The FastAPI backend exposes a /api/v1/generate-blog endpoint that takes a YouTube URL and returns a structured blog post (title, markdown, thumbnail, etc.).

---

## 📂 Usage (CLI, optional)

The CLI entry point (main.py) simply runs the agent and prints the generated blog post to the console. It does not store results or process input/output files.

Example usage:

```bash
python main.py
```

You will be prompted for a YouTube URL, and the generated blog post will be displayed in your terminal.

---

## 🧠 Prompt Structure

All prompts are defined in:

```
backend/services/prompts/
├── system/
│   └── recipe_prompt.md
├── user/
│   └── recipe_prompt.md
```

Prompt builders like `build_recipe_prompt_messages()` return:

- `system_prompt`: defines the assistant's role
- `user_prompt`: provides the actual content scaffold (e.g. Markdown structure + transcript)

These are passed to the OpenAI chat API in a structured format.

---

## ✨ Example Output

```
# Super Creamy Macaroni Salad

> **Posted on April 18, 2025**  
> *Recipes that impress with ease*

## Ingredients
...

## Method
...

Happy cooking,  
Wendy
```

---
## 🖥️ Screenshots
<img width="1185" alt="image" src="https://github.com/user-attachments/assets/31905d99-4e4c-4c03-88bd-59ec75324f17" />
<img width="1107" alt="image" src="https://github.com/user-attachments/assets/0315bce0-93a9-45d7-a802-9848f2277c2b" />
<img width="1071" alt="image" src="https://github.com/user-attachments/assets/18b11299-4bef-4d4b-9443-b9a566c7c7f8" />

---
## 🧪 Notes

- Output is deterministic (controlled by structured prompt templates)
- All LLM logic is modular and role-based (system/user separation)
- Prompt templates can be edited without touching Python code
- The React frontend is the recommended way to use the tool interactively

---

## 🐍 Need Python 3.10+?

Install via:

### macOS

```bash
brew install python@3.11
```

### Ubuntu

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
```

### Windows

Download: https://www.python.org/downloads/  
✅ Check “Add Python to PATH” during install

---

## 🤝 Contributing

Pull requests welcome!  
Feel free to open issues for bugs, features, or feedback.

---

## 📜 License

MIT License © Saarthak Sangamnerkar

---
