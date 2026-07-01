# 💀 FARCAVE 💀

An uncompromising, dark-fantasy text-based roguelike RPG engine played entirely within your command terminal. 

You awaken with frozen stone pressed hard against your cheek. The chill of ancient rock sinks deep into your bones, and your memory is entirely blank. Dripping echoes ring out from vast, invisible voids somewhere far above. You remember absolutely nothing—neither your origin nor the dark machine that brought you here. Below the surface, an ancient world waits, demanding your survival.

Farcave features a modular expansion architecture, built-in cryptographic anti-cheat save tracking, and an asymptotic luck-based dice-rolling mechanic where choices dictate life or permanent death.

---

## 🚀 Getting Started

### Option A: Standalone Executable (No Python Needed)
1. Go to the **Releases** section of this repository or look inside the `dist/` folder.
2. Download `farcave.exe`.
3. Launch the file to start playing immediately.

### Option B: From Source (Python 3.8+)
1. Clone this repository or download the latest `farcave_vX-X-X.py` source script.
2. Install the required visual interface library via your terminal:
   ```bash
   pip install rich

3. Boot the game engine runtime:
``
python farcave_main.py``
---

## 🎮 How to Play

* **Read Before You Roll:** Every choice displays the specific Core Attribute (`STR`, `AGI`, `DEX`, `INT`, `CHA`, `WIS`) it will test. Always choose paths that align with your character's explicit strengths.
* **Manage Your Health:** Healing points (`HP`) are incredibly scarce. Rest groves and traveling merchants are rare; losing all health will instantly wipe your save file permanently.
* **Leveling Matrix:** Accumulate Experience Points (`EXP`) from encounters to level up. Pressing **`[L]`** at action checkpoints unlocks **+8 Attribute Points** to distribute freely into your profile layout.
* **Keep Extensions Synced:** Use the main menu to sync online expansion chapters. The automation pipeline will automatically download upcoming modules (e.g., `chapter2.py`) directly into your local workspace.

## Current Version
Version `0.0.3` - pre-alpha build

## Notes
Expect stat balancing.
