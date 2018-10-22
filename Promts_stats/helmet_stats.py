class Helmet:
    name = ""
    info = ""
    level = 0
    visibility = 0
    _type = ""
    heaviness = 0
    loudness = 0
    hit_points = 10000
    cut_damage_reduction = 0  # 1 - 10(%)
    stab_damage_reduction = 0  # 1 - 10(%)
    smash_damage_reduction = 0  # 1 - 10(%)
    special_abilities = []
    occupied = False


no_helmet = Helmet()


# helmets patterns
class RustyOrkHelmet(Helmet):
    name = "rezavá orkská helma"
    info = "vyrobená skřety ve velmi primitivní podmínkách velmi primitivními nástroji, která se" \
           " pak někde dlouho válela, nejspíš i s mrtvolou mrtvého orka, takže je dosti zrezlá a" \
           " nositel si musí dát pozor aby se omylem nepořezal. Je velmi těžká ale hlavu docela ochrání"
    level = 1  # 1 - 3
    visibility = 1  # 0 - 3
    heaviness = 10  # 1 - 10
    loudness = 3
    hit_points = 2000
    cut_damage_reduction = 8  # 1 - 10(%)
    stab_damage_reduction = 2  # 1 - 10(%)
    smash_damage_reduction = 3  # 1 - 10(%)
    special_abilities = ["rusty", "elf_debuff"]


class DwarvenMinerHelmet(Helmet):
    name = "trpasličí důlnická helma"
    info = "používaná trpaslíky v dolech slouží spíše jako ochrana hlavy při chození tunelem než" \
           " na boj, ale část úderu rozhodně zastaví"
    level = 1
    visibility = 1
    loudness = 2
    cut_damage_reduction = 5
    stab_damage_reduction = 3
    smash_damage_reduction = 5


# helmets
class Helmet1(RustyOrkHelmet):
    hit_points = 500


class Helmet2(RustyOrkHelmet):
    pass


class Helmet3(DwarvenMinerHelmet):
    pass


helmet_1 = Helmet1()
helmet_2 = Helmet2()
helmet_3 = Helmet3()
