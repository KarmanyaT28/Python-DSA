<label>Director Name(s):</label>
    <select name="director_name" multiple size="5" required>
        {% for name in names %}
            <option value="{{ name }}">{{ name }}</option>
        {% endfor %}
    </select>

    <label>DBA Person(s):</label>
    <select name="dba_person" multiple size="5" required>
        {% for name in names %}
            <option value="{{ name }}">{{ name }}</option>
        {% endfor %}
    </select>


No , i want these names to appear as suggestions , otherwise hidden , only once i checkbox as yes , and type some name 
