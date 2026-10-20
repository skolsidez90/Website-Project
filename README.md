# Scrub-a-dub Laundry

Live website: [LIVE LINK]

A multi-page website for a laundry pickup and delivery service in Cebu City. It is the final project for Event-Driven Programming. All interactive logic is written in Python with PyScript. The booking form is a demo: nothing is sent to a server.

## Run locally

PyScript does not work from file://, so serve the folder:

    python -m http.server 8000

Then open http://localhost:8000. The first load is slow while PyScript downloads Python.

## Pages and PyScript features

| Page | Module | Events | What it does |
| --- | --- | --- | --- |
| all | py/nav.py | click, scroll | Menu button, current page link, header shadow |
| index.html | py/washing_machine.py | click | Runs the wash cycle by adding CSS classes |
| services.html | py/calculator.py | input, change, click | Live price estimate, rows select a service |
| order.html | py/booking.py | blur, submit | Validates the form, shows a confirmation card |
| about.html | py/faq.py | click | Accordion, one answer open at a time |

Shared files: py/config.py (sample prices and fees), py/utils.py (helpers), pyscript.toml (file list for PyScript).

## How the code is organized

Each module separates logic from the page. compute_total and validate are plain functions that take values and return results. The event handlers read the inputs, call those functions, and update the page.

## Before you publish

Replace every [PLACEHOLDER] in the HTML, set real prices in py/config.py, and replace assets/logo.png, assets/logo-small.png, assets/ad-poster.jpg, and add assets/ad.mp4.

## Deploy

GitHub Pages: Settings, Pages, deploy from the main branch, root folder. Vercel: import the repo with no build command. Then put the link at the top of this file.
