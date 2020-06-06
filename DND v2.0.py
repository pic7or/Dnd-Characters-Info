from tkinter import *



# Dnd app v2.0 by pic7or
# patch 0.0

# Skilz

rest = 'REST - You can rest for 8 hours and 50% of your health will be recovered'
meditation = 'MEDITATE - You can meditate for a short period of time to recover your HP. 1d100'
one_hand_sword_shield = 'One hand Sword and Shield - Your can successfully handle a 1h Sword & a Shield in battle'
two_one_hand_sword = 'Two Swords at a time - You can successfully handle 2 1hand Swords in Battle'
two_one_hand_hammer = "Two Hammers at a time - You can successfully handle 2 1hand Hammers in Battle"
two_two_hand_sword = "Two Hand Sword in one Hand - You can successfully handle 2 2hand Swords in Battle"
two_two_hand_hammer = "Two Hand Hammer in one Hand - You can successfully handle 2 2hand Hammers in Battle"
block = "Block - you can block the next physical attack. Str +17 and req shield"
divine_call = "Divine Call - An old warrior spirit will join the battle for the next 3 rounds. Str +15 & Wis +15"
defence_stance = "Defence Stance - In defence stance, you can not attack but you can block 75% of the attacks until you exit the stance.\nstr +17 and req shield"
daddy_bless = "Daddy's Bless - You will become blessed! From now on, you will receive double health bonus and double stats point at level up."
rush = "Rush - You will run to the target with an increased speed and stun the target for a round. Can be upgraded. Str +15 & Dex +15"
ground_slam = "Ground Slam - You will smash the hammers to the ground, knocking down all the enemies in front of you. Req Hammers and str +17"
heroic_leap = "Heroic Leap - You can jump over small fences or people, smashing the ground with your hammers, on the impact area. dmg: 200% of hammers dmg and 25% to nearby enemies. Str +17 Req Hammers. Can be upgraded"
twin_dance = "Twin Dance - If you have 2 hammers equipped, dmg will be 100% off hammers dmg, aoe. and stuns all enemies that were damaged for 2 rounds. If you have 2 swords equipped, dmg will be 200% of swords."
two_one_hand_knife = "Two knifes - You can successfully handle 2 1hand knifes in Battle"
two_one_hand_shot_swords = "Two Short Swords - You can successfully handle 2 1hand Short Swords in Battle"
invisibility = "Invisibility - You can enter in to a invisibility state. Any combat action will force the stance to break. Dex +17"
ambush = "Ambush - Sneak behind you target to successfully applied an ambush. you will give 200% of knife / short sword. Req. Class Rogue, dex +17. 50 energy"
cheap_shot = "Cheap Shot - You will destroy ur target nuts, i know is not fair but you have to do what you have to do. It req Invisibility stance and to attack the target from behind. This will stun the target for 3 rounds. Can be upgraded"
stab = "Stab - You can stab someone, rotating the knife in the target's flash to provoke massive bleeding. Dmg: 50% of one knife / short sword and bleeding for 2 rounds, taking the same dmg as the first one. req. knife / short sword dex +15, str +15. Can be upgraded!"
poison_knife = 'Poison Knife - From now on you can successfully apply poison on your knife or short sword.'
multiple_poison = "Multiple Poisons - Your chemistry class was useful. You know how to apply up to 2 poison/ knife. Can be upgraded."
two_strike_round = "Two Strikes per Round - From now one, you can apply more attacks per round, up to 2 more attacks. Each additional attack will cost 25 energy. Can be upgraded."
bow = "Bow - You can successfully handle a Bow in Battle"
predator_bow = "Predator Bow - You can successfully handle a predator Bow in Battle"
long_bow = "Long Bow - You can successfully handle a Long Bow in Battle"
long_predator_bow = "Long Predator Bow - You can successfully handle a Long Predator Bow in Battle"
nature_friend = "Nature Friend - You will have a little companion with you, that will help you in different situations."
stone_arrow = "Stone Arrow - You can successfully craft a stone arrow."
iron_arrow = "Iron Arrow - You can successfully craft an iron arrow."
poison_arrow = "Poison Arrow - You can successfully apply poison on your arrows"
eagle_eye = "Eagle Eye - Your sight is 100% more accurate and you can see weak spots on your targets."
spiritual_call = "Spiritual Call - You will stands still for a round, calling your spirit outside your body, healing your nearby allys with 4 HP for 3 rounds. Wis +17"
flash_heal = "Flash Heal - Yor magical power will be used to heal a target for 15 heal. Can be used once/day. req int +15 Wis +15"
natural_call = "Nature Call - You will penetrate the ground with your fists, calling for natures help. Trees roots will came from underground, grabbing nearby enemies and snare them for 3 rounds. req Wis +17 int +13"
dart_tube = "Dart Tube - You can successfully handle a dart tube in battle."
poison_dart  = "Poison Dart - You can successfully apply poison on your darts"
sleep_dart = "Sleep Dart - You can successfully apply sleep poison on your darts"
stun_dart = "Stun Dart - You can successfully apply stun poison on your darts"
mini_arrow = "Mini Arrow - You can handle a larger dart tube, that can use mini arrows."
pray = "Pray - You will pray at your god to get your health back, up to 15 heal. req intel +15"
nature_manipulation = "Nature Manipulation - You can manipulate small creatures or small branches. req. Int +17"
wind_control = "Wind Control - You can manipulate the wind, Req +17 int and a windy environment. Can be upgraded"
water_control = "Water Control - You can manipulate water, Req +17 int & +15 Wis and aquatic environment. Can be upgraded"
mind_control = "Mind Control - You have the power to manipulate other life beings mind. req. int +20 & wis +15."
freeze_bolt = "Freeze Bolt - You will lunch a bolt of cold particles to a target.  Dmg. 50% of character level and will snare the target for one round. Req Wizard Staff Int +12."
ice_bolt = "Ice Bolt - You will lunch a sharp bolt of ice to your target. Dmg: Character Level. Req. Int +17. Can be upgraded."
ice_block = "Ice Block - Your will enter into the ice block state where you won't be able to move but neither the enemies can't attack you. You can stay in Ice Block state up to 3 rounds. Req. Int 15+"
ice_elemental = "Ice Elemental - You will create a magical water creature, that will help you in battle with his magical abilities. His size depends of the environment. Ice elemental will disappear when will die or on his master command. Req +20 Int & Wis +15 "
earth_shot = "Earth Shot - You will create a bloc of dirt that will be lunched into the target. Has an grate advantage against non-flash targets. Dmg: 50% of lv against non-flash targets, dmg will be 200%. Req Int +15. "
earth_control = "Earth Contorl - YOu will manipulate the earth creating earthquakes that will knockdown all the targets in front of you. Req +17 int"
earth_golem = "Earth Golem - You will create an massive earth golem that will help you in the battle. His power will be strength and his size depends of the environment. Req int +20"
fire_bolt = "Fire Bolt - You will launch a fire bolt from your wizzard staff. Dmg: 100% of your lv. Req. +12 int"
magma_bolt = "Magma Bolt - You will create a magma bloc that can be launched to the target. Grate advantage against flash targets. Dmg: 50% of your lv and against flash targets will be 200% of your lv. Req int +17. Can be upgraded"
phoenix_call = "Phoenix Call - You will call a magical phoenix, made out of fire, that will fly above you and your team, healing all the party with 3hp/round for 5 rounds. Req int +15 & wis +15"
orc_rage = "RAGE - You will enter into the rage state where you will receive 100% more dmg but you will deal 100% more dmg. Up to 5 rounds. Req Str +15. Can be upgraded"
nature_heal = "Nature Heal - Using the nature's support, you can heal a target, up to 10 heal. This can be used twice/day. Req. wis +15"
druid_transformation = "Transformation - Once you killed an animal (do not include mythical creatures) you can transform into it. This can be done twice/day."

