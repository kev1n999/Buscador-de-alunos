import os 
import requests 
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("URL")


def request(aluno):
    req = requests.post(api, {
        "Nome": aluno,
        "btn_cons": "Consultar"
    })

    if (req.status_code == 200):
        parse = BeautifulSoup(req.text, "html.parser")
        f = parse.find("table")
        for names in f.find_all("td", attrs={"class": "verde10"}):
            text = names.get_text()
            print(text)

    else:
        print(f"[error: status {req.status_code}] não foi possível identificar este aluno.")
    
while True:
    os.system("cls")
    aluno = str(input("\n[*] Buscar aluno: "))
    if aluno == "quit" or aluno == "sair":
        exit()

    request(aluno)
    input("\n[*] Pression enter para continuar...")