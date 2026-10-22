__version__ = "1.0.0"

def greet(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"

def classify_status(code: int) -> str:
    if 200 <= code < 300: return "success"
    if 400 <= code < 500: return "client_error"
    if 500 <= code < 600: return "server_error"
    return "other"
