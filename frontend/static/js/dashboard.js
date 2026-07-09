/**
 * Dashboard JavaScript
 * ---------------------
 * Handles sidebar collapse/expand behavior for desktop and
 * mobile viewports, plus small UI interaction enhancements.
 */

document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const mainContent = document.getElementById("mainContent");
    const sidebarToggleBtn = document.getElementById("sidebarToggleBtn");
    const sidebarCloseBtn = document.getElementById("sidebarCloseBtn");
    const sidebarOverlay = document.getElementById("sidebarOverlay");

    const MOBILE_BREAKPOINT = 992;

    /**
     * Determines whether the current viewport is mobile-sized.
     */
    function isMobileView() {
        return window.innerWidth < MOBILE_BREAKPOINT;
    }

    /**
     * Toggles the sidebar open/closed depending on viewport size.
     * - Desktop: collapses sidebar to icon-only mode.
     * - Mobile: slides sidebar in/out with an overlay.
     */
    function toggleSidebar() {
        if (isMobileView()) {
            sidebar.classList.toggle("mobile-open");
            sidebarOverlay.classList.toggle("active");
        } else {
            sidebar.classList.toggle("collapsed");
            mainContent.classList.toggle("expanded");
        }
    }

    /**
     * Closes the mobile sidebar (used by overlay click / close button).
     */
    function closeMobileSidebar() {
        sidebar.classList.remove("mobile-open");
        sidebarOverlay.classList.remove("active");
    }

    if (sidebarToggleBtn) {
        sidebarToggleBtn.addEventListener("click", toggleSidebar);
    }

    if (sidebarCloseBtn) {
        sidebarCloseBtn.addEventListener("click", closeMobileSidebar);
    }

    if (sidebarOverlay) {
        sidebarOverlay.addEventListener("click", closeMobileSidebar);
    }

    /**
     * Resets sidebar state when resizing across the mobile breakpoint
     * to avoid inconsistent open/collapsed states.
     */
    window.addEventListener("resize", function () {
        if (!isMobileView()) {
            sidebar.classList.remove("mobile-open");
            sidebarOverlay.classList.remove("active");
        }
    });
});