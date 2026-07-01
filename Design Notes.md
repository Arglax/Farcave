# 💀 FARCAVE - Design Notes

> "A cave is not merely a dungeon. It is a world beneath another world."

---

# Vision

Farcave is designed as a terminal-first dark fantasy RPG that emphasizes imagination over graphical fidelity.

Rather than relying on visual effects, players are encouraged to construct the world through descriptive storytelling, risk assessment, and meaningful decision-making.

The objective is not simply to "win," but to survive.

---

# Core Design Philosophy

Every mechanic should satisfy at least one of these principles:

- Meaningful decisions
- High tension
- Permanent consequences
- Player imagination over graphical presentation
- Expandability

If a feature does not improve one of these, it probably doesn't belong.

---

# Terminal First

Farcave intentionally targets the command terminal.

Reasons include:

- Extremely lightweight
- Platform independent
- Easy to modify
- Encourages reading
- Accessible over remote systems
- Focuses development effort on gameplay instead of graphics

The terminal is treated as the game's canvas.

---

# The Attribute System

The six core attributes are:

- STR
- AGI
- DEX
- INT
- CHA
- WIS

Every choice in the game clearly indicates which attribute is being tested.

Players should never be punished by hidden information.

---

# Luck (LUK)

Luck is intentionally different from other attributes.

It never directly passes a check.

Instead, it provides a passive chance to enhance attribute rolls.

Current design:

- Base chance: 5%
- Maximum chance: 85%
- Maximum LUK: 999
- Uses a smooth exponential growth curve.

The purpose is to reward dedicated investment without making Luck mandatory.

---

# Permanent Death

Death deletes the active save.

There are no retries.

This creates meaningful tension during exploration.

Victory is earned through careful decision making instead of repeated attempts.

---

# Modular Chapter System

Farcave is designed as an expandable engine.

Chapter 1 exists inside the core engine.

Future chapters are distributed independently inside:

```
chapters/
```

Each chapter registers itself using:

```python
CHAPTER_INFO = {
    "id": 2,
    "title": "...",
    "version": "...",
    "author": "...",
}
```

This architecture allows new adventures to be added without modifying the core engine.

---

# Save System

Player saves are protected using cryptographic integrity verification.

The objective is not to make cheating impossible, but to discourage save editing while preserving player trust.

---

# Difficulty

Failure is expected.

Not every build is viable.

Players are encouraged to learn from mistakes and adapt rather than reload saves.

---

# Writing Style

Narrative should be:

- concise
- atmospheric
- descriptive
- choice-driven

Avoid excessive exposition.

The player should discover the world naturally.

---

# Contributions

Community contributions are welcome.

Contributors should follow the chapter template and existing code style to maintain consistency.

---

# Future Goals

- Expanded chapter ecosystem
- Community-made adventures
- Better procedural encounters
- Additional merchants
- More equipment systems
- Crafting
- Branching storylines
- Optional mod support

---

Farcave is ultimately an engine for telling dangerous stories beneath the earth.
