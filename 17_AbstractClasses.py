[26/May/2025 01:58:55] "GET /roleintake/form/view/ HTTP/1.1" 200 52169
[26/May/2025 01:59:12,758] - Broken pipe from ('127.0.0.1', 52754)
[26/May/2025 01:59:13] "GET /roleintake/form/view/?term=SHARON HTTP/1.1" 200 52169
[26/May/2025 01:59:19,888] - Broken pipe from ('127.0.0.1', 52769)
[26/May/2025 01:59:20] "GET /roleintake/form/view/?term=SHAR HTTP/1.1" 200 52169
Not Found: /.well-known/appspecific/com.chrome.devtools.json
[26/May/2025 02:02:17] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 2723        
Not Found: /.well-known/appspecific/com.chrome.devtools.json
[26/May/2025 02:03:01] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 2723        
[26/May/2025 02:08:50] "GET /roleintake/form/view/?term=SHARON HTTP/1.1" 200 52169





    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Include jQuery and Select2 CSS/JS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/css/select2.min.css" />
    <!-- <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0/dist/css/select2.min.css" rel="stylesheet" /> -->
    <script src="https://cdn.jsdelivr.net/npm/select2@4.1.0/dist/js/select2.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js"></script>
          
    <title>MY Forms</title>
</head>
<body>
<div class="container">
<a class="dashboard-link" href="{% url 'dashboard' %}">Dashboard</a>
<h1>MY FORMS</h1>
   {% if forms %}
<table>
<thead>
<tr>
<th>Form ID</th>
<th>Form Data</th>
<th>Created At</th>
<th>Status</th>
<th>Actions</th>
</tr>
</thead>
<tbody>
           {% for form in forms %}
<tr>
<td><a href="{% url 'preview_form' form.0 %}">{{ form.0 }}</a></td>
<td><a href="{% url 'preview_form' form.0 %}">{{ form.1 }}</a></td>
<td><a href="{% url 'preview_form' form.0 %}">{{ form.2 }}</a></td>
<td>
    {% if form.3 == 'Submitted' %}
<span class="status-submitted">{{ form.3 }}</span>
    {% elif form.3 == 'In Progress' %}
<span class="status-progress">{{ form.3 }}</span>
    {% elif form.3 == 'Pending Approval' %}
<span class="status-pending">{{ form.3 }}</span>
    {% elif form.3 == 'Approved' %}
<span class="status-approved">{{ form.3 }}</span>
    {% elif form.3 == 'Mail Sent' %}
<span class="status-mail">{{ form.3 }}</span>
    {% endif %}
</td>
<td class="form-actions">
                   {% if form.3 == 'In Progress' %}
<form action="{% url 'submit_form' form.0 %}" method="post">
                           {% csrf_token %}
<button type="submit">Submit</button>
</form>
                   {% elif form.3 == 'Submitted' %}
<!-- Button to move to Pending Approval -->
<button onclick="showDropdownPrompt('{{ form.0 }}')">Pending Approval</button>
<br>
<!-- Button to move back to In Progress -->
<form action="{% url 'in_progress_form' form.0 %}" method="post">
                           {% csrf_token %}
<button type="submit">Revert to In Progress</button>
</form>
                   {% elif form.3 == 'Pending Approval' %}
<!-- Button to re-submit the form -->
<form action="{% url 'submit_form' form.0 %}" method="post">
                           {% csrf_token %}
<button type="submit">Submit</button>
</form>
<!-- Button to add Approval Links -->
<button onclick="showApprovalPrompt('{{ form.0 }}')">Approval Links</button>
                   {% elif form.3 == 'Approved' %}
<form action="{% url 'update_form_status_mail' form.0 %}" method="post">
                           {% csrf_token %}
<button type="submit">Mark as Completed</button>
</form>
                   {% endif %}
</td>
</tr>
           {% endfor %}
</tbody>
</table>
   {% else %}
<p class="no-forms">You have not created any forms.</p>
   {% endif %}
