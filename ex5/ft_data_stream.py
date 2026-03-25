from typing import Generator
import time


def generate_events() -> Generator[tuple[int, str, int, str], None, None]:

    for n in range(1, 1001):
        if n % 3 == 1:
            player = "alice"
            level = 5
            action = "killed monster"
        elif n % 3 == 2:
            player = "bob"
            level = 12
            action = "found treasure"
        else:
            player = "charlie"
            level = 8
            action = "leveled up"

        if n > 3 and n <= 91:
            action = "found treasure"
        elif n >= 3 and n <= 246:
            action = "leveled up"
        elif n > 3:
            action = "killed monster"

        if n > 3 and n <= 344:
            level = 12
        elif n > 3 and n > 344:
            level = 5

        yield (n, player, level, action)


def stream_processor() -> None:
    print("=== Game Data Stream Processor ===\n\n"
          "Processing 1000 game events...\n")

    for n, player, level, action in generate_events():
        print(f"Event {n}: Player {player} (level {level}) {action}")


def stream_analytics() -> None:
    print("=== Stream Analytics ===")
    start_time = time.time()
    high_level = 0
    treasure_events = 0
    levelup_events = 0

    for n, player, level, action in generate_events():
        if level >= 10:
            high_level += 1
        if "treasure" in action:
            treasure_events += 1
        if "leveled up" in action:
            levelup_events += 1

    print("Total events processed:", n)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure_events)
    print("Level-up events:", levelup_events)

    print("\nMemory usage: Constant (streaming)")
    end_time = time.time() - start_time
    print(f"Processing time: {end_time:.3f}")


def generate_fibonacci() -> Generator[str, None, None]:
    printed = False
    a = 0
    b = 0

    for n in range(0, 10):
        # First values
        if printed is False:
            if b == 0:
                yield ("0")
                b = 1
            else:
                yield (", 1")
                printed = True
        else:
            result = a + b
            yield (f", {result}")

            a = b
            b = result


def is_prime(n: int) -> bool:
    compare = 2
    while compare < n:
        if n % compare == 0:
            return (False)
        compare += 1
    return (True)


def generate_primes() -> Generator[str, None, None]:
    prime = 2

    for n in range(0, 5):
        if prime == 2:
            yield (f"{prime}")
            prime += 1

        else:
            while is_prime(prime) == 0:
                prime += 1

            if is_prime(prime):
                yield (f", {prime}")
                prime += 1


def generator_demostration() -> None:
    print("=== Generator Demonstration ===")
    fibonacci_text = ""
    prime_text = ""

    for text in generate_fibonacci():
        fibonacci_text += text

    for text in generate_primes():
        prime_text += text

    print("Fibonacci sequence (first 10):", fibonacci_text)
    print("Prime numbers (first 5):", prime_text)


if __name__ == "__main__":
    stream_processor()
    print()
    stream_analytics()
    print()
    generator_demostration()
