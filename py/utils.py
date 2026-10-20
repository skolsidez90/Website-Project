"""Small helpers shared by the other modules."""
from pyscript import document, window
from config import PESO


def q(selector):
    return document.querySelector(selector)


def qa(selector):
    return document.querySelectorAll(selector)


def peso(amount):
    return f"{PESO}{amount:,.2f}"


def today_iso():
    """Today's date in the visitor's local time, as YYYY-MM-DD."""
    d = window.Date.new()
    return f"{d.getFullYear()}-{d.getMonth() + 1:02d}-{d.getDate():02d}"


def after(ms, func):
    """Run func once after ms milliseconds."""
    from pyscript.ffi import create_proxy
    window.setTimeout(create_proxy(func), ms)
