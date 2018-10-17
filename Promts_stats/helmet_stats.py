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


# helmets
no_helmet = Helmet()

dwarven_miner_helmet = Helmet()
dwarven_miner_helmet.name = "trpasličí důlnická helma"
dwarven_miner_helmet.info = "používaná trpaslíky v dolech slouží spíše jako ochrana hlavy při chození tunelem než" \
                            " na boj, ale část úderu rozhodně zastaví"
dwarven_miner_helmet.level = 1
dwarven_miner_helmet.visibility = 1
dwarven_miner_helmet.loudness = 2
dwarven_miner_helmet.cut_damage_reduction = 5
dwarven_miner_helmet.stab_damage_reduction = 3
dwarven_miner_helmet.smash_damage_reduction = 5

rusty_ork_helmet = Helmet()
rusty_ork_helmet.name = "rezavá orkská helma"
rusty_ork_helmet.info = "vyrobená skřety ve velmi primitivní podmínkách velmi primitivními nástroji, která se" \
                        " pak někde dlouho válela, nejspíš i s mrtvolou mrtvého orka, takže je dosti zrezlá a" \
                        " nositel si musí dát pozor aby se omylem nepořezal. Je velmi těžká ale hlavu docela ochrání"
rusty_ork_helmet.level = 1  # 1 - 3
rusty_ork_helmet.visibility = 1  # 0 - 3
rusty_ork_helmet.heaviness = 10  # 1 - 10
rusty_ork_helmet.loudness = 3
rusty_ork_helmet.hit_points = 500
rusty_ork_helmet.cut_damage_reduction = 8  # 1 - 10(%)
rusty_ork_helmet.stab_damage_reduction = 2  # 1 - 10(%)
rusty_ork_helmet.smash_damage_reduction = 3  # 1 - 10(%)
rusty_ork_helmet.special_abilities = ["rusty", "elf_debuff"]

helmet_1 = dwarven_miner_helmet

helmet_2 = rusty_ork_helmet
helmet_2.hit_points += 500
