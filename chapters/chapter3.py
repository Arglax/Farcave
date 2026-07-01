import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import farcave_v0_0_2 as core

console = Console()

# =========================================================================
# CHAPTER METADATA
# =========================================================================
CHAPTER_INFO = {
    "id": 3,
    "title": "Chapter 3: Beyond the Obsidian Gate",
    "version": "0.0.4",
    "author": "Arglax",
}

# =========================================================================
# CHAPTER 3 ASCII ART EXTENSIONS
# =========================================================================

VOID_GATE = r"""
     ____________________
    /  ________________  \
   /  /  /_ _  _ _ _ \  \ \
  |  |  | # # # # # # |  |  |
  |  |  | # EMERALD # |  |  |
  |  |  | # MATRIX  # |  |  |
   \  \  \_ _ _ _ _ _/  /  /
    \____________________/
"""

VOID_BAZAAR = r"""
     .==.       .==.       .==.
    ()::()     ()::()     ()::()
    _______\_/_______\_/_______
   / _ _ _ _ _ _ _ _ _ _ _ _ _ \
  |  [V]   [O]   [I]   [D]   [!] |
"""

# =========================================================================
# SCENES 21 - 30: THE DEEPING MATRIX
# =========================================================================

class Scene21ObsidianThreshold(core.Scene):
    def __init__(self): super().__init__(21, "CH3: THE OBSIDIAN THRESHOLD")
    def run(self, player):
        core.clear()
        console.print(Text(VOID_GATE, style="bold green"))
        story = (
            "The massive obsidian doors slam shut behind you with a deafening, absolute finality that echoes through your teeth. "
            "The heat and sulfur of the crumbling volcanic upper tunnels vanish instantly, replaced by a freezing, artificial chill. "
            "You stand inside a vast, geometric hall that stretches infinitely upward into complete darkness.\n\n"
            "Humming emerald frequency grids ripple across the seamless black floors like digital water. The air smells heavily of "
            "ozone, static electricity, and centuries of undisturbed dust. You can feel a faint, rhythmic pulse beneath your boots, "
            "as if you are stepping directly onto the chest of a sleeping, mechanical titan.\n\n"
            "A looming sense of isolation settles over you. There is no turning back; the surface world is gone, buried under "
            "hundreds of tons of liquid slag. Ahead lies nothing but the hyper-advanced engineering of an ancient, forgotten precursor race."
        )
        console.print(Panel(story, title="The Point of No Return", border_style="green"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Analyze the floating light arrays to deduce their architectural meaning (INT Check)",
            "2": "Brace your physical posture against the crushing gravitational hum (STR Check)"
        })
        if ch == "1":
            if core.roll_check(player, "INT", 15): player.gain_exp(40); return 22
            else: player.hp -= 10; return 23
        else:
            if core.roll_check(player, "STR", 15): player.gain_exp(40); return 23
            else: player.hp -= 12; return 22

class Scene22EmeraldCorridor(core.Scene):
    def __init__(self): super().__init__(22, "CH3: THE EMERALD CORRIDOR")
    def run(self, player):
        core.clear()
        story = (
            "You press forward into a narrow, suffocating hallway where green light matrices project shifting hyper-cubes along "
            "the polished walls. The geometric shapes twist and recalculate themselves every few seconds, hurting your eyes if you stare too long. "
            "The air tastes faintly of old copper coins and chemical fire.\n\n"
            "Suddenly, the solid stone walls begin to phase out, replaced by intersecting webs of burning energy beams. These lasers form a "
            "lethal, moving labyrinth that systematically blocks your advance. One wrong step will slice through your armor like hot butter.\n\n"
            "The timing is erratic, but a logical mind can see the mathematical loop hidden within the shifting patterns. Alternatively, "
            "raw speed might carry you through before the grid cycles can reset."
        )
        console.print(Panel(story, title="The Optical Maze", border_style="green"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Sprint blindly through the shifting laser-grids with flawless momentum (AGI Check)",
            "2": "Stand perfectly still and calculate the exact frequency intervals (INT Check)"
        })
        if ch == "1" and core.roll_check(player, "AGI", 15): player.gain_exp(45); return 24
        elif ch == "2" and core.roll_check(player, "INT", 14): player.gain_exp(50); return 24
        else: console.print("[bold red]The energy beams catch your flank, searing flesh![/bold red]"); player.hp -= 15; return 24

