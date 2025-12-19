import os
from urllib.parse import quote
import unicodedata

# ===============================
# CONFIGURAÇÃO – SEUS DADOS
# ===============================
GITHUB_USER = "efylaiapp-web"
GITHUB_REPO = "gd2e23irf_ap3psd"
BRANCH = "main"

# Pasta dentro do repositório onde estão os GIFs de Funcional & Mobilidade
# (nome EXATO da pasta no GitHub)
BASE_PATH_REPO = "Funcional e Mobilidade"   # sem barra no começo nem no final

# Nome do arquivo de saída com as URLs
OUTPUT_FILE = "urls_funcional_mobilidade.txt"
# ===============================


def main():
    base_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"

    # Diretório raiz para procurar GIFs (relativo à raiz do repo)
    root_dir = BASE_PATH_REPO if BASE_PATH_REPO else "."

    urls = []

    for root, dirs, files in os.walk(root_dir):
        # Ignorar pasta .git, se aparecer
        if ".git" in root.split(os.sep):
            continue

        for fname in files:
            if fname.lower().endswith(".gif"):
                file_path = os.path.join(root, fname)
                # caminho relativo à raiz do repositório
                rel_path = os.path.relpath(file_path, ".")
                rel_path = rel_path.replace(os.sep, "/")

                # Normalizar acentos (forma que o GitHub usa)
                rel_path_norm = unicodedata.normalize("NFC", rel_path)

                # Codificar caracteres especiais na URL
                rel_path_url = quote(rel_path_norm, safe="/")

                url = base_url + rel_path_url
                urls.append(url)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for u in urls:
            f.write(u + "\n")

    print(f"[OK] {len(urls)} URLs de FUNCIONAL & MOBILIDADE (.gif) geradas.")
    print(f"Arquivo salvo como: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()