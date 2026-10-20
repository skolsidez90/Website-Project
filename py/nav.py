"""Navigation. Events: click (menu button), scroll (header shadow)."""
from pyscript import when, window
from pyscript.ffi import create_proxy
from utils import q, qa

# Mark the link for the page we are on.
page = window.location.pathname.split("/")[-1] or "index.html"
for link in qa("#nav a"):
    if link.getAttribute("href") == page:
        link.setAttribute("aria-current", "page")


@when("click", "#nav-toggle")
def toggle_menu(event):
    is_open = q("#nav").classList.toggle("open")
    q("#nav-toggle").setAttribute("aria-expanded", "true" if is_open else "false")


def on_scroll(event):
    q(".site-header").classList.toggle("scrolled", window.scrollY > 8)


window.addEventListener("scroll", create_proxy(on_scroll))
