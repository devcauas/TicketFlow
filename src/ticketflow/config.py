"""Caminhos e configurações lidos do ambiente (.env)."""

from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

load_dotenv(ROOT_DIR / ".env")

HF_DATASET = "Tobi-Bueck/customer-support-tickets"
# Versão 5 do dataset: 28.587 tickets em inglês e alemão, com as 10 filas.
# Os outros dois arquivos do repositório não entram (ver README, seção Dataset).
MAIN_FILE = "aa_dataset-tickets-multi-lang-5-2-50-version.csv"
