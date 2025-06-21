# Web Surfer - AI-Powered Web Assistant

A Streamlit-based web application that provides an AI-powered assistant capable of browsing the web, extracting information, running Python code, and more.

## Features

- 🌐 Web browsing and navigation
- 📄 Information extraction from websites
- 🐍 Python code execution
- 💾 File management capabilities
- 🤖 AI-powered task completion
- 📊 Real-time feedback and evaluation

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Run the application:**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser:**
   The application will automatically open in your default browser at `http://localhost:8501`

3. **Start using Web Surfer:**
   - Enter your request in the text area
   - Specify your success criteria
   - Click "Go!" to process your request
   - Use the reset button to start fresh

## How it Works

The Web Surfer uses:
- **LangGraph** for workflow orchestration
- **Playwright** for web automation
- **OpenAI GPT-4** for AI processing
- **Streamlit** for the user interface

The system follows a workflow where:
1. Your request is processed by an AI worker
2. The worker uses various tools (web browsing, Python execution, etc.)
3. An evaluator checks if the success criteria are met
4. The process continues until completion or user input is needed

## File Structure

- `main.py` - Streamlit application interface
- `web_serfer.py` - Core Web Surfer class and logic
- `web_serfer_tools.py` - Tool definitions for web browsing and other capabilities
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this file)

## Tips

- Be specific in your requests
- Provide clear success criteria
- The assistant will ask questions if clarification is needed
- Use the reset button to start fresh conversations
- Check the sidebar for additional information and tips

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for web browsing capabilities 