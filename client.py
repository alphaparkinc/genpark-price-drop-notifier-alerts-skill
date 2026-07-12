class PriceDropNotifierAlertsClient:
    def check_alert(self, sku: str, percent_drop: float) -> dict:
        return {"alert_triggered": percent_drop > 10.0}