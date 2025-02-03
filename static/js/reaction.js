document.querySelectorAll('.like').forEach(item => { 
    item.addEventListener('click', () => {
        const postId = item.getAttribute('data-post-id');
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(`/add_like/${postId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({})
        })
        .then(response => response.json())
        .then(data => {
            if (data.liked) {
                item.classList.add('liked');
            } else {
                item.classList.remove('liked');
            }
            item.querySelector('.like-count').textContent = data.like_count;
        })
        .catch(error => console.error('Error:', error));
    });
});