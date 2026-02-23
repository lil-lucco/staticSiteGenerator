# Static Site Generator (Python)

A lightweight static site generator built in Python that converts Markdown content into a fully static HTML site.

This project was built as part of the Boot.dev static site generator course and includes:
- Markdown parsing into HTML nodes
- Recursive page generation from `content/` into `docs/`
- Static asset copying from `static/` into `docs/`
- Unit tests for parser and generation behavior

## Tech Stack

- Python 3
- Standard library only (`pathlib`, `shutil`, `unittest`)

## Project Structure

```text
10_site_generator/
├── content/        # Markdown source files
├── static/         # CSS + images copied as-is
├── docs/           # Generated site output
├── src/
│   ├── main.py     # Build entry point
│   ├── functions/  # Generation and parsing functions
│   ├── nodes_and_blocks/
│   └── tests/      # Unit tests
├── template.html   # HTML template for generated pages
├── build.sh        # Build with production-style base path
└── test.sh         # Run unit tests
```

## Features

Supported Markdown block types:
- Headings (`#` through `######`)
- Paragraphs
- Blockquotes
- Unordered lists
- Ordered lists
- Fenced code blocks

Supported inline styles:
- Bold (`**text**`)
- Italic (`_text_`)
- Inline code (`` `code` ``)
- Links (`[label](url)`)
- Images (`![alt](url)`)

## How It Works

1. `src/main.py` removes and recreates `docs/`, then copies everything from `static/`.
2. It recursively walks `content/` and converts each `.md` file to a matching `.html` file path in `docs/`.
3. It injects generated HTML and page title into `template.html`.
4. It rewrites absolute asset/content paths (`/`) using a configurable `basepath`.

## Run Locally

From the project root:

```bash
python3 src/main.py
cd docs
python3 -m http.server 8888
```

Then open: `http://localhost:8888`

## Build With Base Path (GitHub Pages style)

```bash
./build.sh
```

Current script builds with:

```text
/staticSiteGenerator/
```

This is useful when hosting the site under a repository subpath.

## Run Tests

```bash
./test.sh
```

## Notes

- Generated files in `docs/` are build artifacts.
- Content edits belong in `content/`; style/assets belong in `static/`.
