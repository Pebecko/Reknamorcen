from Promts_stats.opponent_stats import Opponent
from Promts_stats.helmet_stats import Helmet
from Promts_stats.armor_stats import Armor
from Promts_stats.weapon_stats import Fists
from character_stats import player
from main_funcs import slow_print, player_killed, base_options, wrong_input
import random


class AttackConclusion:
    def major_fail_damaging(self, opponent):
        multiplier = 1

        if player.helmet.name != "" and player.armor.name == "":
            slow_print("Poté co váš útok nezasáhl soupeře vás nechal plně odkrytého a tím dal soupeři možnost vás"
                       " zasáhnout plnou silou. Váš soupeř se rozhodl vám jít po těle.\n")
            if "smash" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.armor.smash_damage_reduction * 0.05
                else:
                    multiplier -= player.armor.smash_damage_reduction * 0.025
            elif "cut" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.armor.cut_damage_reduction * 0.09
                else:
                    multiplier -= player.armor.cut_damage_reduction * 0.045
            elif "stab" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.armor.stab_damage_reduction * 0.09
                else:
                    multiplier -= player.armor.stab_damage_reduction * 0.045
        else:
            slow_print("Váš nepovedený útok vás nechal úplně otevřeného soupeřovým útokům, na to byl váš soupeř"
                       " připraven a tak vám ihned zasadil ránu do hlavy.\n")
            multiplier += 0.2
            if "smash" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.helmet.smash_damage_reduction * 0.05
                else:
                    multiplier -= player.helmet.smash_damage_reduction * 0.025
            elif "cut" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.helmet.cut_damage_reduction * 0.09
                else:
                    multiplier -= player.helmet.cut_damage_reduction * 0.045
            elif "stab" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.helmet.stab_damage_reduction * 0.09
                else:
                    multiplier -= player.helmet.stab_damage_reduction * 0.045

        player.health -= multiplier * opponent.weapon.damage

        if "life_steal" in opponent.weapon.special_abilities:
            opponent.health += multiplier * 0.5

        return self.major_fail_specials(opponent)

    def major_fail_specials(self, opponent):
        if "cut" in opponent.weapon.damage_type and "no_bleeding" not in player.special_abilities:
            if "bleeding_1" in player.special_abilities:
                player.special_abilities.remove("bleeding_1")
                player.special_abilities.append("bleeding_3")
                slow_print("Velmi těžce krvácíte.\n")
            elif "bleeding_2" in player.special_abilities:
                player.special_abilities.remove("bleeding_2")
                player.special_abilities.append("bleeding_3")
                slow_print("Velmi těžce krvácíte.\n")
            elif "bleeding_3" in player.special_abilities:
                slow_print("Velmi těžce krvácíte.\n")
            else:
                player.special_abilities.append("bleeding_2")
                slow_print("Začali jste těžce krvácíte.\n")

        elif "smash" in opponent.weapon.damage_type and "no_bones" not in player.special_abilities:
            if player.helmet.name != "" and player.armor.name == "":
                damage = random.randint(0, 15)
                if damage < 3 and ("broken_left_arm" not in player.special_abilities and "no_left_arm" not in
                                   player.special_abilities):
                    slow_print("Soupeři se povedlo jeho ranou vám zlomit levou ruku.\n")
                    player.special_abilities.append("broken_left_arm")
                elif damage < 6 and ("broken_right_arm" not in player.special_abilities and "no_right_arm" not in
                                     player.special_abilities):
                    slow_print("Soupeři se povedlo jeho ranou vám zlomit pravou ruku.\n")
                    player.special_abilities.append("broken_right_arm")
            else:
                if player.difficulty == "nightmare" and random.randint(0, 20) == 20:
                    slow_print("Soupeřova rána byla tak tvrdá, že vám rozdrtila lebku na padrť.\n")
                    player_killed()
                elif random.randint(0, 9) == 9:
                    slow_print("Soupeř vám dal takovou ránu, že vůbec nevíte co se děje.\n")
                    player.special_abilities.append("super_stun")
                elif random.randint(0, 2) == 0:
                    slow_print("Jeho rána byla dost tvrdá a tak se vám teď trochu motá hlava.\n")
                    player.special_abilities.append("stun")

        if player.difficulty != "easy":
            if "cut" in opponent.weapon.damage_type:
                if player.helmet.name != "" and player.armor.name == "" and "no_limbs" not in player.special_abilities:
                    damage = random.randint(0, 25)
                    if damage < 3 and "no_left_arm" not in player.special_abilities:
                        slow_print("Soupeři se povedlo jeho ranou vám useknout levou ruku.\n")
                        if "broken_left_arm" in player.special_abilities:
                            player.special_abilities.remove("broken_left_arm")
                        player.special_abilities.append("no_left_arm")
                    elif damage < 6 and "no_right_arm" not in player.special_abilities:
                        slow_print("Soupeři se povedlo jeho ranou vám useknout pravou ruku.\n")
                        if "broken_right_arm" in player.special_abilities:
                            player.special_abilities.remove("broken_right_arm")
                        player.special_abilities.append("no_right_arm")
                    elif player.difficulty == "nightmare" and damage == 25:
                        slow_print("soupeřova rána vás rozťala vejpůl.\n")
                        player_killed()
                elif player.difficulty == "nightmare" and random.randint(0, 11) == 11:
                    if random.randint(0, 1) == 0:
                        slow_print("Soupeřova precizně mířená rána vám rozťala hlavu ve dví.\n")
                    else:
                        slow_print("Soupeřúv úder zaměřený na váš krk čistě prošel a usekl vám hlavu.\n")
                    player_killed()

        return

    def attack_major_fail(self, strike_dir, opponent, defence_type, defence_dir):
        if defence_type == "block":
            if random.randint(0, 4) == 0:
                block_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
            elif random.randint(0, 3) != 0:
                block_output = "Ale váš útok trval příliš dlouho byl příliš čitelný takže vaši ránu vykryl"
                opponent.weapon.hit_points -= 2 * player.weapon.damage
            else:
                block_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"

            if defence_dir == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "A tak se mu povedlo váš útok zablokovat"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif defence_dir == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "A tak se mu povedlo váš útok zablokovat"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif defence_dir == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "A tak se mu povedlo váš útok zablokovat"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            else:
                block_message = "proti bodání"
                block_output = "A jak vytáčel svou zbraň tak zachytil tu vaši a tím odklonil váš úder"
                opponent.weapon.hit_points -= 0.5 * player.weapon.damage

            slow_print("Soupeř se snažil krýt {}. {}.\n".format(block_message, block_output))
        else:
            if defence_dir == "left":
                dodge_message = "doleva"
                if strike_dir == "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku"
            elif defence_dir == "back":
                dodge_message = "dozadu"
                if strike_dir == "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku"
            else:
                dodge_message = "doprava"
                if strike_dir == "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku"
            slow_print("Soupeř se snažil uhnout {}. {}.\n".format(dodge_message, dodge_output))

        return self.major_fail_damaging(opponent)

    def attack_minor_fail(self, strike_dir, opponent, defence_type, defence_dir):
        if defence_type == "block":
            if random.randint(0, 5) == 0:
                block_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
            elif random.randint(0, 4) != 0:
                block_output = "Ale váš útok trval příliš dlouho a byl příliš čitelný" \
                               " takže si počkal a vykryl vaši ránu"
                opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif opponent.helmet.name != "" and strike_dir == "head" and defence_dir != "kvinta":
                block_output = "Ale na poslední chvíli stihl zdvihnout zbraň a částečně vám úder vykrýt a tu sílu" \
                               " kterou nevykryl zbraní absorbovala jeho helma"
                opponent.weapon.hit_points -= player.weapon.damage
                opponent.helmet.hit_points -= 1.5 * player.weapon.damage
                if "armor_piercing" in player.weapon.special_abilities:
                    opponent.helmet -= player.weapon.damage
            else:
                block_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"

            if defence_dir == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "Takže vám vaši ránu vykryl"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif defence_dir == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "Takže vám vaši ránu vykryl"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif defence_dir == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "Takže vám vaši ránu vykryl"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            else:
                block_message = "proti bodání"
                block_output = "A jak vytáčel svou zbraň tak zachytil tu vaši a tím odklonil váš úder"
                opponent.weapon.hit_points -= 0.5 * player.weapon.damage

            slow_print("Váš soupeř se snažil krýt {}. {}.\n".format(block_message, block_output))
        else:
            if defence_dir == "left":
                dodge_message = "doleva"
                if strike_dir == "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš zbrklý a tak se vám nepodařilo odhadnout správně" \
                                       " vzdálenost, takže jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku"
            elif defence_dir == "back":
                dodge_message = "dozadu"
                if strike_dir == "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš zbrklý a tak se vám nepodařilo odhadnout správně" \
                                       " vzdálenost, takže jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku"
            else:
                dodge_message = "doprava"
                if strike_dir == "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš zbrklý a tak se vám nepodařilo odhadnout správně" \
                                       " vzdálenost, takže jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku"

            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        slow_print("Měli jste ovšem štěstí, protože soupeř svoji obranu provedl dost nešikovně, byl celý ztuhlý a mimo "
                   "balanc, takže když viděl že vy jste se po útoku ihned vzpamatovali, ani se nepokoušel odseknout.\n")

        return

    def minor_success_damaging(self, opponent, strike_type, strike_dir, strike_power, defence_type):
        multiplier = 0.5

        if defence_type == "":
            multiplier += 0.25

        if strike_dir == "head":
            if opponent.helmet != Helmet():
                opponent.helmet.hit_points -= 1.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.05
                else:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.025
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.02
                else:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.01
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.05
                else:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.025
        else:
            if opponent.armor != Armor():
                opponent.armor.hit_points -= 1.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.05
                else:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.025
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.02
                else:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.01
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.05
                else:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.025

        if strike_power == "low":
            multiplier -= 0.25
        elif strike_power == "high":
            multiplier += 0.25

        opponent.health -= multiplier * player.weapon.damage

        if "life_steal" in player.weapon.special_abilities:
            player.health += multiplier * 0.5

        return self.minor_success_specials(opponent, strike_type)

    def minor_success_specials(self, opponent, strike_type):
        if "no_bleeding" not in opponent.special_abilities and strike_type == "cut":
            if "bleeding_1" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_1")
                opponent.special_abilities.append("bleeding_2")
                slow_print("Váš soupeř těžce krvácí.\n")
            elif "bleeding_2" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_2")
                opponent.special_abilities.append("bleeding_3")
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            elif "bleeding_3" in opponent.special_abilities:
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            else:
                opponent.special_abilities.append("bleeding_1")
                slow_print("Váš soupeř začal lehce krvácet.\n")

        return

    def attack_minor_success(self, strike_dir, strike_type, strike_power, opponent, defence_type, defence_dir):
        if defence_type == "":
            slow_print("Soupeř se vám nijak nebránil, jenže vám se nepodařilo ho dobře trefit a tak jste ho"
                       " nezasáhli plnou silou")
        elif defence_type == "block":
            block_message = ""
            if random.randint(0, 5) == 0:
                block_output = "Ale vy jste úplně neodhadli vzdálenost a tak jste soupeře jen lehce zasáhli"
            elif random.randint(0, 4) != 0:
                block_output = "Ale než ho vaše zbraň zasáhla stihl zareagovat a částečně váš úder zablokoval, takže" \
                               " jste ho jen lehce zranili"
                opponent.weapon.hit_points -= 1.5 * player.weapon.damage
            else:
                block_output = "Ale vaše zbraň vám trochu sklouzla v prstech a tím se váš útok trochu opozdil, což" \
                               " dalo soupeři čas na to vaši ránu ještě částečně vykrýt a tak jste mu způsobili jen" \
                               " malé zranění"

            if defence_dir == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "Jeho kryt byl ovšem dost pomalý, takže ho váš úder částečně prorazil a zasáhl " \
                                   "soupeře, takže mu způsobil lehké zranění"
                    opponent.weapon.hit_points -= player.weapon.damage
            elif defence_dir == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "Jeho kryt ovšem nebyl dost rychlý, takže ho váš úder částečně prorazil a zasáhl " \
                                   "soupeře, takže mu způsobil lehké zranění"
                    opponent.weapon.hit_points -= player.weapon.damage
            elif defence_dir == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "Jeho kryt ovšem nebyl dost rychlý, a tak váš úder zablokoval jen částečně, takže" \
                                   " mu způsobil lehké zranění"
                    opponent.weapon.hit_points -= player.weapon.damage
            elif defence_dir == "second":
                block_message = "proti bodání"
                if random.randint(0, 1) == 0 and defence_dir != "side":
                    block_output = "Ale vatáčel ji příliš rychle takže vaši zbraň jen částečně odklonil a tak ho váš" \
                                   " útok lehce zranil"
                else:
                    block_output = "Ale vytáčel svou zbraň dost pomalu a tak nestihl úplně odklonit váš rychlý útok," \
                                   " který ho lehce zranil"
                opponent.weapon.hit_points -= 0.5 * player.weapon.damage

            slow_print("Váš soupeř se snažil krýt {}. {}.\n".format(block_message, block_output))
        else:
            if defence_dir == "left":
                dodge_message = "doleva"
                if strike_dir == "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš rychlý a tak ještě než soupeř uhnul máchli jste tam" \
                                       " kam jste předpokládali, že se dostane a se štěstím jste ho lehce zasáhli"
                    else:
                        dodge_output = "Ale váš útok trval dost dlouho takže se oponentovi téměř podařilo se mu" \
                                       " vyhnout, jen se štěstím jste ho lehce zasáhli"
                else:
                    dodge_output = "Vy jste si toho na poslední chvíli všimli a tak se vám ho povedlo alespoň lehce" \
                                   " zasáhnout"
            elif defence_dir == "back":
                dodge_message = "dozadu"
                if strike_dir == "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok nebyl úplně tak dlouhý jak jste potřebovali a tak jste soupeře" \
                                       " zasáhli jen lehce"
                    else:
                        dodge_output = "Ale vy jste na soupeře zaútočili ve chvíli kdy začal uhýbat a už se vám" \
                                       " povedlo protáhnout útok jen trochu takže jste ho nezasáhli plnou silou"
                else:
                    dodge_output = "Vy jste si toho na poslední chvíli všimli a tak se vám ho povedlo alespoň lehce" \
                                   " zasáhnout"
            else:
                dodge_message = "doprava"
                if strike_dir == "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš rychlý a tak ještě než soupeř uhnul máchli jste tam" \
                                       " kam jste předpokládali že se dostane a se štěstím jste ho lehce zasáhli"
                    else:
                        dodge_output = "Ale váš útok trval dost dlouho takže se oponentovi téměř podařilo se mu" \
                                       " vyhnout, jen se štěstím jste ho lehce zasáhli"
                else:
                    dodge_output = "Vy jste si toho na poslední chvíli všimli a tak se vám ho povedlo alespoň lehce" \
                                   " zasáhnout"

            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        return self.minor_success_damaging(opponent, strike_type, strike_dir, strike_power, defence_type)

    def major_success_damaging(self, opponent, strike_type, strike_dir, strike_power, defence_type):
        multiplier = 1

        if defence_type == "":
            multiplier += 0.5
        if strike_dir == "head":
            if opponent.helmet != Helmet():
                opponent.helmet.hit_points -= 2.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.09
                else:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.045
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.04
                else:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.02
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.09
                else:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.045
        else:
            if opponent.armor != Armor():
                opponent.armor.hit_points -= 2.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.09
                else:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.045
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.04
                else:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.02
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.09
                else:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.045

        if strike_power == "low":
            multiplier -= 0.5
        elif strike_power == "high":
            multiplier += 0.5

        opponent.health -= multiplier * player.weapon.damage

        if "life_steal" in player.weapon.special_abilities:
            player.health += multiplier * 0.5

        return self.major_success_specials(opponent, strike_type, strike_dir)

    def major_success_specials(self, opponent, strike_type, strike_dir):
        if "no_bleeding" not in opponent.special_abilities and strike_type is "cut":
            if "bleeding_1" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_1")
                opponent.special_abilities.append("bleeding_3")
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            elif "bleeding_2" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_2")
                opponent.special_abilities.append("bleeding_3")
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            elif "bleeding_3" in opponent.special_abilities:
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            else:
                opponent.special_abilities.append("bleeding_2")
                slow_print("Váš soupeř začal těžce krvácet.\n")

        elif strike_type == "smash" and "no_bones" not in opponent.special_abilities:
            if strike_dir != "head":
                damage = random.randint(0, 13)
                if damage < 3 and ("broken_left_arm" not in opponent.special_abilities and "no_left_arm"
                                   not in opponent.special_abilities):
                    slow_print("Vaše rána soupeři zlomila levou ruku.\n")
                    opponent.special_abilities.append("broken_left_arm")
                elif damage < 6 and ("broken_right_arm" not in opponent.special_abilities and "no_right_arm"
                                   not in opponent.special_abilities):
                    slow_print("Vaše rána soupeři zlomila pravou ruku.\n")
                    opponent.special_abilities.append("broken_right_arm")
            else:
                if random.randint(0, 1) == 0:
                    if random.randint(0, 7) == 0:
                        slow_print("Vaše rána byla tak tvrdá, že soupeři rozdrtila lebku na padrť.\n")
                        opponent.health = 0
                    elif random.randint(0, 5) == 5:
                        slow_print("Dali jste soupeři takovou ránu, že jste ho lehce omráčili\n")
                        opponent.special_abilities.append("super_stun")
                    else:
                        slow_print("Vaše rána měla takovou sílu, že se soupeř začal motat.\n")
                        opponent.special_abilities.append("stun")

        if strike_type == "cut":
            if strike_dir != "head" and "no_limbs" not in opponent.special_abilities:
                damage = random.randint(0, 19)
                if damage < 3 and "no_left_arm" not in opponent.special_abilities:
                    slow_print("Povedlo se vám useknout soupeřovu levou ruku.\n")
                    opponent.special_abilities.append("no_left_arm")
                    if "broken_left_arm" in opponent.special_abilities:
                        opponent.special_abilities.remove("broken_left_arm")
                elif damage < 6 and "no_right_arm" not in opponent.special_abilities:
                    slow_print("Povedlo se vám useknout soupeřovu pravou ruku.\n")
                    opponent.special_abilities.append("no_right_arm")
                    if "broken_right_arm" in opponent.special_abilities:
                        opponent.special_abilities.remove("broken_right_arm")
                elif damage < 7:
                    slow_print("Povedlo se vám useknout soupeřovu levou nohu, ten pak spadl na zem v proudu krve a"
                               " vy už jste ho jen vaší další ranou dorazili.\n")
                    opponent.health = 0
                elif damage < 8:
                    slow_print("Povedlo se vám useknout soupeřovu pravou nohu, ten pak spadl na zem v proudu krve a"
                               " vy už jste ho jen vaší další ranou dorazili.\n")
                    opponent.health = 0
                elif damage < 9:
                    slow_print("Vaše rána prošla soubeřovým tělem skrz na skrz a rozůlila ho. Zbytky poté spadly"
                               " bezvládně na zem.\n")
                    opponent.health = 0
            elif random.randint(0, 7) == 7:
                if random.randint(0, 1) == 0:
                    slow_print("Vaše rána rozsekla soupeřovi hlavu ve dví.\n")
                else:
                    slow_print("Váš úder strefil soupeřův krk a čistě mu uťal hlavu, která se pak rozkutálela po"
                               " zemi v proudu jeho krve.\n")
                opponent.health = 0

        return

    def attack_major_success(self, strike_dir, strike_type, strike_power, opponent, defence_type, defence_dir):
        if defence_type == "":
            slow_print("Váš soupeř se vám nebránil a váš úder ho tvrdě zasáhl, takže jste ho velmi poranili.")
        elif defence_type == "block":
            block_message = ""
            if random.randint(0, 4) == 0:
                block_output = "Ale všiml si že sekáte jinam tak se ještě snažil svou zbraň nastavit tak aby váš úder" \
                               " vykryl ale už to nestihl a vy jste mu uštedřili silný úder"
            elif random.randint(0, 3) != 0:
                block_output = "Takže váš úder čistě prošel a tak zasáhl soupeře plnou silou"
            else:
                block_output = "Což vám dovolilo zasadit soupeři těžký zásah"

            if defence_dir == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "Jeho kryt byl ovšem dost slabý a váš úder naopak velmi silný takže jste ho tvrdě" \
                                   " zasáhli"
                    opponent.weapon.hit_points -= 0.5 * player.weapon.damage
            elif defence_dir == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "Ale pozdě vytočil svou zbraň a tak váše zbraň čistě prošla a zasáhla ho plnou silou"
                    opponent.weapon.hit_points -= 0.5 * player.weapon.damage
            elif defence_dir == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "Jeho kryt byl ovšem dost slabý a váš úder naopak velmi silný takže jste ho tvrdě" \
                                   " zasáhli"
                    opponent.weapon.hit_points -= 0.5 * player.weapon.damage
            elif defence_dir == "second":
                block_message = "proti bodání"
                if random.randint(0, 1) == 0 and defence_dir != "side":
                    block_output = "Ale vatáčel ji hrozně rychle, takže vaši zbraň úplně minul a váš úder mohl" \
                                   " zasáhnout plnou silou"
                else:
                    block_output = "Ale vytáčel svou zbraň příliš pomalu, tím pádem jeho zbraň vaši ani neškrtla, než" \
                                   " se vám povedlo dokončit svůj bleskový úder"

            slow_print("Váš soupeř se snažil krýt {}. {}.\n".format(block_message, block_output))
        else:
            if defence_dir == "left":
                dodge_message = "doleva"
                if strike_dir != "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vášemu soupeři trvalo příliš dlouho než se rozhýbat a tak jste ho zasáhli"
                    else:
                        dodge_output = "Jenže váš soupež si špatně načasoval svůj pohyb a tak uhnul moc brzo čímž vám" \
                                       " dal ideální prostor pro výpad kterým jste mu uštědřili tvrdou ránu"
                else:
                    dodge_output = "Soupeř vám uskočil přímo do rány a tak jste ho zasáhli plnou silou"
            elif defence_dir == "back":
                dodge_message = "dozadu"
                if strike_dir != "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vášemu soupeři trvalo příliš dlouho než se rozhýbat a tak jste ho zasáhli"
                    else:
                        dodge_output = "Jenže váš soupež si špatně načasoval svůj pohyb a tak uhnul moc brzo čímž vám" \
                                       " dal ideální prostor pro výpad kterým jste mu uštědřili tvrdou ránu"
                else:
                    dodge_output = "Soupeř vám uskočil přímo do rány a tak jste ho zasáhli plnou silou"
            else:
                dodge_message = "doprava"
                if strike_dir != "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vášemu soupeři trvalo příliš dlouho než se rozhýbat a tak jste ho zasáhli"
                    else:
                        dodge_output = "Jenže váš soupež si špatně načasoval svůj pohyb a tak uhnul moc brzo čímž vám" \
                                       " dal ideální prostor pro výpad kterým jste mu uštědřili tvrdou ránu"
                else:
                    dodge_output = "Soupeř vám uskočil přímo do rány a tak jste ho zasáhli plnou silou"

            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        return self.major_success_damaging(opponent, strike_type, strike_dir, strike_power, defence_type)


