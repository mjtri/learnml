/* Tap-to-define glossary + iframe helpers. No dependencies.
   Every <abbr title="..."> (generated from glossary/terms.jsonl) opens a bottom sheet on tap/click/Enter. */
(function () {
  "use strict";
  var sheet, backdrop, lastFocus;

  function build() {
    backdrop = document.createElement("div");
    backdrop.className = "gl-backdrop";
    backdrop.hidden = true;
    sheet = document.createElement("div");
    sheet.className = "gl-sheet";
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.setAttribute("aria-labelledby", "gl-term");
    sheet.hidden = true;
    sheet.innerHTML =
      '<div class="gl-grip"></div>' +
      '<div class="gl-term" id="gl-term"></div>' +
      '<div class="gl-def"></div>' +
      '<div class="gl-actions"><a class="gl-more">Open in glossary →</a>' +
      '<button type="button" class="gl-close">Got it</button></div>';
    document.body.appendChild(backdrop);
    document.body.appendChild(sheet);
    backdrop.addEventListener("click", close);
    sheet.querySelector(".gl-close").addEventListener("click", close);
  }

  function glossaryUrl(term) {
    var map = window.LEARNML_GLOSSARY || {};
    var anchor = map[term] || "";
    var base = typeof __md_scope !== "undefined" ? __md_scope : new URL(".", location);
    return new URL("glossary.html" + (anchor ? "#" + anchor : ""), base).href;
  }

  function open(el) {
    if (!sheet) build();
    var term = el.textContent.trim();
    // The title is moved to data-def so the browser's own slow tooltip never doubles up on touch.
    sheet.querySelector(".gl-term").textContent = term;
    sheet.querySelector(".gl-def").textContent = el.getAttribute("data-def") || el.getAttribute("title") || "";
    sheet.querySelector(".gl-more").href = glossaryUrl(term);
    lastFocus = el;
    backdrop.hidden = false;
    sheet.hidden = false;
    requestAnimationFrame(function () { sheet.classList.add("is-open"); backdrop.classList.add("is-open"); });
    sheet.querySelector(".gl-close").focus({ preventScroll: true });
  }

  function close() {
    if (!sheet || sheet.hidden) return;
    sheet.classList.remove("is-open");
    backdrop.classList.remove("is-open");
    setTimeout(function () { sheet.hidden = true; backdrop.hidden = true; }, 160);
    if (lastFocus) lastFocus.focus({ preventScroll: true });
  }

  function prepare() {
    var coarse = matchMedia("(hover: none)").matches;
    var map = window.LEARNML_GLOSSARY || {};
    var seen = {};
    // Every occurrence is tappable, but only the first one per section is underlined, to keep the page calm.
    document.querySelectorAll(".md-content h2, .md-content abbr[title]").forEach(function (el) {
      if (el.tagName === "H2") { seen = {}; return; }
      var key = map[el.textContent.trim()] || el.textContent.trim().toLowerCase();
      if (!seen[key] && !el.closest("h1, h2, h3, summary")) { seen[key] = true; el.classList.add("gl-first"); }
      el.setAttribute("tabindex", el.classList.contains("gl-first") ? "0" : "-1");
      el.setAttribute("role", "button");
      el.setAttribute("data-def", el.getAttribute("title"));
      if (coarse) el.removeAttribute("title"); // desktop keeps the hover tooltip
    });
  }

  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest(".md-content abbr[data-def]");
    if (!el) return;
    // A term inside a link or a collapsible title should still let that control work.
    if (el.closest("a, summary")) return;
    e.preventDefault();
    e.stopPropagation();
    open(el);
  }, true);

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") close();
    if ((e.key === "Enter" || e.key === " ") && e.target.matches && e.target.matches("abbr[data-def]")) {
      e.preventDefault();
      open(e.target);
    }
  });

  // Visuals report their own height so iframes never scroll internally.
  window.addEventListener("message", function (e) {
    var d = e.data;
    if (!d || typeof d.learnmlHeight !== "number") return;
    document.querySelectorAll(".visual iframe").forEach(function (f) {
      if (f.contentWindow === e.source) f.style.height = Math.ceil(d.learnmlHeight) + "px";
    });
  });

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", prepare);
  else prepare();
})();
