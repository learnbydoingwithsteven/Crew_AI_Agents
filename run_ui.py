"""
Launcher script for Crew AI Agents Unified UI
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if required packages are installed."""
    try:
        import streamlit
        import crewai
        import langchain
        print("✅ All required packages are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {str(e)}")
        print("Installing requirements...")
        
        # Get the absolute path to the requirements.txt file
        requirements_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
        
        # Install the requirements
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
            print("✅ Requirements installed successfully.")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements.")
            return False

def start_ui():
    """Start the Streamlit UI."""
    # Get the path to the UI app.py file
    ui_app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "app.py")
    
    # Check if the app.py file exists
    if not os.path.exists(ui_app_path):
        print(f"❌ UI application file not found at {ui_app_path}")
        return False
        
    # Start Streamlit
    print("🚀 Starting Crew AI Agents Unified UI...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", ui_app_path, "--server.port=8501"])
        return True
    except Exception as e:
        print(f"❌ Failed to start UI: {str(e)}")
        return False

if __name__ == "__main__":
    if check_requirements():
        start_ui()
    else:
        print("❌ Failed to start the UI due to missing requirements.")
        sys.exit(1)
