# API Usage
# 🌐 Module 01 — API Usage

## 🎯 Objective
Learn how to fetch live data from online sources using Python’s `requests` library.  
APIs (Application Programming Interfaces) let us access real-time crypto or blockchain information — a key skill for data or blockchain roles.

---

## 📚 Lessons
| File | Description |
|------|--------------|
| `lesson2_api_basics.py` | Example: get Bitcoin price from CoinGecko and parse JSON response |
| `exercise2.py` | Practice: ask user for a crypto name and fetch its price in USD & EUR |
| `README.md` | Documentation for this module |

---

## 🧠 Key Concepts
- **HTTP requests**: communication between Python and web APIs.  
- **Status codes**: `200` = success, `404` = not found, `429` = rate limit.  
- **JSON parsing**: `.json()` converts API responses to Python dictionaries.  
- **Dynamic URLs**: use f-strings to insert variables in API endpoints.

---

## 🧪 Practice Task
1. Ask for user input (`bitcoin`, `ethereum`, etc.).  
2. Fetch its price via CoinGecko API:  
