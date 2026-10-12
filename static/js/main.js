const navigationToggle = document.querySelector(".nav-toggle");
const navigationMenu = document.querySelector("#primary-navigation");

if (navigationToggle && navigationMenu) {
    document.documentElement.classList.add("js");
    navigationToggle.hidden = false;

    navigationToggle.addEventListener("click", () => {
        const isExpanded = navigationToggle.getAttribute("aria-expanded") === "true";
        navigationToggle.setAttribute("aria-expanded", String(!isExpanded));
    });

    navigationMenu.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && navigationToggle.getAttribute("aria-expanded") === "true") {
            navigationToggle.setAttribute("aria-expanded", "false");
            navigationToggle.focus();
        }
    });
}
