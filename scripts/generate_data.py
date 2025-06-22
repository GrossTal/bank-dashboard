import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 100
NUM_ACCOUNTS = 150
NUM_TRANSACTIONS = 1000

# --- Customers Table ---
customers = []
risk_levels = ["Low", "Medium", "High"]

for cid in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": cid,
        "name": fake.name(),
        "age": random.randint(18, 85),
        "region": fake.city(),
        "risk_level": random.choices(risk_levels, weights=[0.6, 0.3, 0.1])[0]
    })

customers_df = pd.DataFrame(customers)
customers_df.to_csv("data/customers.csv", index=False)

# --- Accounts Table ---
accounts = []

for aid in range(1, NUM_ACCOUNTS + 1):
    accounts.append({
        "account_id": aid,
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "account_type": random.choice(["Checking", "Savings"]),
        "balance": round(random.uniform(100, 50000), 2)
    })

accounts_df = pd.DataFrame(accounts)
accounts_df.to_csv("data/accounts.csv", index=False)

# --- Transactions Table ---
transactions = []

channels = ["ATM", "Online", "Branch", "Mobile"]
types = ["Debit", "Credit", "Transfer", "Wire"]

start_date = datetime.now() - timedelta(days=90)

for tid in range(1, NUM_TRANSACTIONS + 1):
    timestamp = start_date + timedelta(minutes=random.randint(0, 129600))  # ~90 days
    amount = round(random.uniform(5, 10000), 2)
    account_id = random.randint(1, NUM_ACCOUNTS)

    transactions.append({
        "transaction_id": tid,
        "account_id": account_id,
        "amount": amount,
        "type": random.choice(types),
        "channel": random.choice(channels),
        "currency": random.choice(["ILS", "USD", "EUR"]),
        "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S')
    })

transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv("data/transactions.csv", index=False)

print("Data generated: customers.csv, accounts.csv, transactions.csv")
