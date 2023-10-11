# questions_web_api
# Setup
<div>
    <ul>
        <li>
            <h4>First, copy the repository</h4>
            <p>Command:</p>
            <pre>git clone https://github.com/ronik-v/questions_web_api.git</pre>
        </li>
        <li>
            <h4>Compiling the project (docker-compose)</h4>
            <p>Command:</p>
            <pre>docker-compose build</pre>
        </li>
        <li>
            <h4>Create database and use script for create Question model</h4>
            <p>Database:</p>
            <pre>CREATE DATABASE question_quiz;</pre>
            <p>Run file: .\questions_web_api\data\database.py</p>
        </li>
        <li>
            <h4>Launch of the project</h4>
            <p>Command:</p>
            <pre>docker-compose up</pre>
        </li>
        <li>
            <h4>Used libraries</h4>
            <a href="requirements.txt">File with libraries versions</a>
        </li>
    </ul>
</div>

# Use example
<div>
    <h4>Submitting question records to the database</h4>
    <pre>from requests import post<br>url = 'http://localhost:9000/questions_api<br>_json = {'questions_num': 100}<br>result = post(url, json=_json)<br>print(result.json())</pre>
    <p>This post request returns the last question added to the database, <b>filtering out duplicates</b> and at the same time saving as many queries as were specified in the post request in the <b>'questions_num'</b> parameter</p>
</div>

# License
<div>
    <p>Apache License 2.0, details  <a href="LICENSE">here</a></p>
</div>
