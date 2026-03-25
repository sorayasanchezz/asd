if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer",
                  "arena_win", "treasure_hunter"],
        "bob": ["first_kill", "level_10", "arena_win"],
        "charlie": ["first_kill", "level_10", "boss_slayer", "arena_win",
                    "treasure_hunter", "speed_runner", "dungeon_master"],
        "diana": ["first_kill", "level_10"]
    }
    regions = ["north", "east", "north", "central"]

    print("\n=== List Comprehension Examples ===")
    # Filter high scores
    high_scores = [players[n] for n in range(len(players)) if scores[n] > 2000]
    print("High scorers (>2000):", high_scores)
    # Transform data (scores)
    scores_doubled = [score * 2 for score in scores]
    print("Scores doubled:", scores_doubled)
    # Create new lists (active players)
    active_player = [player for player in players if player != "diana"]
    print("Active players:", active_player)

    print("\n=== Dict Comprehension Examples ===")
    # Create score mapping
    player_scores = {players[n]: scores[n] for n in range(len(players))}
    print("Player scores:", player_scores)
    # Group scores by category
    score_categories = {
        "high": len([n for n in scores if n > 2000]),
        "medium": len([n for n in scores if 1500 < n <= 2000]),
        "low": len([n for n in scores if n <= 1500])
    }
    print("Score categories:", score_categories)
    # Count occurrences (achievement counts)
    ach_counts = {player: len(achievements[player]) for player in players}
    print("Achievement counts:", ach_counts)

    print("\n=== Set Comprehension Examples ===")
    # Find unique players
    unique_players = {player for player in players}
    print("Unique players:", unique_players)
    # Unique achievements
    uniqu_ach = {ach for ach_list in achievements.values() for ach in ach_list}
    print("Unique achievements:", uniqu_ach)
    # Deduplicate data
    active_regions = {region for region in regions}
    print("Active regions:", active_regions)

    max_score = max(scores)
    max_index_score = scores.index(max_score)
    max_player = players[max_index_score]
    n_ach = len((achievements[max_player]))

    print("\n=== Combined Analysis ===")
    print("Total players:", len(players))
    print("Total unique achievements:", len(uniqu_ach))
    print("Average score:", sum(scores) / len(scores))
    print(f"Top performer: {max_player} ({max_score} points, "
          f"{n_ach} achievements)")
