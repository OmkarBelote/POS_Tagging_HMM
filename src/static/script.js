document.addEventListener('DOMContentLoaded', function() {
    const tagButton = document.getElementById('tag-button');
    const resultSection = document.getElementById('result');
    const taggedContent = document.getElementById('tagged-content');
    
    // If you want to use AJAX instead of form submission
    tagButton.addEventListener('click', function(e) {
        // Prevent the default form submission
        e.preventDefault();
        
        const inputText = document.getElementById('sentence-input').value;
        
        if (inputText.trim() === '') {
            alert('Please enter a sentence to tag.');
            return;
        }
        
        // Make an API call to the backend
        fetch('/api/tag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sentence: inputText })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Show the result section
            resultSection.classList.add('active');
            
            // Clear previous results
            taggedContent.innerHTML = '';
            
            // Display the tagged words
            data.forEach(item => {
                const taggedWord = document.createElement('div');
                taggedWord.className = 'tagged-word';
                
                const wordSpan = document.createElement('span');
                wordSpan.className = 'word';
                wordSpan.textContent = item.word;
                
                const tagSpan = document.createElement('span');
                tagSpan.className = 'tag';
                tagSpan.textContent = item.tag;
                
                taggedWord.appendChild(wordSpan);
                taggedWord.appendChild(tagSpan);
                taggedContent.appendChild(taggedWord);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while tagging the sentence.');
        });
    });
});