class Scene23SunkenReliquary(core.Scene):
    def __init__(self): super().__init__(23, "CH3: THE SUNKEN RELIQUARY")
    def run(self, player):
        core.clear()
        story = (
            "You drop into a flooded lower chamber where you find yourself wading knee-deep through a bizarre, silver liquid metal. "
            "It doesn't wet your clothes, but it clings to your limbs with a heavy, magnetic drag that makes every single movement exhausting.\n\n"
            "Floating throughout the room are strange, glowing relics of a precursor civilization. Disembodied metallic faces, "
            "perfectly carved crystal spheres, and broken runic weapons bob gently in the silver mire like trash in a harbor. "
            "A low, corrupt whispers echo directly into your mind as you pass them.\n\n"
            "The silver sludge hides deep structural pits. You must rely on physical stamina to push through the heavy fluid, or use your "
            "instincts to read the ripples on the surface to locate safe, shallow paths."
        )
        console.print(Panel(story, title="The Mercury Depths", border_style="cyan"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Dredge through the thick, magnetic sludge manually via brute force (STR Check)",
            "2": "Use structural intuition to map out the shallowest paths (WIS Check)"
        })
        if ch == "1" and core.roll_check(player, "STR", 16): console.print("[bold green]You salvage a sunken cache![/bold green]"); player.coins += 40; return 24
        elif ch == "2" and core.roll_check(player, "WIS", 14): player.gain_exp(45); return 24
        else: console.print("[bold red]You sink into a toxic trench, absorbing an ancient curse![/bold red]"); player.hp -= 14; player.cursed = True; return 24

class Scene24WhisperingPylons(core.Scene):
    def __init__(self): super().__init__(24, "CH3: THE WHISPERING PYLONS")
    def run(self, player):
        core.clear()
        story = (
            "The path opens into a colossal amphitheater dominated by towering obsidian pylons. Each structure is wrapped in spinning "
            "copper coils that emit a deafening, high-pitched sonic frequency. The noise vibrates your skull and completely scrambles your inner ear.\n\n"
            "You lose your balance immediately, falling to your knees as your vision blurs into a chaotic smear of green and black. "
            "The pylons seem to be responding to your vital signs, escalating their volume to match your rising heartbeat in a lethal feedback loop.\n\n"
            "To survive the acoustic onslaught, you must either find a way to project your own voice to disrupt the soundwaves, or interact "
            "mechanically with the base circuits to ground the pylons' power supply."
        )
        console.print(Panel(story, title="The Acoustic Gauntlet", border_style="magenta"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Match the tonal resonance with an authoritative vocal shout (CHA Check)",
            "2": "Rig an electronic ground loop wire using your tools (DEX Check)"
        })
        if ch == "1" and core.roll_check(player, "CHA", 15): player.gain_exp(50); return 25
        elif ch == "2" and core.roll_check(player, "DEX", 16): player.gain_exp(55); return 25
        else: console.print("[bold red]The vibrations burst your capillaries, causing internal bleeding![/bold red]"); player.hp -= 18; return 25

