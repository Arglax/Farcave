
import os
import math
import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
# Import structural assets from our main codebase module
import Farcave as core
console = Console()
# =========================================================================
# CHAPTER METADATA
# =========================================================================
CHAPTER_INFO = {
    "id": 2,
    "title": "Chapter 2: Ascent and Ash",
    "version": "0.0.4",
    "author": "Arglax",
}

# =========================================================================
# CHAPTER 2 ASCII ART EXTENSIONS
# =========================================================================

BAZAAR_ART = r"""
     .---.   .---.   .---.
    | I |   | S |   | C |
    |___|___|___|___|___|
    [___________________]
     |  $_$       $_$  |
     |   [X]     [X]   |
     |_________________|
"""

CAVE_MAW_ART = r"""
     ______  __          __
    /  __  | \ \        / /
   /  /  | |  \ \  /\  / / 
  |  /__/ /    \ \/  \/ /  
  |  ___ /      \  /\  /   
  | /            \/  \/    
 /_/ JAGGED MOUNTAIN MAW  
"""

ALTAR_ART = r"""
         /\
        /  \
       /____\
      /\    /\
     /  \  /  \
    /____\/____\
    ||||||||||||
   [= ENERGY CORE =]
"""

# =========================================================================
# MODULAR CHAPTER 2 SCENE INJECTIONS
# =========================================================================

class Scene11TheSurfaceThreshold(core.Scene):
    def __init__(self):
        super().__init__(11, "CHAPTER 2 INTRO: THE SURFACE THRESHOLD")
        
    def run(self, player):
        core.clear()
        core.draw_header(self.title)
        console.print(Panel(
            "Blinding natural starlight cascades down across a magnificent outdoor mountain shelf.\n"
            "You have broken past the underground cavern roof! Fresh pine wind hits your face.\n"
            "Down below, smoke trails curl upward from a high-altitude settlement outpost.",
            title="Fresh Air Horizon", border_style="green"
        ))
        input("\nPress Enter to see choices...")
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "March confidently down the open trail paths (CHA Check)",
            "2": "Scout the tree perimeter for hidden lookouts (WIS Check)"
        })
        
        if ch == "1":
            if core.roll_check(player, "CHA", 14):
                console.print("[bold green]Success! Mountain rangers salute your path and guide you in safely.[/bold green]")
                player.gain_exp(30)
            else:
                console.print("[bold red]Failure! You look suspicious. They detail you under heavy watch overnight.[/bold red]")
                player.hp -= 5
        else:
            if core.roll_check(player, "WIS", 15):
                console.print("[bold green]Success! You spot a hunter trap line ahead, salvaging valuable dynamic tools.[/bold green]")
                player.coins += 40
                player.gain_exp(35)
            else:
                console.print("[bold red]Failure! You trip a wire string, taking damage from rockfalls.[/bold red]")
                player.hp -= 15
                
        input("\nPress Enter to continue...")
        return 12 if player.hp > 0 else 0


class Scene12TheOutpostSquare(core.Scene):
    def __init__(self):
        super().__init__(12, "CHAPTER 2: THE OUTPOST SQUARE")
        
    def run(self, player):
        core.clear()
        core.draw_header(self.title)
        console.print(Panel(
            "You enter the vibrant frontier settlement town plaza. Locals stare at your cave-weathered gear.\n"
            "A bustling merchant house stands left, and a grand meeting hall stands right.",
            title="Frontier Crossings", border_style="sky_blue1"
        ))
        input("\nPress Enter to see choices...")
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Barter scrap items with trading agents (DEX Check)",
            "2": "Listen to global town rumors near the well (INT Check)"
        })
        
        if ch == "1":
            if core.roll_check(player, "DEX", 13):
                console.print("[bold green]Success! Excellent trades net you a massive bag of coin credits.[/bold green]")
                player.coins += 60
                player.gain_exp(20)
            else:
                console.print("[bold red]Failure! You get pickpocketed during the rowdy negotiations.[/bold red]")
                player.coins = max(0, player.coins - 15)
        else:
            if core.roll_check(player, "INT", 14):
                console.print("[bold green]Success! You discover the location coordinates of a secret valley vault.[/bold green]")
                player.gain_exp(45)
            else:
                console.print("[bold red]Failure! Misleading lore confuses your next directions completely.[/bold red]")
                player.hp -= 5
                
        input("\nPress Enter to continue...")
        return 13 if player.hp > 0 else 0