# Help commands: Stats, Skills, Inventory, Gold, Exp, Pet, Secondary skills, History

# command_list = ['Stats', 'Skills', 'Inventory', 'Gold', 'Exp', 'Pet', 'Secondary skills', 'History', 'Classes', 'Races']
# welcome_text = 'What would you like to know? '
dnd_classes = ["Ranger", "Barbarian", "Paladin", "Warrior", "Rogue", "Wizard", "Mystic", "Monk"]
dnd_races = ["Human", "Demi-God", "Orc", "Elf", "Druid", "Goblin", "Viking"]

# Gaia Stats

str_gaia = 13
str_mod_gaia = (str_gaia - 11) // 2
int_gaia = 19
int_mod_gaia = (int_gaia - 11) // 2
wis_gaia = 25
wis_mod_gaia = (wis_gaia - 11) // 2
dex_gaia = 19
dex_mod_gaia = (dex_gaia - 11) // 2
con_gaia = 12
con_mod_gaia = (con_gaia - 11) // 2
char_gaia = 10
char_mod_gaia = (char_gaia - 11) // 2
hp_gaia = 34
ac_gaia = 8

skilz_gaia = [meditation,
              spiritual_call,
              natural_call,
              nature_friend,
              nature_heal,
              eagle_eye,
              flash_heal,
              poison_dart,
              sleep_dart]
