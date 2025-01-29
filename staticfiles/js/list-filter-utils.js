// If block to ensure no console errors when user is not authenticated
if (document.getElementById("yourCoffees")) {
    const yourCoffees = document.getElementById("yourCoffees");

    if (window.location.href.endsWith("mylistings/" || "mylistings")) {
        yourCoffees.checked = true;
    }
    else {
        yourCoffees.checked = false;
    }
}