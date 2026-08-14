import time


class SiriService:

    def __init__(self, driver):
        self.driver = driver

    def activate(self):
        print("Launching Siri...")

        self.driver.execute_script(
            "mobile: siriCommand",
            {
                "text": ""
            }
        )

        time.sleep(2)

    def ask_question(self, question):
        print(f"Asking Siri: {question}")

        self.driver.execute_script(
            "mobile: siriCommand",
            {
                "text": question
            }
        )

        time.sleep(3)

        response = self.get_response()

        print("========== SIRI RESPONSE ==========")
        print(response)
        print("====================================")

        return response

    def get_response(self):
        print("Reading Siri response...")

        time.sleep(2)

        page_source = self.driver.page_source

        print("Siri UI captured.")

        return page_source