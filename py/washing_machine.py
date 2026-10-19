"""Interactive washing-machine illustration for the home page."""

import asyncio
from js import document
from pyscript import when

machine = document.querySelector("#washer-button")
status = document.querySelector("#washer-status")
cycle_number = 0
is_running = False


# Click event: start the wash cycle, or stop it and reset the machine.
@when("click", "#washer-button")
async def run_wash_cycle(event):
    global cycle_number, is_running

    cycle_number += 1
    this_cycle = cycle_number

    # A second click changes the cycle number, so the earlier animation stops.
    if is_running:
        is_running = False
        machine.classList.remove("is-running")
        machine.classList.remove("is-done")
        status.textContent = "Ready"
        return

    is_running = True
    machine.classList.add("is-running")

    steps = [
        ("Washing", 2.0),
        ("Rinsing", 1.5),
        ("Spinning", 1.5),
    ]

    for label, seconds in steps:
        if this_cycle != cycle_number:
            return
        status.textContent = label
        await asyncio.sleep(seconds)

    if this_cycle == cycle_number:
        is_running = False
        machine.classList.remove("is-running")
        machine.classList.add("is-done")
        status.textContent = "Done!"
        machine.setAttribute("aria-label", "Fresh and clean!")
        await asyncio.sleep(0.45)
        if this_cycle == cycle_number:
            machine.classList.remove("is-done")
            machine.setAttribute("aria-label", "Start the washing machine cycle")
            status.textContent = "Fresh and clean!"
