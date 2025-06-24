"""
main.py: Defines the Langgraph StateGraph for a simple play selection
and demonstrates its execution.

This module sets up a graph that starts, makes a random choice between
cricket and badminton, and then ends. It showcases basic state management
and conditional routing in Langgraph.
"""

from typing_extensions import TypedDict
import random
from typing import Literal

# We've removed IPython.display as this is for a standalone script.
# For graph visualization, you can uncomment the lines below and use
# graph_builder.get_graph().draw_mermaid_png() or .draw_mermaid_svg()
# to save the image to a file.
# from langgraph.graph import StateGraph, START, END
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
  """
  Defines the schema for the graph's state.
  `graph_info`: A string to accumulate information as the graph progresses.
  """
  graph_info: str

def start_play(state: State) -> State:
  """
  The initial node in the graph.
  Appends a planning message to the 'graph_info' state.

  Args:
    state (State): The current state of the graph.

  Returns:
    State: The updated state with the planning message.
  """
  print("start_play node has been called")
  return {'graph_info': state['graph_info'] + " I am planning to play"}

def cricket(state: State) -> State:
  """
  Node representing the 'cricket' activity.
  Appends a playing cricket message to the 'graph_info' state.

  Args:
    state (State): The current state of the graph.

  Returns:
    State: The updated state with the cricket message.
  """
  print("cricket node has been called")
  return {'graph_info': state['graph_info'] + " I am playing cricket"}

def badminton(state: State) -> State:
  """
  Node representing the 'badminton' activity.
  Appends a playing badminton message to the 'graph_info' state.

  Args:
    state (State): The current state of the graph.

  Returns:
    State: The updated state with the badminton message.
  """
  print("badminton node has been called")
  return {'graph_info': state['graph_info'] + " I am playing badminton"}

def random_play(state: State) -> Literal['cricket', 'badminton']:
  """
  Conditional edge function that randomly decides the next activity.
  Routes the graph flow to either 'cricket' or 'badminton' node.

  Args:
    state (State): The current state of the graph (unused in this function,
                   but required by Langgraph's conditional edge signature).

  Returns:
    Literal['cricket', 'badminton']: The name of the next node to transition to.
  """
  if random.random() > 0.5:
    return 'cricket'
  else:
    return 'badminton'

def build_and_compile_graph() -> StateGraph:
  """
  Builds and compiles the Langgraph StateGraph.

  Returns:
    StateGraph: The compiled Langgraph graph_builder object.
  """
  # Build graph
  graph = StateGraph(State)

  # Add all nodes to the graph
  graph.add_node('start_play', start_play)
  graph.add_node('cricket', cricket)
  graph.add_node('badminton', badminton)

  # Define the flow of the graph
  # The graph starts at 'start_play'
  graph.add_edge(START, 'start_play')

  # After 'start_play', the flow is conditionally routed by 'random_play'
  # 'random_play' returns 'cricket' or 'badminton', directing to the respective node
  graph.add_conditional_edges('start_play', random_play)

  # Both 'cricket' and 'badminton' nodes lead to the END state
  graph.add_edge('cricket', END)
  graph.add_edge('badminton', END)

  # Compile the graph for execution
  graph_builder = graph.compile()
  return graph_builder

if __name__ == "__main__":
  # Build and compile the graph
  graph_builder = build_and_compile_graph()

  # --- Graph Visualization (Optional - for development/debugging) ---
  # To visualize the graph, you would typically save it to a file.
  # This requires 'graphviz' to be installed on your system.
  # try:
  #   from PIL import Image
  #   # If you want to save the image to a file:
  #   # Make sure you have graphviz installed (e.g., `brew install graphviz` on macOS,
  #   # `sudo apt-get install graphviz` on Debian/Ubuntu, or install the MSI on Windows)
  #   # and also `pip install pydot` if you're using Langchain's draw methods.
  #   # image_bytes = graph_builder.get_graph().draw_mermaid_png()
  #   # with open("graph_flow.png", "wb") as f:
  #   #   f.write(image_bytes)
  #   # print("Graph visualization saved to graph_flow.png")
  # except ImportError:
  #   print("PIL (Pillow) not found. Cannot save graph image to file.")
  # except Exception as e:
  #   print(f"Could not generate graph visualization. Ensure 'graphviz' is installed: {e}")
  # ------------------------------------------------------------------

  # Usage: Invoke the graph with an initial state
  print("Invoking the graph with initial state: {'graph_info': 'Hi'}")
  final_state = graph_builder.invoke({"graph_info": "Hi"})

  print("-" * 30)
  print("Graph execution finished.")
  print("Final state after graph execution:")
  print(final_state)
