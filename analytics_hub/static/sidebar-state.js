(function () {
  "use strict";

  var toggle = document.getElementById("sidebarToggle");

  if (!toggle) {
    return;
  }

  var storageKey = "analyticsHubSidebarCollapsed";

  function readStoredState() {
    try {
      return window.localStorage.getItem(storageKey) === "true";
    } catch (error) {
      return document.cookie
        .split("; ")
        .some(function (item) {
          return item === storageKey + "=true";
        });
    }
  }

  function saveState(collapsed) {
    try {
      window.localStorage.setItem(storageKey, String(collapsed));
    } catch (error) {
      document.cookie =
        storageKey +
        "=" +
        String(collapsed) +
        "; path=/; max-age=31536000; SameSite=Lax";
    }
  }

  toggle.checked = readStoredState();

  toggle.addEventListener("change", function () {
    saveState(toggle.checked);
  });
})();
