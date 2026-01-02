# YerLocal – Derry Visitor Guide

YerLocal (*pronounced "Your Local"*), is a web application designed to give visitors to Derry/Londonderry a *“local in their pocket”*.
The app focuses on helping visitors understand the city as a local would: where to walk, what they are seeing, how to get around, and where to eat or relax.

This project is being developed as a personal project and follows an MVP-first approach, with features added incrementally.

---

## Project Status

- **Status**: In active development
- **Current focus**: Bus checker

---

## Project Goals

The primary goal for ***YerLocal*** is to improve visitor knowledge with simple and easy to use technology.

The app, unlike commercial platforms, will focus on:

- Curated local content
- Walkable routes
- Practical transport advice
- A clean, mobile friendly interface

---

## MVP Features

The current MVP will focus on a self-guided walking tour of the historic city walls and a bus stop checker, to help clarify departure times when not at the closest stop.

### City Walls Guide

Implemented features for the MVP will include:

- An interactive map using Leaflet
- Marked points of interest on the route
- Each stop will include:
  - Stop position
  - Name
  - A brief historical description
- A highlighted path to mark out the walking route
- Stop content will be managed through the Django admin panel.

All data will be stored locally in the projects SQLite database.

### Bus Checker

The bus checker idea came from myself staying outside the city, before I left for the bus I had to check multiple timetables for the next bus as
multiple buses passed the stop I was using. The user experience was tedious, so I wanted to simplify that for any visitors staying in the outskirts of the city.

Features for the MVP will include:

- Arrival times of the next bus for a chosen stop.
- Focusing on travelling to and from the city.
- A clear UI displaying the next bus, and following buses.

---

## Planned Features (My full vision)

The full vision that I have for the project is that any visitor to the city will have an insight to the city through the eyes of a local.

Planned features include:

- Places to eat:
  - Local restaurants, cafes and pubs.
  - Descriptions on the style of food, atmosphere and menu previews.
  - Contact details and location.
- Things to do:
  - Attractions and activities.
  - Practical visitor information.
- Multi-language support:
  - Languages added incrementally based on visitor demographics.
- Media:
  - Images for stops and locations.
  - Audio narration for the walls self-guided tour.

These features are out of scope for the MVP and will be added throughout time.

---

## Tech Stack

- **Backend**: Django
- **Database**: SQLite (*for development*)
- **Mapping**: Leaflet
- **Map data**: OpenStreetMap (tile providers)
- **Styling**: HTML/Bootstrap (for mobile responsive layout)

Django was chosen as its well-structured, allows for modularity and has a built-in admin interface.

---

