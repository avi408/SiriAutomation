from pages.base_page import BasePage
from locators.siri_locators import SiriLocators


class SiriPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_microphone(self):
        self.click(SiriLocators.MICROPHONE_BUTTON)

    def enter_question(self, question):
        self.enter_text(
            SiriLocators.TEXT_INPUT,
            question
        )

    def get_response(self):
        return self.get_text(
            SiriLocators.RESPONSE_TEXT
        )

    def activate(self):
        print("Launching Siri...")

    def ask(self, question):
        print(f"Asking Siri: {question}")

    def response(self):
        return None