class AttackEvaluation:
    def __init__(self):
        self.atk_conc = AttackConclusion()

        self.lower_border = 0
        self.middle_border = 0
        self.higher_border = 0

    def border_setting(self, lower_border, middle_border, higher_border):
        self.lower_border = lower_border
        self.middle_border = middle_border
        self.higher_border = higher_border

    def border_addition(self, lower_iterator=0.0, middle_iterator=0.0, higher_iterator=0.0):
        self.lower_border += lower_iterator
        self.middle_border += middle_iterator
        self.higher_border += higher_iterator

    def border_multiplication(self, number, lower_multiplier=0.0, middle_multiplier=0.0, higher_multiplier=0.0):
        self.lower_border += (number * lower_multiplier)
        self.middle_border += (number * middle_multiplier)
        self.higher_border += (number * higher_multiplier)

    def fistfight(self):
        pass
        # TODO Add fistfight

    def defence_none(self, strike_dir, strike_power):
        self.border_setting(-200, -200, 60)

        # player target effect
        if strike_dir is "head":
            self.higher_border += 6

        # player helmet effects
        self.border_multiplication(player.helmet.heaviness, 0.2, 0.2, 0.2)

        self.border_multiplication(player.helmet.visibility, 3.5, 3, 4)

        # player armor effects
        self.border_multiplication(player.armor.heaviness, 0.3, 0.4, 0.4)

        # player attack power effects
        if strike_power == "small":
            self.higher_border -= 10
        elif strike_power == "medium":
            self.higher_border += 2
        elif strike_power == "high":
            self.higher_border += 15

        return

    def defence_dodge(self, opponent, strike_dir, strike_power, defence_dir):
        # setting base levels depending on player weapon
        if player.weapon.weapon_class == "unarmed":
            self.border_setting(5, 15, 50)
        elif player.weapon.weapon_type == "light":
            self.border_setting(5, 30, 60)  # 10 35 65
        elif player.weapon.weapon_type == "medium":
            self.border_setting(15, 40, 75)  # 20 45 80
        else:
            self.border_setting(20, 45, 85)  # 25 50 90

        # opponent weapon effects
        if opponent.weapon.weapon_class == "unarmed":
            self.border_addition(6, 8, 7)
        elif opponent.weapon.weapon_type == "light":
            self.border_addition(4, 5, 5)
        elif opponent.weapon.weapon_type == "medium":
            self.border_addition(-2, -3, -3.5)
        elif opponent.weapon.weapon_type == "heavy":
            self.border_addition(-6, -8, -9)
        elif opponent.weapon.weapon_type == "super_heavy":
            self.border_addition(-12, -15, -19)

        # opponent defence direction and player attack direction and type effects
        if defence_dir == "back":
            if strike_dir == "body" or strike_dir == "head":
                self.border_addition(-11, -14, -12)
            else:
                self.border_addition(8, 15, 14)
        elif defence_dir == "left":
            if strike_dir == "belly":
                self.border_addition(-14, -16.5, -15)
            elif strike_dir == "body" or strike_dir == "head":
                self.border_addition(10.25, 18, 16.5)
            else:
                self.border_addition(7.5, 16, 14)
        else:
            if strike_dir == "side":
                self.border_addition(-13, -16, -14)
            elif strike_dir == "body" or strike_dir is "head":
                self.border_addition(10, 17, 16)
            else:
                self.border_addition(7, 15, 15)

        # player helmet effects
        self.border_multiplication(player.helmet.heaviness, 0.1, 0.2, 0.2)
        self.border_multiplication(player.helmet.visibility, 3, 2.5, 3)

        # player armor effects
        self.border_multiplication(player.armor.heaviness, 0.3, 0.4, 0.4)

        # opponent helmet effects
        self.border_multiplication(opponent.helmet.heaviness, -0.7, -0.8, -0.9)
        self.border_multiplication(opponent.helmet.visibility, -1, -1.5, -1.5)

        # opponent armor effects
        self.border_multiplication(opponent.armor.heaviness, -1, -1.2, -1.3)

        # opponent dodge skill effects
        self.border_multiplication(opponent.dodge_effectiveness, 0.5, 0.5, 0.5)

        # player attack power effects
        if strike_power == "small":
            self.border_addition(-9, -11, -8)
        elif strike_power == "medium":
            self.border_addition(2, 4, 3)
        elif strike_power == "high":
            self.border_addition(7, 12, 10)

        # equipment special buffs and debuffs
        if "extra_dodge" in opponent.weapon.special_abilities:
            self.border_addition(4, 5, 5)
        if "weak_dodge" in opponent.weapon.special_abilities:
            self.border_addition(-4, -5, -5)

        if "extra_dodge" in opponent.helmet.special_abilities:
            self.border_addition(3, 4, 4)
        if "weak_dodge" in opponent.weapon.special_abilities:
            self.border_addition(-3, -4, -4)

        if "extra_dodge" in opponent.armor.special_abilities:
            self.border_addition(5, 6, 6)
        if "weak_dodge" in opponent.weapon.special_abilities:
            self.border_addition(-5, -6, -6)

        return self.opponent_char_effects(opponent)

    def defence_block(self, opponent, strike_dir, strike_power, defence_dir):
        # setting base levels depending on player weapon
        if player.weapon.weapon_class == "unarmed":
            self.border_setting(60, 90, 100)
        elif player.weapon.weapon_type == "light":
            self.border_setting(20, 40, 90)
        elif player.weapon.weapon_type == "medium":
            self.border_setting(10, 35, 80)
        else:  # player weapon type is heavy
            self.border_setting(5, 25, 65)

        # opponent weapon effects
        if opponent.weapon.weapon_type == "light":
            self.border_addition(-5, -6, -7)
        elif opponent.weapon.weapon_type == "medium":
            self.border_addition(-2, -2, -1)
        else:  # opponent weapon type is heavy
            self.border_addition(3, 6, 4)

        # player helmet effects
        self.border_multiplication(player.helmet.heaviness, 0.1, 0.2, 0.2)
        self.border_multiplication(player.helmet.visibility, 3, 3, 3)

        # player armor effects
        self.border_multiplication(player.armor.heaviness, 0.3, 0.4, 0.4)

        # opponent helmet effects
        self.border_multiplication(opponent.helmet.heaviness, -0.1, -0.2, -0.2)
        self.border_multiplication(opponent.helmet.visibility, -3, -3.5, -3.5)

        # opponent armor effects
        self.border_multiplication(opponent.armor.heaviness, -0.3, -0.4, -0.4)

        # opponent action effects
        if defence_dir == "kvinta":
            if strike_dir == "head":
                self.border_addition(12, 18.5, 16)
            elif strike_dir == "body":
                self.border_addition(-13, -15, -12)
            elif strike_dir == "belly":
                self.border_addition(-12, -15, -13)
            else:  # player strike direction is side
                self.border_addition(-11, -14, -12)
        elif defence_dir == "kvarta":
            if strike_dir == "head":
                self.border_addition(-12.5, -15, -12)
            elif strike_dir == "body":
                self.border_addition(-8, -11, -10)
            elif strike_dir == "belly":
                self.border_addition(9, 14, 13)
            else:  # player strike direction is side
                self.border_addition(-13, -15, -13)
        elif defence_dir == "terca":
            if strike_dir == "head":
                self.border_addition(-12, -14.5, -11)
            elif strike_dir == "body":
                self.border_addition(-7.5, -11, -9)
            elif strike_dir == "belly":
                self.border_addition(-12, -13, -12)
            else:  # player strike direction is side
                self.border_addition(10, 16, 14)
        else:  # opponent block is second
            if strike_dir == "head":
                self.border_addition(-13, -16, -15)
            elif strike_dir == "body":
                self.border_addition(9, 15, 12)
            elif strike_dir == "belly":
                self.border_addition(-8.5, -11, -10)
            else:  # player strike direction is side
                self.border_addition(-10, -13, -12)

        # opponent block skill effects
        self.border_multiplication(opponent.block_effectiveness, 0.5, 0.5, 0.5)

        # player attack power effects
        if strike_power == "small":
            self.border_addition(5, 10, 7)
        elif strike_power == "medium":
            self.border_addition(1, 4, 4)
        elif strike_power == "high":
            self.border_addition(-6, -8, -7)

        # equipment special buffs and debuffs
        if "extra_block" in opponent.weapon.special_abilities:
            self.border_addition(-5, -7, -7)
        if "weak_block" in opponent.weapon.special_abilities:
            self.border_addition(5, 7, 7)

        if "extra_block" in opponent.helmet.special_abilities:
            self.border_addition(-1, -2, -2)
        if "weak_block" in opponent.weapon.special_abilities:
            self.border_addition(1, 2, 2)

        if "extra_block" in opponent.armor.special_abilities:
            self.border_addition(-2, -3, -3)
        if "weak_block" in opponent.weapon.special_abilities:
            self.border_addition(2, 3, 3)

        # opponent injuries
        if 1 in opponent.weapon.hands and 2 not in opponent.weapon.hands:
            if "broken_left_arm" in opponent.special_abilities and "broken_right_arm" not in opponent.special_abilities:
                self.border_addition(-2, -3, -3)
            elif "broken_right_arm" in opponent.special_abilities and "broken_left_arm" not in opponent.special_abilities:
                self.border_addition(-4, -5, -6)
            elif "broken_right_arm" in opponent.special_abilities and "broken_left_arm" in opponent.special_abilities:
                self.border_addition(-12, -17, -22)

            if "no_right_arm" in opponent.special_abilities and "no_left_arm" not in opponent.special_abilities:
                self.border_addition(-2, -3, -3)
            elif "no_right_arm" not in opponent.special_abilities and "no_left_arm" in opponent.special_abilities:
                self.border_addition(-5, -6, -7)
        elif 2 in opponent.weapon.hands and 1 not in opponent.weapon.hands:
            if "broken_right_arm" in opponent.special_abilities and "broken_left_arm" not in opponent.special_abilities:
                self.border_addition(-8, -10, -11)
            elif "broken_right_arm" not in opponent.special_abilities and "broken_left_arm" in opponent.special_abilities:
                self.border_addition(-6, -8, -9)
            elif "broken_right_arm" in opponent.special_abilities and "broken_left_arm" in opponent.special_abilities:
                self.border_addition(-23, -28, -33)

            if "no_right_arm" in opponent.special_abilities and "no_left_arm" not in opponent.special_abilities:
                self.border_addition(-9, -11, -12)
            elif "no_right_arm" not in opponent.special_abilities and "no_left_arm" in opponent.special_abilities:
                self.border_addition(-7, -9, -10)
        else:
            if "broken_right_arm" in opponent.special_abilities and "broken_left_arm" not in opponent.special_abilities:
                self.border_addition(-6, -7, -8)
            elif "broken_right_arm" not in opponent.special_abilities and "broken_left_arm" in opponent.special_abilities:
                self.border_addition(-5, -6, -6)
            elif "broken_right_arm" in opponent.special_abilities and "broken_left_arm" in opponent.special_abilities:
                self.border_addition(-17, -22, -27)

            if "no_right_arm" in opponent.special_abilities and "no_left_arm" not in opponent.special_abilities:
                self.border_addition(-8, -9, -10)
            elif "no_right_arm" not in opponent.special_abilities and "no_left_arm" in opponent.special_abilities:
                self.border_addition(-7, -8, -8)

        return self.opponent_char_effects(opponent)

    def player_char_effects(self):
        if "stun_effect" in player.special_abilities:
            self.border_addition(3, 5, 5)

        if 1 in player.weapon.hands and 2 not in player.weapon.hands:
            if "broken_left_arm" in player.special_abilities and "broken_right_arm" not in player.special_abilities:
                self.border_addition(1, 2, 2)
            elif "broken_right_arm" in player.special_abilities and "broken_left_arm" not in player.special_abilities:
                self.border_addition(3, 4, 5)
            elif "broken_right_arm" in player.special_abilities and "broken_left_arm" in player.special_abilities:
                self.border_addition(10, 15, 20)

            if "no_right_arm" in player.special_abilities and "no_left_arm" not in player.special_abilities:
                self.border_addition(1.5, 2.5, 2.5)
            elif "no_right_arm" not in player.special_abilities and "no_left_arm" in player.special_abilities:
                self.border_addition(4, 5, 6)
        elif 2 in player.weapon.hands and 1 not in player.weapon.hands:
            if "broken_right_arm" in player.special_abilities and "broken_left_arm" not in player.special_abilities:
                self.border_addition(7, 9, 10)
            elif "broken_right_arm" not in player.special_abilities and "broken_left_arm" in player.special_abilities:
                self.border_addition(5, 7, 8)
            elif "broken_right_arm" in player.special_abilities and "broken_left_arm" in player.special_abilities:
                self.border_addition(20, 25, 30)

            if "no_right_arm" in player.special_abilities and "no_left_arm" not in player.special_abilities:
                self.border_addition(8, 10, 11)
            elif "no_right_arm" not in player.special_abilities and "no_left_arm"in player.special_abilities:
                self.border_addition(6, 8, 9)
        else:
            if "broken_right_arm" in player.special_abilities and "broken_left_arm" not in player.special_abilities:
                self.border_addition(5, 6, 7)
            elif "broken_right_arm" not in player.special_abilities and "broken_left_arm" in player.special_abilities:
                self.border_addition(4, 5, 5)
            elif "broken_right_arm" in player.special_abilities and "broken_left_arm" in player.special_abilities:
                self.border_addition(15, 20, 25)

            if "no_right_arm" in player.special_abilities and "no_left_arm" not in player.special_abilities:
                self.border_addition(7, 8, 9)
            elif "no_right_arm" not in player.special_abilities and "no_left_arm" in player.special_abilities:
                self.border_addition(6, 7, 7)

        if player.char == "elf":
            if "elf_debuff" in player.weapon.special_abilities:
                self.border_addition(4, 6, 6)
            if "elf_buff" in player.weapon.special_abilities:
                self.border_addition(-4, -6, -6)

            if "elf_debuff" in player.helmet.special_abilities:
                self.border_addition(2, 3, 3)
            if "elf_buff" in player.helmet.special_abilities:
                self.border_addition(-2, -3, -3)

            if "elf_debuff" in player.armor.special_abilities:
                self.border_addition(3, 4, 4)
            if "elf_buff" in player.armor.special_abilities:
                self.border_addition(-3, -4, -4)
        elif player.char == "dwarf":
            if "dwarf_debuff" in player.weapon.special_abilities:
                self.border_addition(4, 6, 6)
            if "dwarf_buff" in player.weapon.special_abilities:
                self.border_addition(-4, -6, -6)

            if "dwarf_debuff" in player.helmet.special_abilities:
                self.border_addition(2, 3, 3)
            if "dwarf_buff" in player.helmet.special_abilities:
                self.border_addition(-2, -3, -3)

            if "dwarf_debuff" in player.armor.special_abilities:
                self.border_addition(3, 4, 4)
            if "dwarf_buff" in player.armor.special_abilities:
                self.border_addition(-3, -4, -4)
        elif player.char == "human":
            if "human_debuff" in player.weapon.special_abilities:
                self.border_addition(4, 6, 6)
            if "human_buff" in player.weapon.special_abilities:
                self.border_addition(-4, -6, -6)

            if "human_debuff" in player.helmet.special_abilities:
                self.border_addition(2, 3, 3)
            if "human_buff" in player.helmet.special_abilities:
                self.border_addition(-2, -3, -3)

            if "human_debuff" in player.armor.special_abilities:
                self.border_addition(3, 4, 4)
            if "human_buff" in player.armor.special_abilities:
                self.border_addition(-3, -4, -4)

        return

    def opponent_char_effects(self, opponent):
        if "stun_effect" in opponent.special_abilities:
            self.border_addition(-4, -6, -6)

        return self.player_char_effects()

    def attack_output(self, opponent, strike_type, strike_dir, strike_power, defence_type, defence_dir):
        # generating random number
        random_num = random.randint(0, 100)

        # editing of levels
        if defence_type == "":
            self.defence_none(strike_dir, strike_power)
        elif player.weapon == Fists():
            self.fistfight()
        elif defence_type == "dodge":
            self.defence_dodge(opponent, strike_dir, strike_power, defence_dir)
        else:  # opponent action is block
            if opponent.weapon == opponent.unarmed_weapon and player.weapon != Fists():
                self.defence_none(strike_dir, strike_power)
            self.defence_block(opponent, strike_dir, strike_power, defence_dir)

        if player.difficulty == "easy":
            self.border_addition(-10, -10, -10)
        if player.difficulty == "nightmare":
            self.border_addition(5, 5, 5)

        # borders rounding part
        self.lower_border = round(self.lower_border, 1)
        self.middle_border = round(self.middle_border, 1)
        self.higher_border = round(self.higher_border, 1)

        # debug part
        if player.test is True:
            print(random_num, self.lower_border, self.middle_border, self.higher_border)

        # result
        last_action = "attack"

        if random_num <= self.lower_border:
            self.atk_conc.attack_major_fail(strike_dir, opponent, defence_type, defence_dir)
            last_action = "defence"
        elif random_num <= self.middle_border:
            self.atk_conc.attack_minor_fail(strike_dir, opponent, defence_type, defence_dir)
        elif random_num <= self.higher_border:
            self.atk_conc.attack_minor_success(strike_dir, strike_type, strike_power, opponent, defence_type,
                                               defence_dir)
        else:
            self.atk_conc.attack_major_success(strike_dir, strike_type, strike_power, opponent, defence_type,
                                               defence_dir)

        # health rounding part
        player.health = round(player.health, 1)
        opponent.health = round(opponent.health, 1)

        return last_action


