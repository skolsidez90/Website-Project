"""Live price estimate for the Services page."""

from js import document
from pyscript import when

# Sample rates for the classroom demo. Replace these after the group agrees
# on real prices. All service rates in this simple calculator are per kilo.
PRICES = {
    "Wash and fold": 50,
    "Dry cleaning": 120,
    "Ironing": 45,
    "Bedding": 80,
    "Rush fee": 50,
    "Pickup and delivery fee": 40,
}

service_input = document.querySelector("#service")
weight_input = document.querySelector("#weight")
rush_input = document.querySelector("#rush")
delivery_input = document.querySelector("#delivery")
message = document.querySelector("#estimate-message")


def format_pesos(amount):
    """Show a number as Philippine pesos with two decimal places."""
    return f"₱{amount:,.2f}"


def update_receipt():
    """Calculate the total and place each amount in the receipt."""
    try:
        weight = float(weight_input.value)
    except (TypeError, ValueError):
        message.textContent = "Enter a laundry weight greater than zero."
        return

    if weight <= 0:
        message.textContent = "Enter a laundry weight greater than zero."
        return

    service_name = service_input.value
    subtotal = PRICES[service_name] * weight
    rush_fee = PRICES["Rush fee"] if rush_input.checked else 0
    delivery_fee = PRICES["Pickup and delivery fee"] if delivery_input.checked else 0
    total = subtotal + rush_fee + delivery_fee

    document.querySelector("#receipt-service").textContent = service_name
    document.querySelector("#receipt-subtotal").textContent = format_pesos(subtotal)
    document.querySelector("#receipt-rush").textContent = format_pesos(rush_fee)
    document.querySelector("#receipt-delivery").textContent = format_pesos(delivery_fee)
    document.querySelector("#receipt-total").textContent = format_pesos(total)
    message.textContent = ""


# Change event: recalculate when the visitor chooses a different service.
@when("change", "#service")
def on_service_change(event):
    update_receipt()


# Input event: recalculate while the visitor edits the laundry weight.
@when("input", "#weight")
def on_weight_input(event):
    update_receipt()


# Change event: include or remove the rush-service fee.
@when("change", "#rush")
def on_rush_change(event):
    update_receipt()


# Change event: include or remove the pickup-and-delivery fee.
@when("change", "#delivery")
def on_delivery_change(event):
    update_receipt()


# Show an estimate as soon as the page loads.
update_receipt()
