# 🍳 Video Subtitles to Recipe Blog Generator

A lightweight tool that automatically generates clean, structured Markdown recipe blog posts from `.srt` video transcripts using OpenAI’s GPT-4.1 API.  

Originally built for the food blog **Platin' It with Wendy**, this project is adaptable for any cooking or content creation workflow that starts with spoken video transcripts.

---

## 🚀 Features

- 🧠 Converts transcripts into warm, engaging recipe blog posts using GPT-4.1  
- 📝 Outputs structured Markdown (title, intro, ingredients, steps, sign-off)  
- 📂 Organizes blog posts by recipe title and creation date  
- 🔐 Uses a `.env` file to securely load your OpenAI API key

---

## 📦 Requirements

- Python **3.10 or higher**
- An OpenAI API key

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/recipe_blog_generator.git
cd recipe_blog_generator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> ✅ The `requirements.txt` only includes packages explicitly installed (e.g. `openai`, `python-dotenv`).

---

## 🔐 Environment Setup

Create a `.env` file in the root of the repo:

```bash
touch .env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 📂 Usage

1. Drop `.srt` transcript files into:

```
recipe_blog_generator/transcripts/
```

2. Run the generator:

```bash
python main.py
```

This will:
- Process all unconverted `.srt` files
- Skip those already processed
- Save blog posts to:

```
recipe_blog_generator/blog_posts/<Recipe Title>/<Title> - YYYY-MM-DD.md
```

---

## ✨ Example Output

```markdown
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

- The script treats `recipe_blog_generator` as the project root
- Blog posts are generated via GPT-4.1
- Duplicate outputs are skipped unless deleted manually

---

## 🐍 Don't Have Python 3.10+?

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

Download from [python.org](https://www.python.org/downloads/)  
Be sure to check **"Add Python to PATH"** during install

---

## 🤝 Contributing

Pull requests welcome!
Feel free to open issues for bugs or feature requests.
---

## 📜 License

MIT License © Saarthak Sangamnerkar

---

