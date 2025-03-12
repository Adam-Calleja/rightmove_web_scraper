from datetime import datetime

class Logger:

    def __init__(self, log_file: str) -> None:
        if log_file:
            self.log_file = log_file
        else:
            self.log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    def log_info(self, message: str) -> None:
        with open(self.log_file, "a") as file:
            file.write(f"[INFO] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

    def log_warning(self, message: str) -> None:
        with open(self.log_file, "a") as file:
            file.write(f"[WARNING] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

    def log_error(self, message: str) -> None:
        with open(self.log_file, "a") as file:
            file.write(f"[ERROR] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

    def log_debug(self, message: str) -> None:
        with open(self.log_file, "a") as file:
            file.write(f"[DEBUG] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
