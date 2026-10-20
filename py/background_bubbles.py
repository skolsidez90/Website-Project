"""Lets visitors pop the decorative bubbles with a click event."""
from pyscript import when
from utils import after


@when("click", ".bubble-background__bubble")
def on_bubble_click(event):
    bubble = event.target
    bubble.classList.add("is-popping")
    after(320, lambda: bubble.remove())