history_gaia = 'tbc'
inventory_gaia = ["Green stone Elf ring""Skillet - 1d4" "\nCrossbow - 4 + 1d8", "\nDart Tube - 2 + 1d4", "\nFancy BligBling Tube - 8 + 1d8", "\nTransparent Pendant - Can see in darkness", "\nBlue Ring - aware of wind", "\nYellow eye-ring - While activated, you can see through your pet/companion eyes", "\nDark Navy Ring - You are aware of the water", "\n70 Poison darts", "\nUnfinished Vest - While equipped, you can turn invisible"]
gold_gaia = 17300
stats_gaia = ["Str: "+ str(str_mod_gaia), "Dex: "+ str(dex_mod_gaia), "Int: "+ str(int_mod_gaia), "Wis: "+ str(wis_mod_gaia), "Con: "+ str(con_mod_gaia), "Char: "+ str(char_mod_gaia), "HP :" + str(hp_gaia), "AC: "+ str(ac_gaia)]
pet_gaia = 'Freya, lv 10'
profession_gaia = 'Cooking'


# Bjorn Stats

str_bjorn = 25
str_mod_bjorn = (str_bjorn - 11) // 2
int_bjorn = 12
int_mod_bjorn = (int_bjorn - 11) // 2
wis_bjorn = 14
wis_mod_bjorn = (wis_bjorn - 11) // 2
dex_bjorn = 19
dex_mod_bjorn = (dex_bjorn - 11) // 2
con_bjorn = 15
con_mod_bjorn = (con_bjorn - 11) // 2
char_bjorn = 14
char_mod_bjorn = (char_bjorn - 11) // 2
hp_bjorn = 28
ac_bjorn = 10

skilz_bjorn = [meditation, two_one_hand_sword, two_two_hand_hammer, rush, heroic_leap, two_one_hand_sword, twin_dance]
history_bjorn = 'tbc'
inventory_bjorn = ["1 x Battle Axe - Dmg: 2 + 1d4", "2 x Arakh - Dmg: 2 + 1d8", "1 x Custom Dagger", "1 x Elf ring with green stone"]
gold_bjorn = 100
stats_bjorn = ["Str: "+ str(str_mod_bjorn), "Dex: "+ str(dex_mod_bjorn), "Int: "+ str(int_mod_bjorn), "Wis: "+ str(wis_mod_bjorn), "Con: "+ str(con_mod_bjorn), "Char: "+ str(char_mod_bjorn), "HP :" + str(hp_bjorn), "AC: "+ str(ac_bjorn)]
pet_bjorn = 'N/A'
profession_bjorn = 'Blacksmith'


# Lyra Stats

str_lyra = 11
str_mod_lyra = (str_lyra - 11) // 2
int_lyra = 23
int_mod_lyra = (int_lyra - 11) // 2
wis_lyra = 21
wis_mod_lyra = (wis_lyra - 11) // 2
dex_lyra = 13
dex_mod_lyra = (dex_lyra - 11) // 2
con_lyra = 13
con_mod_lyra = (con_lyra - 11) // 2
char_lyra = 13
char_mod_lyra = (char_lyra - 11) // 2
hp_lyra = 29
ac_lyra = 8

skilz_lyra = [meditation, pray, nature_manipulation, wind_control, water_control, nature_heal, mind_control]
history_lyra = 'tbc'
inventory_lyra = ["Green stone Elf ring", "Artefact: Libelula"]
gold_lyra = 100
stats_lyra = ["Str: "+ str(str_mod_lyra), "Dex: "+ str(dex_mod_lyra), "Int: "+ str(int_mod_lyra), "Wis: "+ str(wis_mod_lyra), "Con: "+ str(con_mod_lyra), "Char: "+ str(char_mod_lyra), "HP :" + str(hp_lyra), "AC: "+ str(ac_lyra)]
pet_lyra = 'N/A'
profession_lyra = 'N/A'


