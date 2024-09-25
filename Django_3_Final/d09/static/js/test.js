document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // Empêche le formulaire de se soumettre par défaut

    const csrftoken = getCookie("csrftoken");
    const username = document.getElementById('id_username').value;
    const password = document.getElementById('id_password').value;

    try {
        const response = await fetch("/account/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",  // Ajout de l'en-tête ici
                "X-CSRFToken": csrftoken
            },
            body: new URLSearchParams({
                'username': username,
                'password': password
            })
        });

        const data = await response.json();
        if (data.logged_in) {
            // Injecter le contenu de l'utilisateur connecté
            document.getElementById('content-area').innerHTML = `
                <h3>Bienvenue, ${data.username}!</h3>
                <button id="logoutButton" class="btn btn-danger">Logout</button>
            `;

            // Mettre à jour la barre de navigation
            updateNavbar(data.username);

            // Gestion de la déconnexion
            document.getElementById("logoutButton").addEventListener("click", async function() {
                const logoutResponse = await fetch("/account/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-Requested-With": "XMLHttpRequest",  // Ajout de l'en-tête ici
                        "X-CSRFToken": csrftoken
                    },
                    body: new URLSearchParams({
                        "logout": "true"
                    })
                });

                const logoutData = await logoutResponse.json();
                if (logoutData.logged_out) {
                    // Afficher le formulaire de connexion à la place
                    document.getElementById('content-area').innerHTML = `
                        <form method="post" id="loginForm" class="form-signin">
                            {% csrf_token %}
                            <div class="form-group mb-3">
                                <label for="id_username">Username</label>
                                <input type="text" id="id_username" name="username" class="form-control" required autofocus>
                            </div>
                            <div class="form-group mb-3">
                                <label for="id_password">Password</label>
                                <input type="password" id="id_password" name="password" class="form-control" required>
                            </div>
                            <div id="error-message" class="text-danger"></div>
                            <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
                        </form>
                    `;

                    // Mettre à jour la barre de navigation
                    updateNavbar(null); // Utilisateur déconnecté
                }
            });
        } else {
            document.getElementById("error-message").innerText = "Login failed: " + (data.errors || "Unknown error");
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

// Fonction pour mettre à jour la barre de navigation
function updateNavbar(username) {
    const navbar = document.getElementById('navbar'); // Changez ceci en fonction de votre structure HTML
    if (navbar) {
        if (username) {
            navbar.innerHTML = `
                <li class="nav-item">Welcome, ${username}</li>
                <li class="nav-item"><button id="logoutButton" class="btn btn-danger">Logout</button></li>
            `;
        } else {
            navbar.innerHTML = `
                <li class="nav-item"><a href="#" class="nav-link" data-toggle="modal" data-target="#loginModal">Login</a></li>
                <li class="nav-item"><a href="#" class="nav-link">Register</a></li>
            `;
        }
    }
}