class Scene13TheEldersLore(core.Scene):
    def __init__(self):
        super().__init__(13, "CHAPTER 2: THE ELDER'S ANCIENT LORE")
        
    def run(self, player):
        core.clear()
        core.draw_header(self.title)
        console.print(Panel(
            "An elderly chronicler invites you inside his smoky study. He recognizes your marking emblems.\n"
            "He rolls out an ancient world map tracking the deep underground ruins you just survived.\n\n"
            "\"The Core Monolith you altered down there... it was a tectonic lock,\" he whispers hoarsely.\n"
            "\"The mountains are fracturing. Black smoke is bleeding from the valleys. If someone doesn't\n"
            "descend into the mountain's deeper Maw to stabilize the secondary fault lines, this outpost—\n"
            "and everyone in it—will slide straight into the abyss.\"",
            title="The Unavoidable Burden", border_style="gold1"
        ))
        input("\nPress Enter to see choices...")
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Absorb his specialized deep historical maps (WIS Check)",
            "2": "Demand funding/supplies to aid your mandatory return (CHA Check)"
        })
        
        if ch == "1":
            if core.roll_check(player, "WIS", 15):
                console.print("[bold green]Success! You discover ancient structural layouts. Mapping arrays updated![/bold green]")
                player.gain_exp(60)
            else:
                console.print("[bold red]Failure! Complex runic coordinates strain your mind. Brain fog sets in.[/bold red]")
                player.hp -= 10
        else:
            if core.roll_check(player, "CHA", 14):
                console.print("[bold green]Success! The Elder signs a treasury draft granting you gold supplies.[/bold green]")
                player.coins += 50
            else:
                console.print("[bold red]Failure! He calls you a mercenary scavenger and locks his chest tight.[/bold red]")
                
        input("\nPress Enter to gear up at the Outpost Market...")
        return 14 if player.hp > 0 else 0


class Scene14FrontierBazaar(core.Scene):
    def __init__(self):
        super().__init__(14, "CHAPTER 2: THE FRONTIER BAZAAR & ALCHEMIST")
        
    def run(self, player):
        while True:
            core.clear()
            core.draw_header(self.title)
            console.print(Text(BAZAAR_ART, style="bold yellow"))
            
            status_text = "Status: [bold green]Healthy[/bold green]"
            if getattr(player, "cursed", False):
                status_text = "Status: [bold red]⚠️ CURSED (Luck Proc Inhibited)[/bold red]"
                
            console.print(Panel(
                f"Welcome to the last civilized trading post. Prepare your stats before the dark descent.\n"
                f"Your Current Balance: [bold yellow]{player.coins}💰[/bold yellow] | {status_text}",
                title="Trading Matrix Shop", border_style="yellow"
            ))
            
            # Interactive shop mechanics using input selection loops
            console.print("  [1] Buy Giant's Draught (+1 STR) -------- 45 Coins")
            console.print("  [2] Buy Mercury Tincture (+1 AGI) ------ 45 Coins")
            console.print("  [3] Buy Sage's Insight (+1 INT) --------- 45 Coins")
            if getattr(player, "cursed", False):
                console.print("  [4] Pay Alchemist to Cleanse Curse ------ 30 Coins")
            else:
                console.print("  [4] Buy Blessed Charm (+1 LUK) --------- 50 Coins")
            console.print("  [5] Exit Shop & Head Down to the Maw")
            
            choice = input("\nSelect purchase target index: ").strip()
            
            if choice == "1" and player.coins >= 45:
                player.coins -= 45
                player.stats["STR"] += 1
                player._update_derived_stats()
                console.print("[bold green]Success! Raw physical power surges through your veins (+1 STR).[/bold green]")
                time.sleep(1.2)
            elif choice == "2" and player.coins >= 45:
                player.coins -= 45
                player.stats["AGI"] += 1
                console.print("[bold green]Success! Your reflexes tighten and accelerate (+1 AGI).[/bold green]")
                time.sleep(1.2)
            elif choice == "3" and player.coins >= 45:
                player.coins -= 45
                player.stats["INT"] += 1
                console.print("[bold green]Success! Complex mental matrices lock cleanly into focus (+1 INT).[/bold green]")
                time.sleep(1.2)
            elif choice == "4" and getattr(player, "cursed", False) and player.coins >= 30:
                player.coins -= 30
                player.cursed = False
                console.print("[bold green]✓ The Alchemist burns away the dark fog! THE CURSE HAS BEEN LIFTED![/bold green]")
                time.sleep(1.5)
            elif choice == "4" and not getattr(player, "cursed", False) and player.coins >= 50:
                player.coins -= 50
                player.stats["LUK"] += 1
                console.print("[bold green]Success! A strange aura of fate wraps around your choices (+1 LUK).[/bold green]")
                time.sleep(1.2)
            elif choice == "5":
                console.print("[yellow]Steeling your resolve, you lock your armor plates and head for the trench...[/yellow]")
                time.sleep(1.2)
                break
            else:
                console.print("[bold red]Transaction Denied: Insufficient gold coins or invalid entry.[/bold red]")
                time.sleep(1.2)
                
        return 15


