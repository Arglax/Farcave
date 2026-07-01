# Contributing

Thank you for your interest in contributing to Farcave.

Whether you're fixing bugs, improving code quality, or writing new chapters, your help is appreciated.

---

## Before You Start

Please open an Issue before beginning large features or story additions. This helps avoid duplicated work and ensures new content fits the project's direction.

---

## Code Style

* Follow existing naming conventions.
* Keep functions focused and readable.
* Write clear comments only where necessary.
* Preserve the existing formatting style.

---

## Chapter Structure

All chapters belong inside:

```text
chapters/
```

Each chapter should define:

```python
CHAPTER_INFO = {
    "id": 0,
    "title": "Chapter X: Title",
    "version": "1.0.0",
    "author": "Your Name",
}
```

and implement:

```python
def inject_scenes():
```

to register all chapter scenes.

Please use the official chapter template included with the project.

---

## Writing Guidelines

Narrative should be:

* concise
* atmospheric
* choice-driven
* consistent with the existing tone

Avoid unnecessary exposition or modern slang unless contextually appropriate.

---

## Pull Requests

Before submitting a Pull Request:

* Ensure the project still runs.
* Test new scenes.
* Keep commits focused.
* Update documentation when appropriate.

---

## Ownership

By contributing to Farcave, you agree that your contribution may be modified, reorganized, or incorporated into future versions of the project.

Contributors retain credit for their work.

---

Thank you for helping build Farcave.
