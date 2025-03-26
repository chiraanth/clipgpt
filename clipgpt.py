import os
import time
import openai
import pyperclip
import keyboard
from pynput.keyboard import Controller

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Configurable topic
TOPIC = "cars"

# Define static system prompt, can be customized
SYSTEM_PROMPT = (
    f"Multiple choice test based on {TOPIC}, give me just the correct option"
)

keyboard_controller = Controller()

def log(msg):
    """Utility for clean logging."""
    print(f"[ClipGPT] {msg}")

def query_chatgpt(prompt):
    """
    Sends a prompt to OpenAI GPT and returns the response.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def copy_selected_text():
    """
    Clears the clipboard, simulates Ctrl+C, and retrieves clipboard contents.
    """
    try:
        pyperclip.copy("")  # Clear clipboard
        time.sleep(0.2)
        keyboard.press_and_release("ctrl+c")

        for attempt in range(5):
            time.sleep(0.5)
            text = pyperclip.paste().strip()
            if text:
                log(f"Copied text: '{text}'")
                return text
            log(f"Retry {attempt + 1}/5: Clipboard not updated yet.")
        return None
    except Exception as e:
        log(f"Clipboard error: {e}")
        return None

def process_text_with_gpt():
    """
    Processes selected text and sends response to clipboard.
    """
    log("Hotkey triggered!")
    selected_text = copy_selected_text()

    if not selected_text:
        log("No text copied.")
        return

    log("Querying GPT...")
    response = query_chatgpt(selected_text)

    if response.startswith("Error:"):
        log(response)
    else:
        pyperclip.copy(response)
        log("Response copied to clipboard!")

def main():
    log("ClipGPT is running.")
    log("Press Ctrl+Alt+D to use. Press Esc to exit.")
    keyboard.add_hotkey("ctrl+alt+d", process_text_with_gpt)
    keyboard.add_hotkey("esc", lambda: exit("[ClipGPT] Exiting..."))

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        log("Exiting...")

if __name__ == "__main__":
    main()
