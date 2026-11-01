from typing import TypedDict, NotRequired, Literal

class TicketState(TypedDict):
    """
        Estado de um ticket.
        
        Preenchidos ao longo do caminho (NotRequired): 
        Entrada: ticket_id, subject, body
        verificar_completude: is_complete, missing_info, suggested_info (+ route, se incompleto)
        classificar: queue, confidence, top_queues, route
    """
    ticket_id: str
    subject: str
    body: str
    is_complete: NotRequired[bool]
    missing_info: NotRequired[list[str]]
    suggested_info: NotRequired[list[str]]
    queue: NotRequired[str]
    confidence: NotRequired[float]
    top_queues: NotRequired[list[tuple[str, float]]]
    route: NotRequired[Literal["pedir_esclarecimento", "encaminhar", "revisar"]]