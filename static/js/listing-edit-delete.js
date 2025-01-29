// Delete listing
// If blocks to ensure no console errors when user is not authenticated
if (document.getElementById("deleteBtn")) {
    const deleteBtn = document.getElementById("deleteBtn");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");

    deleteBtn.addEventListener("click", () => {
        deleteModal.show();
    });

    deleteConfirm.addEventListener("click", () => {
        deleteConfirm.href = "delete";
    });
}

// Edit listing
if (document.getElementById("editBtn")) {
    const editBtn = document.getElementById("editBtn");

    const editModal = new bootstrap.Modal(document.getElementById("editModal"));
    editBtn.addEventListener("click", () => {
        editModal.show();
    });
}
