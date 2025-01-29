const loaders = document.querySelectorAll('[data-load]');
const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));

loaders.forEach(loader => {
    loader.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey) {
            return;
        }

        loadingModal.show();
    });
});