
# finagent
 LLM powered stock analysis agent 
  <p align="">
  <img src="assets/logo.png" alt="Logo" width="150">
</p>


## Features
- LLM-powered analysis for stock trends
- Real-time data processing
- User-friendly interface for stock queries
- Light weight , uses in-device LLMs ( eg llama3:8b)

## Design
- In a nutshell 
    - Uses yfinance APIs to pull stock data
    - Compares fundamentals to universally agreed thresholds and limits
    - Creates a pipeline with LLM integration to compare data and generate text
    - Consolidates the commentary

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/finagent.git
    ```
2. Navigate to the project directory:
    ```bash
    cd finagent
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To start the agent, run:
```
 python main.py --symbol <stock ticker> --country <US/IN> --output_dir ./
 eg :  python main.py --symbol TATAMOTORS --country IN --output_dir ./
 ```

 ## Disclaimer

 This is still work in progress. Use with caution :)

 Planned immediate work :
 - Integration of technical analysis 
 - Provide buy/hold/sell recommendation
 - Feedback from friends/colleagues.