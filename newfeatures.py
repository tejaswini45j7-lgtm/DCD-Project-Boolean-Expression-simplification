import streamlit as st
from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.boolalg import simplify_logic
from sympy import symbols
from sympy.logic import SOPform

st.title("Digital Logic Minimizer")
st.markdown("Simplify Boolean expressions instantly.")

num_vars = st.number_input("How many variables?", min_value=1, max_value=26, value=3)

# Create two separate tabs on the web page
tab1, tab2 = st.tabs(["Expression Mode", "Minterm & Don't Care Mode"])

# --- TAB 1: Expression Mode ---
with tab1:
    st.info("Syntax Guide: Use `&` for AND, `|` for OR, `~` for NOT.")
    raw_expression = st.text_input("Enter your boolean expression:")
    
    if st.button("Minimize Expression"):
        if raw_expression: 
            # 1. Check for reserved math letters before doing any algebra
            upper_expr = raw_expression.upper()
            if "E" in upper_expr or "I" in upper_expr or "O" in upper_expr:
                st.warning("⚠️ Warning: SymPy reserves 'E' (Euler's number), 'I' (Imaginary unit), and 'O' (Big-O notation). Please use other letters like H, J, or K.")
            else:
                # 2. If it is safe, try to solve it
                try:
                    math_expr = parse_expr(raw_expression)
                    minimized = simplify_logic(math_expr, form='dnf')
                    st.success("Logic reduced successfully!")
                    st.code(minimized, language="text")
                except Exception as e:
                    st.error("Syntax error. Make sure you used &, |, and ~ correctly.")
        else:
            st.warning("Please enter an expression first.")

# --- TAB 2: Minterm & Don't Care Mode ---
with tab2:
    st.info("Enter minterms (1s) and don't cares (Xs) as comma-separated numbers (e.g., 0, 1, 4, 5).")
    
    minterms_input = st.text_input("Minterms (∑m):", placeholder="e.g., 1, 3, 7")
    dont_care_input = st.text_input("Don't Cares (∑d):", placeholder="e.g., 0, 5")
    
    if st.button("Optimize with Don't Cares"):
        try:
            minterms = [int(x.strip()) for x in minterms_input.split(",") if x.strip().isdigit()]
            
            dont_cares = []
            if dont_care_input:
                dont_cares = [int(x.strip()) for x in dont_care_input.split(",") if x.strip().isdigit()]
            
            if not minterms:
                st.warning("Please enter at least one minterm.")
            else:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                var_symbols = symbols(' '.join(alphabet[:num_vars]))
                
                optimized_logic = SOPform(var_symbols, minterms, dontcares=dont_cares)
                
                st.success("Logic optimized successfully!")
                st.code(optimized_logic, language="text")
                
        except Exception as e:
            st.error("Error processing numbers. Please ensure you only used numbers and commas.")