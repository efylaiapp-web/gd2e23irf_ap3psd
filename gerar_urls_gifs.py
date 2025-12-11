import os
from urllib.parse import quote
import unicodedata

# ===============================
# CONFIGURAÇÃO – SEUS DADOS
# ===============================
GITHUB_USER = "efylaiapp-web"
GITHUB_REPO = "gd2e23irf_ap3psd"
BRANCH = "main"

# Pasta dentro do repositório onde estão os arquivos
BASE_PATH_REPO = "Academia"   # sem barra no começo nem no final

# Nome do arquivo de saída com as URLs
OUTPUT_FILE = "urls_gifs.txt"
# ===============================

# extensões que queremos pegar
EXTENSOES_VALIDAS = (".gif", ".png")


def main():
    # Base da URL crua do GitHub
    base_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"

    # Diretório raiz para procurar arquivos
    root_dir = BASE_PATH_REPO if BASE_PATH_REPO else "."

    urls = []

    for root, dirs, files in os.walk(root_dir):
        # Ignorar pasta .git, se aparecer
        if ".git" in root.split(os.sep):
            continue

        for fname in files:
            if fname.lower().endswith(EXTENSOES_VALIDAS):
                # Caminho relativo ao repositório
                file_path = os.path.join(root, fname)
                rel_path = os.path.relpath(file_path, ".")  # relativo à raiz
                rel_path = rel_path.replace(os.sep, "/")    # padronizar com /

                # 🔑 NORMALIZAR ACENTOS PARA NFC (forma que o GitHub usa)
                rel_path_norm = unicodedata.normalize("NFC", rel_path)

                # Codificar caracteres especiais (espaço, acento, colchete…)
                rel_path_url = quote(rel_path_norm, safe="/")

                url = base_url + rel_path_url
                urls.append(url)

    # Gravar todas as URLs em um arquivo .txt
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for u in urls:
            f.write(u + "\n")

    print(f"[OK] {len(urls)} URLs geradas.")
    print(f"Arquivo salvo como: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()