import os.path

from utils import *

script_license()

print("开始优化!")


def optimize_prop():
    prop = ServerPropLoader()
    prop.data["view-distance"] = 7
    prop.data["allow-flight"] = "true"
    prop.data["use-native-transport"] = "true"
    prop.data["simulation-distance"] = 4
    prop.dump()


@handler('bukkit.yml')
def optimize_bukkit(bukkit):
    bukkit["spawn-limits"] = {
        "monsters": 20,
        "animals": 5,
        "water-animals": 2,
        "water-ambient": 2,
        "ambient": 1,
        "axolotls": 3,
        "water-underground-creature": 3
    }
    bukkit["chunk-gc"]["period-in-ticks"] = 400
    bukkit["ticks-per"] = {
        "animal-spawns": 400,
        "monster-spawns": 10,
        "water-spawns": 400,
        "water-ambient-spawns": 400,
        "water-underground-creature-spawns": 400,
        "axolotl-spawns": 400,
        "ambient-spawns": 400,
        "autosave": 6000
    }


@handler('spigot.yml')
def optimize_spigot(spigot):
    spigot["world-settings"]["default"]["mob-spawn-range"] = 3
    r = spigot["world-settings"]["default"]["entity-activation-range"]
    r["animals"] = 16
    r["monsters"] = 24
    r["raiders"] = 48
    r["misc"] = 8
    r["water"] = 8
    r["villagers"] = 16
    r["flying-monsters"] = 48
    r["tick-inactive-villagers"] = False
    spigot["world-settings"]["default"]["nerf-spawner-mobs"] = True
    spigot["world-settings"]["default"]["merge-radius"] = {
        "item": 3.5,
        "exp": 4.0
    }
    spigot["world-settings"]["default"]["ticks-per"] = {
        "hopper-transfer": 8,
        "hopper-check": 8
    }


@handler(r'config/paper-global.yml')
def optimize_paper_global(paper):
    paper["timings"]["enabled"] = False


