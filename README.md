API Integration – Cryptocurrency Price Fetcher
📌 Project Overview
This project is a Python script that integrates with an external REST API to fetch and display real-time cryptocurrency prices. It demonstrates how to make HTTP GET requests, handle API responses, parse JSON data, and manage potential errors gracefully.
This project was completed as part of Level 2 – Task 3 of my internship program.
🎯 Objectives
Use the requests library to make GET requests to an external API
Fetch live data from a public API
Parse JSON responses
Display data in a user-friendly format
Handle network and invalid response errors
🛠️ Technologies Used
Python 3
Requests library
CoinGecko Public API (No API key required)
🔗 API Used
CoinGecko Simple Price API
Endpoint:

https://api.coingecko.com/api/v3/simple/price
Example parameters:
ids: cryptocurrency name (e.g., bitcoin, ethereum)
vs_currencies: target currency (usd)
⚙️ Features
Fetches real-time prices for any cryptocurrency
Supports dynamic user input
Handles:
Network errors
Invalid cryptocurrency names
Failed API requests
Clean and readable output formatting
🧑‍💻 How It Works
User enters a cryptocurrency name
Script sends a GET request to the CoinGecko API
API response is validated and parsed
Current price is displayed in USD
Errors are handled gracefully without crashing
▶️ How to Run the Project
1️⃣ Install dependencies
Bash
pip install requests
2️⃣ Run the script
Bash
python crypto_price.py
3️⃣ Enter a cryptocurrency

bitcoin
ethereum
solana
📌 Sample Output

Enter cryptocurrency (bitcoin, ethereum, solana, etc.): ethereum
✅ Current price of Ethereum: $2,320
(Prices vary based on real-time data)
🛡️ Error Handling
The script handles:
Network failures (no internet, timeout)
Invalid API responses
Incorrect cryptocurrency names