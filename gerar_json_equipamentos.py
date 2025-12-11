import os
import json
import unicodedata
from urllib.parse import quote

# ===============================
# CONFIGURAÇÃO – SEUS DADOS
# ===============================
GITHUB_USER = "efylaiapp-web"
GITHUB_REPO = "gd2e23irf_ap3psd"
BRANCH = "main"

# Pasta dentro do repositório onde estão os EQUIPAMENTOS (.png)
BASE_PATH_REPO = "Academia/Equipamentos"   # sem barra no começo nem no final

# Nome do arquivo de saída com os equipamentos
OUTPUT_JSON = "equipamentos.json"
# ===============================


def main():
    base_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"

    root_dir = BASE_PATH_REPO
    equipamentos = []

    for root, dirs, files in os.walk(root_dir):
        # Ignorar .git se aparecer
        if ".git" in root.split(os.sep):
            continue

        for fname in files:
            if not fname.lower().endswith(".png"):
                continue

            file_path = os.path.join(root, fname)
            rel_path = os.path.relpath(file_path, ".")
            rel_path = rel_path.replace(os.sep, "/")

            # Normaliza acentos (forma que o GitHub usa)
            rel_path_norm = unicodedata.normalize("NFC", rel_path)
            rel_path_url = quote(rel_path_norm, safe="/")

            url = base_url + rel_path_url

            # Categoria = subpasta logo depois de "Equipamentos"
            # ex: Academia/Equipamentos/Acessórios/Cabo.png
            # partes = ["Academia", "Equipamentos", "Acessórios", "Cabo.png"]
            partes = rel_path.split("/")
            categoria = partes[2] if len(partes) > 2 else "Geral"

            nome_sem_ext = fname.rsplit(".", 1)[0]

            equipamentos.append({
                "categoria": categoria,
                "nome": nome_sem_ext,
                "arquivo": fname,
                "caminho": rel_path,
                "url": url,
            })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(equipamentos, f, ensure_ascii=False, indent=2)

    print(f"[OK] {len(equipamentos)} equipamentos salvos em {OUTPUT_JSON}")


if __name__ == "__main__":
    main()