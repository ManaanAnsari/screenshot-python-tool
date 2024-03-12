from pynput import mouse
import pyautogui
from helper import read_config, save_config

# Counter for left mouse clicks
left_clicks = 0




def on_click(x, y, button, pressed):
    global left_clicks
    config = read_config()
    print(f"Mouse clicked at ({x}, {y}) with {button} button")
    counter = config.get("counter", 0)
    # Check if the left button is pressed
    if button == mouse.Button.left and pressed:
        left_clicks += 1
        print(f"Left mouse click {left_clicks}")
        
        # If left mouse is clicked 3 times, take a screenshot
        if left_clicks == 3:
            screenshot = pyautogui.screenshot()
            screenshot.save(config["path"]+str(counter)+'.png')
            print("Screenshot taken and saved as 'screenshot.png'")
            left_clicks = 0  # Reset counter after taking a screenshot
            counter += 1
            config["counter"] = counter
            save_config(config)
            
# Set up mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
