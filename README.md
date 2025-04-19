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
│   ├── services/
│   │   ├── prompts/        # Prompt templates (system/user)
│   │   └── ...
│   └── ...
├── frontend/               # React + Vite frontend
│   ├── src/                # React source code
│   └── ...
├── config.py
├── requirements.txt
├── README.md
└── ...
```

- **Prompts:** are now in `backend/services/prompts/`
- **Input transcripts:** (if using CLI) go in `input_transcripts/`
- **Generated posts:** (if using CLI) go in `generated_posts/`

---

## 📂 Usage (CLI, optional)

If you want to use the Python CLI for batch processing:

1. Download `.srt` subtitle files (see below)
2. Place them in:

```
input_transcripts/
```

3. Run the generator:

```bash
python main.py
```

This will:
- Clean the title using LLM
- Rename the `.srt` file based on the cleaned title
- Generate a Markdown blog post
- Save it to:

```
generated_posts/<Recipe Title>/<Title> - YYYY-MM-DD.md
```

---

## 📥 How to Download `.srt` Files from YouTube

Use [https://downsub.com](https://downsub.com):

1. Paste the YouTube link
2. Click **Download**
3. Save the `.srt` file
4. Drop it in `input_transcripts/`

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

## 🧪 Notes

- Already-processed `.srt` files are skipped unless deleted
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
