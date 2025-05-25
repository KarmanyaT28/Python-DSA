$(document).ready(function () {
    function attachAutocomplete(inputSelector) {
        $(inputSelector).autocomplete({
            source: function (request, response) {
                $.ajax({
                    url: "/update_form_status/" + $("#intakeFormId").val(),  // dynamically includes intake_form_id
                    dataType: "json",
                    data: {
                        term: request.term
                    },
                    success: function (data) {
                        response(data); // Data should be a list of strings
                    },
                    error: function (xhr, status, error) {
                        console.error("Autocomplete error:", error);
                    }
                });
            },
            minLength: 2
        });
    }

    // Attach to multiple fields if needed
    attachAutocomplete("#id_director_name");
    attachAutocomplete("#id_dba_person");
});


<input type="hidden" id="intakeFormId" value="{{ intake_form_id }}">
<input type="text" id="id_director_name" name="director_name" />
<input type="text" id="id_dba_person" name="dba_person" />
