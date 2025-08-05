document.addEventListener("DOMContentLoaded", () => {
    // Password Strength Checker
    const passwordInput = document.querySelector("input[name='password1']");
    const strengthBar = document.getElementById("password-strength-bar");

    if (passwordInput && strengthBar) {
        passwordInput.addEventListener("input", () => {
            const value = passwordInput.value;
            let strength = 0;

            if (value.length >= 8) strength += 1;
            if (/[a-z]/.test(value)) strength += 1;
            if (/[A-Z]/.test(value)) strength += 1;
            if (/[0-9]/.test(value)) strength += 1;
            if (/[^A-Za-z0-9]/.test(value)) strength += 1;

            strengthBar.style.width = `${strength * 20}%`;

            if (strength <= 2) {
                strengthBar.style.backgroundColor = "#e74c3c"; // red
            } else if (strength <= 4) {
                strengthBar.style.backgroundColor = "#f1c40f"; // yellow
            } else {
                strengthBar.style.backgroundColor = "#2ecc71"; // green
            }
        });
    }

    // Input Focus/Blur Effects
    const inputs = document.querySelectorAll(".form-group input");
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.parentElement.classList.add("focused");
        });
        input.addEventListener("blur", () => {
            if (!input.value.trim()) {
                input.parentElement.classList.remove("focused");
            }
        });
    });

    // Show/Hide Password Toggle
    const toggle = document.getElementById("show-password-toggle");
    if (passwordInput && toggle) {
        toggle.addEventListener("change", () => {
            passwordInput.type = toggle.checked ? "text" : "password";
        });
    }
});
