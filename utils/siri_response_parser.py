class SiriResponseParser:

    @staticmethod
    def contains_weather_response(response):
        if not response:
            return False

        response = response.lower()

        weather_keywords = [
            "weather",
            "temperature",
            "degrees",
            "forecast",
            "sunny",
            "cloudy",
            "rain",
            "wind"
        ]

        return any(keyword in response for keyword in weather_keywords)