class Scene25CipherVault(core.Scene):
    def __init__(self): super().__init__(25, "CH3: THE CIPHER VAULT")
    def run(self, player):
        core.clear()
        story = (
            "You arrive at a massive, circular vault door blocking the entire terminal path. Instead of a traditional lock, the face "
            "of the door features a complex, spinning grid of shifting numeric runes that glow with an angry crimson light.\n\n"
            "A digital countdown display ticks backward on the wall above. Small vents along the ceiling begin to hiss, leaking a sweet-smelling, "
            "paralyzing nerve gas into the room. It is clear that the precursor security network expects an architectural authorization key.\n\n"
            "You have seconds to act. You can try to deconstruct the algorithmic patterns of the runes to solve the sequence properly, "
            "or use specialized lockpicks to force the internal mechanical pins apart by force."
        )
        console.print(Panel(story, title="Precursor Security Intercept", border_style="yellow"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Deconstruct the algorithmic patterns of the shifting code matrix (INT Check)",
            "2": "Force the internal locking pins apart manually (DEX Check)"
        })
        if ch == "1" and core.roll_check(player, "INT", 16): player.coins += 60; return 26
        elif ch == "2" and core.roll_check(player, "DEX", 15): player.coins += 30; return 27
        else: console.print("[bold red]The system locks down, venting burning defense gas![/bold red]"); player.hp -= 20; return 27

class Scene26GravityChasm(core.Scene):
    def __init__(self): super().__init__(26, "CH3: THE GRAVITY CHASM")
    def run(self, player):
        core.clear()
        story = (
            "The ground simply ends. Before you lies a vast, bottomless chasm where physics have been completely broken. "
            "Gravity reverses itself cleanly every twelve seconds, marked by a loud, hydraulic click from the distant walls.\n\n"
            "Shattered pieces of architecture, old stone pillars, and debris drift lazily upward toward the ceiling, only to plummet "
            "back down when the cycle flips. You must navigate this vertical nightmare to reach the far ledge.\n\n"
            "A single error in judgment means either falling into the dark void below or being smashed against the spiked ceiling when "
            "the gravity field violently changes direction."
        )
        console.print(Panel(story, title="The Inverted Void", border_style="blue"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Time a leap across the floating debris mid-air (AGI Check)",
            "2": "Anchor yourself to the wall using magnetic piton lines (STR Check)"
        })
        if ch == "1" and core.roll_check(player, "AGI", 16): return 28
        elif ch == "2" and core.roll_check(player, "STR", 15): return 28
        else: console.print("[bold red]You tumble wildly as gravity flips, hitting the rocks hard![/bold red]"); player.hp -= 15; return 29

class Scene27SilentFoundry(core.Scene):
    def __init__(self): super().__init__(27, "CH3: THE SILENT FOUNDRY")
    def run(self, player):
        core.clear()
        story = (
            "You stumble into an automated manufacturing bay that stretches for miles in absolute, eerie silence. "
            "Massive overhead laser assemblers move back and forth along magnetic rails, silently welding complex drone chassis together.\n\n"
            "There are no workers here, only the cold precision of thousands of robotic arms moving with flawless efficiency. "
            "Bright blue scanning arcs sweep across the floor tiles below you, looking for any anomalous material or organic intruders to incinerate.\n\n"
            "To pass through, you must either find a blind spot in the motion sensors' paths or access a sub-station terminal to rewrite the foundry's targeting protocols."
        )
        console.print(Panel(story, title="Automated Assembler Lines", border_style="red"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Sneak past the moving blue motion sensors (DEX Check)",
            "2": "Reprogram the assembly sub-station terminal (INT Check)"
        })
        if ch == "1" and core.roll_check(player, "DEX", 16): return 29
        elif ch == "2" and core.roll_check(player, "INT", 15): player.gain_exp(60); return 28
        else: console.print("[bold red]A welding laser tracks your position and scores your armor![/bold red]"); player.hp -= 22; return 29

class Scene28BioluminescentMire(core.Scene):
    def __init__(self): super().__init__(28, "CH3: THE BIOLUMINESCENT MIRE")
    def run(self, player):
        core.clear()
        story = (
            "Nature has reclaimed this segment of the matrix shell. Thick, damp clumps of glowing purple moss cover the metal floors, "
            "transforming the sterile corridor into a swampy, subterranean wetland filled with alien flora.\n\n"
            "Strange, pale spores float lazily through the humid air, glowing with an internal bioluminescence. Beautiful as it is, "
            "your throat begins to tighten immediately. The spores are toxic, reacting with your lung tissue to create mild, suffocating chemical burns.\n\n"
            "You need to cross this ecosystem quickly. You can rely on deep biological tracking knowledge to pick out safe paths, or simply "
            "hold your breath and sprint through via sheer physical stamina."
        )
        console.print(Panel(story, title="The Precursor Swamp", border_style="green"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Identify safe pathways via deep biological tracking (WIS Check)",
            "2": "Push through the toxic marsh via raw physical stamina (STR Check)"
        })
        if ch == "1" and core.roll_check(player, "WIS", 15): return 30
        elif ch == "2" and core.roll_check(player, "STR", 16): return 30
        else: console.print("[bold red]Spore inhalation compromises your blood arrays! You are cursed![/bold red]"); player.hp -= 15; player.cursed = True; return 30

