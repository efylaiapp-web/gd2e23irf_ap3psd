import json
import os
from urllib.parse import urlparse, unquote

URLS_FILE = "urls_gifs.txt"
OUTPUT_JSON = "exercicios.json"

def main():
    if not os.path.exists(URLS_FILE):
        print(f"Arquivo {URLS_FILE} não encontrado.")
        return

    with open(URLS_FILE, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    exercicios = []

    for url in linhas:
        path = urlparse(url).path
        path_decodificado = unquote(path)

        marcador = "/Academia/"
        idx = path_decodificado.find(marcador)
        if idx == -1:
            continue

        subpath = path_decodificado[idx + len(marcador):]
        # ex: "Tríceps (103)/[Tríceps] Flexão de braço reversa para baixo (Cabo).gif"

        partes = subpath.split("/")
        if len(partes) < 2:
            continue

        pasta_grupo = partes[0]       # "Tríceps (103)"
        nome_arquivo = partes[-1]     # "[Tríceps] Flexão ... (Cabo).gif"

        if " (" in pasta_grupo:
            grupo = pasta_grupo.split(" (")[0]
        else:
            grupo = pasta_grupo

        if nome_arquivo.lower().endswith(".gif"):
            nome = nome_arquivo[:-4]
        else:
            nome = nome_arquivo

        exercicios.append({
            "grupo": grupo,
            "nome": nome,
            "url": url
        })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(exercicios, f, ensure_ascii=False, indent=2)

    print(f"[OK] {len(exercicios)} exercícios salvos em {OUTPUT_JSON}")

if __name__ == "__main__":
    main()