from random import randint, choice
from game.character_stats.opponent import all_opponent_types
from game.important_modules.main_funcs import slow_print, base_options, wrong_input
from game.equipment_stats.weapon import ShortSword, ShortSwordMordhau, LongSword, LongSwordMordhau, \
    TwoHandedSword, TwoHandedSwordMordhau


class Preparation:
    def __init__(self, player, room_info):
        self.player = player
        self.room_info = room_info

        self.opponents = []

    def main(self):
        self.opponents_creation()

        self.setting_base_balance()

        self.special_fight_techniques()

        self.opponents_introduction()

        return self.opponents

    def opponents_creation(self):
        race = self.setting_opponents_race()

        while len(self.opponents) <= 5:
            possible_opponents = self.choosing_possible_opponents(race)

            if not possible_opponents:
                return
            else:
                self.opponents.append(choice(possible_opponents))

    def setting_opponents_race(self):
        if self.room_info.race is not None:
            possible_races = [self.room_info.race for _ in range(5)]
        else:
            possible_races = []

        for opponent in all_opponent_types:
            if opponent.race not in possible_races:
                possible_races.append(opponent.race)

        return possible_races

    def choosing_possible_opponents(self, race):
        possible_opponents = []

        opponents_size = self.finding_opponents_size()

        for opponent in all_opponent_types:
            if opponent.race == race and opponent.size <= self.room_info.size - opponents_size:
                possible_opponents.append(opponent)

        return possible_opponents

    def finding_opponents_size(self):
        opponents_size = 0

        for opponent in self.opponents:
            opponents_size += opponent.size

        return opponents_size

    def setting_base_balance(self):
        pass

    def special_fight_techniques(self):
        pass

    def opponents_introduction(self):
        message = "=" * 20

        for num, opponent in enumerate(self.opponents):
            if num == 0:
                message += "Stojí před vámi {}\n".format(str(opponent))
            else:
                message += "Dále před vámi stojí {}\n".format(str(opponent))
            #
            # if opponent.weapon.number == "sin":
            #     slow_print(" Jeho zbraň je {}.\n".format(opponent.weapon.name))
            # elif opponent.weapon.number == "plu":
            #     slow_print(" Jeho zbraně jsou {}.\n".format(opponent.weapon.name))
            #
            # if isinstance(opponent.armor, Armor):
            #     slow_print("Jeho brnění je {}\n".format(opponent.armor.name))
            # if isinstance(opponent.helmet, Helmet):
            #     slow_print("Jeho helma je {}\n".format(opponent.helmet.name))


class _Preparation:
    def __init__(self, player):
        self.player = player

    def opponents_creation(self, opponent_level):



        if opponent_level == 0:
            num = 2
            if player.difficulty == "hard":
                num = 3
            opponent_level = randint(1, num)

        if opponent_level == 1:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                opponent = SmallSpider()

        elif opponent_level == 2:
            opponent_number = randint(0, 1)
            if opponent_number == 0:
                opponent = Skeleton()
            else:
                opponent = Zombie()

        elif opponent_level == 3:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                opponent = OrkBoy()

        elif opponent_level == 4:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                pass

        elif opponent_level == 5:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                pass

        else:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                pass

        opponent.health = randint(opponent.lowest_health, opponent.highest_health)
        opponent.max_health = opponent.health
        opponent.weapon = choice(opponent.weapons)
        opponent.helmet = choice(opponent.helmets)
        opponent.weapon = choice(opponent.weapons)

        return opponents

    @staticmethod
    def first_fight_action(opponent):
        loudness = opponent.awareness
        if player.last_fight is True:
            loudness += 4
        if player.char == "dwarf":
            loudness += 3
        elif player.char == "human":
            loudness += 2
        loudness += player.helmet.loudness
        loudness += player.armor.loudness
        first_opponent_action = "defence"
        if loudness > 20:
            first_opponent_action = "attack"
        elif loudness > 10:
            if randint(0, loudness) < 10:
                first_opponent_action = "attack"

        return first_opponent_action

    @staticmethod
    def special_fight_techniques():
        if "mordhau" in player.weapon.special_abilities:
            while True:
                slow_print("Chcete si meč [o]točit, abyste s ním mohli mlátit spíše než sekat, nebo [n]e??")
                style_decision = base_options()
                if style_decision == "o":
                    if isinstance(player.weapon, ShortSword):
                        player.weapon = ShortSwordMordhau(player.weapon.hit_points)
                    elif isinstance(player.weapon, LongSword):
                        player.weapon = LongSwordMordhau(player.weapon.hit_points)
                    elif isinstance(player.weapon, TwoHandedSword):
                        player.weapon = TwoHandedSwordMordhau(player.weapon.hit_points)
                    break
                elif style_decision == "n":
                    break
                elif style_decision != "skip":
                    wrong_input()

            return
