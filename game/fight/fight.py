from random import randint, choice
from game.movement.room_info import RoomInfo
from game.important_modules.main_funcs import slow_print, player_killed, clearing_screen
from game.fight.preparation import Preparation
from game.fight.combat_modules.combat import Combat
from game.character_stats.opponent import Opponent
from game.equipment_stats.armor_stats.helmet_stats import Helmet
from game.equipment_stats.armor_stats.chest_armor_stats import ChestArmor
from game.equipment_stats.weapon import Fists


# TODO Add fighting multiple opponents
class Fight:
    def __init__(self, player, room_info=RoomInfo()):
        self.room_info = room_info

        self.player = player
        self.opponents = Preparation(self.player, self.room_info).main()

    def main(self):
        while self.finding_if_any_opponents_live():
            attacker = self.choosing_attacker()
            defender = self.choosing_defender(attacker)

            Combat(attacker, defender).main()

            self.applying_special_effects()

            if self.player.health <= 0:
                return []

            self.fight_status()

        else:
            return self.all_opponents_dead()

    def finding_if_any_opponents_live(self):
        pass

    def choosing_attacker(self):
        attacker = self.player
        for character in self.opponents:
            if character.balance > attacker.balance:
                attacker = character
        return attacker

    def choosing_defender(self, attacker):
        if not attacker.player_controlled:
            defender = self.player
        else:
            defender = choice(self.opponents)
        return defender

    def applying_special_effects(self):
        pass

    def fight_status(self):
        for character in [self.player] + self.opponents:
            slow_print(str(character))

    def all_opponents_dead(self):
        pass


class _Fight:
    def __init__(self, player):
        self.player = player

        self.opponents = [Opponent]

    def main(self, fight_level):
        # preparation
        self.opponents = Preparation(self.player).opponents_creation(fight_level)

        self.opponent_introduction()

        last_action = Preparation(self.player).first_fight_action(self.opponents)

        Preparation(self.player).special_fight_techniques()

        # fight
        while self.finding_if_any_opponents_live():


            self.fight_status()

            if (last_action == "defence" or "stun" in
                    self.opponent.special_abilities) and "stun" not in self.player.special_abilities:
                last_action = self.attack.opponent_defence_action(self.opponent)

            else:
                last_action = self.defence.opponent_attack_action(self.opponent)

            self.special_effects()

        return self.fight_resetting()

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

    def finding_if_any_opponents_live(self):
        pass

    def fight_status(self):
        slow_print("    Váš život: {}/{}".format(self.player.health, self.player.max_health))

        for opponent in self.opponents:
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

            slow_print("\t{} vypadá {}".format(opponent.name, opponent_health_state).capitalize())
            if self.player.test is True:
                print("        {}/{}".format(opponent.health, opponent.max_health))

            return

    def special_effects(self):
        if "no_right_arm" in self.player.special_abilities and "no_left_arm" in self.player.special_abilities:
            slow_print("Poté co vám už nezbyly žádné ruce nemohli jste se bránito soupeři a ten vás jednoduše dorazil.")
            player_killed()

        if "no_right_arm" in self.opponent.special_abilities and "no_left_arm" in self.opponent.special_abilities:
            slow_print("Poté co jste soupeře připravili o poslední ruku jste ho ještě stihli rychlým úderem"
                       " připravit i o život.\n")
            self.opponent.health = 0
        # player gear destruction
        if self.player.weapon.hit_points <= 0 and self.player.weapon.weapon_class != "unarmed":
            self.player.weapon = Fists()
            slow_print("Rozbila se vám zbraň.\n")
        if self.player.helmet.hit_points <= 0 and self.player.helmet != Helmet():
            self.player.helmet = Helmet()
            slow_print("Rozbila se vám helma.\n")
        if self.player.armor.hit_points <= 0 and self.player.armor != ChestArmor():
            self.player.armor = ChestArmor()
            slow_print("Rozbilo se vám brnění.\n")

        # opponent gear destruction
        if self.opponent.weapon.hit_points <= 0 and self.opponent.weapon.weapon_class != "unarmed":
            self.opponent.weapon = self.opponent.unarmed_weapon
            slow_print("Soupeřova zbraň nevydržela úder té vaší a roztříštila se na kusy.\n")
        if self.opponent.helmet.hit_points <= 0 and self.opponent.helmet != Helmet():
            self.opponent.helmet = Helmet()
            slow_print("Vaše rána soupeři rozbila helmu.\n")
        if self.opponent.armor.hit_points <= 0 and self.opponent.armor != ChestArmor():
            self.opponent.armor = ChestArmor()
            slow_print("Vaše rána soupeři rozbila brnění.\n")

        # rusty effect on opponent
        if "rusty" in self.opponent.helmet.special_abilities and randint(0, 4) == 3:
            self.opponent.health -= 10
            slow_print("Váš soupeř se ošklivě pořezal o svoji helmu.\n")
        if "rusty" in self.opponent.armor.special_abilities and randint(0, 3) == 3:
            self.opponent.health -= 10
            slow_print("Váš soupeř se ošklivě pořezal o svoje brnění.\n")

        # rusty effect on player
        if "rusty" in self.player.helmet.special_abilities and randint(0, 4) == 3:
            self.player.health -= 10
            slow_print("Ošklivě jste se pořezali o svoji helmu.\n")
        if "rusty" in self.player.armor.special_abilities and randint(0, 3) == 3:
            self.player.health -= 10
            slow_print("Ošklivě jste se pořezali o svoje brnění.\n")

        # bleeding effects
        if "no_bleeding" not in self.player.special_abilities:
            if "bleeding_1" in self.player.special_abilities:
                self.player.special_abilities.remove("bleeding_1")
                if "bleeding_resistance" in self.player.special_abilities:
                    self.player.health -= 5
                else:
                    self.player.health -= 15
            elif "bleeding_2" in self.player.special_abilities:
                self.player.special_abilities.remove("bleeding_2")
                self.player.special_abilities.append("bleeding_1")
                if "bleeding_resistance" in self.player.special_abilities:
                    self.player.health -= 10
                else:
                    self.player.health -= 25
            elif "bleeding_3" in self.player.special_abilities:
                self.player.special_abilities.remove("bleeding_3")
                self.player.special_abilities.append("bleeding_2")
                if "bleeding_resistance" in self.player.special_abilities:
                    self.player.health -= 20
                else:
                    self.player.health -= 40

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

        if "stun" in self.player.special_abilities:
            self.player.special_abilities.append("stun_effect")
            self.player.special_abilities.remove("stun")
        elif "stun_effect" in self.player.special_abilities:
            self.player.special_abilities.remove("stun_effect")
        elif "super_stun" in self.player.special_abilities:
            self.player.special_abilities.append("stun")
            self.player.special_abilities.remove("super_stun")

        if "stun" in self.opponent.special_abilities:
            self.opponent.special_abilities.append("stun_effect")
            self.opponent.special_abilities.remove("stun")
        elif "stun_effect" in self.opponent.special_abilities:
            self.opponent.special_abilities.remove("stun_effect")
        elif "super_stun" in self.opponent.special_abilities:
            self.opponent.special_abilities.append("stun")
            self.opponent.special_abilities.remove("super_stun")

        return

    def fight_resetting(self):
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


if __name__ == '__main__':
    from game.character_stats.player import all_player_types
    fight = Fight(all_player_types[0])
