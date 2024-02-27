def spacebars_only(text: str) -> bool:
    """Check if a string contains only spaces"""
    t = text.strip()
    return (len(t)>0)


a = "         "
b = "Hello World!"

print(spacebars_only(a))
print(spacebars_only(b))