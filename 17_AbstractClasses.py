<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Form with Conditional Autocomplete Inputs</title>
<style>
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
      <input type="text" name="director_name" placeholder="Type director name" autocomplete="off" id="directorInput" />
      <div class="autocomplete-suggestions hidden" id="directorSuggestions"></div>
    </div>

    <label>
      <input type="checkbox" name="dba_approval" value="Yes" id="dbaCheckbox" />
      DBA Approval
    </label>
    <div class="input-wrapper hidden" id="dbaInputWrapper">
      <input type="text" name="dba_person" placeholder="Type DBA person name" autocomplete="off" id="dbaInput" />
      <div class="autocomplete-suggestions hidden" id="dbaSuggestions"></div>
    </div>

    <label>DUR Number:</label>
    <input type="text" name="dur_number" placeholder="Enter DUR Number" />

    <button type="submit">Submit</button>
</form>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // Your backend names list passed to JS
    const names = [
      {% for name in names %}
        "{{ name|escapejs }}",
      {% endfor %}
    ];

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

    // Show/hide input box based on checkbox
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

    // Filter names array for suggestions based on input
    function filterSuggestions(term) {
        if (term.length < 2) return [];
        term = term.toLowerCase();
        return names.filter(name => name.toLowerCase().includes(term));
    }

    // Show suggestions dropdown
    function showSuggestions(suggestions, container, inputField) {
        container.innerHTML = '';
        if (suggestions.length === 0) {
            container.classList.add('hidden');
            return;
        }
        suggestions.forEach(suggestion => {
            const div = document.createElement('div');
            div.textContent = suggestion;
            div.classList.add('autocomplete-suggestion');
            div.addEventListener('click', () => {
                inputField.value = suggestion;
                container.classList.add('hidden');
            });
            container.appendChild(div);
        });
        container.classList.remove('hidden');
    }

    // Event listeners
    directorCheckbox.addEventListener('change', () => {
        toggleInput(directorCheckbox, directorInputWrapper, directorInput, directorSuggestions);
    });

    directorInput.addEventListener('input', () => {
        const filtered = filterSuggestions(directorInput.value);
        showSuggestions(filtered, directorSuggestions, directorInput);
    });

    directorInput.addEventListener('blur', () => {
        setTimeout(() => directorSuggestions.classList.add('hidden'), 200);
    });

    dbaCheckbox.addEventListener('change', () => {
        toggleInput(dbaCheckbox, dbaInputWrapper, dbaInput, dbaSuggestions);
    });

    dbaInput.addEventListener('input', () => {
        const filtered = filterSuggestions(dbaInput.value);
        showSuggestions(filtered, dbaSuggestions, dbaInput);
    });

    dbaInput.addEventListener('blur', () => {
        setTimeout(() => dbaSuggestions.classList.add('hidden'), 200);
    });

    // Initialize inputs visibility on page load if checkbox is checked
    toggleInput(directorCheckbox, directorInputWrapper, directorInput, directorSuggestions);
    toggleInput(dbaCheckbox, dbaInputWrapper, dbaInput, dbaSuggestions);
});
</script>

</body>
</html>
