# 🧠 ClipGPT – GPT at Your Fingertips

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)

✨ **ClipGPT** is a lightweight Python utility that allows you to query OpenAI's GPT model using a keyboard shortcut. It instantly grabs the selected text from your screen (via clipboard), sends it to GPT-4o (or any other model you choose) with a configurable system prompt, and copies the answer back to your clipboard. Designed for speed and simplicity, ClipGPT is perfect for students, researchers, or anyone who frequently works with multiple-choice questions.

---

## 🚀 Features

- ⚡ Instant GPT Answers with one keyboard shortcut
- 📋 Clipboard Integration – auto-copies selected text and the result
- 🎛️ Customizable Prompts and Models – change the topic, prompt style, and model
- 🛠️ Minimal Setup – install dependencies, set your API key, and go
- 🎹 Hotkey Binding – `Ctrl+Alt+D` to trigger, `Esc` to exit
- 🧩 Modular Design – easily extend or integrate into your own workflows

---

## 💡 Example Use Case

Set your topic to `cybersecurity`:

```python
TOPIC = "cybersecurity"
```

Then copy a multiple-choice question like:

> Which of the following is a passive reconnaissance technique?
>
> A) SQL Injection  
> B) Dumpster Diving  
> C) Banner Grabbing  
> D) Social Engineering

Press `Ctrl+Alt+D` ➜ Clipboard will be updated with the correct option: `C) Banner Grabbing`

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/clipgpt.git
cd clipgpt
```

2. **Create and activate a virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API key**
Create a `.env` file:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Or export it temporarily:
```bash
export OPENAI_API_KEY=sk-xxxx   # Windows: set OPENAI_API_KEY=sk-xxxx
```

5. **Run the tool**
```bash
python clipgpt.py
```

---

## ⌨️ Keyboard Shortcuts

| Action                | Shortcut         |
|-----------------------|------------------|
| Query selected text   | `Ctrl + Alt + D` |
| Exit script           | `Esc`            |

---

## 🛠️ Configuration

ClipGPT is designed to be flexible and customizable:

### 🧩 Change the Topic
Set your desired subject area:
```python
TOPIC = "biology"  # or math, physics, cars, etc.
```

### 🧠 Change the System Prompt
```python
SYSTEM_PROMPT = f"Multiple choice test based on {TOPIC}, give me just the correct option"
```
Want full explanations?
```python
SYSTEM_PROMPT = f"Multiple choice test based on {TOPIC}, explain the correct answer briefly"
```

### 🤖 Change the Model
```python
response = openai.chat.completions.create(
    model="gpt-4o",  # change to gpt-3.5-turbo, gpt-4, etc.
```
> Make sure your OpenAI account has access to the model you choose.

---

## 📂 File Structure

```
clipgpt/
├── clipgpt.py         # Main script
├── requirements.txt   # Python dependencies
├── .env.sample        # Sample environment config
└── README.md          # You're here
```
---

## 📚 References

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [pyperclip Docs](https://pyperclip.readthedocs.io/en/latest/)
- [keyboard Library](https://keyboard.readthedocs.io/en/latest/)
- [pynput Library](https://pynput.readthedocs.io/en/latest/)

---

## 🙌 Credits

Crafted by [@chiraanth](https://github.com/chiraanth) – built to scratch the itch of answering MCQs fast using AI.

If you found this useful, drop a ⭐ and share it with your friends!

