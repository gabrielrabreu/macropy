import pyautogui
import pytesseract
from typing import Tuple
from PIL import Image
from PIL.ImagePath import Path

from .models import Box


class ScreenVerifier:
    @staticmethod
    def size() -> str:
        screen_size = pyautogui.size()
        return f"{screen_size.width}x{screen_size.height}"

    @staticmethod
    def image_in_screen(target_image_path: Path) -> Box | None:
        target_image = Image.open(target_image_path)
        image_location = pyautogui.locateOnScreen(target_image, 5, grayscale=True)
        if image_location is None:
            return None
        return Box(image_location.left, image_location.top, image_location.width, image_location.height)

    @staticmethod
    def get_screen_text(region: Tuple[int, int, int, int] | None) -> str | None:
        screenshot = pyautogui.screenshot()
        if region:
            screenshot = screenshot.crop(region)
        text = pytesseract.image_to_string(screenshot)
        return text
