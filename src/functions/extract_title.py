def extract_title(markdown):
# It should pull the h1 header from the markdown file (the line that starts with a single "#") and return it.
    if not isinstance(markdown, str):
        raise TypeError("extract_title requires str input")
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")
    raise Exception("h1 header not found")