class AttackPreparation:
    def __init__(self):
        self.atk_eval = AttackEvaluation()

        self.opponent = Opponent()
        self.action_split = 0
        self.opponent_action = ""
        self.opponent_last_action_I = ""
        self.opponent_last_action_II = ""
        self.opponent_direction = ""
        self.opponent_last_direction_I = ""
        self.opponent_last_direction_II = ""

        self.player_action = ""
        self.player_last_action_I = ""
        self.player_last_action_II = ""
        self.player_direction = ""
        self.player_last_direction_I = ""
        self.player_last_direction_II = ""
        self.player_power = ""
        self.player_last_power_I = ""
        self.player_last_power_II = ""

    def opponent_action_deciding(self):
        # TODO Upgrade opponent action choosing
        self.action_split = 20
        # player weapon effects
        if "stab" in player.weapon.damage_type:
            self.action_split += 1
        if player.weapon.weapon_type is "light":
            self.action_split += 4
        elif player.weapon.weapon_type is "heavy":
            self.action_split -= 4

        # opponent weapon effects
        if self.opponent.weapon.weapon_type is "light":
            self.action_split -= 2
        elif self.opponent.weapon.weapon_type is "heavy":
            self.action_split += 2

        # last player attack types effects
        if self.player_last_action_II is "stab":
            self.action_split -= 2
        if self.player_last_action_I is "stab":
            self.action_split -= 3
        if self.player_action is "stab":
            self.action_split -= 4

        # opponent last actions effects
        if self.opponent_last_action_II is "dodge":
            self.action_split += 1
        elif self.opponent_last_action_II is "block":
            self.action_split -= 1
        if self.opponent_last_action_I is "dodge":
            self.action_split += 2
        elif self.opponent_last_action_I is "block":
            self.action_split -= 2
        if self.opponent_action is "dodge":
            self.action_split += 3
        elif self.opponent_action is "block":
            self.action_split -= 3

        if self.player_last_power_II == "low":
            self.action_split -= 1
        elif self.player_last_power_II == "high":
            self.action_split += 1
        if self.player_last_power_I == "low":
            self.action_split -= 2
        elif self.player_last_power_I == "high":
            self.action_split += 2
        if self.player_power == "low":
            self.action_split -= 3
        elif self.player_power == "high":
            self.action_split += 3

    def opponent_defence_action(self, opponent):
        self.opponent = opponent

        if self.opponent.defence is []:
            self.opponent_action = ""
            return self.strike_type_choosing()
        elif "dodge" in self.opponent.defence and "block" not in self.opponent.defence:
            return self.opponent_dodge_direction()
        elif "block" in self.opponent.defence and "dodge" not in self.opponent.defence:
            return self.opponent_block_direction()
        else:
            if opponent.weapon == opponent.unarmed_weapon and player.weapon != Fists():
                return self.opponent_dodge_direction()

            self.opponent_action_deciding()

            self.opponent_last_action_II = self.opponent_last_action_I
            self.opponent_last_action_I = self.opponent_action

            opponent_action_num = random.randint(0, 39)

            if opponent_action_num < self.action_split:
                return self.opponent_block_direction()
            else:
                return self.opponent_dodge_direction()

    def opponent_block_direction(self):
        # TODO Upgrade block direction choosing
        self.opponent_action = "block"

        direction_num = random.randint(0, 64)
        lower_split = 20
        higher_split = 40
        special_split = 60

        if "stab" in player.weapon.damage_type:
            lower_split -= 1
            higher_split -= 2
            special_split -= 3

        # changing levels depending on last opponents directions
        if self.opponent_last_direction_II is "left" or self.opponent_last_direction_II is "terca":
            lower_split -= 2
            higher_split -= 1
        elif self.opponent_last_direction_II is "back" or self.opponent_last_direction_II is "kvinta":
            lower_split += 1
            higher_split -= 1
        elif self.opponent_last_direction_II is "right" or self.opponent_last_direction_II is "kvarta":
            lower_split += 1
            higher_split += 2
        elif self.opponent_last_direction_II is "second":
            lower_split += 2
            higher_split += 1
            special_split += 3

        if self.opponent_last_direction_I is "left" or self.opponent_last_direction_I is "terca":
            lower_split -= 2
            higher_split -= 1
        elif self.opponent_last_direction_I is "back" or self.opponent_last_direction_I is "kvinta":
            lower_split += 1
            higher_split -= 1
        elif self.opponent_last_direction_I is "right" or self.opponent_last_direction_I is "kvarta":
            lower_split += 1
            higher_split += 2
        elif self.opponent_last_direction_I is "second":
            lower_split += 2
            higher_split += 1
            special_split += 3

        if self.opponent_direction is "left" or self.opponent_direction is "terca":
            lower_split -= 4
            higher_split -= 2
        elif self.opponent_direction is "back" or self.opponent_direction is "kvinta":
            lower_split += 2
            higher_split -= 2
        elif self.opponent_direction is "right" or self.opponent_direction is "kvarta":
            lower_split += 2
            higher_split += 4
        elif self.opponent_direction is "second":
            lower_split += 4
            higher_split += 2
            special_split += 6

        # changing levels depending on last players directions
        if self.player_last_direction_II is "body":
            lower_split -= 3
            higher_split -= 6
            special_split -= 9
        elif self.player_last_direction_II is "side":
            lower_split += 4
            higher_split += 2
        elif self.player_last_direction_II is "belly":
            lower_split -= 2
            higher_split -= 4
        elif self.player_last_direction_II is "head":
            lower_split -= 2
            higher_split += 2

        if self.player_last_direction_I is "body":
            lower_split -= 4
            higher_split -= 8
            special_split -= 12
        elif self.player_last_direction_I is "side":
            lower_split += 6
            higher_split += 3
        elif self.player_last_direction_I is "belly":
            lower_split -= 3
            higher_split -= 6
        elif self.player_last_direction_I is "head":
            lower_split -= 3
            higher_split += 3

        if self.player_direction is "body":
            lower_split -= 5
            higher_split -= 10
            special_split -= 15
        elif self.player_direction is "side":
            lower_split += 8
            higher_split += 4
        elif self.player_direction is "belly":
            lower_split -= 4
            higher_split -= 8
        elif self.player_direction is "head":
            lower_split -= 4
            higher_split += 4

        self.opponent_last_direction_II = self.opponent_last_direction_I
        self.opponent_last_direction_I = self.opponent_direction

        if direction_num < lower_split:
            self.opponent_direction = "terca"
        elif direction_num < higher_split:
            self.opponent_direction = "kvinta"
        elif direction_num < special_split:
            self.opponent_direction = "kvarta"
        else:
            self.opponent_direction = "second"

        if player.test is False:
            return self.strike_type_choosing()

        return self.opponent_action_debug()

    def opponent_dodge_direction(self):
        # TODO Upgrade dodge direction choosing
        self.opponent_action = "dodge"

        direction_num = random.randint(0, 59)
        lower_split = 20
        higher_split = 40

        # changing levels depending on last opponents directions
        if self.opponent_last_direction_II is "left" or self.opponent_last_direction_II is "terca":
            lower_split -= 2
            higher_split -= 1
        elif self.opponent_last_direction_II is "back" or self.opponent_last_direction_II is "kvinta":
            lower_split += 1
            higher_split -= 1
        elif self.opponent_last_direction_II is "right" or self.opponent_last_direction_II is "kvarta":
            lower_split += 1
            higher_split += 2

        if self.opponent_last_direction_I is "left" or self.opponent_last_direction_I is "terca":
            lower_split -= 2
            higher_split -= 1
        elif self.opponent_last_direction_I is "back" or self.opponent_last_direction_I is "kvinta":
            lower_split += 1
            higher_split -= 1
        elif self.opponent_last_direction_I is "right" or self.opponent_last_direction_I is "kvarta":
            lower_split += 1
            higher_split += 2

        if self.opponent_direction is "left" or self.opponent_direction is "terca":
            lower_split -= 4
            higher_split -= 2
        elif self.opponent_direction is "back" or self.opponent_direction is "kvinta":
            lower_split += 2
            higher_split -= 2
        elif self.opponent_direction is "right" or self.opponent_direction is "kvarta":
            lower_split += 2
            higher_split += 4

        # changing levels depending on last players directions
        if self.player_last_direction_II is "body" or self.player_last_direction_II is "head":
            lower_split += 3
            higher_split -= 3
        elif self.player_last_direction_II is "side":
            lower_split -= 2
            higher_split += 1
        elif self.player_last_direction_II is "belly":
            lower_split -= 1
            higher_split += 2

        if self.player_last_direction_I is "body" or self.player_last_direction_I is "head":
            lower_split += 4
            higher_split -= 4
        elif self.player_last_direction_I is "side":
            lower_split -= 4
            higher_split += 2
        elif self.player_last_direction_I is "belly":
            lower_split -= 2
            higher_split += 4

        if self.player_direction is "body" or self.player_direction is "head":
            lower_split += 5
            higher_split -= 5
        elif self.player_direction is "side":
            lower_split -= 6
            higher_split += 3
        elif self.player_direction is "belly":
            lower_split -= 3
            higher_split += 6

        if self.player_direction is "body" or self.player_direction is "head":
            lower_split += 5
            higher_split -= 5
        elif self.player_direction is "side":
            lower_split -= 6
            higher_split += 3
        elif self.player_direction is "belly":
            lower_split -= 3
            higher_split += 6

        self.opponent_last_direction_II = self.opponent_last_direction_I
        self.opponent_last_direction_I = self.opponent_direction

        if direction_num < lower_split:
            self.opponent_direction = "left"
        elif direction_num < higher_split:
            self.opponent_direction = "back"
        else:
            self.opponent_direction = "right"

        if player.test is True:
            return self.opponent_action_debug()

        return self.strike_type_choosing()

    def opponent_action_debug(self):
        print(self.opponent_action, "-", self.opponent_direction, ",", self.opponent_last_action_I, "-",
              self.opponent_last_direction_I, ",", self.opponent_last_action_II, "-",
              self.opponent_last_direction_II)

        return self.strike_type_choosing()

    def strike_type_choosing(self):
        self.player_last_action_II = self.player_last_action_I
        self.player_last_action_I = self.player_action

        self.player_last_direction_II = self.player_last_direction_I
        self.player_last_direction_I = self.player_direction

        if "cut" and "stab" in player.weapon.damage_type:
            while True:
                slow_print("Chcete [b]odat, nebo [s]ekat?")
                attack_type = base_options()
                if attack_type == "b":
                    self.player_action = "stab"
                    return self.strike_direction_two()
                elif attack_type == "s":
                    self.player_action = "cut"
                    break
                elif attack_type != "skip":
                    wrong_input()

        elif "cut" in player.weapon.damage_type:
            self.player_action = "cut"

        elif "stab" in player.weapon.damage_type:
            self.player_action = "stab"

        elif player.weapon.weapon_class == "unarmed":
            self.player_action = "punch"

            return self.strike_direction_two()

        elif "smash" in player.weapon.damage_type:
            self.player_action = "smash"

        return self.strike_direction_three()

    def strike_direction_two(self):
        if self.player_action == "stab":
            while True:
                slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
                attack_direction = base_options()
                if attack_direction == "t":
                    self.player_direction = "body"
                    break
                elif attack_direction == "h":
                    self.player_direction = "head"
                    break
                elif attack_direction != "skip":
                    wrong_input()

        elif self.player_action == "punch":
            while True:
                slow_print("Chcete ho praštit do [h]lavy, nebo do [b]řicha?")
                attack_direction = base_options()
                if attack_direction == "b":
                    self.player_direction = "body"
                    break
                elif attack_direction == "h":
                    self.player_direction = "head"
                    break
                elif attack_direction != "skip":
                    wrong_input()

        return self.strike_power_choosing()

    def strike_direction_three(self):
        while True:
            slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
            attack_direction = base_options()
            if attack_direction == "h":
                self.player_direction = "head"
                break
            elif attack_direction == "o":
                self.player_direction = "side"
                break
            elif attack_direction == "b":
                self.player_direction = "belly"
                break
            elif attack_direction != "skip":
                wrong_input()

        return self.strike_power_choosing()

    def strike_power_choosing(self):
        self.player_last_power_II = self.player_last_power_I
        self.player_last_power_I = self.player_power

        while True:
            slow_print("Jakou moc se chcete rozmáchnout, [m]álo, [s]tředně, nebo [h]odně?\n")
            power_selection = base_options()
            if power_selection == "m":
                self.player_power = "small"
                break
            elif power_selection == "s":
                self.player_power = "medium"
                break
            elif power_selection == "h":
                self.player_power = "high"
                break
            elif power_selection != "skip":
                wrong_input()

        return self.atk_eval.attack_output(self.opponent, self.player_action, self.player_direction, self.player_power,
                                           self.opponent_action, self.opponent_direction)
