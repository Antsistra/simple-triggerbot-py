import cv2
import pyautogui
import numpy as np
from PIL import ImageGrab

def is_cursor_in_circle(cursor_pos, circle_center, radius):

    distance = np.sqrt((cursor_pos[0] - circle_center[0])**2 + (cursor_pos[1] - circle_center[1])**2)
    return distance <= radius

def main():
    radius = 30  

    template = cv2.imread('asset.png', cv2.IMREAD_UNCHANGED)
    if template is None:
        print("Template image not found.")
        return
    
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    
    while True:
  
        screen = np.array(ImageGrab.grab())
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        
    
        res = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 1  
        loc = np.where(res >= threshold)
        
        detected_circles = False
        
        for pt in zip(*loc[::-1]):
            detected_circles = True
            circle_center = (pt[0] + w//2, pt[1] + h//2)
            cursor_pos = pyautogui.position()
            if is_cursor_in_circle(cursor_pos, circle_center, radius):
                print(f"Cursor is inside the circle at {circle_center}. Clicking...")
                pyautogui.press('u') 
                break
        
        if not detected_circles:
            print("No circles detected.")
    
        for pt in zip(*loc[::-1]):
            circle_center = (pt[0] + w//2, pt[1] + h//2)
            cv2.circle(screen, circle_center, radius, (0, 255, 0), 2)
        
        cv2.imshow('Screen', screen)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
