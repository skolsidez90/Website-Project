"""Runs the cartoon washer on button click and bursts bubbles when it stops."""
from pyscript import when
from utils import q, after

machine = q("#machine")
status = q("#status")
busy = False


@when("click", "#machine")
def on_machine_click(event):
    global busy
    if busy:
        return

    if machine.classList.contains("is-done"):
        machine.classList.remove("is-done")
        status.textContent = "Ready to wash"
        machine.setAttribute("aria-label", "Start the washing machine")
        return

    busy = True
    machine.classList.add("is-spinning")
    machine.setAttribute("aria-busy", "true")
    status.textContent = "Spinning!"

    def finish_cycle():
        global busy
        machine.classList.remove("is-spinning")
        machine.classList.add("is-done")
        machine.setAttribute("aria-busy", "false")
        machine.setAttribute("aria-label", "Reset the washing machine")
        status.textContent = "Fresh and clean!"
        busy = False

    after(3200, finish_cycle)
