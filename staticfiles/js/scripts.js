// Function to open modal
function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "block";
}

// Function to close modal
function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none";
}

document.addEventListener("DOMContentLoaded", function() {
    // Attach event listeners to open and close modal buttons
    document.querySelectorAll("[data-open-modal]").forEach(button => {
        button.addEventListener("click", function() {
            var modalId = this.getAttribute("data-open-modal");
            openModal(modalId);
        });
    });

    document.querySelectorAll(".close").forEach(button => {
        button.addEventListener("click", function() {
            var modalId = this.closest(".modal").id;
            closeModal(modalId);
        });
    });

    // Close the modal when clicking outside of it
    window.addEventListener("click", function(event) {
        document.querySelectorAll(".modal").forEach(modal => {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        });
    });

    // Handle form submissions via AJAX
    function handleFormSubmission(event) {
        event.preventDefault();
        var form = event.target;

        fetch(form.action, {
            method: form.method,
            body: new FormData(form),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': form.querySelector("[name=csrfmiddlewaretoken]").value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();  // Reload the page if the form submission is successful
            } else {
                alert("There was an error processing the request.");
            }
        });
    }

    document.querySelectorAll(".edit-form").forEach(form => {
        form.addEventListener("submit", handleFormSubmission);
    });

    document.querySelectorAll(".delete-form").forEach(form => {
        form.addEventListener("submit", handleFormSubmission);
    });
});
