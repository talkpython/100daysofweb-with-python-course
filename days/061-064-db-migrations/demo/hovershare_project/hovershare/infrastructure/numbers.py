def try_int(text: str, default=-1) -> int:
    try:
        return int(text)
    except:
        return default
