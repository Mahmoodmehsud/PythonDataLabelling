x = 0
y = 0
Dict = {
 "Info":{
    "os": "windows",
    "application": "desktop application",
    "task": "text bold",
  },
  "0": {
    "mouse": {
      "position": [x,y],
      "left_click": "false",
      "right_click": "false",
      "scroll": ""
    },
    "keyboard": {
      "key_pressed": []
    },
    "image": "image_name.png"
  },
  "1": {
    "mouse": {
      "position": [x,y],
      "left_click": "true",
      "right_click": "false",
      "scroll": "up/down"
    },
    "keyboard": {
      "key_pressed": ["ctrl + b"]
    },
    "image": "image_name.png"
  }
}
print(Dict)