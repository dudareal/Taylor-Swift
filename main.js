document.addEventListener('DOMContentLoaded', () => {
    fetchUsers();

    document.getElementById('user-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const userName = document.getElementById('user-name').value;
        addUser (userName);
    });
});

function fetchUsers() {
    fetch('http://127.0.0.1:3000')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('user-list');
            userList.innerHTML = '';
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = user.nome;
                userList.appendChild(li);
            });
        })
        .catch(error => console.error('Erro ao buscar usuários:', error));
}

function addUser (name) {
    fetch('http://127.0.0.1:3000', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome: name }),
    })
    .then(response => {
        if (response.ok) {
            fetchUsers();
            document.getElementById('user-name').value = '';
        } else {
            console.error('Erro ao cadastrar usuário:', response.statusText);
        }
    })
    .catch(error => console.error('Erro ao cadastrar usuário:', error));
}