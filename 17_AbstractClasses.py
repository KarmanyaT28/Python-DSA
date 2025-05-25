<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Approval Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef2f7;
            padding: 40px;
        }

        form {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        label {
            font-weight: bold;
            display: block;
            margin-top: 20px;
        }

        input[type="text"] {
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-top: 8px;
        }

        .hidden {
            display: none;
        }

        datalist {
            max-height: 150px;
            overflow-y: auto;
        }

        button {
            margin-top: 30px;
            padding: 12px 25px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<h2 style="text-align: center;">Approval Form</h2>

<form method="POST" action="{% url 'form_dropdown_page' intake_form_id=intake_form_id %}">
    {% csrf_token %}

    <!-- Director -->
    <label>
        <input type="checkbox" id="directorCheckbox"> Director Approval
    </label>
    <div id="directorInputWrapper" class="hidden">
        <input type="text" id="directorInput" name="director_name" list="directorList" placeholder="Type Director Name...">
        <datalist id="directorList">
            {% for name in names %}
                <option value="{{ name }}">
            {% endfor %}
        </datalist>
    </div>

    <!-- DBA -->
    <label>
        <input type="checkbox" id="dbaCheckbox"> DBA Approval
    </label>
    <div id="dbaInputWrapper" class="hidden">
        <input type="text" id="dbaInput" name="dba_person" list="dbaList" placeholder="Type DBA Name...">
        <datalist id="dbaList">
            {% for name in names %}
                <option value="{{ name }}">
            {% endfor %}
        </datalist>
    </div>

    <!-- DUR Number -->
    <label for="dur">DUR Number:</label>
    <input type="text" id="dur" name="dur_number" placeholder="Enter DUR Number">

    <button type="submit">Submit</button>
</form>

<script>
    document.getElementById('directorCheckbox').addEventListener('change', function () {
        const inputWrapper = document.getElementById('directorInputWrapper');
        inputWrapper.classList.toggle('hidden', !this.checked);
    });

    document.getElementById('dbaCheckbox').addEventListener('change', function () {
        const inputWrapper = document.getElementById('dbaInputWrapper');
        inputWrapper.classList.toggle('hidden', !this.checked);
    });
</script>

</body>
</html>
