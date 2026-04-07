from unittest.mock import patch                                                                                                                                                                                                      
from app.strategy import choose_strategy

def test_strategy_parses_valid_json():
    llm_response = '{"best_move": "EO", "explanation": "Eichel-Ober sticht alles"}'

    with patch("app.strategy.generate", return_value=llm_response):
        state = {                                                                                                                                                                                                                    
            "hand": ["EO", "GU", "HZ"],               
            "played_cards": [],                                                                                                                                                                                                      
            "game_type": "Sauspiel",
            "valid_moves": ["EO", "GU", "HZ"],                                                                                                                                                                                       
        }                                             
        result = choose_strategy(state)

    assert result["best_move"] == "EO"
    assert result["explanation"] == "Eichel-Ober sticht alles"

def test_strategy_fallback_on_invalid_json():
    with patch("app.strategy.generate", return_value="das ist kein json"):
        state = {
            "hand": ["EO", "GU"],
            "played_cards": [],                                                                                                                                                                                                      
            "game_type": "Sauspiel",                  
            "valid_moves": ["EO", "GU"],            
        }
        result = choose_strategy(state)
    
    assert result["best_move"] == "EO"
    assert "Konnte LLM-Antwort nicht parsen" in result["explanation"]