# Q Stats
str_q = 13
str_mod_q = (str_q - 11) // 2
int_q = 13
int_mod_q = (int_q - 11) // 2
wis_q = 15
wis_mod_q = (wis_q - 11) // 2
dex_q = 29
dex_mod_q = (dex_q - 11) // 2
con_q = 9
con_mod_q = (con_q - 11) // 2
char_q = 19
char_mod_q = (char_q - 11) // 2
hp_q = 25
ac_q = 8

skilz_q = [meditation, druid_transformation, invisibility, ambush, cheap_shot, stab, poison_knife, two_strike_round]
history_q = 'tbc'
inventory_q = ["Green stone Elf ring","Fish Knife - 2 + 1d6", "Fancy Short Swords - 6 + 1d4", "Red eye Sword - Magical Item, unknown power", "Fire ring - Fire aware", "Brown Ring - unknown power" "Soul Lamp - Unknown powers", "5 Hp Pots - Each pot will recover 5 hp", "Fishing Rod - Use it to fish"]
gold_q = 36000
stats_q = ["Str: "+ str(str_mod_q), "Dex: "+ str(dex_mod_q), "Int: "+ str(int_mod_q), "Wis: "+ str(wis_mod_q), "Con: "+ str(con_mod_q), "Char: "+ str(char_mod_q), "HP: " +str(hp_q), "AC: " + str(ac_q)]
pet_q = 'tbc'
profession_q = 'Fishing and Crafting'


# PuCi Stats

str_puci = 31
str_mod_puci = (str_puci - 11) // 2
int_puci = 9
int_mod_puci = (int_puci - 11) // 2
wis_puci = 13
wis_mod_puci = (wis_puci - 11) // 2
dex_puci = 15
dex_mod_puci = (dex_puci - 11) // 2
con_puci = 14
con_mod_puci = (con_puci - 11) // 2
char_puci = 7
char_mod_puci = (char_puci - 11) // 2
hp_puci = 29
ac_puci = 16

skilz_puci = [rest, orc_rage, two_one_hand_hammer, two_one_hand_sword, two_two_hand_hammer, two_two_hand_sword, rush, heroic_leap, ground_slam, twin_dance, one_hand_sword_shield, block ]
history_puci = 'tbc'
inventory_puci = ["Two One Hand Swords - 2 + 1d4", "Two One Hand Hammers - 4 + 1d6", "Two Two Hand Hammers - 8 + 1d6"]
gold_puci = 0
stats_puci = ["Str: "+ str(str_mod_puci), "Dex: "+ str(dex_mod_puci), "Int: "+ str(int_mod_puci), "Wis: "+ str(wis_mod_puci), "Con: "+ str(con_mod_puci), "Char: "+ str(char_mod_puci), "HP :" + str(hp_puci), "AC: " + str(ac_puci)]
pet_puci = 'N/A'
profession_puci = 'N/A'


# #################Functions

def button_click(command):
    entry_display.delete('1.0', END)
    entry_display.insert(END, command)

def bjorn():
    button_stats = Button(root, text="Stats", command = lambda: button_click(stats_bjorn))
    button_skills = Button(root, text = "Skills",command = lambda: button_click(skilz_bjorn))
    button_inventory = Button(root,text="Inventory",command = lambda: button_click(inventory_bjorn))
    button_gold = Button(root, text="Gold",command = lambda: button_click(gold_bjorn))
    button_pet = Button(root, text="Pet",command = lambda: button_click(pet_bjorn))
    button_profession = Button(root, text="Profession",command = lambda: button_click(profession_bjorn))
    button_history = Button(root, text="History",command = lambda: button_click(history_bjorn))
    button_stats.grid(row=2, column=4)
    button_skills.grid(row=3, column=4)
    button_inventory.grid(row=4, column=4)
    button_gold.grid(row=5, column=4)
    button_pet.grid(row=6, column=4)
    button_profession.grid(row=7, column=4)
    button_history.grid(row=8, column=4)
