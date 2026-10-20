"""Booking form. Events: blur (check one field), submit (check all, show confirmation)."""
import random
import re
import string
from pyscript import when
from config import SERVICES
from utils import q, today_iso, after

FIELDS = ["name", "phone", "address", "date"]
q("#b-date").min = today_iso()


def read_form():
    return {f: q(f"#b-{f}").value for f in FIELDS + ["service", "notes"]}


def validate(data, today):
    """Pure validation. Returns {field: message} for every problem found."""
    errors = {}
    if len(data["name"].strip()) < 2:
        errors["name"] = "Enter your full name."
    phone = re.sub(r"[ -]", "", data["phone"])
    if not re.fullmatch(r"(09\d{9}|\+639\d{9})", phone):
        errors["phone"] = "Use 09XXXXXXXXX or +639XXXXXXXXX."
    if len(data["address"].strip()) < 8:
        errors["address"] = "Enter your street and barangay."
    if not data["date"]:
        errors["date"] = "Pick a pickup date."
    elif data["date"] < today:
        errors["date"] = "Pick today or a later date."
    return errors


def show_error(field, message):
    q(f"#e-{field}").textContent = message
    q(f"#f-{field}").classList.toggle("invalid", bool(message))
    q(f"#b-{field}").setAttribute("aria-invalid", "true" if message else "false")


def make_reference(today):
    code = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"SAD-{today.replace('-', '')[2:]}-{code}"  # SAD-YYMMDD-XXXX


@when("blur", "#b-name, #b-phone, #b-address, #b-date")
def on_blur(event):
    field = event.target.id[2:]
    show_error(field, validate(read_form(), today_iso()).get(field, ""))


@when("submit", "#booking-form")
def on_submit(event):
    event.preventDefault()
    today = today_iso()
    data = read_form()
    errors = validate(data, today)
    for field in FIELDS:
        show_error(field, errors.get(field, ""))
    if errors:
        q(f"#b-{next(f for f in FIELDS if f in errors)}").focus()
        return
    ticket = q("#ticket")
    ticket.classList.remove("show")
    q("#c-ref").textContent = make_reference(today)
    q("#c-name").textContent = data["name"].strip()
    q("#c-service").textContent = SERVICES[data["service"]]["label"]
    q("#c-date").textContent = data["date"]
    q("#c-empty").hidden = True
    ticket.hidden = False
    after(30, lambda: ticket.classList.add("show"))  # restart the stamp animation
    q("#confirmation").focus()
    q("#booking-form").reset()
