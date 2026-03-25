def gen_player_achievements(alice: set, bob: set,
                            charlie: set, dylan: set) -> None:

    # find the coommon achievements of players
    common = alice.union(bob).union(charlie).union(dylan)
    print("\nAll distinct achievements:", common)

    # common achievements
    inter = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print("\nCommon achievements:", inter)

    # all distinct achievements
    dif_alice = alice.difference(bob).difference(charlie).difference(dylan)
    dif_bob = bob.difference(alice).difference(charlie).difference(dylan)
    dif_charlie = charlie.difference(alice).difference(bob).difference(dylan)
    dif_dylan = dylan.difference(alice).difference(bob).difference(charlie)
    print("\nOnly Alice has:", dif_alice)
    print("Only Bob has:", dif_bob)
    print("Only Charlie has:", dif_charlie)
    print("Only Dylan has:", dif_dylan)

    # find the unique achievements
    print("\nAlice is missing:", common.difference(alice))
    print("Bob is missing:", common.difference(bob))
    print("Charlie is missing:", common.difference(charlie))
    print("Dylan is missing:", common.difference(dylan))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    # handle sets used to store achevements (without duplicates)
    alice = {'Crafting Genius', 'World Savior', 'Master Explorer',
             'Collector Supreme', 'Untouchable', 'Boss Slayer'}
    bob = {'Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer',
           'Unstoppable', 'Collector Supreme', 'Untouchable'}
    charlie = {'Strategist', 'Speed Runner', 'Survivor', 'Master Explorer',
               'Treasure Hunter', 'First Steps', 'Collector Supreme',
               'Untouchable', 'Sharp Mind'}
    dylan = {'Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable',
             'Boss Slayer'}

    print("Player Alice:", alice)
    print("Player Bob", bob)
    print("Player Charlie", charlie)
    print("Player Dylan", dylan)

    gen_player_achievements(alice, bob, charlie, dylan)
