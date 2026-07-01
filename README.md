![Version](https://img.shields.io/badge/version-0.0.4-blue)
![Status](https://img.shields.io/badge/status-Pre--Alpha-orange)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)

# 💀 FARCAVE 💀

An uncompromising, dark-fantasy text-based roguelike RPG engine played entirely within your command terminal.

You awaken with frozen stone pressed hard against your cheek. The chill of ancient rock sinks deep into your bones, and your memory is entirely blank. Dripping echoes ring out from vast, invisible voids somewhere far above. You remember absolutely nothing, neither your origin nor the dark machine that brought you here. Below the surface, an ancient world waits, demanding your survival.

Farcave features a modular expansion architecture, built-in cryptographic anti-cheat save tracking, and an asymptotic luck-based dice-rolling mechanic where choices dictate life or permanent death.

---

# 🚀 Getting Started

## Option A: Standalone Executable (Recommended)

1. Download the latest release from the repository's **Releases** page.
2. Extract the archive (if applicable).
3. Launch `farcave.exe`.
4. No Python installation is required.

## Option B: Run From Source

1. Clone or download this repository.
2. Install the required dependency:

```bash
pip install rich
```

3. Start the game:

```bash
python farcave_main.py
```

---

# 🔄 Updating the Game

Farcave supports two methods of updating.

## Method 1: In-Game Auto Update (Recommended)

From the Main Menu:

```
Update / Sync Chapters
```

The game will automatically:

- Check for newly released chapter modules.
- Download missing or updated chapters.
- Store them inside the local `chapters/` directory.
- Make them immediately available the next time the game starts.

This method only updates downloadable chapter content and does **not** replace the core game engine.

---

## Method 2: Manual Update (GitHub)

For the latest engine updates:

1. Visit the GitHub repository.
2. Download the newest release or source code.
3. Replace your existing:

```
farcave_main.py
```

or

```
farcave.exe
```

with the latest version.

If downloading the source manually, also replace the contents of the:

```
chapters/
```

folder with the newest chapter files.

Your save data will remain compatible whenever possible.

---

# 📁 Folder Structure

Your installation should resemble:

```
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

Do not rename the `chapters` folder, as the engine automatically scans it for expansion content.

---

# 🎮 How to Play

- **Read Before You Roll**  
  Every decision displays the Core Attribute (`STR`, `AGI`, `DEX`, `INT`, `CHA`, `WIS`) it tests. Choose options that match your strongest attributes.

- **Manage Your Health**  
  Healing opportunities are scarce. Running out of HP permanently deletes your save.

- **Level Up**  
  Gain EXP from encounters to level up. Press **`L`** whenever available to allocate **+8 Attribute Points**.

- **Luck (LUK)**  
  LUK passively grants a chance to empower attribute checks. The chance starts low and scales smoothly as your LUK increases.

- **Sync Chapters**  
  Check for newly released chapters directly from the Main Menu.

---

# 📦 Current Version

**Version:** `0.0.4` (Pre-Alpha)

---

# ⚠️ Notes

- Save compatibility is maintained whenever possible but is not guaranteed during the pre-alpha stage.
- Gameplay balance and mechanics are still actively evolving.
- Additional chapters will continue to be released through the modular chapter system.
