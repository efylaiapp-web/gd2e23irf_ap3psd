import json
from urllib.parse import unquote

INPUT_URLS_FILE = "urls_funcional_mobilidade.txt"
OUTPUT_JSON_FILE = "exercicios_funcional_mobilidade.json"

# Nome do grupo que você quer que apareça no JSON
GRUPO_NOME = "Funcional e Mobilidade"


def main():
    exercicios = []

    with open(INPUT_URLS_FILE, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]

    for url in linhas:
        # pega só o nome do arquivo
        filename = url.split("/")[-1]
        # remove %20 etc pra ficar legível
        filename_decoded = unquote(filename)
        # tira a extensão (.gif)
        nome_sem_ext = filename_decoded.rsplit(".", 1)[0]

        exercicios.append({
            "grupo": GRUPO_NOME,
            "nome": nome_sem_ext,
            "url": url,
        })

    with open(OUTPUT_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(exercicios, f, ensure_ascii=False, indent=2)

    print(f"[OK] {len(exercicios)} exercícios salvos em {OUTPUT_JSON_FILE}")


if __name__ == "__main__":
    main()