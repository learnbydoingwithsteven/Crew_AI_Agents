"""
Unified UI for Crew AI Agents - Financial and Research Use Cases
"""

import streamlit as st
import os
import sys
import time
import json
from core import UseCaseManager

# Configure Streamlit page
st.set_page_config(
    page_title="Crew AI Agents Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "use_case_manager" not in st.session_state:
    st.session_state.use_case_manager = UseCaseManager()
if "current_use_case" not in st.session_state:
    st.session_state.current_use_case = None
if "result" not in st.session_state:
    st.session_state.result = None
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "input_data" not in st.session_state:
    st.session_state.input_data = {}

def reset_result():
    """Reset the result state."""
    st.session_state.result = None
    st.session_state.is_running = False
    
def set_use_case(use_case_id):
    """Set the current use case and reset result."""
    if st.session_state.current_use_case != use_case_id:
        st.session_state.current_use_case = use_case_id
        reset_result()
        st.session_state.input_data = {}

def run_use_case():
    """Run the selected use case."""
    if st.session_state.current_use_case:
        st.session_state.is_running = True
        # Get the use case manager from session state
        manager = st.session_state.use_case_manager
        
        # Run the use case in session state to avoid recomputation
        st.session_state.result = manager.run_use_case(
            st.session_state.current_use_case,
            st.session_state.input_data
        )
        st.session_state.is_running = False

# App header
st.title("🤖 Crew AI Agents Hub")
st.markdown("""
This application provides a unified interface to run and interact with various Crew AI agents
for financial and research use cases. Each use case has its own specialized agents and tasks.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")

# Financial Use Cases Section
st.sidebar.header("Financial Use Cases")
financial_cases = st.session_state.use_case_manager.financial_use_cases

for case_id, case_data in financial_cases.items():
    if st.sidebar.button(f"📊 {case_data['title']}", key=f"fin_{case_id}"):
        set_use_case(case_id)

# Research Use Cases Section
st.sidebar.header("Research Use Cases")
research_cases = st.session_state.use_case_manager.research_use_cases

for case_id, case_data in research_cases.items():
    if st.sidebar.button(f"🔬 {case_data['title']}", key=f"res_{case_id}"):
        set_use_case(case_id)

# Main content area
if st.session_state.current_use_case:
    # Get all use cases and find the current one
    all_cases = st.session_state.use_case_manager.get_all_use_cases()
    current_case = all_cases.get(st.session_state.current_use_case)
    
    if current_case:
        st.header(current_case['title'])
        st.markdown(current_case['description'])
        
        # Create a form for input parameters (can be customized per use case)
        with st.form(key="use_case_form"):
            st.subheader("Input Parameters")
            
            # Common parameters for all use cases
            query = st.text_area("Query or Task Description", 
                                placeholder="Enter your specific query or task description here...",
                                height=100)
            
            # Use case specific parameters could be added here
            # For example, if the use case is fraud detection:
            if current_case['id'] == 'use_case_01_fraud_detection':
                st.text_area("Transaction Data (JSON)",
                            placeholder='{"transactions": [{"id": 1, "amount": 1000, "timestamp": "2023-01-01T12:00:00Z", "description": "Purchase"}]}',
                            height=150,
                            key="transaction_data")
            
            # Add a run button to the form
            submit_button = st.form_submit_button("Run Use Case")
            
            if submit_button:
                # Prepare input data
                input_data = {"query": query}
                
                # Add use case specific parameters
                if current_case['id'] == 'use_case_01_fraud_detection' and "transaction_data" in st.session_state:
                    try:
                        transaction_data = json.loads(st.session_state.transaction_data)
                        input_data["transactions"] = transaction_data
                    except:
                        st.error("Invalid JSON format for transaction data")
                        
                # Save input data to session state
                st.session_state.input_data = input_data
                
                # Run the use case
                run_use_case()
            
        # Display result if available
        if st.session_state.is_running:
            with st.spinner("Running use case..."):
                time.sleep(0.1)  # Just to show the spinner
                
        if st.session_state.result:
            st.subheader("Result")
            
            result = st.session_state.result
            
            if result.get('success', False):
                # Show the result in an expandable section
                with st.expander("Result Details", expanded=True):
                    # Handle different result formats
                    if isinstance(result.get('result'), str):
                        st.markdown(result['result'])
                    elif isinstance(result.get('result'), dict):
                        st.json(result['result'])
                    else:
                        st.write(result['result'])
                    
                # Show raw output in an expandable section
                with st.expander("Raw Output", expanded=False):
                    st.code(result.get('output', 'No output captured'), language='text')
            else:
                st.error("Error running use case")
                st.code(result.get('error', 'Unknown error'))
                with st.expander("Error Details"):
                    st.code(result.get('traceback', 'No traceback available'))
else:
    st.info("👈 Select a use case from the sidebar to get started")

# Footer
st.markdown("---")
st.markdown("""
### About This Application

This unified interface provides access to multiple Crew AI agent applications for both financial and research domains.
Each use case utilizes specialized agents working together to solve specific problems.

**Technologies Used**:
- [CrewAI](https://crewai.io/) - Agent framework
- [Ollama](https://ollama.ai/) - Local language models
- [Streamlit](https://streamlit.io/) - UI framework
""")
