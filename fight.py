from Fight_modules.preparation import *
from Fight_modules.attack import *
from Fight_modules.defence import *
from Fight_modules.conclusion import Conclusion


class Fight:
    def __init__(self):
        self.preparation = Preparation()
        self.attack = AttackPreparation()
        self.defence = DefencePreparation()
        self.conclusion = Conclusion()

        self.opponent = Opponent()

    def main_(self, opponent_level):
        # preparation
        self.opponent = self.preparation.opponent_creation(opponent_level)

        self.opponent_introduction()

        last_action = self.preparation.first_fight_action(self.opponent)

        self.preparation.special_fight_techniques()

        # fight
        while self.opponent.health > 0:
            if player.health <= 0:
                player_killed()

            self.fight_status()

            if (last_action == "defence" or "stun" in
                self.opponent.special_abilities) and "stun" not in player.special_abilities:
                last_action = self.attack.opponent_defence_action(self.opponent)

            else:
                last_action = self.defence.opponent_attack_action(self.opponent)

            self.special_effects()

        return self.fight_reseting()

    def opponent_introduction(self):
        slow_print("Stojí před vámi {}.\n".format(self.opponent.name))
        if self.opponent.weapon.number == "sin":
            slow_print("Jeho zbraň je {}.\n".format(self.opponent.weapon.name))
        elif self.opponent.weapon.number == "plu":
            slow_print("Jeho zbraň jsou {}.\n".format(self.opponent.weapon.name))

        if self.opponent.armor.name != "":
            slow_print("Jeho brnění je {}\n".format(self.opponent.armor.name))
        if self.opponent.helmet.name != "":
            slow_print("Jeho helma je {}\n".format(self.opponent.helmet.name))

    def fight_status(self):
        if self.opponent.max_health * 0.95 <= self.opponent.health:
            opponent_health_state = "bez zranění"
        elif self.opponent.max_health * 0.75 <= self.opponent.health:
            opponent_health_state = "lehce zraněn"
        elif self.opponent.max_health * 0.40 <= self.opponent.health:
            opponent_health_state = "středně zraněn"
        elif self.opponent.max_health * 0.20 <= self.opponent.health:
            opponent_health_state = "těžce zraněn"
        else:
            opponent_health_state = "velmi těžce zraněn"

        opponent_stamina_state = "plný energie"

        slow_print("    Váš život: {}/{}".format(player.health, player.max_health))
        slow_print("    Vaše energie: {}/{}\n".format(player.stamina, player.max_stamina))

        slow_print("    Soupeř vypadá {}".format(opponent_health_state))
        if player.test is True:
            print("        {}/{}".format(self.opponent.health, self.opponent.max_health))
        slow_print("    Soupeř vypadá {}".format(opponent_stamina_state))
        if player.test is True:
            print("        {}/{}\n".format(self.opponent.stamina, self.opponent.max_stamina))

        return

    def special_effects(self):
        if "no_right_arm" in player.special_abilities and "no_left_arm" in player.special_abilities:
            slow_print("Poté co vám už nezbyly žádné ruce nemohli jste se bránito soupeři a ten vás jednoduše dorazil.")
            player_killed()

        if "no_right_arm" in self.opponent.special_abilities and "no_left_arm" in self.opponent.special_abilities:
            slow_print("Poté co jste soupeře připravili o poslední ruku jste ho ještě stihli rychlým úderem"
                       " připravit i o život.\n")
            self.opponent.health = 0
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
        if self.opponent.weapon.hit_points <= 0 and self.opponent.weapon.weapon_class != "unarmed":
            self.opponent.weapon = self.opponent.unarmed_weapon
            slow_print("Soupeřova zbraň nevydržela úder té vaší a roztříštila se na kusy.\n")
        if self.opponent.helmet.hit_points <= 0 and self.opponent.helmet != no_helmet:
            self.opponent.helmet = no_helmet
            slow_print("Vaše rána soupeři rozbila helmu.\n")
        if self.opponent.armor.hit_points <= 0 and self.opponent.armor != no_armor:
            self.opponent.armor = no_armor
            slow_print("Vaše rána soupeři rozbila brnění.\n")

        # rusty effect on opponent
        if "rusty" in self.opponent.helmet.special_abilities and random.randint(0, 4) == 3:
            self.opponent.health -= 10
            slow_print("Váš soupeř se ošklivě pořezal o svoji helmu.\n")
        if "rusty" in self.opponent.armor.special_abilities and random.randint(0, 3) == 3:
            self.opponent.health -= 10
            slow_print("Váš soupeř se ošklivě pořezal o svoje brnění.\n")

        # rusty effect on player
        if "rusty" in player.helmet.special_abilities and random.randint(0, 4) == 3:
            player.health -= 10
            slow_print("Ošklivě jste se pořezali o svoji helmu.\n")
        if "rusty" in player.armor.special_abilities and random.randint(0, 3) == 3:
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

        if "no_bleeding" not in self.opponent.special_abilities:
            if "bleeding_1" in self.opponent.special_abilities:
                self.opponent.special_abilities.remove("bleeding_1")
                if "bleeding_resistance" in self.opponent.special_abilities:
                    self.opponent.health -= 5
                else:
                    self.opponent.health -= 15
            elif "bleeding_2" in self.opponent.special_abilities:
                self.opponent.special_abilities.remove("bleeding_2")
                self.opponent.special_abilities.append("bleeding_1")
                if "bleeding_resistance" in self.opponent.special_abilities:
                    self.opponent.health -= 10
                else:
                    self.opponent.health -= 25
            elif "bleeding_3" in self.opponent.special_abilities:
                self.opponent.special_abilities.remove("bleeding_3")
                self.opponent.special_abilities.append("bleeding_2")
                if "bleeding_resistance" in self.opponent.special_abilities:
                    self.opponent.health -= 20
                else:
                    self.opponent.health -= 40

        if "stun" in player.special_abilities:
            player.special_abilities.append("stun_effect")
            player.special_abilities.remove("stun")
        elif "stun_effect" in player.special_abilities:
            player.special_abilities.remove("stun_effect")
        elif "super_stun" in player.special_abilities:
            player.special_abilities.append("stun")
            player.special_abilities.remove("super_stun")

        if "stun" in self.opponent.special_abilities:
            self.opponent.special_abilities.append("stun_effect")
            self.opponent.special_abilities.remove("stun")
        elif "stun_effect" in self.opponent.special_abilities:
            self.opponent.special_abilities.remove("stun_effect")
        elif "super_stun" in self.opponent.special_abilities:
            self.opponent.special_abilities.append("stun")
            self.opponent.special_abilities.remove("super_stun")

        return

    def fight_reseting(self):
        self.attack.opponent_action = ""
        self.attack.opponent_last_action_I = ""
        self.attack.opponent_last_action_II = ""
        self.attack.opponent_direction = ""
        self.attack.opponent_last_direction_I = ""
        self.attack.opponent_last_direction_II = ""
        self.attack.player_action = ""
        self.attack.player_last_action_I = ""
        self.attack.player_last_action_II = ""
        self.attack.player_direction = ""
        self.attack.player_last_direction_I = ""
        self.attack.player_last_direction_II = ""
        self.attack.player_power = ""
        self.attack.player_last_power_I = ""
        self.attack.player_last_power_II = ""

        self.conclusion.returning_from_technique()
