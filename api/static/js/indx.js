const registerData = async (event) => {
    const userForm = document.querySelector('.user');
    var notificationDiv = document.getElementById('notification');
    event.preventDefault();

    const formData = new FormData(userForm);

    fetch('/register/', {
        method: 'POST', body: formData,
    })
        .then(response => response.json())
        .then(data => {

            if (data.message === 'Registro exitoso') {

                notificationDiv.style.display = 'block';

            }
        })
        .catch(error => {
            console.error(error);
        });

}


const LoginForm = async (event) => {
    event.preventDefault();

    const userForm = document.querySelector('.user');
    const formData = new FormData(userForm);
    const dataDisplay = document.getElementById('notification');

    fetch('/login/', {

        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData,

    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {

                dataDisplay.textContent = 'Error: ' + data.error;

            } else {

                dataDisplay.textContent = '¡Bienvenido! Datos: ' + JSON.stringify(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            dataDisplay.textContent = 'Error inesperado';
        });


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}
