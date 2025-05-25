<style>
  /* Simple styling for the autocomplete dropdown */
  .autocomplete-suggestions {
    border: 1px solid #ccc;
    max-height: 150px;
    overflow-y: auto;
    background: white;
    position: absolute;
    z-index: 1000;
    width: 200px;
  }
  .autocomplete-suggestion {
    padding: 8px;
    cursor: pointer;
  }
  .autocomplete-suggestion:hover {
    background-color: #ddd;
  }
  .hidden {
    display: none;
  }
  .input-wrapper {
    position: relative;
    display: inline-block;
  }
</style>




<script>
  // Utility: debounce function to limit API calls
  function debounce(func, wait) {
    let timeout;
    return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  // Show/hide director name input box based on checkbox
  const directorCheckbox = document.querySelector('input[name="director_approval"]');
  const directorContainer = document.createElement('div');
  directorContainer.classList.add('input-wrapper');
  
  const directorInput = document.createElement('input');
  directorInput.type = 'text';
  directorInput.name = 'director_name';
  directorInput.placeholder = 'Type director name';
  directorInput.autocomplete = 'off';

  const suggestionsBox = document.createElement('div');
  suggestionsBox.classList.add('autocomplete-suggestions', 'hidden');

  directorContainer.appendChild(directorInput);
  directorContainer.appendChild(suggestionsBox);

  directorCheckbox.insertAdjacentElement('afterend', directorContainer);

  function fetchNames(term) {
    if (term.length < 2) {
      suggestionsBox.classList.add('hidden');
      return;
    }
    fetch(`?term=${encodeURIComponent(term)}`)
      .then(res => res.json())
      .then(data => {
        suggestionsBox.innerHTML = '';
        if (data.length === 0) {
          suggestionsBox.classList.add('hidden');
          return;
        }
        data.forEach(name => {
          const div = document.createElement('div');
          div.textContent = name;
          div.classList.add('autocomplete-suggestion');
          div.addEventListener('click', () => {
            directorInput.value = name;
            suggestionsBox.classList.add('hidden');
          });
          suggestionsBox.appendChild(div);
        });
        suggestionsBox.classList.remove('hidden');
      });
  }

  const debouncedFetch = debounce(fetchNames, 300);

  directorInput.addEventListener('input', e => {
    debouncedFetch(e.target.value);
  });

  directorInput.addEventListener('blur', () => {
    setTimeout(() => suggestionsBox.classList.add('hidden'), 200); // slight delay to allow click
  });

  // Toggle input box visibility based on checkbox state
  function toggleDirectorInput() {
    if (directorCheckbox.checked) {
      directorContainer.style.display = 'inline-block';
      directorInput.focus();
    } else {
      directorContainer.style.display = 'none';
      directorInput.value = '';
      suggestionsBox.classList.add('hidden');
    }
  }

  toggleDirectorInput();
  directorCheckbox.addEventListener('change', toggleDirectorInput);
</script>
