from config.settings import Settings

Settings.validate()

print("Configuration Loaded Successfully")

print(Settings.get("device"))

print(Settings.get("device", "deviceName"))