from pathlib import Path
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, name):

        directory = Path("screenshots")
        directory.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = directory / f"{name}_{timestamp}.png"

        driver.save_screenshot(str(filename))

        return filename