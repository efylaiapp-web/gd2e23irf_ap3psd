import json
from urllib.parse import unquote

INPUT_TXT = "urls_calistenia.txt"
OUTPUT_JSON = "exercicios_calistenia.json"

def limpar_nome(url):
    nome = url.split("/")[-1]
    nome = unquote(nome)
    nome = nome.replace(".gif", "").replace(".png", "")
    return nome

def main():
    exercicios = []

    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        for linha in f:
            url = linha.strip()
            if not url:
                continue

            nome = limpar_nome(url)

            exercicios.append({
                "grupo": "Calistenia",
                "nome": nome,
                "url": url
            })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(exercicios, f, ensure_ascii=False, indent=2)

    print(f"[OK] {len(exercicios)} exercícios salvos em {OUTPUT_JSON}")

if __name__ == "__main__":
    main()