# Smart AI Assistant

**Smart AI Assistant** is a Streamlit-based AI-powered chatbot that provides detailed responses for finance, stocks, and general knowledge queries. It utilizes the `phi` framework, integrating `Groq` models and external tools like DuckDuckGo for web search and YFinance for financial data analysis.

## Features
- **Web Search Agent**: Retrieves and summarizes information from the web with citations.
- **Finance Agent**: Fetches stock prices, analyst recommendations, and financial fundamentals.
- **Multi-Agent System**: Combines different agents for enhanced responses.
- **Streamlit UI**: Simple and user-friendly interface.
- **Markdown Support**: Displays responses with headings, bullet points, and tables for clarity.
- **Debug Mode**: Provides detailed logs and insights.

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/smart-ai-assistant.git
cd smart-ai-assistant
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add necessary API keys if required.

## Running the App
```bash
streamlit run app.py
```

## Usage
1. Enter your query in the text area.
2. Click the **Ask** button.
3. View the detailed response along with sources.

## Requirements
- Python 3.8+
- Streamlit
- phi
- python-dotenv

## Contributing
Feel free to submit issues or pull requests to improve this project.

## License
This project is licensed under the MIT License.

---
**Author:** KIRIT P S

