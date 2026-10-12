import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def box_plan(wallCm, boxCm):
    if not (wallCm > 0) or not (boxCm > 0):
        return {"error": "the wall and the labeled box width must be positive"}
    if wallCm < boxCm:
        return {"error": "the wall is shorter than one labeled cabinet box"}
    boxes = math.floor(wallCm / boxCm)
    filler = round1(wallCm - boxes * boxCm)
    if boxes <= 2: verdict = "a modest run"
    elif boxes <= 4: verdict = "a working kitchen"
    else: verdict = "a full galley"
    return {"boxes": boxes, "filler": filler, "verdict": verdict}

def shelf_plan(heightCm, spacingCm):
    if not (heightCm > 0) or not (spacingCm > 0):
        return {"error": "the box height and the labeled spacing must be positive"}
    if heightCm < spacingCm:
        return {"error": "the box is shorter than one labeled shelf spacing"}
    shelves = math.floor(heightCm / spacingCm)
    topGap = round1(heightCm - shelves * spacingCm)
    if shelves <= 2: verdict = "a sparse stack"
    elif shelves <= 4: verdict = "a working stack"
    else: verdict = "a pantry tower"
    return {"shelves": shelves, "topGap": topGap, "verdict": verdict}

def sheet_plan(sheetCm, panelCm, kerfMm):
    if not (sheetCm > 0) or not (panelCm > 0) or not (kerfMm >= 0):
        return {"error": "the sheet and the labeled panel must be positive and the kerf zero or more"}
    if panelCm > sheetCm:
        return {"error": "the panel is longer than the sheet"}
    sheetMm = sheetCm * 10
    panelMm = panelCm * 10
    panels = math.floor((sheetMm + kerfMm) / (panelMm + kerfMm))
    usedMm = panels * (panelMm + kerfMm) - kerfMm
    leftover = round1((sheetMm - usedMm) / 10)
    if leftover <= 10: verdict = "a tight sheet"
    elif leftover <= 40: verdict = "a working sheet"
    else: verdict = "a generous offcut"
    return {"panels": panels, "leftover": leftover, "verdict": verdict}

def render_box(r, wallCm, boxCm):
    return ("A wall " + fmt(wallCm) + " cm at a labeled " + fmt(boxCm) + " cm box takes "
            + plural(r["boxes"], "cabinet box", "cabinet boxes") + " with " + fmt(r["filler"]) + " cm of filler to split between the ends - " + r["verdict"] + ".")

def render_shelf(r, heightCm, spacingCm):
    return ("A box " + fmt(heightCm) + " cm tall at a labeled " + fmt(spacingCm) + " cm spacing holds "
            + plural(r["shelves"], "shelf", "shelves") + " with " + fmt(r["topGap"]) + " cm left at the top - " + r["verdict"] + ".")

def render_sheet(r, sheetCm, panelCm, kerfMm):
    return ("A sheet " + fmt(sheetCm) + " cm at a labeled " + fmt(panelCm) + " cm panel with a " + fmt(kerfMm)
            + " mm kerf yields " + plural(r["panels"], "panel") + " and leaves " + fmt(r["leftover"]) + " cm of offcut - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[320,60],[120,60],[240,60],[600,60],[0,60],[320,0],[50,60],[60,60],[200,80],[145.5,60]]:
    add("boxPlan", box_plan, render_box, a)
for a in [[90,30],[72,30],[150,30],[30,30],[0,30],[90,0],[25,30],[96.5,30],[130,30],[200,40]]:
    add("shelfPlan", shelf_plan, render_shelf, a)
for a in [[244,60,3],[244,30,3],[244,120,3],[244,244,3],[0,60,3],[244,0,3],[244,60,-1],[244,300,3],[244,61.5,3],[200,45,2]]:
    add("sheetPlan", sheet_plan, render_sheet, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
