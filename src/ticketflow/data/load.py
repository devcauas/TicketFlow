"""Leitura do dataset bruto com a limpeza mínima que todas as etapas precisam."""

import pandas as pd

from ticketflow.config import MAIN_FILE, RAW_DIR

TAG_COLUMNS = [f"tag_{i}" for i in range(1, 9)]


def load_tickets() -> pd.DataFrame:
    """Lê a versão 5 do dataset.

    O texto vem com quebras de linha escapadas ("\\n" literal); aqui elas viram
    quebras reais. O assunto ausente vira string vazia, porque o modelo usa
    assunto + corpo e um ticket sem assunto continua válido.
    """
    df = pd.read_csv(RAW_DIR / MAIN_FILE)
    for col in ["subject", "body", "answer"]:
        df[col] = df[col].str.replace("\\n", "\n", regex=False)
    df["subject"] = df["subject"].fillna("")
    df["tags"] = df[TAG_COLUMNS].apply(lambda row: [t for t in row if pd.notna(t)], axis=1)
    return df.drop(columns=TAG_COLUMNS)
