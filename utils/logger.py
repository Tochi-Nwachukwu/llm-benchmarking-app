class Logger:
    def __init__(self):
        pass

    def log(self, component_name, message):
        print(f"[{component_name}] : -  {message}")

    def err(self, component_name, error_message):
        print(f"[{component_name}] : -  {error_message}")
