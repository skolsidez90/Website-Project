"""Washing machine animation. Event: click on the machine.
Python only adds and removes CSS classes. The CSS does the animating."""
from pyscript import when
from utils import q, after

machine = q("#machine")
status = q("#status")
state = {"busy": False, "done": False}


def stage(label, add=(), remove=()):
    status.textContent = label
    for name in add:
        machine.classList.add(name)
    for name in remove:
        machine.classList.remove(name)


def finish():
    stage("Done. Fresh and clean!", add=["is-done"], remove=["is-running"])
    state["busy"] = False
    state["done"] = True
    machine.setAttribute("aria-busy", "false")
    machine.setAttribute("aria-label", "Reset the washing machine")


def run_cycle():
    state["busy"] = True
    machine.setAttribute("aria-busy", "true")
    stage("Loading clothes", add=["is-open"])
    after(900, lambda: stage("Washing", add=["is-running"], remove=["is-open"]))
    after(3300, lambda: stage("Rinsing"))
    after(5100, lambda: stage("Spinning"))
    after(6900, finish)


def reset():
    state["done"] = False
    stage("Tap to wash", remove=["is-done"])
    machine.setAttribute("aria-label", "Start a wash cycle")


@when("click", "#machine")
def on_machine_click(event):
    if state["busy"]:
        return  # ignore clicks while a cycle is running
    reset() if state["done"] else run_cycle()
