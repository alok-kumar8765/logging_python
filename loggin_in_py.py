# ==============================
# PYTHON SNIPPETS
# HOW TO DO LOGGING IN PYTHON
# ==============================

import logging

logger=logging.getLogger(____name___)

logger.setLevel (logging.DEBUG)
logger.propagate = False # avoid duplicate logs via root logger

if not logger.handlers: # prevent duplicate handlers on re-import Logging.Formatter(
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
file_handler = logging.FileHandler("sample.log", encoding="utf-8")
file_handler.setLevel(logging.ERROR)    # only ERROR+ to file
file_handler.setFormatter (formatter)

stream_handler = logging.StreamHandler() 
stream_handler.setLevel(logging.INFO)   # INFO+ to console
stream_handler.setFormatter (formatter)

logger.addHandler(file_handler) 
logger.addHandler(stream_handler)
