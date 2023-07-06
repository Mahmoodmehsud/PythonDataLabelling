import time
import json
from pynput.mouse import Listener
from PIL import ImageGrab, Image

screenshot_counter = 0
pixels_threshold = 40  # Number of pixels to move before taking a screenshot
pixels_moved = 0
captured_data=[]


def save_data_to_json():
    global captured_data
    with open("MetaData.json", "w") as file:
        json.dump(captured_data, file)


def on_move(x, y):
    global screenshot_counter, pixels_moved,TS,captured_data


    pixels_moved += 1

    if pixels_moved >= pixels_threshold:
        pixels_moved = 0
        print("Mouse moved to ({0}, {1})".format(x, y))
        screenshot = ImageGrab.grab()
        TS = time.time()
        print(TS)
        cursor_image = Image.open("Cursor.png")  # Replace "cursor.png" with the path to your cursor image
        cursor_position = (x - cursor_image.width // 2, y - cursor_image.height // 2)
        screenshot.paste(cursor_image, cursor_position, cursor_image)
        screenshot.save(f"screenshot_{screenshot_counter}.png")
        captured_data.append ({
                        "ts": TS,
                        "x_Pos": x,
                        "y_Pos": y,
                        "img_name": ""f"screenshot_{screenshot_counter}"
                    })
        save_data_to_json()

        screenshot_counter += 1
        print(screenshot_counter)


def on_click(x, y, button, pressed):
    global screenshot_counter, pixels_moved
    print('Mouse clicked at ({0}, {1}) with {2}, {3}'.format(x, y, button, pressed))
    screenshot = ImageGrab.grab()
    TS=time.time()
    print(TS)
    cursor_image = Image.open("Cursor.png")  # Replace "cursor.png" with the path to your cursor image
    cursor_position = (x - cursor_image.width // 2, y - cursor_image.height // 2)
    screenshot.paste(cursor_image, cursor_position, cursor_image)
    screenshot.save(f"screenshot_{screenshot_counter}.png")
    captured_data.append ({
                        "ts": TS,
                        "x_Pos": x,
                        "y_Pos": y,
                        "Mouse_Button": "{0}".format(button),
                        "pressed": pressed,
                        "img_name": ""f"screenshot_{screenshot_counter}"
                    })
    save_data_to_json()
    
    screenshot_counter += 1
    print(screenshot_counter)
    

def on_scroll(x, y, dx, dy):
    global screenshot_counter, pixels_moved
    
    print('Mouse moved to ({0}, {1}) and scrolled to {2}, {3}'.format(x, y, dx, dy))
    screenshot = ImageGrab.grab()
    TS= time.time()
    print(TS)
    cursor_image = Image.open("Cursor.png")  # Replace "cursor.png" with the path to your cursor image
    cursor_position = (x - cursor_image.width // 2, y - cursor_image.height // 2)
    screenshot.paste(cursor_image, cursor_position, cursor_image)
    screenshot.save(f"screenshot_{screenshot_counter}.png")
    captured_data.append ({
                        "ts": TS,
                        "x_Pos": x,
                        "y_Pos": y,
                        "scroll_state":'Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)),
                        "img_name": ""f"screenshot_{screenshot_counter}"
                    })
    save_data_to_json()
    
    screenshot_counter += 1
    print(screenshot_counter)

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()