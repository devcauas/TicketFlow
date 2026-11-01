from ticketflow.agents.state import TicketState

TAMANHO_MINIMO = 60
LIMIAR_CONFIANCA = 0.95

INFO_MINIMA = ["O quê", "Onde"]                       # sem isto, não dá para resolver
INFO_DESEJAVEL = ["Quando", "Evidência", "Contexto"]  # ajuda, mas não trava o ticket


def verificar_completude(state: TicketState) -> dict:
    body = state["body"]
    if len(body) < TAMANHO_MINIMO:
        return {
            "is_complete": False,
            "missing_info": INFO_MINIMA,
            "suggested_info": INFO_DESEJAVEL,
            "route": "pedir_esclarecimento",
        }
    return {
        "is_complete": True,
        "missing_info": [],
        "suggested_info": INFO_DESEJAVEL,
    }

def classificar(state: TicketState) -> dict:
    texto = f"{state['subject']} {state['body']}".lower()

    if "invoice" in texto or "billing" in texto:
        queue, confidence = "Billing and Payments", 0.98
        segunda = ("Technical Support", 0.70)
    else:
        queue, confidence = "Technical Support", 0.90
        segunda = ("Billing and Payments", 0.65)

    return {
        "queue": queue,
        "confidence": confidence,
        "top_queues": [(queue, confidence), segunda],
        "route": "encaminhar" if confidence >= LIMIAR_CONFIANCA else "revisar",
    }

def pedir_esclarecimento(state: TicketState) -> dict:
    faltam = ", ".join(state["missing_info"])
    print(f"[{state['ticket_id']}] pedindo esclarecimento: faltam {faltam}")
    return {}

def encaminhar(state: TicketState) -> dict:
    print(f"[{state['ticket_id']}] encaminhado para {state['queue']}")
    return {}

def revisar(state: TicketState) -> dict:
    print(f"[{state['ticket_id']}] enviado para revisão (sugestão: {state['queue']})")
    return {}