def lyra():
    button_stats = Button(root, text="Stats", command = lambda: button_click(stats_lyra))
    button_skills = Button(root, text = "Skills",command = lambda: button_click(skilz_lyra))
    button_inventory = Button(root,text="Inventory",command = lambda: button_click(inventory_lyra))
    button_gold = Button(root, text="Gold",command = lambda: button_click(gold_lyra))
    button_pet = Button(root, text="Pet",command = lambda: button_click(pet_lyra))
    button_profession = Button(root, text="Profession",command = lambda: button_click(profession_lyra))
    button_history = Button(root, text="History",command = lambda: button_click(history_lyra))
    button_stats.grid(row=2, column=3)
    button_skills.grid(row=3, column=3)
    button_inventory.grid(row=4, column=3)
    button_gold.grid(row=5, column=3)
    button_pet.grid(row=6, column=3)
    button_profession.grid(row=7, column=3)
    button_history.grid(row=8, column=3)

def gaia(): # button gaia
    button_stats = Button(root, text="Stats", command = lambda: button_click(stats_gaia))
    button_skills = Button(root, text = "Skills",command = lambda: button_click(skilz_gaia))
    button_inventory = Button(root,text="Inventory",command = lambda: button_click(inventory_gaia))
    button_gold = Button(root, text="Gold",command = lambda: button_click(gold_gaia))
    button_pet = Button(root, text="Pet",command = lambda: button_click(pet_gaia))
    button_profession = Button(root, text="Profession",command = lambda: button_click(profession_gaia))
    button_history = Button(root, text="History",command = lambda: button_click(history_gaia))
    button_stats.grid(row=2, column=1)
    button_skills.grid(row=3, column=1)
    button_inventory.grid(row=4, column=1)
    button_gold.grid(row=5, column=1)
    button_pet.grid(row=6, column=1)
    button_profession.grid(row=7, column=1)
    button_history.grid(row=8, column=1)

def q():
    button_stats = Button(root, text="Stats", command = lambda: button_click(stats_q))
    button_skills = Button(root, text = "Skills", command = lambda: button_click(skilz_q))
    button_inventory = Button(root,text="Inventory", command = lambda: button_click(inventory_q))
    button_gold = Button(root, text="Gold", command = lambda: button_click(gold_q))
    button_pet = Button(root, text="Pet", command = lambda: button_click(pet_q))
    button_profession = Button(root, text="Profession", command = lambda: button_click(profession_q))
    button_history = Button(root, text="History", command = lambda: button_click(history_q))
    button_stats.grid(row=2, column=0)
    button_skills.grid(row=3, column=0)
    button_inventory.grid(row=4, column=0)
    button_gold.grid(row=5, column=0)
    button_pet.grid(row=6, column=0)
    button_profession.grid(row=7, column=0)
    button_history.grid(row=8, column=0)

def puci():
    button_stats = Button(root, text="Stats", command = lambda: button_click(stats_puci))
    button_skills = Button(root, text = "Skills", command = lambda: button_click(skilz_puci))
    button_inventory = Button(root,text="Inventory", command = lambda: button_click(inventory_puci))
    button_gold = Button(root, text="Gold", command = lambda: button_click(gold_puci))
    button_pet = Button(root, text="Pet", command = lambda: button_click(pet_puci))
    button_profession = Button(root, text="Profession", command = lambda: button_click(profession_puci))
    button_history = Button(root, text="History", command = lambda: button_click(history_puci))
    button_stats.grid(row=2, column=2)
    button_skills.grid(row=3, column=2)
    button_inventory.grid(row=4, column=2)
    button_gold.grid(row=5, column=2)
    button_pet.grid(row=6, column=2)
    button_profession.grid(row=7, column=2)
    button_history.grid(row=8, column=2)

################# BUTTONS ###########################

root = Tk()
root.title("DnD by pic7oR")
# root.iconbitmap("c:/Users/victo/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/dndd.ico")

#### Text display ####

entry_display = Text(root, height=10, width=30, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=5, padx=30, pady=30)

#### Buttons ####

button_classes = Button(root, text="Classes", command= lambda: button_click(dnd_classes))
button_races = Button(root, text="Races", command= lambda: button_click(dnd_races))
button_adi = Button(root, text="Bjorn", command=bjorn)
button_lyra = Button(root, text="lyra", command=lyra)
button_q = Button(root, text="Q", command=q)
button_gaia = Button(root, text="Gaia", command=gaia)
button_puci = Button(root, text="Puci", command=puci, state=DISABLED)
button_gaia.grid(row=1, column=1)
button_q.grid(row=1, column=0)
button_puci.grid(row=1, column=2)
button_adi.grid(row=1, column=4)
button_lyra.grid(row=1, column=3)
button_classes.grid(row=1, column=5)
button_races.grid(row=2, column=5)

root.mainloop()

