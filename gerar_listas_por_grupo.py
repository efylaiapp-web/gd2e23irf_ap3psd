import os
import unicodedata

# ===============================
# CONFIG
# ===============================
BASE_DIR = "Academia"          # pasta onde estão os grupos
OUTPUT_DIR = "_listas_grupos"  # pasta onde salvar os .txt

# Extensões que você quer listar (edite como quiser)
EXTS = {".gif", ".png"}  # pode trocar por {".gif"} se quiser só gifs

# Se True: inclui arquivos dentro de subpastas (ex: Equipamentos/Acessórios/...)
INCLUDE_SUBFOLDERS = True
# ===============================


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def listar_arquivos(pasta: str):
    itens = []

    if INCLUDE_SUBFOLDERS:
        for root, dirs, files in os.walk(pasta):
            # ignora .git se existir
            if ".git" in root.split(os.sep):
                continue

            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in EXTS:
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, pasta).replace(os.sep, "/")
                    itens.append(nfc(rel))
    else:
        for f in os.listdir(pasta):
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTS:
                itens.append(nfc(f))

    itens.sort(key=lambda x: x.lower())
    return itens


def main():
    if not os.path.isdir(BASE_DIR):
        raise SystemExit(f"[ERRO] Não achei a pasta '{BASE_DIR}' aqui. Rode o script na raiz do projeto.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    grupos = [g for g in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, g))]
    grupos.sort(key=lambda x: x.lower())

    total_arquivos = 0

    for grupo in grupos:
        pasta_grupo = os.path.join(BASE_DIR, grupo)
        arquivos = listar_arquivos(pasta_grupo)

        total_arquivos += len(arquivos)

        out_path = os.path.join(OUTPUT_DIR, f"{grupo}.txt")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"[{grupo}] — Total: {len(arquivos)} arquivos\n")
            f.write("=" * 60 + "\n")
            for a in arquivos:
                f.write(a + "\n")

        print(f"[OK] {grupo}: {len(arquivos)} arquivos → {out_path}")

    print(f"\n✅ Finalizado. Total geral listados: {total_arquivos}")
    print(f"📁 Listas salvas em: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()