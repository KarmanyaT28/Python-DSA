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
        return render(request, 'intake/form_dropdown.html', context)

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
