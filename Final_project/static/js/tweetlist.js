
// Avatar upload functionality
document.querySelector('.avatar-upload')?.addEventListener('change', function () {
    document.getElementById('avatarForm').submit();
});
    document.addEventListener('DOMContentLoaded', function () {
        const searchInput = document.getElementById('tweetSearch');
        const tweetCards = document.querySelectorAll('.tweet-card');

        searchInput.addEventListener('input', function () {
            const searchTerm = this.value.toLowerCase();

            tweetCards.forEach(card => {
                const text = card.querySelector('.tweet-text')?.textContent.toLowerCase();
                const username = card.querySelector('.tweet-username')?.textContent.toLowerCase();

                if (text.includes(searchTerm) || username.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

        
        // Modal functionality
        function openModal(imageUrl) {
            const modal = document.getElementById("imageModal");
            const modalImg = document.getElementById("expandedImage");
            modal.style.display = "block";
            modalImg.src = imageUrl;
            document.body.style.overflow = "hidden";
        }
        
        function closeModal() {
            document.getElementById("imageModal").style.display = "none";
            document.body.style.overflow = "auto";
        }
        
        // Close modal when clicking outside image
        window.onclick = function(event) {
            const modal = document.getElementById("imageModal");
            if (event.target == modal) {
                closeModal();
            }
        }
        
        // Animation for tweet cards
        document.addEventListener('DOMContentLoaded', function() {
            const tweetCards = document.querySelectorAll('.tweet-card');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = 1;
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, { threshold: 0.1 });
            
            tweetCards.forEach(card => {
                card.style.opacity = 0;
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                observer.observe(card);
            });
        });


