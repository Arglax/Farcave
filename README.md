# 💀 FARCAVE

*A terminal-first dark fantasy RPG engine where every decision has weight.*

Farcave is a single-player, text-based roguelike RPG played entirely in the command terminal. Explore an ancient underground world, survive dangerous encounters, and build your character through meaningful choices instead of repetitive grinding.

The game is designed around permanent consequences, modular storytelling, and lightweight deployment. No graphics, no launchers, just the terminal.

---

## Features

* Terminal-first gameplay powered by Python
* Choice-driven progression with attribute-based skill checks
* Permanent death
* Modular chapter expansion system
* Cryptographically verified save integrity
* Automatic chapter synchronization
* Lightweight and cross-platform

---

## Getting Started

### Option A — Standalone Executable (Recommended)

1. Download the latest release.
2. Extract the archive if necessary.
3. Launch **`farcave.exe`**.

No Python installation is required.

### Option B — Run from Source

Install the only required dependency:

```bash
pip install rich
```

Run the game:

```bash
python farcave_main.py
```

---

## Updating

Farcave separates the **engine** from the **story chapters**.

### Automatic Chapter Updates (Recommended)

From the Main Menu, select:

```
Update / Sync Chapters
```

The game will automatically:

* detect available chapter updates
* download missing chapters
* replace outdated chapter files
* install everything inside the `chapters/` directory

No manual file management is required.

> [!NOTE]
> Automatic updates only affect downloadable chapter modules. Core engine updates still require downloading the latest release or source code.

### Manual Updates

If you prefer updating manually:

1. Download the newest release from GitHub.
2. Replace your existing engine (`farcave.exe` or `farcave_main.py`).
3. Replace the contents of the `chapters/` folder with the latest versions.

---

## Folder Structure

```text
Farcave/
│
├── farcave.exe
├── farcave_main.py
├── farcave_save.txt
│
└── chapters/
    ├── chapter2.py
    ├── chapter3.py
    └── ...
```

> [!IMPORTANT]
> Do not rename the `chapters` directory. The engine scans this folder automatically when loading expansions.

---

## Gameplay

### Character Progression

* Gain EXP through encounters.
* Level up to receive **8 Attribute Points**.
* Press **`L`** whenever prompted to distribute points.

### Core Attributes

| Attribute | Purpose                                    |
| --------- | ------------------------------------------ |
| STR       | Physical power                             |
| AGI       | Mobility and reflexes                      |
| DEX       | Precision and finesse                      |
| INT       | Knowledge and reasoning                    |
| CHA       | Presence and persuasion                    |
| WIS       | Awareness and judgment                     |
| LUK       | Passive chance to empower attribute checks |

### Luck (LUK)

Luck does not replace your primary attributes.

Instead, it provides a passive chance to strengthen attribute rolls.

Current balance:

* Starts at **5%**
* Smooth exponential scaling
* Caps at **85%** at **999 LUK**

---

<details>

<summary><strong>Death & Save System</strong></summary>

Farcave uses permanent death.

If your HP reaches zero, your active save is deleted.

Save files are cryptographically verified to discourage manual editing while preserving normal gameplay.

</details>

---

## Project Status

**Current Version:** `v0.0.4`

**Development Stage:** Pre-Alpha

Expect balance adjustments, new mechanics, and additional story content as development continues.

---

## Documentation

* 📖 Design Notes (`DESIGN_NOTES.md`)
* 📜 Changelog (`CHANGELOG.md`)
* 🤝 Contributing (`CONTRIBUTING.md`)
* 📄 License (`LICENSE.md`)

---

## Feedback

Bug reports, balancing feedback, and suggestions are always welcome.

If something feels unfair, confusing, or broken, please open an Issue.
