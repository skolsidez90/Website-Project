"""Price calculator. Events: input (quantity), change (service, toggles), click (service rows)."""
from pyscript import when, window
from pyscript.ffi import create_proxy
from config import SERVICES, RUSH_RATE, DELIVERY_FEE, MAX_QTY
from utils import q, qa, peso

state = {"shown_total": 0.0}


def compute_total(service, qty, rush, delivery):
    """Pure calculation. No DOM access, so it is easy to test and explain."""
    base = SERVICES[service]["price"] * qty
    rush_fee = base * RUSH_RATE if rush else 0.0
    delivery_fee = DELIVERY_FEE if delivery else 0.0
    return {"base": base, "rush": rush_fee, "delivery": delivery_fee,
            "total": base + rush_fee + delivery_fee}


def parse_qty(text):
    """Return a valid quantity or None."""
    try:
        value = float(text)
    except ValueError:
        return None
    return value if 0 < value <= MAX_QTY else None


def count_to(target, steps=12):
    """Make the total count up (or down) instead of jumping."""
    start = state["shown_total"]

    def tick(i):
        q("#r-total").textContent = peso(start + (target - start) * i / steps)
        if i < steps:
            window.setTimeout(create_proxy(lambda: tick(i + 1)), 20)
    tick(1)
    state["shown_total"] = target


def update():
    service = q("#service").value
    q("#qty-label").textContent = f"Quantity ({SERVICES[service]['unit']}s)"
    qty = parse_qty(q("#kilos").value)
    if qty is None:
        q("#calc-msg").textContent = f"Enter a quantity above 0, up to {MAX_QTY}."
        qty = 0
    else:
        q("#calc-msg").textContent = ""
    r = compute_total(service, qty, q("#rush").checked, q("#delivery").checked)
    q("#r-sub").textContent = peso(r["base"])
    q("#r-rush").textContent = peso(r["rush"])
    q("#r-del").textContent = peso(r["delivery"])
    count_to(r["total"])


@when("input", "#kilos")
def on_quantity(event):
    update()


@when("change", "#service, #rush, #delivery")
def on_option(event):
    update()


@when("click", ".svc")
def on_service_row(event):
    q("#service").value = event.currentTarget.dataset.service
    update()
    q("#calculator").scrollIntoView()


# Fill the price shown on each service row from config.py.
for row in qa(".svc"):
    s = SERVICES[row.dataset.service]
    row.querySelector(".price").textContent = f"{peso(s['price'])} per {s['unit']}"
update()