</div>
<!-- Modal for Pending Approval (dropdown options) -->
<div class="dropdown-prompt" id="dropdownPrompt" style="display:none;">
<!-- <form > -->
    <form id="dropdownForm" method="post" action="">
        {% csrf_token %}
       
        <!-- Director Approval -->
        <label for="director_approval">Director Approval:</label>
        <select id="director_approval" name="director_approval">
          <option value="No">No</option>
          <option value="Yes">Yes</option>
        </select>
       
        <div class="form-group" id="director_name_container" style="display:none;">
          <label for="director_name">Select Director Name(s):</label>
          <select id="director_name"
                  name="director_name[]"
                  multiple="multiple"
                  class="form-control"
                  style="width: 100%; min-height: 38px;">
            <!-- Select2 will inject its own search box here -->
          </select>
        </div><br>
       
        <!-- DBA Approval -->
        <label for="dba_approval">DBA Approval:</label>
        <select id="dba_approval" name="dba_approval">
          <option value="No">No</option>
          <option value="Yes">Yes</option>
        </select>
       
        <div class="form-group" id="dba_person_container" style="display:none;">
          <label for="dba_person">Select DBA Person(s):</label>
          <select id="dba_person"
                  name="dba_person[]"
                  multiple="multiple"
                  class="form-control"
                  style="width: 100%; min-height: 38px;">
          </select>
        </div><br>
       
        <!-- <button type="submit">Submit</button> -->

<!-- Data Governance Approval -->
<label for="data_gov_approval">Data Governance Approval:</label>
<select id="data_gov_approval" name="data_gov_approval">
    <option value="No">No</option>
    <option value="Yes">Yes</option>
</select><br>

<input type="text" id="dur_number" name="dur_number" placeholder="Enter DUR Number" style="display:none;"/>

<br>
<button type="button" onclick="submitDropdownPrompt()">Submit</button>
<button type="button" onclick="hideDropdownPrompt()">Cancel</button>
</form>
</div>


<div class="approval-prompt" id="approvalPrompt" style="display: none;">
    <form id="approvalForm">
        <h3>Enter Approval Links</h3>
        <label for="dba_approval">DBA Approval:</label>
        <input type="text" name="dba_approval" id="dba_approval_link" placeholder="Enter DBA Approval Link">
        
        <label for="director_approval">Director Approval:</label>
        <input type="text" name="director_approval" id="director_approval_link" placeholder="Enter Director Approval Link">
        
        <label for="data_gov_approval">Data Governance Approval:</label>
        <input type="text" name="data_gov_approval" id="data_gov_approval_link" placeholder="Enter Data Governance Approval Link">
        
        <button type="button" onclick="submitApprovalPrompt()">Submit</button>
        <button type="button" onclick="hideApprovalPrompt()">Cancel</button>
    </form>