class Scene15ShatteredMaw(core.Scene):
    def __init__(self):
        super().__init__(15, "CHAPTER 2: THE SHATTERED MAW")
        
    def run(self, player):
        def render_story():
            console.print(Text(CAVE_MAW_ART, style="bold red"))
            console.print(Panel(
                "You stand at the smoking edge of the valley fault line—The Shattered Maw.\n"
                "The cave system here is jagged, unstable, and bleeding hot volcanic ash lines.\n"
                "A massive rockfall blockades the main arterial tunnel down. To pass deeper,\n"
                "you can either scale a volatile fault line or navigate a treacherous air vent flue.",
                title="The Re-Entry Point", border_style="red"
            ))
            
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Pry loose blockading granite blocks manually (STR Check)",
            "2": "Squeeze through a narrow, shifting ash vent line (DEX Check)"
        }, story_render_func=render_story)
        
        if ch == "1":
            if core.roll_check(player, "STR", 14):
                console.print("[bold green]Success! You heave the boulders into the gap, clearing a clean descent pathway.[/bold green]")
                player.gain_exp(40)
                return 16  # Branch A
            else:
                console.print("[bold red]Failure! The roof shifts during your attempt. Heavy stones crush your arms.[/bold red]")
                player.hp -= 18
                return 17  # Branch B
        else:
            if core.roll_check(player, "DEX", 14):
                console.print("[bold green]Success! You slide elegantly through the soot channels, bypassing the blocks.[/bold green]")
                player.gain_exp(35)
                return 17  # Branch B
            else:
                console.print("[bold red]Failure! The flue collapses slightly, trapping your torso. Heat blisters your skin.[/bold red]")
                player.hp -= 15
                # Toxic sulfur exposure causes an unholy complication
                console.print("[bold red]⚠️ The volcanic ash inflicts a burning mark! You are CURSED again![/bold red]")
                player.cursed = True
                return 16  # Branch A


class Scene16CrystalSump(core.Scene):
    def __init__(self):
        super().__init__(16, "CHAPTER 2: THE CRYSTAL SUMP")
        
    def run(self, player):
        def render_story():
            console.print(Panel(
                "You plunge down into a subterranean lake bed filled with glowing purple geo-crystals.\n"
                "The air here is heavy with toxic crystal dust that creates blinding colorful hallucinations.\n"
                "At the center of the lake floor, an abandoned surveyor pack shines half-buried in radioactive silt.",
                title="Hallucinatory Grottos", border_style="magenta"
            ))
            
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Use logical sequencing to isolate stable trail paths (INT Check)",
            "2": "Filter out the visual distortions via sheer mental focus (WIS Check)"
        }, story_render_func=render_story)
        
        if ch == "1":
            if core.roll_check(player, "INT", 15):
                console.print("[bold green]Success! You recognize the chemical composition and secure the surveyor cache safely![/bold green]")
                player.coins += 55
                player.gain_exp(40)
            else:
                console.print("[bold red]Failure! You walk directly into a pocket of concentrated gas. Your lungs scream in agony.[/bold red]")
                player.hp -= 15
        else:
            if core.roll_check(player, "WIS", 14):
                console.print("[bold green]Success! Your mind remains clean and calm. You find a shortcut path downward.[/bold green]")
                player.gain_exp(45)
            else:
                console.print("[bold red]Failure! The mental visions break your concentration. You fall down an unsecured shaft floor.[/bold red]")
                player.hp -= 16
                
        input("\nPress Enter to tumble into the Depths Altar...")
        return 18 if player.hp > 0 else 0


