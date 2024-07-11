# Simple Trigger Bot

This project contains a Trigger Bot script written in
Python. The script detects a template image on the screen
and simulates a key press when the mouse cursor is within a
specified radius of the detected template.

## Packages

- OpenCV
- pyautogui
- numpy
- Pillow

## How To Run

- instal packages

```bash
pip install opencv-python pyautogui numpy Pillow
```

- Replace the assets image
- Change radius and pyautogui.press
- Press Q to exit

## How It Works

```bash
1. The script loads a template image asset.png.
2. It captures the screen continuously.
3. It performs template matching to find the template image on the screen.
4. If the cursor is within a specified radius of the detected template, the script simulates pressing the 'u' key.
5. The script displays the screen capture with circles drawn around detected template positions for debugging purposes.
6. The script exits when the 'q' key is pressed.
```

## Configuration

- radius : The radius of the target used to detect if the
  cursor is within the target area. You may need to adjust
  this value depending on your requirements.

- threshold : The threshold value for template matching.
  Adjust this value to improve detection accuracy.

## Notes

- Ensure the template image asset.png is correctly placed in
  the same directory as the script.
- The script uses the ImageGrab module, which may not work
  on all systems. Consider using alternative screen capture
  methods if you encounter issues.

## License

This project is licensed under the MIT License. See the
LICENSE file for details. Feel free to modify the content as
per your needs.