</div>
<script>
  $(document).ready(function() {

// Show/hide director_name multi-select on approval change
$('#director_approval').change(function() {
  if ($(this).val() === 'Yes') {
    $('#director_name_container').show();
  } else {
    $('#director_name_container').hide();
    $('#director_name').val(null).trigger('change');
  }
});

// Show/hide dba_person multi-select on approval change
$('#dba_approval').change(function() {
  if ($(this).val() === 'Yes') {
    $('#dba_person_container').show();
  } else {
    $('#dba_person_container').hide();
    $('#dba_person').val(null).trigger('change');
  }
});

// Initialize Select2 with AJAX for director_name
$('#director_name').select2({
  placeholder: "Search for director(s)...",
  ajax: {
    url: window.location.href,
    dataType: "json",
    delay: 250,
    data: function(params) {
      return { term: params.term };
    },
    processResults: function(data) {
      return {
        results: data.map(function(item) {
          return { id: item, text: item };
        })
      };
    },
    cache: true,
  },
  minimumInputLength: 1,
});

// Initialize Select2 with AJAX for dba_person
$('#dba_person').select2({
  placeholder: "Search for DBA person(s)...",
  ajax: {
    url: window.location.href,
    dataType: "json",
    delay: 250,
    data: function(params) {
      return { term: params.term };
    },
    processResults: function(data) {
      return {
        results: data.map(function(item) {
          return { id: item, text: item };
        })
      };
    },
    cache: true,
  },
  minimumInputLength: 1,
});

});
    </script>
    <!-- <script>
        const intakeFormId = "{{ intake_form_id }}"
    </script> -->
    <!-- <script>
        $(document).ready(function() {
          // Show/hide director_name on approval change
          $('#director_approval').change(function() {
            if (this.value === 'Yes') {
              $('#director_name_container').show();
            } else {
              $('#director_name_container').hide();
              $('#director_name').val(null).trigger('change');
            }
          });
         
          // Show/hide dba_person on approval change
          $('#dba_approval').change(function() {
            if (this.value === 'Yes') {
              $('#dba_person_container').show();
            } else {
              $('#dba_person_container').hide();
              $('#dba_person').val(null).trigger('change');
            }
          });

            $('#dba_person').select2({
            placeholder: "Search for DBA Person...",
            ajax: {
                url: window.location.href, // Use the current URL
                dataType: "json",
                delay: 250,
                data: function (params) {
                    return {
                        term: params.term, // Search term
                    };
                },
                processResults: function (data) {
                    return {
                        results: data.map(function (item) {
                            return { id: item, text: item }; // Map response to id/text format
                        }),
                    };
                },
                cache: true,
            },
            minimumInputLength: 1,
            });


            $('#director_name').select2({
            placeholder: "Search for Directors...",
            ajax: {
                url: window.location.href, // Use the current URL
                dataType: "json",
                delay: 250,
                data: function (params) {
                    return {
                        term: params.term, // Search term
                    };
                },
                processResults: function (data) {
                    return {
                        results: data.map(function (item) {
                            return { id: item, text: item }; // Map response to id/text format
                        }),
                    };
                },
                cache: true,
            },
            minimumInputLength: 1,
            });
         
         
        });
        </script> -->