class Scene29ArchonsLibrary(core.Scene):
    def __init__(self): super().__init__(29, "CH3: THE ARCHON'S LIBRARY")
    def run(self, player):
        core.clear()
        story = (
            "You enter a cathedral-like structure where millions of glowing crystal data rods line shelves that stretch "
            "miles into the sky. This is the repository of all precursor history, knowledge, and scientific data.\n\n"
            "As you walk down the central aisle, a flickering holographic projection of an ancient Archon materializes before you. "
            "Its face is an abstract cluster of shifting geometric lines, and it speaks in a multi-layered language that rings directly inside your brain.\n\n"
            "It offers a choice: absorb the historical indexes of the data banks to learn the true nature of this world, or communicate "
            "directly with its logic core to demand tactical insight."
        )
        console.print(Panel(story, title="The Repository of Ages", border_style="white"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Scan the historical crystal indexes for forgotten lore (INT Check)",
            "2": "Commune with the ancient AI projection directly (CHA Check)"
        })
        if ch == "1" and core.roll_check(player, "INT", 16): player.gain_exp(100); return 30
        elif ch == "2" and core.roll_check(player, "CHA", 15): player.gain_exp(80); return 30
        else: console.print("[bold red]Data overload fractures your working memory metrics![/bold red]"); player.hp -= 10; return 30

class Scene30EchoingOssuary(core.Scene):
    def __init__(self): super().__init__(30, "CH3: THE ECHOING OSSUARY")
    def run(self, player):
        core.clear()
        story = (
            "The architecture turns grim. You stand inside a massive graveyard filled with the calcified, metallic remains "
            "of those who attempted the descent centuries before you. Their bones have been fused directly into the obsidian floor tiles.\n\n"
            "Whispering echoes of their final, terrifying moments bounce off the dark walls. Some of these corpses still clutch ancient "
            "gear, outdated weapons, and bags of pristine currency that survived the passage of time.\n\n"
            "Scavenging here feels like a betrayal of the dead, and the unstable spirits seem to watch your every movement. "
            "Do you risk tempting fate to loot the dead, or move past quietly with respect?"
        )
        console.print(Panel(story, title="Graveyard of the Fallen", border_style="bright_black"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Scavenge the calcified remains for lost currency items (LUK Check)",
            "2": "Steer completely clear of the bodies and move quietly (WIS Check)"
        })
        if ch == "1" and core.roll_check(player, "LUK", 14): console.print("[bold green]You find a hidden coin purse![/bold green]"); player.coins += 70; return 31
        elif ch == "2" and core.roll_check(player, "WIS", 15): return 31
        else: console.print("[bold red]A residual energy trap triggers, draining your vitality![/bold red]"); player.hp -= 12; return 31

# =========================================================================
# SCENES 31 - 40: THE ABYSSAL GAUNTLET
# =========================================================================

