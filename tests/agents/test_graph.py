import pytest
from ticketflow.agents.graph import construir_grafo
from ticketflow.agents.nodes import LIMIAR_CONFIANCA, INFO_MINIMA, TAMANHO_MINIMO

@pytest.fixture
def grafo():
    return construir_grafo()

def test_ticket_curto_pede_esclarecimento(grafo):
    ticket = {
        "ticket_id": "1", 
        "subject": "Help", 
        "body": "help"
    }

    final = grafo.invoke(ticket)

    assert final["route"] == "pedir_esclarecimento"
    assert final["is_complete"] is False
    assert final["missing_info"] == INFO_MINIMA
    assert "queue" not in final          # prova que classificar não rodou

def test_ticket_de_cobranca_e_encaminhado(grafo):
    ticket = {
        "ticket_id": "2",
        "subject": "Invoice wrong",
        "body": "My invoice for October shows a duplicated charge on the account page.",
    }

    final = grafo.invoke(ticket)

    assert final["route"] == "encaminhar"
    assert final["confidence"] >= LIMIAR_CONFIANCA
    assert final["queue"] == "Billing and Payments"

def test_ticket_inseguro_vai_para_revisao(grafo):
    ticket = {
        "ticket_id": "3",
        "subject": "Login",
        "body": "I cannot log into the dashboard since yesterday, it shows error 500 on the page.",
    }

    final = grafo.invoke(ticket)

    assert final["route"] == "revisar"
    assert final["confidence"] < LIMIAR_CONFIANCA

def test_body_no_limite_e_completo(grafo):
    ticket = {
        "ticket_id": "4",
        "subject": "General Inquiry",
        "body": "a" * TAMANHO_MINIMO,
    }

    final = grafo.invoke(ticket)

    assert final["is_complete"] is True
