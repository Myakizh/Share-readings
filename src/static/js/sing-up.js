"use strict"

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    form.addEventListener('submit', formSend);

    async function formSend(e) {
        e.preventDefault();

        //let json = JSON.stringify(object);
        let json = {
            email: form.email.value,
            password: form.password.value,
            is_active: true,
            is_superuser: false,
            is_verified: false
        };

        let respons = await fetch('/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json;charset=utf-8' },
            body: JSON.stringify(json)
        })

        if (respons.ok) {
            let result = await respons.json();
            form.reset();
        }
        else {
            alert("Error");
        }
    }
});