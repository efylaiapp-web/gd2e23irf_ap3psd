import os

PASTA = "CROSSFIT"
PREFIXO = "[Crossfit] "

def main():
    total = 0

    for root, _, files in os.walk(PASTA):
        for file in files:
            if not file.lower().endswith((".gif", ".png")):
                continue

            if file.startswith(PREFIXO):
                continue

            caminho_antigo = os.path.join(root, file)
            novo_nome = PREFIXO + file
            caminho_novo = os.path.join(root, novo_nome)

            os.rename(caminho_antigo, caminho_novo)
            total += 1
            print(f"{file} → {novo_nome}")

    print(f"\n[OK] {total} arquivos renomeados.")

if __name__ == "__main__":
    main()