class Scene17IronNest(core.Scene):
    def __init__(self):
        super().__init__(17, "CHAPTER 2: THE IRON NEST")
        
    def run(self, player):
        def render_story():
            console.print(Panel(
                "This sector of the trench system is lined with bizarre, metallic iron filaments.\n"
                "Chittering sounds echo across the dark; you have entered the breeding nesting grounds\n"
                "of blind, razor-clawed iron mites that react violently to sudden shifts in temperature.",
                title="Metallic Hive Zones", border_style="bright_black"
            ))
            
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Sprint across the razor filaments before they swarm your boots (AGI Check)",
            "2": "Impose total dominance via projection to keep them quiet (CHA Check)"
        }, story_render_func=render_story)
        
        if ch == "1":
            if core.roll_check(player, "AGI", 15):
                console.print("[bold green]Success! You cross the field like a gust of wind, outrunning their sensors.[/bold green]")
                player.gain_exp(40)
            else:
                console.print("[bold red]Failure! Your heel catches a filament. The swarm sets upon your legs, chewing armor seams.[/bold red]")
                player.hp -= 20
        else:
            if core.roll_check(player, "CHA", 15):
                console.print("[bold green]Success! The authoritative resonance of your commands forces the swarm to back down into the walls.[/bold green]")
                player.gain_exp(50)
                player.coins += 30  # Found fallen explorer tokens
            else:
                console.print("[bold red]Failure! The insects reject your vocal frequency and slash wildly at your chest plates.[/bold red]")
                player.hp -= 18
                
        input("\nPress Enter to advance toward the subterranean nexus...")
        return 18 if player.hp > 0 else 0


class Scene18DepthsAltar(core.Scene):
    def __init__(self):
        super().__init__(18, "CHAPTER 2: THE DEPTHS ALTAR MATRIX")
        
    def run(self, player):
        def render_story():
            console.print(Text(ALTAR_ART, style="bold magenta"))
            
            curse_notice = ""
            if getattr(player, "cursed", False):
                curse_notice = "\n[bold red]★ SYSTEM NOTE: The Altar hums fiercely, detecting your CURSE status array.[/bold red]"
                
            console.print(Panel(
                f"You break out into an impossibly vast basalt terminal room. At the absolute core sits\n"
                f"a floating, triangular secondary anchoring system. Its structural locks are grinding\n"
                f"under intense volcanic thermal pressures, threatening to snap permanently.{curse_notice}",
                title="The Tectonic Vault Anchor", border_style="bright_magenta"
            ))
            
        choices_map = {
            "1": "Force lock-pins back into sequence using mechanical leverage (STR Check)",
            "2": "Recalibrate the internal matrix frequencies safely (INT Check)"
        }
        if getattr(player, "cursed", False):
            choices_map["3"] = "Sacrifice half your coin balance to purge the curse using the altar core"
            
        ch = core.prompt_choice(player, self.scene_id, choices_map, story_render_func=render_story)
        
        if ch == "1":
            if core.roll_check(player, "STR", 16):
                console.print("[bold green]Success! With a magnificent display of power, you force the iron pins down. Tectonic faults stabilized![/bold green]")
                player.gain_exp(70)
                player.coins += 50
            else:
                console.print("[bold red]Failure! The piston fires backward, breaking your posture and crushing your ribs.[/bold red]")
                player.hp -= 22
        elif ch == "2":
            if core.roll_check(player, "INT", 16):
                console.print("[bold green]Success! You solve the frequency equations. The core hums quietly and cools down safely.[/bold green]")
                player.gain_exp(80)
            else:
                console.print("[bold red]Failure! Incorrect formulas short-circuit the interface panel. A raw lightning wave blasts your face.[/bold red]")
                player.hp -= 20
        elif ch == "3" and getattr(player, "cursed", False):
            sacrifice_cost = player.coins // 2
            player.coins -= sacrifice_cost
            player.cursed = False
            console.print(f"[bold green]✓ The anchor channels consume {sacrifice_cost} coins and cleanse your timeline! CURSE REPTURED AND PURGED![/bold green]")
            time.sleep(1.5)
            
        input("\nPress Enter to face the seismic tremors...")
        return 19 if player.hp > 0 else 0


