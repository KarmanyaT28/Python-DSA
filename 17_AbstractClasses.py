<!DOCTYPE html>
<html>
<head>
    <title>Form Dropdown Page</title>
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
</head>
<body>
    <h2>Update Form Status - Intake Form ID: {{ intake_form_id }}</h2>

    <form id="approvalForm" method="POST" action="{% url 'form_dropdown_page' intake_form_id=intake_form_id %}">
        {% csrf_token %}

        <label>Director Approval:</label>
        <input type="checkbox" name="director_approval" value="Yes"> Yes
        <br>

        <label>DBA Approval:</label>
        <input type="checkbox" name="dba_approval" value="Yes"> Yes
        <br>

        <label>Data Governance Approval:</label>
        <input type="checkbox" name="data_gov_approval" value="Yes"> Yes
        <br><br>

        <label>Director Name(s):</label><br>
        <select name="director_name" multiple size="5" required>
            {% for name in names %}
                <option value="{{ name }}">{{ name }}</option>
            {% endfor %}
        </select>
        <br><br>

        <label>DBA Person(s):</label><br>
        <select name="dba_person" multiple size="5" required>
            {% for name in names %}
                <option value="{{ name }}">{{ name }}</option>
            {% endfor %}
        </select>
        <br><br>

        <label>DUR Number:</label>
        <input type="text" name="dur_number" placeholder="Enter DUR Number">
        <br><br>

        <button type="submit">Submit</button>
    </form>

    <div id="result"></div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('approvalForm').addEventListener('submit', async function(e) {
                e.preventDefault();

                const form = e.target;
                const formData = new FormData(form);

                // convert FormData to JSON object
                const data = {};
                formData.forEach((value, key) => {
                    // handle multiple select lists
                    if (data[key]) {
                        if (Array.isArray(data[key])) {
                            data[key].push(value);
                        } else {
                            data[key] = [data[key], value];
                        }
                    } else {
                        data[key] = value;
                    }
                });

                const response = await fetch(form.action, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: JSON.stringify(data)
                });

                const resultDiv = document.getElementById('result');
                if (response.ok) {
                    const json = await response.json();
                    resultDiv.innerHTML = '<p style="color:green;">' + json.message + '</p>';
                    form.reset();
                } else {
                    const errorJson = await response.json();
                    resultDiv.innerHTML = '<p style="color:red;">Error: ' + errorJson.error + '</p>';
                }
            });

            // Utility: debounce function to limit API calls
            function debounce(func, wait) {
                let timeout;
                return function(...args) {
                    clearTimeout(timeout);
                    timeout = setTimeout(() => func.apply(this, args), wait);
                };
            }

            const directorCheckbox = document.querySelector('input[name="director_approval"]');
            if (!directorCheckbox) return;  // stop if checkbox not found

            const directorContainer = document.createElement('div');
            directorContainer.classList.add('input-wrapper');

            const directorInput = document.createElement('input');
            directorInput.type = 'text';
            directorInput.name = 'director_name_autocomplete';  // renamed to avoid clash
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
                    }).catch(() => {
                        suggestionsBox.classList.add('hidden');
                    });
            }

            const debouncedFetch = debounce(fetchNames, 300);

            directorInput.addEventListener('input', e => {
                debouncedFetch(e.target.value);
            });

            directorInput.addEventListener('blur', () => {
                setTimeout(() => suggestionsBox.classList.add('hidden'), 200);
            });

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
        });
    </script>

</body>
</html>
