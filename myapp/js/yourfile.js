<script src="script.js"></script>
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("healthMetrics").addEventListener("click", function () {
        window.location.href = "healthMetrics.html";
    });

    document.getElementById("chatAI").addEventListener("click", function () {
        window.location.href = "chatAI.html";
    });

    document.getElementById("visualInsights").addEventListener("click", function () {
        window.location.href = "visualInsights.html";
    });

    document.getElementById("setGoals").addEventListener("click", function () {
        window.location.href = "setGoals.html";
    });

    document.getElementById("trackProgress").addEventListener("click", function () {
        window.location.href = "trackProgress.html";
    });
    document.getElementById("logout-btn").addEventListener("click", function () {
        alert("You are logged out.");
        window.location.href = "/login"; // Redirect to login page
    });
    
    document.getElementById("dietPlan").addEventListener("click", function () {
        window.location.href = "dietPlan.html";
    });
});
fetch("/save_health_data/", {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken') // CSRF token for secure form submission
    },
    body: JSON.stringify(userData)
})