<script>
    async function showApprovalPrompt(formId) {
        try {
            const response = await fetch(`/roleintake/form/form/${formId}/update_form_status_approved/`);
            const result = await response.json();
            if (response.ok) {
                const dbaApprovalInput = document.getElementById("dba_approval_link");
                const directorApprovalInput = document.getElementById("director_approval_link");
                const dataGovApprovalInput = document.getElementById("data_gov_approval_link");
    
                // Debugging the approval data and conditions
                console.log('Approval Check Data:', result);
                console.log(dbaApprovalInput);
                console.log(directorApprovalInput);
                console.log(dataGovApprovalInput);
    
                
                if (result.dba_approval_check === "No") {
                    console.log('Making DBA Approval Input Read-Only');
                    dbaApprovalInput.setAttribute('readonly', 'true');
                } else {
                    dbaApprovalInput.removeAttribute('readonly');
                }
    
                if (result.director_approval_check === "No") {
                    console.log('Making Director Approval Input Read-Only');
                    directorApprovalInput.setAttribute('readonly', 'true');
                } else {
                    directorApprovalInput.removeAttribute('readonly');
                }
    
                if (result.data_gov_approval_check === "No") {
                    console.log('Making Data Governance Approval Input Read-Only');
                    dataGovApprovalInput.setAttribute('readonly', 'true');
                } else {
                    dataGovApprovalInput.removeAttribute('readonly');
                }
    
                // Store the form ID for submission
                document.getElementById("approvalForm").dataset.formId = formId;
    
                // Show the approval prompt
                document.getElementById("approvalPrompt").style.display = "block";
            } else {
                alert(result.error || "Failed to fetch approval check data.");
            }
        } catch (error) {
            console.error("Error fetching approval checks:", error);
            alert("An unexpected error occurred. Please try again.");
        }
    }
    
        function hideApprovalPrompt() {
            // Hide the approval modal
            document.getElementById("approvalPrompt").style.display = "none";
        }
    
        async function submitApprovalPrompt() {
            const form = document.getElementById("approvalForm");
            const formId = form.dataset.formId; // Get the form ID
            const dbaApproval = form.querySelector("input[name='dba_approval']").value.trim();
            const directorApproval = form.querySelector("input[name='director_approval']").value.trim();
            const dataGovApproval = form.querySelector("input[name='data_gov_approval']").value.trim();
    
            // Check if at least one approval field is filled
            if (!dbaApproval && !directorApproval && !dataGovApproval) {
                alert("Please fill at least one approval field.");
                return;
            }
    
            try {
                // Send the approval data to the server
                const response = await fetch(`/roleintake/form/form/${formId}/update_form_status_approved/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": "{{ csrf_token }}",
                    },
                    body: JSON.stringify({
                        dba_approval: dbaApproval,
                        director_approval: directorApproval,
                        data_gov_approval: dataGovApproval,
                    }),
                });
                const result = await response.json();
                if (response.ok) {
                    alert(result.message); // Show success message
                    window.location.reload(); // Refresh the page to update the status
                } else {
                    alert(result.error || "Failed to approve the form.");
                }
            } catch (error) {
                console.error("Error submitting approvals:", error);
                alert("An unexpected error occurred. Please try again.");
            } finally {
                hideApprovalPrompt(); // Hide the modal regardless of success or failure
            }
        }
        
            function showDropdownPrompt(formId) {
                // Store the form ID for submission
                document.getElementById('dropdownForm').dataset.formId = formId;
                // Show the dropdown modal
                document.getElementById('dropdownPrompt').style.display = 'block';
            }
        
            function hideDropdownPrompt() {
                // Hide the dropdown modal
                document.getElementById('dropdownPrompt').style.display = 'none';
            }
        
            async function submitDropdownPrompt() {
                // Get the form data
                const form = document.getElementById('dropdownForm');
                const formId = form.dataset.formId; // Get the form ID
                const dbaApproval = document.getElementById('dba_approval').value;
                const directorApproval = document.getElementById('director_approval').value;
                const dataGovApproval = document.getElementById('data_gov_approval').value;
        
                // Ensure that all approval fields are filled
                if (!dbaApproval || !directorApproval || !dataGovApproval) {
                    alert("Please select a value for all approval fields.");
                    return;
                }
        
                try {
                    // Send the dropdown data to the server
                    const response = await fetch(`/roleintake/form/form/${formId}/update_form_status/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': '{{ csrf_token }}',
                        },
                        body: JSON.stringify({
                            dba_approval: dbaApproval,
                            director_approval: directorApproval,
                            data_gov_approval: dataGovApproval,
                        }),
                    });
                    const result = await response.json();
                    if (response.ok) {
                        alert(result.message); // Show success message
                        window.location.reload(); // Refresh the page to update the status
                    } else {
                        alert(result.error || "Failed to update form status.");
                    }
                } catch (error) {
                    console.error("Error submitting dropdown values:", error);
                    alert("An unexpected error occurred. Please try again.");
                } finally {
                    hideDropdownPrompt(); // Hide the modal regardless of success or failure
                }
            }
        </script>

</body>
</html>







@login_required
def update_form_status(request, intake_form_id):
    if request.method == 'GET' and 'term' in request.GET:
        term = request.GET.get('term','')
        # print(f"[DEBUG] AJAX term received: {term}")
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
        # print({'intake_form_id': intake_form_id, 'results': names})
        # return JsonResponse({'intake_form_id': intake_form_id, 'results': names})


    elif request.method == 'POST':
        user_id = request.user.id
        try:
            data = json.loads(request.body)
            dba_approval = data.get('dba_approval', 'No') == 'Yes'
            director_approval = data.get('director_approval', 'No') == 'Yes'
            data_gov_approval = data.get('data_gov_approval', 'No') == 'Yes'

            director_names = data.get('director_name', [])
            dba_persons = data.get('dba_person', [])
            dur_number = data.get('dur_number', '')

        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid data format'}, status=400)

      
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
