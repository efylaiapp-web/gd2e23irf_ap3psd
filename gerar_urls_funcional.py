import os
from urllib.parse import quote
import unicodedata

GITHUB_USER = "efylaiapp-web"
GITHUB_REPO = "gd2e23irf_ap3psd"
BRANCH = "main"

BASE_PATH = "FUNCIONAL"
OUTPUT_FILE = "urls_funcional.txt"

def main():
    base_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"
    urls = []

    for root, _, files in os.walk(BASE_PATH):
        for file in files:
            if file.lower().endswith((".gif", ".png")):
                path = os.path.join(root, file).replace("\\", "/")
                path = unicodedata.normalize("NFC", path)
                path = quote(path, safe="/")
                urls.append(base_url + path)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")

    print(f"[OK] {len(urls)} URLs geradas.")
    print(f"Arquivo criado: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()