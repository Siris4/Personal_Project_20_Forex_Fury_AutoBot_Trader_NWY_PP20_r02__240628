import win32com.client

# Create a DDE client
dde = win32com.client.Dispatch("DDEClient.DDEClient")

# Connect to MT4's DDE server
dde.Connect("MT4", "BID")

# Request data
eurusd_bid = dde.Request("EURUSD")
print("EURUSD Bid: ", eurusd_bid)

# Disconnect
dde.Disconnect()
