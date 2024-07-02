document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/students')
        .then(response => response.json())
        .then(data => {
            const studentsDiv = document.getElementById('students');
            if (data.error) {
                studentsDiv.textContent = 'Error fetching students: ' + data.error;
                return;
            }

            data.forEach(student => {
                const studentCard = document.createElement('div');
                studentCard.className = 'student-card';

                const name = document.createElement('h2');
                name.textContent = student.Name;
                studentCard.appendChild(name);

                const email = document.createElement('p');
                email.textContent = `Email: ${student.Email}`;
                studentCard.appendChild(email);

                const college = document.createElement('p');
                college.textContent = `College: ${student.College}`;
                studentCard.appendChild(college);

                const year = document.createElement('p');
                year.textContent = `Year: ${student.Year}`;
                studentCard.appendChild(year);

                const major = document.createElement('p');
                major.textContent = `Major: ${student.Major}`;
                studentCard.appendChild(major);

                const pronouns = document.createElement('p');
                pronouns.textContent = `Pronouns: ${student.Pronouns}`;
                studentCard.appendChild(pronouns);

                const address = document.createElement('p');
                address.textContent = `Address: ${student.Address}`;
                studentCard.appendChild(address);

                studentsDiv.appendChild(studentCard);
            });
        })
        .catch(error => {
            const studentsDiv = document.getElementById('students');
            studentsDiv.textContent = 'Error fetching students: ' + error;
        });
});
