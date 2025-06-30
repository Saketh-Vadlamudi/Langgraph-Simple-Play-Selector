# Langgraph Simple Play Selector
 
A basic demonstration of `langgraph`'s `StateGraph` to simulate a random choice between playing cricket or badminton, showcasing conditional edges and state management.
  
## 🚀 Features

* **State Management**: Utilizes `TypedDict` for clear definition of graph state.
* **Conditional Routing**: Employs `add_conditional_edges` to dynamically choose the next node based on a random outcome.
* **Simple Flow**: Demonstrates a straightforward graph flow from start to a chosen activity and then to end.

## 🛠️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Ensure you have Python 3.9+ installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-langgraph-project.git](https://github.com/your-username/your-langgraph-project.git)
    cd your-langgraph-project
    ```
    (Replace `your-username/your-langgraph-project` with your actual GitHub path)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage

To run the Langgraph example:

1.  **Navigate to the project root:**
    ```bash
    cd your-langgraph-project
    ```

2.  **Execute the main script:**
    ```bash
    python src/main.py
    ```

Each execution will randomly select either 'cricket' or 'badminton' and print the execution trace and final state.

## 🌟 Example Output

The output will vary each time due to the random selection, but will follow this pattern:

```text
start_play node has been called
# One of the following two lines will be printed:
cricket node has been called
# OR
badminton node has been called
Final state after graph execution:
# One of the following two outputs:
{'graph_info': 'Hi I am planning to play I am playing cricket'}
# OR
{'graph_info': 'Hi I am planning to play I am playing badminton'}