class Scene31StarSteelSpire(core.Scene):
    def __init__(self): super().__init__(31, "CH3: THE STAR-STEEL SPIRE")
    def run(self, player):
        core.clear()
        story = (
            "You reach a vertical shaft dominated by a massive spire made of a strange, shimmering star-steel alloy. "
            "An elevator platform sits at the base, but its power matrix requires direct authorization security codes from the core.\n\n"
            "Heavy hydraulic fluid leaks from broken conduits nearby, sizzling as it hits the electrified floor plating. "
            "The machinery is ancient but functional, waiting for a commanding hand to force it back into operation.\n\n"
            "You can try to use raw muscle to bypass the locked hydraulic safety valves, or attempt to hotwire the delicate control logic loops."
        )
        console.print(Panel(story, title="The Core Ascension Shaft", border_style="cyan"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Bypass the main hydraulic valve via brute physical leverage (STR Check)",
            "2": "Hotwire the control logic loops using precise instruments (DEX Check)"
        })
        if ch == "1" and core.roll_check(player, "STR", 16): return 32
        elif ch == "2" and core.roll_check(player, "DEX", 15): return 33
        else: console.print("[bold red]High-pressure fluid sprays across your face, causing deep chemical burns![/bold red]"); player.hp -= 18; return 33

class Scene32VoidPromenade(core.Scene):
    def __init__(self): super().__init__(32, "CH3: THE VOID PROMENADE")
    def run(self, player):
        core.clear()
        story = (
            "The elevator deposits you onto an open, metallic bridge with absolutely no guardrails. "
            "The promenade looks out directly into an endless, empty black sky that seems to swallow all ambient light.\n\n"
            "A violent, freezing void wind screams across the bridge, threatening to lift you up and throw you into the infinite vacuum below. "
            "Your armor groans under the atmospheric pressure changes, and your balance is severely tested.\n\n"
            "To reach the safety of the far terminal door, you must either sprint across with perfect balance or move with slow, methodical precision."
        )
        console.print(Panel(story, title="The Bridge of Whispers", border_style="blue"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Sprint across while buffering against the violent void wind (AGI Check)",
            "2": "Maintain a steady, focused spatial awareness with every step (WIS Check)"
        })
        if ch == "1" and core.roll_check(player, "AGI", 16): return 34
        elif ch == "2" and core.roll_check(player, "WIS", 15): return 34
        else: console.print("[bold red]The wind knocks you sideways, slamming you against the metal decking![/bold red]"); player.hp -= 20; return 34

class Scene33QuantumCrucible(core.Scene):
    def __init__(self): super().__init__(33, "CH3: THE QUANTUM CRUCIBLE")
    def run(self, player):
        core.clear()
        story = (
            "You step into an experimental testing chamber where energy particles are accelerating around the room in visible, "
            "bright orange streaks. The air is so hyper-charged that your hair stands on end, and arcs of static electricity jump from your fingers.\n\n"
            "The radiation levels are climbing exponentially, threatening to destabilize your atomic structure on a cellular level. "
            "The control terminal on the far side is your only hope of turning off the accelerator.\n\n"
            "You can try to ground the electrical output using your armor's structural integrity, or predict the mathematical vector paths of the particles to dodge them."
        )
        console.print(Panel(story, title="The Particle Field", border_style="dark_orange"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Absorb and ground the immense voltage output via your armor frame (STR Check)",
            "2": "Predict the mathematical vector paths of the incoming particles (INT Check)"
        })
        if ch == "1" and core.roll_check(player, "STR", 17): return 34
        elif ch == "2" and core.roll_check(player, "INT", 16): return 35
        else: console.print("[bold red]A stray particle arc blasts your chest, boiling your blood arrays![/bold red]"); player.hp -= 25; return 35

