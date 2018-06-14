import sys
import time


def slow_print(s):
    pause = 0.15

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(pause)
    print("")
    time.sleep(0.08)

slow_print("Báč rád kedlubáč! "*20)
