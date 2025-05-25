<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Form Dropdown Page</title>
<style>
  /* Reset some basic styles */
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f5f8fa;
    margin: 0; padding: 20px;
    color: #333;
  }
  h2 {
    color: #2c3e50;
    margin-bottom: 25px;
  }
  form {
    background: #fff;
    padding: 25px 30px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgb(0 0 0 / 0.1);
    max-width: 480px;
  }
  label {
    font-weight: 600;
    display: block;
    margin-bottom: 8px;
    margin-top: 20px;
  }
  input[type="checkbox"] {
    margin-right: 8px;
    transform: scale(1.2);
    vertical-align: middle;
  }
  select[multiple] {
    width: 100%;
    height: 120px;
    padding: 8px;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 14px;
    background-color: #fafafa;
    box-sizing: border-box;
  }
  input[type="text"] {
    width: 100%;
    padding: 10px 12px;
    font-size: 14px;
    border: 1.5px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
    transition: border-color 0.3s;
  }
  input[type="text"]:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 6px #a5d1ff;
  }
  button {
    margin-top: 30px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: 700;
    background-color: #007bff;
    border: none;
    border-radius: 8px;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  button:hover {
    background-color: #0056b3;
  }
  #result {
    margin-top: 20px;
    font-weight: 600;
  }
  /* Autocomplete container */
  .input-wrapper {
    position: relative;
    margin-top: 10px;
  }
  .autocomplete-suggestions {
    border: 1px solid #ccc;
    max-height: 140px;
    overflow-y: auto;
    background: white;
    position: absolute;
    z-index: 1000;
    width: 100%;
    border-radius: 0 0 6px 6px;
    box-shadow: 0 4px 6px rgb(0 0 0 / 0.1);
  }
  .autocomplete-suggestion {
    padding: 10px 12px;
    cursor: pointer;
    font-size: 14px;
  }
  .autocomplete-suggestion:hover {
    background-color: #f0f8ff;
  }
  .hidden {
    display: none;
  }
</style>
</head>
<body>

<h2>Update Form Status - Intake Form ID: {{ intake_form_id }}</h2>

<form id="approvalForm" method="POST" action="{% url 'form_dropdown_page' intake_form_id=intake_form_id %}">
    {% csrf_token %}

    <label>
      <input type="checkbox" name="director_approval" value="Yes" id="directorCheckbox" />
      Director Approval
    </label>
    <div class="input-wrapper hidden" id="directorInputWrapper">
      <input type="text" name="director_name_autocomplete" placeholder="Type director name" autocomplete="off" id="directorInput" />
      <div class="autocomplete-suggestions hidden" id="directorSuggestions"></div>
    </div>

    <label>
      <input type="checkbox" name="dba_approval" value="Yes" id="dbaCheckbox" />
      DBA Approval
    </label>
    <div class="input-wrapper hidden" id="dbaInputWrapper">
      <input type="text" name="dba_person_autocomplete" placeholder="Type DBA person name" autocomplete="off" id="dbaInput" />
      <div class="autocomplete-suggestions hidden" id="dbaSuggestions"></div>
    </div>

    <label>Director Name(s):</label>
    <select name="director_name" multiple size="5" required>
        {% for name in names %}
            <option value="{{ name }}">{{ name }}</option>
        {% endfor %}
    </select>

    <label>DBA Person(s):</label>
    <select name="dba_person" multiple size="5" required>
        {% for name in names %}
            <option value="{{ name }}">{{ name }}</option>
        {% endfor %}
    </select>

    <label>DUR Number:</label>
    <input type="text" name="dur_number" placeholder="Enter DUR Number" />

    <button type="submit">Submit</button>
</form>

<div id="result"></div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // Elements for Director
    const directorCheckbox = document.getElementById('directorCheckbox');
    const directorInputWrapper = document.getElementById('directorInputWrapper');
    const directorInput = document.getElementById('directorInput');
    const directorSuggestions = document.getElementById('directorSuggestions');

    // Elements for DBA
    const dbaCheckbox = document.getElementById('dbaCheckbox');
    const dbaInputWrapper = document.getElementById('dbaInputWrapper');
    const dbaInput = document.getElementById('dbaInput');
    const dbaSuggestions = document.getElementById('dbaSuggestions');

    // Utility debounce
    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // Show/hide input box based on checkbox state
    function toggleInput(checkbox, wrapper, input, suggestions) {
        if (checkbox.checked) {
            wrapper.classList.remove('hidden');
            input.focus();
        } else {
            wrapper.classList.add('hidden');
            input.value = '';
            suggestions.classList.add('hidden');
            suggestions.innerHTML = '';
        }
    }

    // Fetch suggestions from backend (?term=...)
    function fetchSuggestions(term, suggestionsBox, inputField) {
        if (term.length < 2) {
            suggestionsBox.classList.add('hidden');
            suggestionsBox.innerHTML = '';
            return;
        }
        fetch(`?term=${encodeURIComponent(term)}`)
            .then(res => res.json())
            .then(data => {
                suggestionsBox.innerHTML = '';
                if (!data.length) {
                    suggestionsBox.classList.add('hidden');
                    return;
                }
                data.forEach(name => {
                    const div = document.createElement('div');
                    div.textContent = name;
                    div.classList.add('autocomplete-suggestion');
                    div.addEventListener('click', () => {
                        inputField.value = name;
                        suggestionsBox.classList.add('hidden');
                    });
                    suggestionsBox.appendChild(div);
                });
                suggestionsBox.classList.remove('hidden');
            })
            .catch(() => {
                suggestionsBox.classList.add('hidden');
                suggestionsBox.innerHTML = '';
            });
    }

    const debouncedDirectorFetch = debounce(term => fetchSuggestions(term, directorSuggestions, directorInput), 300);
    const debouncedDbaFetch = debounce(term => fetchSuggestions(term, dbaSuggestions, dbaInput), 300);

    // Event listeners
    directorCheckbox.addEventListener('change', () => {
        toggleInput(directorCheckbox, directorInputWrapper, directorInput, directorSuggestions);
    });

    directorInput.addEventListener('input', e => {
        debouncedDirectorFetch(e.target.value);
    });

    directorInput.addEventListener('blur', () => {
        setTimeout(() => directorSuggestions.classList.add('hidden'), 200);
    });

    dbaCheckbox.addEventListener('change', () => {
        toggleInput(dbaCheckbox, dbaInputWrapper, dbaInput, dbaSuggestions);
    });

    dbaInput.addEventListener('input', e => {
        debouncedDbaFetch(e.target.value);
    });

    dbaInput.addEventListener('blur', () => {
        setTimeout(() => dbaSuggestions.classList.add('hidden'), 200);
    });

    // Initialize input visibility based on checkbox (in case of reload)
    toggleInput(directorCheckbox, directorInputWrapper, directorInput, directorSuggestions);
    toggleInput(dbaCheckbox, dbaInputWrapper, dbaInput, dbaSuggestions);

    // Handle form submission with fetch API and JSON payload
    document.getElementById('approvalForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        const form = e.target;

        const formData = new FormData(form);
        // Add input autocomplete values only if checkboxes checked
        if (directorCheckbox.checked) {
            formData.set('director_name', directorInput.value.trim());
        }
        if (dbaCheckbox.checked) {
            formData.set('dba_person', dbaInput.value.trim());
        }

        const payload = Object.fromEntries(formData.entries());

        // Send POST request
        const response = await fetch(form.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        const result = await response.json();

        document.getElementById('result').textContent = result.message || 'Form submitted!';
    });
});
</script>

</body>
</html>
