import json
import os
from urllib.parse import unquote

# ===============================
# CONFIGURAÇÃO
# ===============================
INPUT_TXT = "urls_mobilidade_alongamento.txt"
OUTPUT_JSON = "exercicios_mobilidade_alongamento.json"
# ===============================

def limpar_nome(url):
    """
    Usa o nome do arquivo como chave:
    - remove extensão
    - decodifica %20, acentos etc
    - padroniza para slug
    """
    nome = url.split("/")[-1]
    nome = unquote(nome)
    nome = nome.replace(".gif", "").replace(".png", "")

    slug = (
        nome.lower()
        .replace(" ", "-")
        .replace("(", "")
        .replace(")", "")
        .replace("[", "")
        .replace("]", "")
        .replace(",", "")
    )

    return slug


def main():
    dados = {}

    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        for linha in f:
            url = linha.strip()
            if not url:
                continue

            chave = limpar_nome(url)
            dados[chave] = url

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"[OK] {len(dados)} exercícios salvos em {OUTPUT_JSON}")


if __name__ == "__main__":
    main()