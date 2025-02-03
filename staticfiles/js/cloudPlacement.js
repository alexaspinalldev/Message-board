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
        let randomNum = Math.floor(Math.random() * styles.length);
        let randomStyle = styles[randomNum];
        div.classList.add(randomStyle);

        // Apply the same style to the like button within the post-cloud
        const likeButton = div.querySelector('.like');
        if (likeButton) {
            likeButton.classList.add(`like-style-${randomNum + 1}`);
        }
    });
}

function randomPx(input) {
    return Math.random() * input;
}