import json
from app.state import GameState
from app.llm import generate

def choose_strategy(state: GameState) -> GameState:
    prompt = (                                                                                                                                                                                                                       
        f"Du bist ein Schafkopf-Experte. "                                                                                                                                                                                           
        f"Spieltyp: {state['game_type']}. "                                                                                                                                                                                          
        f"Meine Hand: {state['hand']}. "                                                                                                                                                                                             
        f"Gültige Züge: {state['valid_moves']}. "     
        f"Bereits gespielte Karten: {state['played_cards']}. "                                                                                                                                                                       
        f"Welche Karte soll ich spielen? "                                                                                                                                                                                           
        f"Antworte ausschließlich mit purem JSON, ohne Codeblock, ohne Erklärung davor oder danach: "                                                                                                                                
        f"{{\"best_move\": \"...\", \"explanation\": \"...\"}}"                                                                                                                                                                      
    )  

    response = generate(prompt)

    try:
        data = json.loads(response)
        state["best_move"] = data["best_move"]                                                                                                                                                                                       
        state["explanation"] = data["explanation"]
    except (json.JSONDecodeError, KeyError):                                                                                                                                                                                         
        state["best_move"] = state["valid_moves"][0]                                                                                                                                                                                 
        state["explanation"] = f"Konnte LLM-Antwort nicht parsen: {response}"
                                                                                                                                                                                                                                    
    return state
