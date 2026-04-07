from app.graph import graph

def main():
    state = {
          "hand": ["EO", "GU", "HZ", "S7"],
          "played_cards": ["SO", "H8"],                                                                                                                                                                                                
          "game_type": "Sauspiel",                                                                                                                                                                                                     
          "position": 2,
    }

    result = graph.invoke(state)

    print(f"Bester Zug: {result['best_move']}")                                                                                                                                                                                      
    print(f"Begründung: {result['explanation']}")    

if __name__ == "__main__":
    main()