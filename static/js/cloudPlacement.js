const postContainer = document.getElementById('post-container');
const postContainerSize = postContainer.getBoundingClientRect();
const styles = ["cloud-style-1", "cloud-style-2", "cloud-style-3", "cloud-style-4", "cloud-style-5"];

window.onload = randomCloud();

function randomCloud() {
    document.querySelectorAll('.post-cloud').forEach(div => {
        let divSize = div.getBoundingClientRect();
        div.style.top = randomPx(postContainerSize.height - divSize.height) + 'px';
        div.style.left = randomPx(postContainerSize.width - divSize.width) + 'px';

        // Apply random style
        div.classList.add(styles[Math.floor(Math.random() * styles.length)]);
    });
}

function randomPx(input) {
    return Math.random() * input;
}