class Scene34VoidBazaar(core.Scene):
    def __init__(self): super().__init__(34, "CH3: THE ZERO-G VOID BAZAAR")
    def run(self, player):
        while True:
            core.clear()
            console.print(Text(VOID_BAZAAR, style="bold green"))
            story = (
                "You drift into a localized distortion where gravity drops to absolute zero. Floating in the center of this field "
                "is a spectral merchant projection, its form woven out of shimmering green code lines and shifting light arrays.\n\n"
                "It ignores your biological origins, recognizing only the mathematical value of your currency credits. "
                "Ancient, high-tier augmentations float around its holographic hands, waiting to be bound to a worthy user's matrix profile.\n\n"
                "This is your final chance to optimize your attributes before entering the deepest, most lethal security zones of the trench system."
            )
            status = "[bold red]⚠️ CURSED[/bold red]" if getattr(player, "cursed", False) else "[bold green]Clean[/bold green]"
            console.print(Panel(story, title="The Floating Precursor Market", border_style="green"))
            console.print(f"Your Balance: [bold yellow]{player.coins}💰[/bold yellow] | Curse Status: {status}\n")
            console.print("  [1] Elixir of Might (+2 STR) ----------- 70 Coins\n  [2] Reflex Catalyst (+2 AGI) ---------- 70 Coins\n  [3] Hyper-Focus Core (+2 INT) ---------- 70 Coins")
            if getattr(player, "cursed", False): console.print("  [4] Dissolve Curse Matrix Array -------- 40 Coins")
            console.print("  [5] Exit Void Market")
            ch = input("\nSelection index target: ").strip()
            if ch == "1" and player.coins >= 70: player.coins -= 70; player.stats["STR"] += 2; player._update_derived_stats(); console.print("[bold green]STR Increased![/bold green]"); time.sleep(1)
            elif ch == "2" and player.coins >= 70: player.coins -= 70; player.stats["AGI"] += 2; console.print("[bold green]AGI Increased![/bold green]"); time.sleep(1)
            elif ch == "3" and player.coins >= 70: player.coins -= 70; player.stats["INT"] += 2; console.print("[bold green]INT Increased![/bold green]"); time.sleep(1)
            elif ch == "4" and getattr(player, "cursed", False) and player.coins >= 40: player.coins -= 40; player.cursed = False; console.print("[bold green]Curse Lifted![/bold green]"); time.sleep(1)
            elif ch == "5": break
        return 36

class Scene35ClockworkOverlook(core.Scene):
    def __init__(self): super().__init__(35, "CH3: THE CLOCKWORK OVERLOOK")
    def run(self, player):
        core.clear()
        story = (
            "You look down upon the structural foundation of the entire biome. Massive, ancient brass gears—each the size of a city block—"
            "turn in perfect synchronization, grinding against each other with a force that vibrates the tectonic plates.\n\n"
            "A structural malfunction has occurred ahead: one of the balance springs has warped, locking a main secondary gear and causing "
            "sparks to rain down onto your pathway. The entire sector is building up lethal mechanical pressure.\n\n"
            "You can try to jam the main drive gears using heavy debris to force an automated system shutdown, or manipulate the balance springs precisely to release the tension."
        )
        console.print(Panel(story, title="The Foundational Gears", border_style="yellow"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Jam the drive gears using massive structural debris (STR Check)",
            "2": "Manipulate the balance springs precisely with fine tools (DEX Check)"
        })
        if ch == "1" and core.roll_check(player, "STR", 16): return 36
        elif ch == "2" and core.roll_check(player, "DEX", 16): return 36
        else: console.print("[bold red]A brass spring snaps back, striking your torso with incredible velocity![/bold red]"); player.hp -= 15; return 36

class Scene36SingularityWell(core.Scene):
    def __init__(self): super().__init__(36, "CH3: THE SINGULARITY WELL")
    def run(self, player):
        core.clear()
        story = (
            "In the center of this circular room floats a miniature black hole, held in place by four massive magnetic containment rings. "
            "The containment field is failing, and the singularity is beginning to leak gravity, pulling everything into its center.\n\n"
            "Your weapons, coins, and armor plates are pulled toward the black sphere. The floor tiles are ripping loose one by one, "
            "swirling into the void. You can feel your own body being dragged across the room.\n\n"
            "You must rely on raw physical strength to fight the absolute gravity drag field, or access the override console to re-align the magnetic dampeners."
        )
        console.print(Panel(story, title="The Gravitational Core Failure", border_style="purple"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Resist the heavy gravity drag field via raw muscle power (STR Check)",
            "2": "Re-align the gravitational magnetic dampeners via the terminal (INT Check)"
        })
        if ch == "1" and core.roll_check(player, "STR", 17): return 37
        elif ch == "2" and core.roll_check(player, "INT", 17): return 37
        else: console.print("[bold red]The gravitational pull sprains your limbs and cracks your armor frame![/bold red]"); player.hp -= 20; return 37