@handler(r'config/paper-world-defaults.yml')
def optimize_paper_world(paper):
    paper["chunks"]["delay-chunk-unloads-by"] = "10s"
    paper["chunks"]["max-auto-save-chunks-per-tick"] = 8
    paper["chunks"]["prevent-moving-into-unloaded-chunks"] = True
    paper["chunks"]["entity-per-chunk-save-limit"] = {
        "area_effect_cloud": 8,
        "arrow": 16,
        "dragon_fireball": 3,
        "egg": 8,
        "ender_pearl": 8,
        "experience_bottle": 3,
        "experience_orb": 16,
        "eye_of_ender": 8,
        "fireball": 8,
        "firework_rocket": 8,
        "llama_spit": 3,
        "potion": 8,
        "shulker_bullet": 8,
        "small_fireball": 8,
        "snowball": 8,
        "spectral_arrow": 16,
        "trident": 16,
        "wither_skull": 4
    }
    paper["entities"]["armor-stands"]["tick"] = False
    paper["entities"]["armor-stands"]["do-collision-entity-lookups"] = False
    paper["entities"]["spawning"]["alt-item-despawn-rate"] = {
        "enabled": True,
        "items": {
            "cobblestone": 300,
            "netherrack": 300,
            "sand": 300,
            "red_sand": 300,
            "gravel": 300,
            "dirt": 300,
            "short_grass": 300,
            "pumpkin": 300,
            "melon_slice": 300,
            "kelp": 300,
            "bamboo": 300,
            "sugar_cane": 300,
            "twisting_vines": 300,
            "weeping_vines": 300,
            "oak_leaves": 300,
            "spruce_leaves": 300,
            "birch_leaves": 300,
            "jungle_leaves": 300,
            "acacia_leaves": 300,
            "dark_oak_leaves": 300,
            "mangrove_leaves": 300,
            "cactus": 300,
            "diorite": 300,
            "granite": 300,
            "andesite": 300,
            "scaffolding": 600
        }
    }

    paper["entities"]["spawning"]["despawn-ranges"] = {
        "ambient": {
            "hard": 72,
            "soft": 30
        },
        "axolotls": {
            "hard": 72,
            "soft": 30
        },
        "creature": {
            "hard": 72,
            "soft": 30
        },
        "misc": {
            "hard": 72,
            "soft": 30
        },
        "monster": {
            "hard": 72,
            "soft": 30
        },
        "underground_water_creature": {
            "hard": 72,
            "soft": 30
        },
        "water_ambient": {
            "hard": 72,
            "soft": 30
        },
        "water_creature": {
            "hard": 72,
            "soft": 30
        }
    }
    paper["entities"]["spawning"]["non-player-arrow-despawn-rate"] = 20
    paper["entities"]["spawning"]["creative-arrow-despawn-rate"] = 20
    paper["collisions"]["max-entity-collisions"] = 2
    paper["collisions"]["fix-climbing-bypassing-cramming-rule"] = True
    paper["misc"]["update-pathfinding-on-block-update"] = False
    paper["misc"]["redstone-implementation"] = "ALTERNATE_CURRENT"
    if not os.path.exists("pufferfish.yml"):
        paper["tick-rates"]["behavior"] = {
            "villager": {
                "validatenearbypoi": 60,
                "acquirepoi": 120
            }
        }
        paper["tick-rates"]["sensor"] = {
            "villager": {
                "secondarypoisensor": 80,
                "nearestbedsensor": 80,
                "villagerbabiessensor": 40,
                "playersensor": 40,
                "nearestlivingentitysensor": 40
            }
        }
    paper["hopper"]["disable-move-event"] = False
    paper["hopper"]["ignore-occluding-blocks"] = True
    paper["tick-rates"]["mob-spawner"] = 2
    paper["tick-rates"]["grass-spread"] = 4
    paper["tick-rates"]["container-update"] = 1
    paper["environment"]["optimize-explosions"] = True
    paper["environment"]["treasure-maps"]["enabled"] = False
    paper["environment"]["treasure-maps"]["find-already-discovered"] = {
        "loot-tables": True,
        "villager-trade": True
    }


@handler('pufferfish.yml')
def optimize_pufferfish(pufferfish):
    pufferfish["projectile"]["max-loads-per-projectile"] = 8
    dab = pufferfish["dab"]
    dab["enabled"] = True
    dab["max-tick-freq"] = 20
    dab["activation-dist-mod"] = 7
    pufferfish["enable-async-mob-spawning"] = True
    pufferfish["enable-suffocation-optimization"] = True
    pufferfish["inactive-goal-selector-throttle"] = True
    pufferfish["misc"]["disable-method-profiler"] = True


@handler('purpur.yml')
def optimize_purpur(purpur):
    purpur["settings"]["use-alternate-keepalive"] = True
    purpur["world-settings"]["default"]["mobs"]["zombie"]["aggressive-towards-villager-when-lagging"] = False
    purpur["world-settings"]["default"]["mobs"]["villager"]["lobotomize"]["enabled"] = True
    purpur["world-settings"]["default"]["mobs"]["villager"]["lobotomize"]["search-radius"] = {
        "acquire-poi": 16,
        "nearest-bed-sensor": 16
    }
    purpur["world-settings"]["default"]["mobs"]["dolphin"]["disable-treasure-searching"] = True
    purpur["world-settings"]["default"]["gameplay-mechanics"]["entities-can-use-portals"] = False
    purpur["world-settings"]["default"]["gameplay-mechanics"]["player"]["teleport-if-outside-border"] = True


if __name__ == "__main__":
    optimize_prop()
    optimize_bukkit()
    optimize_spigot()
    optimize_paper_global()
    optimize_paper_world()
    optimize_pufferfish()
    optimize_purpur()
    exit_()
