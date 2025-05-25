from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import connection
import json

@login_required
def update_form_status(request, intake_form_id):
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

    elif request.method == 'POST':
        user_id = request.user.id
        try:
            data = json.loads(request.body)
            # Just parsing these for now; not inserting into form_approvals
            dba_approval = data.get('dba_approval', 'No') == 'Yes'
            director_approval = data.get('director_approval', 'No') == 'Yes'
            data_gov_approval = data.get('data_gov_approval', 'No') == 'Yes'
            dur_number = data.get('dur_number', '')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid data format'}, status=400)

        update_intake_form_status_query = '''
            UPDATE intake_form
            SET status = 'Pending Approval'
            WHERE id = %s AND creator_id = %s
        '''

        try:
            with connection.cursor() as cursor:
                cursor.execute(update_intake_form_status_query, [intake_form_id, user_id])
            return JsonResponse({'message': 'Form status updated successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
