import pyautogui


def isImageOnScreen(image_path):
    image = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=0.75)
    return image
