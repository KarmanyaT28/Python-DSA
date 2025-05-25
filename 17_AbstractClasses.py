from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
import json

@login_required
def form_dropdown_page(request, intake_form_id):
    if request.method == 'GET':
        # Fetch top 10 names from DB for dropdowns
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                SELECT ee_full_nm
                FROM ppl_pltfrm_emp_data
                LIMIT 10
                '''
            )
            names = [row[0] for row in cursor.fetchall()]

        context = {
            'intake_form_id': intake_form_id,
            'names': names,
        }
        return render(request, 'form_dropdown.html', context)

    elif request.method == 'POST':
        user_id = request.user.id
        try:
            dba_approval = request.POST.get('dba_approval', 'No') == 'Yes'
            director_approval = request.POST.get('director_approval', 'No') == 'Yes'
            data_gov_approval = request.POST.get('data_gov_approval', 'No') == 'Yes'

            director_names = request.POST.getlist('director_name')  # list of selected director names
            dba_persons = request.POST.getlist('dba_person')        # list of selected dba persons
            dur_number = request.POST.get('dur_number', '')

            # Convert list to comma separated string to save in DB
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

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




<!DOCTYPE html>
<html>
<head>
    <title>Form Dropdown Page</title>
</head>
<body>
    <h2>Update Form Status - Intake Form ID: {{ intake_form_id }}</h2>

    <form id="approvalForm" method="POST" action="{% url 'form_dropdown' intake_form_id=intake_form_id %}">
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
    </script>

</body>
</html>





from django.urls import path
from . import views

urlpatterns = [
    # other paths...
    path('form_dropdown/<int:intake_form_id>/', views.form_dropdown_page, name='form_dropdown'),
]


