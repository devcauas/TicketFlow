"""Baixa o dataset do Hugging Face para data/raw/.

Uso: uv run python scripts/download_data.py

Baixa os três arquivos do repositório, porque o notebook de exploração mostra por
que só a versão 5 (MAIN_FILE) é usada; o pipeline lê apenas ela.
"""

import urllib.request

from ticketflow.config import HF_DATASET, RAW_DIR

FILES = {
    "aa_dataset-tickets-multi-lang-5-2-50-version.csv": "aa_dataset-tickets-multi-lang-5-2-50-version.csv",
    "dataset-tickets-multi-lang-4-20k.csv": "dataset-tickets-multi-lang-4-20k.csv",
    "dataset-tickets-german_normalized_50_5_2.csv": "dataset-tickets-german_normalized_50_5_2.csv",
    "README.md": "DATASET_CARD.md",
}


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for remote, local in FILES.items():
        url = f"https://huggingface.co/datasets/{HF_DATASET}/resolve/main/{remote}"
        dest = RAW_DIR / local
        print(f"Baixando {remote} -> {dest}")
        urllib.request.urlretrieve(url, dest)


if __name__ == "__main__":
    main()
