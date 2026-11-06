from langgraph.graph import StateGraph, START, END
from typing import Literal
from ticketflow.agents.state import TicketState
from ticketflow.agents.nodes import pedir_esclarecimento, verificar_completude, classificar, encaminhar, revisar

def rotear_completude(state: TicketState) -> Literal["pedir_esclarecimento", "classificar"]:
    if state.get("is_complete"):
        return "classificar"
    return "pedir_esclarecimento"

def rotear_classificacao(state: TicketState) -> Literal["encaminhar", "revisar"]:
    return state["route"]

def construir_grafo():
    return(
        StateGraph(TicketState)
        .add_node("verificar_completude", verificar_completude)
        .add_node("classificar", classificar)
        .add_node("pedir_esclarecimento", pedir_esclarecimento)
        .add_node("encaminhar", encaminhar)
        .add_node("revisar", revisar)
        .add_edge(START, "verificar_completude") 
        .add_conditional_edges("verificar_completude", rotear_completude)
        .add_conditional_edges("classificar", rotear_classificacao)
        .add_edge("pedir_esclarecimento", END)        
        .add_edge("encaminhar", END)
        .add_edge("revisar", END)
        .compile()
    )
