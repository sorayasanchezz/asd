import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv = sys.argv

    # list for storing scores
    scores: list[int] = []

    # no arguments
    if len(argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")

    # are arguments
    else:

        # adds scores(input) to the list, protect in case of non-numeric values
        for score in argv[1:]:
            try:
                scores.append(int(score))
            except ValueError:
                print("Invalid parameter:", score)

        # analythics (calculates), protect in case of non-numeric values
        if len(scores) == 0:
            print("No scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")
        else:
            print("Scores processed:", scores)
            print("Total players:", len(scores))
            print("Total score:", sum(scores))
            print("Average score:", sum(scores) / len(scores))
            print("High score:", max(scores))
            print("Low score:", min(scores))
            print("Score range:", max(scores) - min(scores))
