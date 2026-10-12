(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function boxPlan(wallCm, boxCm) {
    if (!(wallCm > 0) || !(boxCm > 0)) return { error: "the wall and the labeled box width must be positive" };
    if (wallCm < boxCm) return { error: "the wall is shorter than one labeled cabinet box" };
    var boxes = Math.floor(wallCm / boxCm);
    var filler = round1(wallCm - boxes * boxCm);
    var verdict;
    if (boxes <= 2) verdict = "a modest run";
    else if (boxes <= 4) verdict = "a working kitchen";
    else verdict = "a full galley";
    return { boxes: boxes, filler: filler, verdict: verdict };
  }

  function shelfPlan(heightCm, spacingCm) {
    if (!(heightCm > 0) || !(spacingCm > 0)) return { error: "the box height and the labeled spacing must be positive" };
    if (heightCm < spacingCm) return { error: "the box is shorter than one labeled shelf spacing" };
    var shelves = Math.floor(heightCm / spacingCm);
    var topGap = round1(heightCm - shelves * spacingCm);
    var verdict;
    if (shelves <= 2) verdict = "a sparse stack";
    else if (shelves <= 4) verdict = "a working stack";
    else verdict = "a pantry tower";
    return { shelves: shelves, topGap: topGap, verdict: verdict };
  }

  function sheetPlan(sheetCm, panelCm, kerfMm) {
    if (!(sheetCm > 0) || !(panelCm > 0) || !(kerfMm >= 0)) return { error: "the sheet and the labeled panel must be positive and the kerf zero or more" };
    if (panelCm > sheetCm) return { error: "the panel is longer than the sheet" };
    var sheetMm = sheetCm * 10, panelMm = panelCm * 10;
    var panels = Math.floor((sheetMm + kerfMm) / (panelMm + kerfMm));
    var usedMm = panels * (panelMm + kerfMm) - kerfMm;
    var leftover = round1((sheetMm - usedMm) / 10);
    var verdict;
    if (leftover <= 10) verdict = "a tight sheet";
    else if (leftover <= 40) verdict = "a working sheet";
    else verdict = "a generous offcut";
    return { panels: panels, leftover: leftover, verdict: verdict };
  }

  function renderBox(r, wallCm, boxCm) {
    return "A wall " + wallCm + " cm at a labeled " + boxCm + " cm box takes " + plural(r.boxes, "cabinet box", "cabinet boxes") + " with " + r.filler + " cm of filler to split between the ends - " + r.verdict + ".";
  }

  function renderShelf(r, heightCm, spacingCm) {
    return "A box " + heightCm + " cm tall at a labeled " + spacingCm + " cm spacing holds " + plural(r.shelves, "shelf", "shelves") + " with " + r.topGap + " cm left at the top - " + r.verdict + ".";
  }

  function renderSheet(r, sheetCm, panelCm, kerfMm) {
    return "A sheet " + sheetCm + " cm at a labeled " + panelCm + " cm panel with a " + kerfMm + " mm kerf yields " + plural(r.panels, "panel") + " and leaves " + r.leftover + " cm of offcut - " + r.verdict + ".";
  }

  var api = { boxPlan: boxPlan, shelfPlan: shelfPlan, sheetPlan: sheetPlan, renderBox: renderBox, renderShelf: renderShelf, renderSheet: renderSheet };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.CabinetMath = api;
})(this);