class Scene19DesolationBreach(core.Scene):
    def __init__(self):
        super().__init__(19, "CHAPTER 2: THE DESOLATION BREACH")
        
    def run(self, player):
        def render_story():
            console.print(Panel(
                "The core recalibration causes a massive tectonic feedback loop! The ceiling splits wide!\n"
                "Rivers of glowing red magma pour through the seams, vaporizing old structural masonry.\n"
                "The floor is dissolving into liquid slag. You must make an instant escape break\n"
                "toward a newly opened subterranean breach or risk vaporizing instantly.",
                title="The Meltdown Run", border_style="orange3"
            ))
            
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Sprint across collapsing basalt bridge segments (AGI Check)",
            "2": "Read the falling pattern lines to find structural shelters (WIS Check)"
        }, story_render_func=render_story)
        
        if ch == "1":
            if core.roll_check(player, "AGI", 16):
                console.print("[bold green]Success! Blinding velocity carries you clear just as the bridge melts into the slag sea.[/bold green]")
                player.gain_exp(50)
            else:
                console.print("[bold red]Failure! You misstep on a loose slab. Magma heat washes over your armor plates, scorching flesh.[/bold red]")
                player.hp -= 24
        else:
            if core.roll_check(player, "WIS", 16):
                console.print("[bold green]Success! Your insight spots an ancient drainage conduit that shields you from the lava cascades.[/bold green]")
                player.gain_exp(60)
            else:
                console.print("[bold red]Failure! Shifting debris traps your ankle. You inhale toxic magma gases, coughing up blood.[/bold red]")
                player.hp -= 22
                
        input("\nPress Enter to tumble out into safety...")
        return 20 if player.hp > 0 else 0


class Scene20Chapter2Epilogue(core.Scene):
    def __init__(self):
        super().__init__(20, "CHAPTER 2 EPILOGUE: SHADOW OF THE BOTTOMLESS CORE")
        
    def run(self, player):
        core.clear()
        core.draw_header(self.title)
        
        # Save character details safely before final scene transition
        core.save_game(player, self.scene_id)
        
        console.print(Panel(
            f"You dive headfirst through the breach door, slamming it tight as a massive wall of fire explodes\n"
            f"harmlessly behind the ancient iron bulkheads. The frontier outpost above is safe from the volcanic threat.\n\n"
            f"But there is no way back up. The path behind you is sealed under hundreds of tons of liquid slag.\n"
            f"As you look down into the immense, dark void ahead, you see it—the true, bottomless heart of the world.\n"
            f"A massive obsidian doorway stands wide open, pulsing with an alien, mathematical emerald light.\n\n"
            f"You have survived the surface and the secondary vaults. Your stats are forged. Your soul is ready.\n"
            f"Now, the true descent begins.",
            title="★ CHAPTER 2 COMPLETE ★", border_style="gold1"
        ))
        
        console.print(f"\n[bold gold1]Congratulations {player.name}![/bold gold1]")
        console.print(f"  Final Chapter Level Layout: [bold cyan]Lv.{player.level}[/bold cyan]")
        console.print(f"  Final Collected Wealth Array: [bold yellow]{player.coins}💰[/bold yellow]")
        
        input("\nPress Enter to finalize records and unlock Chapter 3: The Abyssal Trench...")
        
        # We pass 21 as the starting scene identifier index for Chapter 3's module file to intercept!
        return 21

# =========================================================================
# MODULAR HOOK EXECUTION
# =========================================================================
def inject_scenes():
    """
    Registers all Chapter 2 scenes cleanly into the unified core execution registry.
    """
    core.SCENE_REGISTRY[11] = Scene11TheSurfaceThreshold()
    core.SCENE_REGISTRY[12] = Scene12TheOutpostSquare()
    core.SCENE_REGISTRY[13] = Scene13TheEldersLore()
    core.SCENE_REGISTRY[14] = Scene14FrontierBazaar()
    core.SCENE_REGISTRY[15] = Scene15ShatteredMaw()
    core.SCENE_REGISTRY[16] = Scene16CrystalSump()
    core.SCENE_REGISTRY[17] = Scene17IronNest()
    core.SCENE_REGISTRY[18] = Scene18DepthsAltar()
    core.SCENE_REGISTRY[19] = Scene19DesolationBreach()
    core.SCENE_REGISTRY[20] = Scene20Chapter2Epilogue()

    console.print("[bold green]✓ Chapter 2 Pipeline extensions completely initialized in the workspace! [/bold green]")
    return True

def load_and_run_with_chapter2():
    """
    Manual override runner: allows running this file directly to execute tests.
    """
    inject_scenes()
    time.sleep(1)
    core.main_menu()

if __name__ == "__main__":
    load_and_run_with_chapter2()
