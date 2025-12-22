from typing import TypedDict

class State(TypedDict):

    customer_name: str
    my_age: int

state: State = {}
customer_name = state.get("customer_name", None)
print(customer_name)

def node_1(state: State):
    if state.get("customer_name") is None:
        return {**state, "customer_name": "Kevin"}
    return {
        "my_age":31
    }

# Construction of the graph
from langgraph.graph import StateGraph, START, END  # According to the project

builder = StateGraph(State)

builder.add_node("node_1", node_1)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()