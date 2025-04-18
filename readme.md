# 🍳 Video Subtitles to Recipe Blog Generator

A lightweight tool that automatically generates clean, structured Markdown recipe blog posts from `.srt` video transcripts using OpenAI’s GPT-4.1 API.  

Originally built for the food blog [**Platin' It with Wendy**](https://www.youtube.com/@PlatinItWithWendy), this project is adaptable for any cooking or content creation workflow that starts with spoken video transcripts.

---

## 🚀 Features

- 🧠 Converts transcripts into warm, engaging recipe blog posts using GPT-4.1  
- 📝 Outputs structured Markdown (title, intro, ingredients, steps, sign-off)  
- 📂 Organizes blog posts by recipe title and creation date  
- 🔐 Uses a `.env` file to securely load your OpenAI API key

---

## 📦 Requirements

- Python **3.10 or higher**
- An OpenAI API key (requires a paid OpenAI account)

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

## 🔑 How to Get an OpenAI API Key (Paid Account Required)

1. Sign up at [platform.openai.com/signup](https://platform.openai.com/signup)  
2. Set up billing: [platform.openai.com/account/billing](https://platform.openai.com/account/billing)  
   - You'll need to add a credit card (OpenAI charges per usage)
3. Generate your key: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)  
4. Paste the key into your `.env` file

> 💡 **You will only see the key once**, so copy it and store it safely.

### 💸 How Much Does It Cost?

As of April 2025, OpenAI charges the following for GPT-4.1 API usage:

| Model     | Input (1M tokens) | Output (1M tokens) |
|-----------|------------------:|-------------------:|
| GPT-4.1   | $2.00             | $8.00              |

#### 🧠 What is a Token?

- 1,000 tokens ≈ 750 words (about 4–5 paragraphs)
- Each blog post generation typically uses **1,000–1,500 tokens total**
- Estimated cost: **~$0.06 to $0.12 per recipe**

> 💡 You are billed based on both input and output tokens.

---

## 📂 Usage

1. Download `.srt` subtitle files for your videos (see below)  
2. Drop them into the `input_transcripts/` folder:

```
recipe_blog_generator/input_transcripts/
```

3. Run the blog generator:

```bash
python main.py
```

This will:
- Process all new `.srt` files
- Skip any already processed
- Save Markdown blog posts to:

```
recipe_blog_generator/generated_posts/<Recipe Title>/<Title> - YYYY-MM-DD.md
```

---

## 📥 How to Download `.srt` Subtitle Files from YouTube

You can extract subtitles from any YouTube video like this:

1. Go to [https://downsub.com](https://downsub.com)
2. Paste the YouTube video link
3. Click **Download**
4. Download the `.srt` subtitle file (not `.txt` or `.vtt`)
5. Drop it into `input_transcripts/` and you're good to go!

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

- The script treats `recipe_blog_generator` as the root
- Blog posts are written using GPT-4.1
- Already-generated posts are skipped unless deleted

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

Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)  
✅ Be sure to check **"Add Python to PATH"** during install.

---

## 🤝 Contributing

Pull requests welcome!  
Feel free to open issues for bugs, feature requests, or ideas to expand this tool.

---

## 📜 License

MIT License © Saarthak Sangamnerkar

---
