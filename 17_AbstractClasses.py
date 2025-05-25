    <style>
           body {
               font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
               background-color: #062241;
               margin: 0;
               padding: 20px;
           }
           .container {
               max-width: 1000px;
               margin: 0 auto;
               background-color: white;
               padding: 30px;
               border-radius: 15px;
               box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
           }
           h1 {
               text-align: center;
               color: #007bff;
               margin-bottom: 30px;
               font-size: 2rem;
           }
           table {
               width: 100%;
               border-collapse: collapse;
               margin-top: 20px;
           }
           th,
           td {
               padding: 15px;
               text-align: center;
               border: 1px solid #ddd;
           }
           th {
               background-color: #007bff;
               color: white;
               font-weight: bold;
           }
           td {
               background-color: #f8f9fa;
           }
           .form-actions {
               display: flex;
               justify-content: center;
               gap: 10px;
               margin-top: 10px;
           }
           .form-actions form {
               display: inline-block;
           }
           button {
               /* padding: 10px 5px; */
               height: 30px;
               background-color: #28a745;
               color: white;
               border: none;
               border-radius: 5px;
               cursor: pointer;
               font-size: 0.9rem;
               transition: background-color 0.3s;
           }
           button:hover {
               background-color: #218838;
           }
           a {
               text-decoration: none;
               color: #007bff;
               font-weight: bold;
           }
           a:hover {
               text-decoration: underline;
           }
           .status-submitted {
               background-color: #ffc107;
               color: #212529;
               border-radius: 5px;
               padding: 5px 10px;
           }
           .status-progress {
               background-color: #17a2b8;
               color: white;
               border-radius: 5px;
               padding: 5px 10px;
           }
           .status-approved {
               background-color: #28a745;
               color: white;
               border-radius: 5px;
               padding: 5px 10px;
           }
           .status-pending {
               background-color: #fd7e14;
               color: white;
               border-radius: 5px;
               padding: 5px 10px;
           }
           .status-mail {
               background-color: #007bff;
               color: white;
               border-radius: 5px;
               padding: 5px 10px;
           }
           .no-forms {
               text-align: center;
               font-size: 1.1rem;
               color: #555;
               margin-top: 20px;
           }
           .dashboard-link {
               display: inline-block;
               padding: 10px 15px;
               background-color: #007bff;
               color: white;
               border-radius: 5px;
               text-align: center;
               margin-bottom: 20px;
               font-size: 1rem;
           }
           .dashboard-link:hover {
               background-color: #0056b3;
           }
           .dropdown-prompt{
               display: none;
               position: fixed;
               top: 50%;
               left: 50%;
               transform: translate(-50%, -50%);
               background-color: white;
               padding: 20px;
               box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
               border-radius: 10px;
               /* z-index: 1000; */
               overflow: visible;
               z-index: 1050; 
    
           }
           .approval-prompt {
               display: none;
               position: fixed;
               top: 50%;
               left: 50%;
               transform: translate(-50%, -50%);
               background-color: white;
               padding: 20px;
               box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
               border-radius: 10px;
               z-index: 1000;
           }
           .dropdown-prompt input {
               margin-bottom: 10px;
               padding: 8px;
               width: 100%;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           .approval-prompt input {
               margin-bottom: 10px;
               padding: 8px;
               width: 100%;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           .dropdown-prompt button {
               width: 48%;
               padding: 10px;
               margin-top: 10px;
               border: none;
               border-radius: 5px;
               cursor: pointer;
               font-size: 0.9rem;
           }
           .approval-prompt button {
               width: 48%;
               padding: 10px;
               margin-top: 10px;
               border: none;
               border-radius: 5px;
               cursor: pointer;
               font-size: 0.9rem;
           }
           .btn-approve {
               background-color: #28a745;
               color: white;
           }
           .btn-cancel {
               background-color: #dc3545;
               color: white;
           }

    .suggestions-list {
       list-style: none;
       margin: 0;
       padding: 5px;
       border: 1px solid #ccc;
       max-height: 150px;
       overflow-y: auto;
       display: none;
       position: absolute;
       background: #fff;
       z-index: 1000;
       width: 200px;
    }
    .suggestions-list li {
       padding: 4px;
       cursor: pointer;
    }
    .suggestions-list li:hover {
       background-color: #eee;
    }
            /* Force the text color in the Select2 dropdown to black */
        
        .select2-container {
            z-index: 9999 !important;  /* ensures dropdown is above modals, prompts */
        }
        
        .select2-dropdown {
            min-height: 100px !important;  /* ensures dropdown has some visible height */
            overflow-y: auto !important;
            background-color: white;
            border: 1px solid red;
        }
        
        .select2-results__options {
            max-height: 300px;
            overflow-y: auto;
        }


    </style>



[26/May/2025 03:09:08] "GET /roleintake/form/view/ HTTP/1.1" 200 52169
[26/May/2025 03:09:25,000] - Broken pipe from ('127.0.0.1', 54943)
[26/May/2025 03:09:26,125] - Broken pipe from ('127.0.0.1', 54956)
[26/May/2025 03:09:26] "GET /roleintake/form/view/?term=SHARON HTTP/1.1" 200 52169
