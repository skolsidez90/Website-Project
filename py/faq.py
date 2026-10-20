"""FAQ accordion. Event: click on a question. One answer open at a time."""
from pyscript import when
from utils import qa


@when("click", ".faq-q")
def on_question(event):
    button = event.currentTarget
    opening = button.getAttribute("aria-expanded") != "true"
    for other in qa(".faq-q"):
        other.setAttribute("aria-expanded", "false")
        other.parentElement.classList.remove("open")
    if opening:
        button.setAttribute("aria-expanded", "true")
        button.parentElement.classList.add("open")
