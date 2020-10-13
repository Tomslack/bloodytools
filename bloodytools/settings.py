#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Settings for bloodytools

  Look for the matching paragraphs of what you want to do. Change settings responsibly. If anything breaks too hard, just reload the settings-file from the repository.
"""

##
# General setttings
tier = "PR"  # number or PR (PreRaid)
wow_class_spec_list = []  # leave empty to simulate all
# wow_class_spec_list = [("shaman", "elemental"), ("mage", "frost")] # example for a specific list
wow_class_spec_list = [
    ("death_knight", "blood"),
    ("death_knight", "frost"),
    ("death_knight", "unholy"),
    ("demon_hunter", "havoc"),
    ("demon_hunter", "vengeance"),
    ("druid", "balance"),
    ("druid", "feral"),
    ("druid", "guardian"),
    ("hunter", "beast_mastery"),
    ("hunter", "marksmanship"),
    ("hunter", "survival"),
    ("mage", "arcane"),
    ("mage", "fire"),
    ("mage", "frost"),
    ("monk", "brewmaster"),
    ("monk", "windwalker"),
    # ("paladin", "protection"),
    ("paladin", "retribution"),
    ("priest", "discipline"),
    # ("priest", "holy"),
    ("priest", "shadow"),
    ("rogue", "assassination"),
    ("rogue", "outlaw"),
    ("rogue", "subtlety"),
    # ("shaman", "elemental"),
    # ("shaman", "enhancement"),
    # ("shaman", "restoration"),
    ("warlock", "affliction"),
    ("warlock", "demonology"),
    ("warlock", "destruction"),
    ("warrior", "arms"),
    ("warrior", "fury"),
    # ("warrior", "protection"),
]

###############################################################################
# SimulationCraft
executable = "../SimulationCraft/simc.exe"
fight_styles = [
    "patchwerk",
    "hecticaddcleave",
    # "beastlord"
]
iterations = "20000"  # sane value, should be enough for 0.2
profileset_work_threads = "2"
ptr = "0"
default_actions = "1"
target_error = {
    "patchwerk": "0.1",
    "hecticaddcleave": "0.2",
    "beastlord": "0.2",
}
threads = "8"

custom_apl = False
custom_fight_style = False
# custom profile overrides standard profile, standard profile is still used as baseline
custom_profile = False

###############################################################################
# Race simulations
enable_race_simulations = True

###############################################################################
# Trinket simulations
enable_trinket_simulations = True
# ilevel_step is used to determine the size of each itemlevel step taken to max_ilevel
ilevel_step = 15
max_ilevel = 140  # max_itemlevel determines the upper border of steps taken
# min_ilevel is used to determine the first simulated itemlevel and second trinket (vers stat stick)
min_ilevel = 100
# example: min 300, max 325, step 10, resulting simulated ilevels: 300, 310, 320
lua_trinket_export = True

###############################################################################
# Secondary distributions
enable_secondary_distributions_simulations = True
# in percent of full available secondary sum
secondary_distributions_step_size = 10
talent_list = (
    {}
)  # if no list is provided for a class-spec, all dps talent combinations will be run. If you want to only sim the base profiles, set 'talent_permutations' to False
# talent_list = {
#   ("shaman", "elemental"): [
#     "2301022",
#   ],
# }  # example for a talent list for Elemental Shamans
# set to False, to sim only the base profile talent combinations
talent_permutations = False
write_humanreadable_secondary_distribution_file = False

###############################################################################
# Azerite traits
enable_azerite_trait_simulations = True
azerite_trait_ilevels = [  # determines the itemlevel used to sim the traits
    "100",
    "115",
    "130",
]  # ascending order required

###############################################################################
# Gear path
enable_gear_path = False
step_size = 50
start_value = 50

###############################################################################
# Talent worth
enable_talent_worth_simulations = False

###############################################################################
# Azerite Essences (necklace)
enable_azerite_essence_simulations = True

###############################################################################
# Azerite Essences Combinations (necklace)
enable_azerite_essence_combination_simulations = True

###############################################################################
# Corruptions
enable_corruption_simulations = False

###############################################################################
# Development setting - you usually don't want to touch these
debug = False
use_own_threading = False
use_raidbots = False
try:
    from bloodytools.apikey import apikey
except Exception:
    if use_raidbots:
        exit("Error: apikey required! Add your apikey to apikey.py")
    pass
