// Add listing
// If block to ensure no console errors when user is not authenticated
if (document.getElementById("addBtn")) {
    const addBtn = document.getElementById("addBtn");
    const addModal = new bootstrap.Modal(document.getElementById("addModal"));

    addBtn.addEventListener("click", () => {
        addModal.show();
    });
}
