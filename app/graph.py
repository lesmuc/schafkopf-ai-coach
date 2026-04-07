from langgraph.graph import StateGraph, START, END                                                                                                                                                                                   
from app.state import GameState                                                                                                                                                                                                      
from app.rules import compute_valid_moves
from app.strategy import choose_strategy

workflow = StateGraph(GameState)

workflow.add_node("rules", compute_valid_moves)
workflow.add_node("strategy", choose_strategy)
workflow.add_edge(START, "rules")
workflow.add_edge("rules", "strategy")
workflow.add_edge("strategy", END)

graph = workflow.compile()