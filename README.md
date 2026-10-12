# Cabinet math

Cabinet math plans the run before the order: the wall at a labeled box
width becomes the cabinet boxes and the filler, the box height at a labeled
spacing becomes the shelves, and the sheet at a labeled panel with a saw
kerf becomes the cut plan with an honest offcut.

Live site: https://ilanis-agent.github.io/cabinetmath/

## The three tools

- **Box plan** - `floor(wall / labeled box width (60 cm))` cabinet boxes
  and the filler to split between the ends, with a modest run / working
  kitchen / full galley verdict.
- **Shelf plan** - `floor(box height / labeled spacing (30 cm))` shelves
  and the gap left at the top, with a sparse stack / working stack /
  pantry tower verdict.
- **Sheet plan** - panels per sheet with the saw kerf charged on every cut
  (`floor((sheet + kerf) / (panel + kerf))` in mm) and the honest offcut,
  with a tight sheet / working sheet / generous offcut verdict.

## Limits

Every default is labeled and illustrative. Real cabinets carry dishes,
kids and local rules about anchoring. This is planning arithmetic, not a
structural design: measure the real wall and let the manufacturer specs
and a qualified installer govern.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 140 checks)

Run the tests: `python3 oracle.py && node test.js`
