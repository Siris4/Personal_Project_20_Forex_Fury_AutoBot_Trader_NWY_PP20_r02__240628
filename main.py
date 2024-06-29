import metatrader as MT4
import pandas as pd

# Connect to MetaTrader 4
mt4 = MT4()
mt4.initialize()

# Log in to your account
mt4.login(account_number='your_account_number', password='your_password', server='your_broker_server')

# Fetch trade history
trades = mt4.get_trade_history()

# Convert to DataFrame
df = pd.DataFrame(trades)

# Display trade history
print(df)

# Shutdown connection
mt4.shutdown()
