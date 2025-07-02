import pyautogui
import time
import random

def move_cursor_randomly(interval=10):
    print("Auto Cursor Mover Started. Press Ctrl+C to stop.")
    try:
        while True:
            # Generate random screen coordinates
            x = random.randint(100, 500)
            y = random.randint(100, 500)
            
            # Move the cursor
            pyautogui.moveTo(x, y, duration=0.5)
            print(f"Moved to ({x}, {y})")
            
            # Wait for the next move
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nCursor movement stopped.")

if __name__ == "__main__":
    move_cursor_randomly(interval=10)
