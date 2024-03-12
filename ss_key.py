from pynput import keyboard
import pyautogui
import datetime
from helper import read_config, save_config


current_keys = set()

def on_press(key):
    try:
        # For readability, convert special keys to a readable format
        if key == keyboard.Key.cmd:
            current_keys.add("cmd")
        else:
            # Standard alphanumeric keys
            key_char = key.char
            current_keys.add(key_char)
    except AttributeError:
        # Special keys (like space, ctrl, etc.) can cause an AttributeError when accessing char
        pass
    
    # Check if the user has pressed Cmd + X
    if "cmd" in current_keys and "x" in current_keys:
        config = read_config()
        counter = config.get("counter", 0)
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        # Save the screenshot with a timestamp
        # filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
        filename = config["path"]+str(counter)+'.png'
        screenshot.save(filename)
        print(f"Screenshot taken and saved as {filename}")
        counter += 1
        config["counter"] = counter
        save_config(config)

def on_release(key):
    try:
        # Remove keys from the current set on release
        if key == keyboard.Key.cmd:
            current_keys.remove("cmd")
        else:
            key_char = key.char
            current_keys.remove(key_char)
    except KeyError:
        # Ignore if the key isn't in the set
        pass
    except AttributeError:
        # This could happen with special keys
        pass

# Listen for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