class Scene37PrimordialEngine(core.Scene):
    def __init__(self): super().__init__(37, "CH3: THE PRIMORDIAL ENGINE")
    def run(self, player):
        core.clear()
        story = (
            "You reach the main drive matrix powering the alien gate architecture. It is a massive, pulsing engine core filled with "
            "liquid plasma that glows with a blinding white intensity. The system is overloaded, venting super-heated steam into the room.\n\n"
            "The terminal screens are flashing warning alerts in precursor script. The defensive protocols are preparing to vent the entire "
            "chamber into the abyssal void to preserve the main mainframe core. You have seconds to act before decompression occurs.\n\n"
            "You can try to overload the plasma exhaust lines to force a manual reset, or use deep mechanical insight to safely de-escalate the core parameters."
        )
        console.print(Panel(story, title="The Overloaded Plasma Core", border_style="red"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Overload the plasma exhaust lines manually before venting occurs (AGI Check)",
            "2": "De-escalate the core core parameters safely via the interface panel (WIS Check)"
        })
        if ch == "1" and core.roll_check(player, "AGI", 17): return 38
        elif ch == "2" and core.roll_check(player, "WIS", 17): return 38
        else: console.print("[bold red]Super-heated plasma steam scalds your flesh and lungs![/bold red]"); player.hp -= 22; return 38

class Scene38ParadoxAltar(core.Scene):
    def __init__(self): super().__init__(38, "CH3: THE PARADOX ALTAR")
    def run(self, player):
        core.clear()
        story = (
            "You stumble into a quiet, crystalline vault isolated from the rest of the facility's chaotic energy fields. "
            "In the center sits an ancient altar made of shifting, translucent crystals that seem to alter probability itself around them.\n\n"
            "As you approach, your temporal timeline splits: you can see ghost-like versions of your past choices floating in the air. "
            "The altar demands a tribute of absolute fate to unlock its hidden potential or repair a broken destiny.\n\n"
            "This ancient mechanism can be manipulated to permanently increase your core cognitive attributes, or used to completely purge any active curse matrices."
        )
        console.print(Panel(story, title="The Temporal Distortion Vault", border_style="magenta"))
        choices = {"1": "Force a permanent structural upgrade to your mental matrix (+2 WIS) (INT Check)"}
        if getattr(player, "cursed", False): choices["2"] = "Purge the active curse timeline instantly from your profile"
        ch = core.prompt_choice(player, self.scene_id, choices)
        if ch == "1" and core.roll_check(player, "INT", 16): player.stats["WIS"] += 2; return 39
        elif ch == "2" and getattr(player, "cursed", False): player.cursed = False; return 39
        else: console.print("[bold red]The altar rejects your mental frequency, shocking your cognitive profile![/bold red]"); player.hp -= 15; return 39

class Scene39ThresholdOfEternity(core.Scene):
    def __init__(self): super().__init__(39, "CH3: THE THRESHOLD OF ETERNITY")
    def run(self, player):
        core.clear()
        story = (
            "You arrive at the final mechanical gateway out of the deep matrix. Before you can reach the platform, the facility's "
            "main defensive security protocol wakes up completely. Towering laser turrets deploy from the ceiling tiles, locking their red targeting arcs onto your chest.\n\n"
            "A synthetic, monotone voice booms through the intercom arrays, identifying you as an organic contamination vector marked for immediate termination. "
            "The terminal doors begin to lock down one by one, sealing you inside the kill box.\n\n"
            "This is the ultimate gauntlet. You must either project absolute authority to intimidate the firewall's main network protocols, "
            "or rely on pure, explosive reflexes to outmaneuver the tracking speed of the automated turrets."
        )
        console.print(Panel(story, title="The Automated Fire Suppression Grid", border_style="bright_red"))
        ch = core.prompt_choice(player, self.scene_id, {
            "1": "Intimidate the defensive array firewall via authority overrides (CHA Check)",
            "2": "Outmaneuver the tracking speed of the laser turrets (AGI Check)"
        })
        if ch == "1" and core.roll_check(player, "CHA", 17): player.gain_exp(150); return 40
        elif ch == "2" and core.roll_check(player, "AGI", 17): player.gain_exp(150); return 40
        else: console.print("[bold red]The defense turrets fire a coordinated volley, tearing through your defenses![/bold red]"); player.hp -= 30; return 40 if player.hp > 0 else 0

