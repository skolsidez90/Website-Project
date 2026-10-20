"""Shop settings. Every price here is a SAMPLE. Replace with the shop's real numbers."""

PESO = "₱"
SERVICES = {
    "wash": {"label": "Wash and fold", "unit": "kilo", "price": 50.0, "note": "Everyday clothes, washed, dried, folded."},
    "dry": {"label": "Dry cleaning", "unit": "item", "price": 150.0, "note": "Suits, dresses, and delicate pieces."},
    "iron": {"label": "Ironing", "unit": "item", "price": 30.0, "note": "Pressed and ready to hang."},
    "bed": {"label": "Bedding", "unit": "piece", "price": 200.0, "note": "Sheets, blankets, and comforters."},
}
RUSH_RATE = 0.5      # rush adds 50% of the laundry cost
DELIVERY_FEE = 60.0  # flat fee for pickup and delivery
MAX_QTY = 100        # largest quantity the calculator accepts
