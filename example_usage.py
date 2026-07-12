from client import PriceDropNotifierAlertsClient
client = PriceDropNotifierAlertsClient()
print(client.check_alert("ITEM-01", 12.5))