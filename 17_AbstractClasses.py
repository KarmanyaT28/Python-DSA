from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required

@login_required
def form_dropdown_page(request, intake_form_id):
    if request.method == 'GET' and 'term' in request.GET:
        term = request.GET.get('term', '')
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                SELECT ee_full_nm
                FROM ppl_pltfrm_emp_data
                WHERE ee_full_nm LIKE %s
                LIMIT 10
                ''',
                [f"%{term}%"]
            )
            names = [row[0] for row in cursor.fetchall()]
        return JsonResponse(names, safe=False)

    elif request.method == 'GET':
        return render(request, 'intake/form_dropdown.html', {'intake_form_id': intake_form_id})

    elif request.method == 'POST':
        user_id = request.user.id
        try:
            dba_approval = request.POST.get('dba_approval', 'No') == 'Yes'
            director_approval = request.POST.get('director_approval', 'No') == 'Yes'
            data_gov_approval = request.POST.get('data_gov_approval', 'No') == 'Yes'

            director_names = request.POST.getlist('director_name')
            dba_persons = request.POST.getlist('dba_person')
            dur_number = request.POST.get('dur_number', '')

            director_names_str = ','.join(director_names)
            dba_persons_str = ','.join(dba_persons)

        except Exception as e:
            return JsonResponse({'error': 'Invalid form data: ' + str(e)}, status=400)

        insert_or_update_approvals_query = '''
            INSERT INTO form_approvals (intake_form_id, dba_approval_check, director_approval_check, data_gov_approval_check,
                                        dba_person, director_name, dur_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            dba_approval_check = VALUES(dba_approval_check),
            director_approval_check = VALUES(director_approval_check),
            data_gov_approval_check = VALUES(data_gov_approval_check),
            dba_person = VALUES(dba_person),
            director_name = VALUES(director_name),
            dur_number = VALUES(dur_number)
        '''
        update_intake_form_status_query = '''
            UPDATE intake_form
            SET status = 'Pending Approval'
            WHERE id = %s AND creator_id = %s
        '''

        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_or_update_approvals_query, [
                    intake_form_id, dba_approval, director_approval, data_gov_approval,
                    dba_persons_str, director_names_str, dur_number
                ])
                cursor.execute(update_intake_form_status_query, [intake_form_id, user_id])
            return JsonResponse({'message': 'Form approvals and status updated successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form Approval</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef2f7;
            padding: 40px;
        }

        form {
            max-width: 700px;
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

        input[type="text"], input[type="checkbox"] {
            margin-top: 8px;
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .hidden {
            display: none;
        }

        .autocomplete-suggestions {
            border: 1px solid #ccc;
            background: white;
            max-height: 150px;
            overflow-y: auto;
            position: absolute;
            z-index: 1000;
            width: calc(100% - 42px);
        }

        .autocomplete-suggestions div {
            padding: 8px;
            cursor: pointer;
        }

        .autocomplete-suggestions div:hover {
            background-color: #f0f0f0;
        }

        .input-wrapper {
            position: relative;
            margin-bottom: 20px;
        }

        button {
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

    <!-- Director Approval -->
    <label><input type="checkbox" id="directorCheck" name="director_approval" value="Yes"> Director Approval</label>
    <div class="input-wrapper hidden" id="directorWrapper">
        <input type="text" id="directorInput" name="director_name" autocomplete="off" placeholder="Type Director Name">
        <div class="autocomplete-suggestions" id="directorSuggestions"></div>
    </div>

    <!-- DBA Approval -->
    <label><input type="checkbox" id="dbaCheck" name="dba_approval" value="Yes"> DBA Approval</label>
    <div class="input-wrapper hidden" id="dbaWrapper">
        <input type="text" id="dbaInput" name="dba_person" autocomplete="off" placeholder="Type DBA Name">
        <div class="autocomplete-suggestions" id="dbaSuggestions"></div>
    </div>

    <!-- DUR -->
    <label for="dur_number">DUR Number:</label>
    <input type="text" id="dur_number" name="dur_number" placeholder="Enter DUR Number">

    <button type="submit">Submit</button>
</form>

<script>
    function handleAutocomplete(inputId, suggestionBoxId) {
        const input = document.getElementById(inputId);
        const suggestions = document.getElementById(suggestionBoxId);

        input.addEventListener('input', function () {
            const term = this.value;
            if (term.length < 1) {
                suggestions.innerHTML = '';
                return;
            }

            fetch(`?term=${encodeURIComponent(term)}`)
                .then(response => response.json())
                .then(data => {
                    suggestions.innerHTML = '';
                    data.forEach(name => {
                        const div = document.createElement('div');
                        div.textContent = name;
                        div.onclick = () => {
                            input.value = name;
                            suggestions.innerHTML = '';
                        };
                        suggestions.appendChild(div);
                    });
                });
        });

        document.addEventListener('click', function (e) {
            if (!input.contains(e.target) && !suggestions.contains(e.target)) {
                suggestions.innerHTML = '';
            }
        });
    }

    document.getElementById('directorCheck').addEventListener('change', function () {
        document.getElementById('directorWrapper').classList.toggle('hidden', !this.checked);
    });

    document.getElementById('dbaCheck').addEventListener('change', function () {
        document.getElementById('dbaWrapper').classList.toggle('hidden', !this.checked);
    });

    handleAutocomplete('directorInput', 'directorSuggestions');
    handleAutocomplete('dbaInput', 'dbaSuggestions');
</script>

</body>
</html>
