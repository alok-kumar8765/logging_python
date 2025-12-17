# logging_python

This code is about **setting up structured logging in Python** using the built-in `logging` module.
Its goal is to **control where log messages go, how detailed they are, and how they look**.

I’ll explain **what it does**, **what it can do**, and **what’s slightly wrong in the snippet**.

---

## 1️⃣ What this code is about (in simple terms)

It creates a **custom logger** that:

* Logs messages with timestamps and metadata
* Sends **INFO and above** messages to the **console**
* Sends **ERROR and above** messages to a **log file**
* Avoids **duplicate log messages**
* Uses a **consistent log format**

This is commonly used in **real applications**, not just small scripts.

---

## 2️⃣ What each part does

### Import logging module

```python
import logging
```

Python’s built-in logging system (no extra installation needed).

---

### Create a logger

```python
logger = logging.getLogger(__name__)
```

* Creates a **named logger**
* `__name__` means:

  * If this is in `main.py`, the logger name is `"main"`
  * If imported as a module, the name matches the module path

✅ Best practice for libraries and applications.

⚠️ **Bug in the code**
I wrote:

```python
____name___
```

Correct version:

```python
__name__
```

---

### Set the logger level

```python
logger.setLevel(logging.DEBUG)
```

* The logger **accepts all messages from DEBUG and above**
* Filtering happens later at the handler level

Levels (low → high):

```
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

### Prevent duplicate logs

```python
logger.propagate = False
```

* Stops logs from being passed to the **root logger**
* Prevents the same message from appearing twice

---

### Prevent duplicate handlers

```python
if not logger.handlers:
```

* Important when files are imported multiple times
* Without this, every import adds new handlers → duplicated output

---

### Define log format

```python
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
```

Example output:

```
2025-12-17 14:22:01 | ERROR | mymodule | File not found
```

---

## 3️⃣ Handlers (where logs go)

### File handler (ERROR+)

```python
file_handler = logging.FileHandler("sample.log", encoding="utf-8")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
```

- ✔ Writes logs to `sample.log`
- ✔ Only logs **ERROR and CRITICAL**

---

### Console handler (INFO+)

```python
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
```

- ✔ Prints logs to the terminal
- ✔ Shows **INFO, WARNING, ERROR, CRITICAL**

---

### Attach handlers to logger

```python
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
```

Now the logger knows **where to send messages**.

---

## 4️⃣ What this logger can do (example)

```python
logger.debug("Debugging info")
logger.info("App started")
logger.warning("Low disk space")
logger.error("Failed to connect to DB")
```

### Console output:

```
INFO | App started
WARNING | Low disk space
ERROR | Failed to connect to DB
```

### sample.log file:

```
ERROR | Failed to connect to DB
```

---

## 5️⃣ What this code is useful for

✅ Production applications
✅ Backend services
✅ Debugging issues
✅ Keeping audit trails
✅ Separating user output from error logs

---

## 6️⃣ Fixed & cleaned-up version (recommended)

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler("sample.log", encoding="utf-8")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
```

---

