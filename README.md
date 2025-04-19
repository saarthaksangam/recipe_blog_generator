# 🍳 Video Subtitles to Recipe Blog Generator

A lightweight tool that automatically generates clean, structured Markdown recipe blog posts from `.srt` video
transcripts using OpenAI’s GPT-4.1 API.

Originally built for the food blog [**Platin' It with Wendy**](https://www.youtube.com/@PlatinItWithWendy), this project
is adaptable for any cooking or content creation workflow that starts with spoken video transcripts.

---

## 🚀 Features

- 🧠 Converts transcripts into warm, engaging recipe blog posts using GPT-4.1
- ✍️ Uses OpenAI's chat format with separate **system** and **user** prompts
- 📄 Markdown-based template files (no prompt logic in code!)
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

---

## 🔐 Environment Setup

Create a `.env` file in the root of the repo:

```bash
touch .env
```

Add your OpenAI API key:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🔑 How to Get an OpenAI API Key

1. Sign up at https://platform.openai.com/signup
2. Add a billing method: https://platform.openai.com/account/billing
3. Generate your key: https://platform.openai.com/api-keys
4. Paste the key into your `.env` file

💡 You only see the key once — copy it somewhere safe!

---

## 💰 Cost Estimate

GPT-4.1 pricing as of April 2025:

| Model   | Input (1M tokens) | Output (1M tokens) |
|---------|------------------:|-------------------:|
| GPT-4.1 |             $2.00 |              $8.00 |

1,000 tokens ≈ 750 words.  
Each blog post costs ~**$0.06 to $0.12** depending on transcript length.

---

## 📂 Usage

1. Download `.srt` subtitle files (see below)
2. Place them in:

```
recipe_blog_generator/input_transcripts/
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
recipe_blog_generator/generated_posts/<Recipe Title>/<Title> - YYYY-MM-DD.md
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
recipe_blog_generator/generator/prompts/
├── system/
│   ├── recipe_prompt.md
│   └── title_prompt.md
├── user/
│   ├── recipe_prompt.md
│   └── title_prompt.md
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
