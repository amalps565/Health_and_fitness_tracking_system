import logging

from flask import g, has_request_context


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.request_id = getattr(g, "request_id", "")
        else:
            record.request_id = ""
        return super().format(record)


def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = RequestFormatter("%(asctime)s - %(name)s - %(levelname)s - [%(request_id)s] - %(message)s")
    # Check if handler already exists to avoid duplicate logs
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
