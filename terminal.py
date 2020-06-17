from os import system
import sys


class Color:
    RED = "\033[31m"
    BLACK = "\033[30m"
    GREEN = "\033[32m"

print(Color.RED)


def clearTerminal():
    if (sys.platform.startswith("win")):
        system("cls")
    else:
        system("clear")


def cracking(password):
    clearTerminal()
    print("""
                === ===   === ===     =======     =========== ===         ============= =======   ====
                ===    ===    ===   ===      ===  ===     === ===         ===       === ===  ===  ====
                ===    ===    === ===         === ===     === ===         ===       === ===   === ====
                ===           === ===  =====  === ===  ====== ===         ===       === ===    ======
                ===           === ===         === ===     === =========== ============= ===
            """)
    print("...FORCING CRACK...")
    print(f"PASSWORD: {password}")

def finded_password(password):
    print(
        "================================ SEARCHED ===================================")
    print(f"Your password: {password}")