class Scene40Chapter3Epilogue(core.Scene):
    def __init__(self): super().__init__(40, "CHAPTER 3 EPILOGUE: THE GRAND DESIGN")
    def run(self, player):
        core.clear()
        core.save_game(player, self.scene_id)
        story = (
            f"The facility's main security mainframe shatters into thousands of glowing code strings, dissolving into the air. "
            f"The emerald light matrices that have guided your path across the deep tunnels begin to dim down to an absolute, terrifying pitch black.\n\n"
            f"Suddenly, the metallic floor plates beneath your feet split wide open with a grinding mechanical shriek. Before you can grab onto a ledge, "
            f"you fall through the breach, plunging straight past the crust of the planet into an impossibly vast, empty subterranean rift corridor.\n\n"
            f"You have survived the ancient precursor vaults and unraveled their optical mazes. Your attributes are legendary, your pocket is weighted down with "
            f"valuable gold tokens, and your profile is forged in electronic blood. The true architecture of the world awaits below.\n\n"
            f"Prepare for Chapter 4: The Core Unbound."
        )
        console.print(Panel(story, title="★ CHAPTER 3 COMPLETE ★", border_style="gold1"))
        console.print(f"\n[bold gold1]Congratulations {player.name}![/bold gold1]")
        console.print(f"  Final Level Layout: [bold cyan]Lv.{player.level}[/bold cyan]")
        console.print(f"  Final Wallet Balance: [bold yellow]{player.coins}💰[/bold yellow]")
        input("\nPress Enter to exit safely back to the Main Menu...")
        return 41

# =========================================================================
# MODULAR HOOK EXECUTION
# =========================================================================
def inject_scenes():
    """Dynamically initializes and injects all 20 scenes into the SCENE_REGISTRY."""
    core.SCENE_REGISTRY[21] = Scene21ObsidianThreshold()
    core.SCENE_REGISTRY[22] = Scene22EmeraldCorridor()
    core.SCENE_REGISTRY[23] = Scene23SunkenReliquary()
    core.SCENE_REGISTRY[24] = Scene24WhisperingPylons()
    core.SCENE_REGISTRY[25] = Scene25CipherVault()
    core.SCENE_REGISTRY[26] = Scene26GravityChasm()
    core.SCENE_REGISTRY[27] = Scene27SilentFoundry()
    core.SCENE_REGISTRY[28] = Scene28BioluminescentMire()
    core.SCENE_REGISTRY[29] = Scene29ArchonsLibrary()
    core.SCENE_REGISTRY[30] = Scene30EchoingOssuary()
    core.SCENE_REGISTRY[31] = Scene31StarSteelSpire()
    core.SCENE_REGISTRY[32] = Scene32VoidPromenade()
    core.SCENE_REGISTRY[33] = Scene33QuantumCrucible()
    core.SCENE_REGISTRY[34] = Scene34VoidBazaar()
    core.SCENE_REGISTRY[35] = Scene35ClockworkOverlook()
    core.SCENE_REGISTRY[36] = Scene36SingularityWell()
    core.SCENE_REGISTRY[37] = Scene37PrimordialEngine()
    core.SCENE_REGISTRY[38] = Scene38ParadoxAltar()
    core.SCENE_REGISTRY[39] = Scene39ThresholdOfEternity()
    core.SCENE_REGISTRY[40] = Scene40Chapter3Epilogue()
    
    console.print("[bold green]✓ Chapter 3 Gauntlet (20 Narrative-Enhanced Scenes) initialized successfully![/bold green]")
    return True

if __name__ == "__main__":
    inject_scenes()
    core.main_menu()