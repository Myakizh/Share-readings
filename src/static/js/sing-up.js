"use strict"

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    form.addEventListener('submit', formSend);

    async function formSend(e) {
        e.preventDefault();
        
        console.log("qawe");

        let formData = new FormData(form);

        let respons = await fetch('http://127.0.0.1:8000/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json;charset=utf-8' },
            body: JSON.stringify(formData)
        })
        .then(response => response.ok ? response.json() : response.status)
        .then(result => console.log(result));

        if (respons.ok) {
            let result = await respons.json();
            form.reset();
        }
        else {
            alert("Error");
        }
    }
});