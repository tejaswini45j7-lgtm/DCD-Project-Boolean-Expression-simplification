# DCD-Project-Boolean-Expression-simplification
A Digital Circuit Design (DCD) tool built to simplify Boolean logic. It features raw algebraic minimization with error handling and standard SOP optimization using minterms and don't-care conditions, providing an automated alternative to manual Karnaugh maps.

## About the Project
**What it does**
This project is an interactive web dashboard built to automate the simplification of complex Boolean algebra. It serves as an advanced computational alternative to manual Karnaugh maps (K-maps), easily handling high-variable expressions that are tedious to minimize by hand.

**How it does it**
The application accepts user input in two ways: as a raw algebraic Boolean expression or as standard Minterms (1s) and Don't Care (X) conditions. The logic engine applies the Quine-McCluskey algorithm (the tabular method) to process the inputs and calculate the absolute minimized Sum of Products (SOP) form. 

**Tools and Technologies Used**
* **Python:** Core programming language.
* **Streamlit:** Web framework for the interactive front-end UI.
* **SymPy:** Computer algebra library used to execute the Quine-McCluskey minimization algorithm.

## Features
1. **Expression Mode:** Enter raw Boolean logic directly. Includes built-in error handling to catch and resolve reserved mathematical constants (like E, I, O) before they interrupt the engine.
2. **Minterm & Don't Care Mode:** Optimize logic using standard SOP form by entering minterms (∑m) and don't care conditions (∑d).

## How the Code Works (Architecture Breakdown)
* **Input Parsing & Validation:** The script reads user strings and converts them into SymPy mathematical objects. It actively intercepts reserved characters to prevent engine failure.
* **Algebraic Minimization:** Uses `simplify_logic()` to reduce algebraic strings into Disjunctive Normal Form (SOP).
* **Quine-McCluskey Execution:** In Minterm mode, the script dynamically generates variable symbols based on user input, processes the integer lists, and feeds them into SymPy's `SOPform()` to find prime implicants and output the smallest logic footprint.

## How to Run Locally
1. Install the required dependencies:
   `pip install -r requirements.txt`
2. Start the local web server:
   `streamlit run minimizer_app.py`

## Test Examples
**Example 1: Expression Mode**
* Input: `(A & B) | (A & ~B)`
* Minimized Output: `A`

**Example 2: Minterm & Don't Care Mode**
* Variables: `3`
* Minterms (∑m): `1, 3, 7`
* Don't Cares (∑d): `5`
* Minimized Output: `C`
