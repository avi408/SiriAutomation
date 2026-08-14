import time


class SiriService:

    def __init__(self, driver):
        self.driver = driver

    def activate(self):
        """Prepare Siri for interaction."""
        print("Preparing Siri...")
        time.sleep(1)

    def ask_question(self, question):
        """Ask Siri a question and capture the response."""

        print(f"Asking Siri: {question}")

        self.driver.execute_script(
            "mobile: siriCommand",
            {
                "text": question
            }
        )

        time.sleep(3)

        return self.get_response()

    def get_response(self):
        print("Reading Siri response...")

        time.sleep(2)

        response = self.driver.page_source

        print("Siri UI captured.")

        return response