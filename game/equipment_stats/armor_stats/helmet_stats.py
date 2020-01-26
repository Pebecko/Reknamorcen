from game.equipment_stats.armor_stats.armor import Armor


class Helmet(Armor):
    visibility = 0


class RustyOrkHelmet(Helmet):
    name = "rezavá orkská helma"
    info = "vyrobená skřety ve velmi primitivní podmínkách velmi primitivními nástroji, která se" \
           " pak někde dlouho válela, nejspíš i s mrtvolou mrtvého orka, takže je dosti zrezlá a" \
           " nositel si musí dát pozor aby se omylem nepořezal. Je velmi těžká ale hlavu docela ochrání"
    visibility = 2  # 0 - 3
    heaviness = 10  # 1 - 10
    loudness = 3
    min_durability = 800
    max_durability = 1_600
    cut_damage_reduction = 7  # 1 - 10(%)
    stab_damage_reduction = 2  # 1 - 10(%)
    smash_damage_reduction = 3  # 1 - 10(%)
    item_traits = ["rusty"]


class DwarvenMinerHelmet(Helmet):
    name = "trpasličí důlnická helma"
    info = "používaná trpaslíky v dolech slouží spíše jako ochrana hlavy při chození tunelem než" \
           " na boj, ale část úderu rozhodně zastaví"
    visibility = 1
    loudness = 2
    min_durability = 3_000
    max_durability = 9_000
    cut_damage_reduction = 5
    stab_damage_reduction = 3
    smash_damage_reduction = 5


class GromrilHelmet(Helmet):
    name = "gromrilová přilba"
    info = "přilba vyrobená trpaslíky z nejtvrdšího kovu jim známého, gromrilu, který nejen že je ohromně pevný, ale" \
           " dokonce ho jeho váhu na sobě nositel téměř necítí, bohužel je ohromně vzácný a tak se tato brnění" \
           " předávájí z generace na generaci a každý klan jich má jen pár jestli nějaká má"
    level = 3
    visibility = 3
    heaviness = 3
    loudness = 3
    hit_points = 1_000_000
    cut_damage_reduction = 10
    stab_damage_reduction = 10
    smash_damage_reduction = 10


class GuardsmenHelmet(Helmet):
    pass


class ElvenPathfinderHelmet(Helmet):
    pass
