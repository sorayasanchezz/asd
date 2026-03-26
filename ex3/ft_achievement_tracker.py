import random


def gen_player_achievements() -> set:
    achievements = ['Crafting Genius', 'World Savior', 'Master Explorer',
                    'Collector Supreme', 'Untouchable', 'Boss Slayer',
                    'Strategist', 'Unstoppable', 'Speed Runner',
                    'Survivor', 'Treasure Hunter', 'First Steps',
                    'Sharp Mind', 'Hidden Path Finder']

    nb = random.randint(5, len(achievements))
    return set(random.sample(achievements, nb))


def track_achievements(alice: set, bob: set,
                       charlie: set, dylan: set,
                       achievements: set) -> None:

    # find all distinct achievements of players
    all_ach = alice.union(bob).union(charlie).union(dylan)
    print("\nAll distinct achievements:", all_ach)

    # common achievements
    inter = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print("\nCommon achievements:", inter)

    # achievements only one player has
    dif_alice = alice.difference(bob).difference(charlie).difference(dylan)
    dif_bob = bob.difference(alice).difference(charlie).difference(dylan)
    dif_charlie = charlie.difference(alice).difference(bob).difference(dylan)
    dif_dylan = dylan.difference(alice).difference(bob).difference(charlie)
    print("\nOnly Alice has:", dif_alice)
    print("Only Bob has:", dif_bob)
    print("Only Charlie has:", dif_charlie)
    print("Only Dylan has:", dif_dylan)

    # find the missing achievements
    print("\nAlice is missing:", achievements.difference(alice))
    print("Bob is missing:", achievements.difference(bob))
    print("Charlie is missing:", achievements.difference(charlie))
    print("Dylan is missing:", achievements.difference(dylan))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    # handle sets used to store achievements (without duplicates)
    achievements = {'Crafting Genius', 'World Savior', 'Master Explorer',
                    'Collector Supreme', 'Untouchable', 'Boss Slayer',
                    'Strategist', 'Unstoppable', 'Speed Runner',
                    'Survivor', 'Treasure Hunter', 'First Steps',
                    'Sharp Mind', 'Hidden Path Finder'}

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    track_achievements(alice, bob, charlie, dylan, achievements)
