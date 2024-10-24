import logging
import colorama

colorama.init()


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': colorama.Fore.BLUE,
        'INFO': colorama.Fore.GREEN,
        'WARNING': colorama.Fore.YELLOW,
        'ERROR': colorama.Fore.RED,
        'CRITICAL': colorama.Fore.RED + colorama.Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, colorama.Fore.WHITE)
        message = super().format(record)
        return f"{log_color}{message}{colorama.Style.RESET_ALL}"


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)