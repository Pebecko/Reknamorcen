from Fight_modules.preparation import *
from Fight_modules.attack import Attack
from Fight_modules.defence import Defence
from Fight_modules.conclusion import Conclusion


class Fight:
    preparation = Preparation()
    attack = Attack()
    defence = Defence()
    conclusion = Conclusion()

    def __init__(self, opponent_level):
        self.opponent_level = opponent_level

    def main_(self):
        # preparation
        opponent = self.preparation.opponent_creation(self.opponent_level)
        slow_print("Stojí před vámi {}, {}. A jeho zbraň je {}, {}.\n"
                   "".format(opponent.name, opponent.info, opponent.weapon.name, opponent.weapon.info))
        if opponent.armor.name != "":
            slow_print("Jeho brnění je {}, {}\n".format(opponent.armor.name, opponent.armor.info))
        if opponent.helmet != "":
            slow_print("Jeho helma je {}, {}\n".format(opponent.helmet.name, opponent.helmet.info))
        print("")

        last_action = self.preparation.first_fight_action(opponent)

        self.preparation.special_fight_techniques()

        # fight
        while opponent.health > 0:
            if player.health <= 0:
                player_killed()

            self.fight_status(opponent)

            # útok na soupeře
            if last_action == "defence":
                if player.test is True:
                    print("Opponent weapon, helmet, armor info:", opponent.weapon.hit_points, opponent.helmet.hit_points,
                        opponent.armor.hit_points, "\n")
                last_action = self.attack.strike_direction_choosing(opponent)

            # test part
            last_action = "defence"

            # obrana před soupeřovým útokem
            """
            else:
                last_action = self.random_num_definition(self.guard_choosing)
            """

            self.special_effects(opponent)

        self.opponent_action = ""
        self.opponent_last_action_I = ""
        self.opponent_last_action_II = ""
        self.last_attack_zone = ""

        self.conclusion.returning_from_technique()

        return

    def fight_status(self, opponent):
        if opponent.max_health * 0.95 <= opponent.health:
            opponent_health_state = "bez zranění"
        elif opponent.max_health * 0.75 <= opponent.health:
            opponent_health_state = "lehce zraněn"
        elif opponent.max_health * 0.40 <= opponent.health:
            opponent_health_state = "středně zraněn"
        elif opponent.max_health * 0.20 <= opponent.health:
            opponent_health_state = "těžce zraněn"
        else:
            opponent_health_state = "velmi těžce zraněn"
        opponent_stamina_state = "plný energie"
        time.sleep(0.3)
        slow_print("    Váš život: " + str(player.health) + "/" + str(player.max_health))
        slow_print("    Vaše energie: " + str(player.weapon.stamina) + "/" + str(player.weapon.max_stamina) + "\n")
        time.sleep(0.3)
        slow_print("    Soupeř vypadá " + opponent_health_state)
        if player.test is True:
            print("        ", opponent.health, "/", opponent.max_health)
        slow_print("    Soupeř vypadá " + opponent_stamina_state + "\n")
        if player.test is True:
            print("        ", opponent.weapon.stamina, "/", opponent.weapon.max_stamina, "\n")
        time.sleep(0.25)

        return

    def special_effects(self, opponent):
        # player gear destruction
        if player.weapon.hit_points <= 0 and player.weapon.weapon_class != "unarmed":
            player.weapon = fists
            slow_print("Rozbila se vám zbraň.\n")
        if player.helmet.hit_points <= 0 and player.helmet != no_helmet:
            player.helmet = no_helmet
            slow_print("Rozbila se vám helma.\n")
        if player.armor.hit_points <= 0 and player.armor != no_armor:
            player.armor = no_armor
            slow_print("Rozbilo se vám brnění.\n")

        # opponent gear destruction
        if opponent.weapon.hit_points <= 0 and opponent.weapon.weapon_class != "unarmed":
            opponent.weapon = opponent.unarmed_weapon
            slow_print("Soupeřova zbraň nevydržela úder té vaší a roztříštila se na kusy.\n")
        if opponent.helmet.hit_points <= 0 and opponent.helmet != no_helmet:
            opponent.helmet = no_helmet
            slow_print("Vaše rána soupeři rozbila helmu.\n")
        if opponent.armor.hit_points <= 0 and opponent.armor != no_armor:
            opponent.armor = no_armor
            slow_print("Vaše rána soupeři rozbila brnění.\n")

        # rusty effect on opponent
        if "rusty" in opponent.helmet.special_abilities:
            if random.randint(0, 4) == 3:
                opponent.health -= 10
                slow_print("Váš soupeř se ošklivě pořezal o svoji helmu.\n")
        if "rusty" in opponent.armor.special_abilities:
            if random.randint(0, 3) == 3:
                opponent.health -= 10
                slow_print("Váš soupeř se ošklivě pořezal o svoje brnění.\n")

        # rusty effect on player
        if "rusty" in player.helmet.special_abilities:
            if random.randint(0, 4) == 3:
                player.health -= 10
                slow_print("Ošklivě jste se pořezali o svoji helmu.\n")
        if "rusty" in player.armor.special_abilities:
            if random.randint(0, 3) == 3:
                player.health -= 10
                slow_print("Ošklivě jste se pořezali o svoje brnění.\n")

        # bleeding effects
        if "no_bleeding" not in player.special_abilities:
            if "bleeding_1" in player.special_abilities:
                player.special_abilities.remove("bleeding_1")
                if "bleeding_resistance" in player.special_abilities:
                    player.health -= 5
                else:
                    player.health -= 15
            elif "bleeding_2" in player.special_abilities:
                player.special_abilities.remove("bleeding_2")
                player.special_abilities.append("bleeding_1")
                if "bleeding_resistance" in player.special_abilities:
                    player.health -= 10
                else:
                    player.health -= 25
            elif "bleeding_3" in player.special_abilities:
                player.special_abilities.remove("bleeding_3")
                player.special_abilities.append("bleeding_2")
                if "bleeding_resistance" in player.special_abilities:
                    player.health -= 20
                else:
                    player.health -= 40

        if "no_bleeding" not in opponent.special_abilities:
            if "bleeding_1" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_1")
                if "bleeding_resistance" in opponent.special_abilities:
                    opponent.health -= 5
                else:
                    opponent.health -= 15
            elif "bleeding_2" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_2")
                opponent.special_abilities.append("bleeding_1")
                if "bleeding_resistance" in opponent.special_abilities:
                    opponent.health -= 10
                else:
                    opponent.health -= 25
            elif "bleeding_3" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_3")
                opponent.special_abilities.append("bleeding_2")
                if "bleeding_resistance" in opponent.special_abilities:
                    opponent.health -= 20
                else:
                    opponent.health -= 40

        return


"""
fight = Fight(2)
fight.main_()
"""