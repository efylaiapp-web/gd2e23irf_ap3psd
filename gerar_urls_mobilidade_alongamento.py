import os
from urllib.parse import quote
import unicodedata

GITHUB_USER = "efylaiapp-web"
GITHUB_REPO = "gd2e23irf_ap3psd"
BRANCH = "main"

BASE_PATH_REPO = "Funcional e Mobilidade/Mobilidade e Alongamento"
OUTPUT_FILE = "urls_mobilidade_alongamento.txt"

def main():
    base_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"
    urls = []

    for root, dirs, files in os.walk(BASE_PATH_REPO):
        for fname in files:
            if fname.lower().endswith(".gif"):
                file_path = os.path.join(root, fname)
                rel_path = os.path.relpath(file_path, ".").replace(os.sep, "/")
                rel_path = unicodedata.normalize("NFC", rel_path)
                rel_path = quote(rel_path, safe="/")
                urls.append(base_url + rel_path)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for u in urls:
            f.write(u + "\n")

    print(f"[OK] {len(urls)} URLs de MOBILIDADE/ALONGAMENTO geradas.")
    print(f"Arquivo: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()