"use strict"

let user = {
  email: "user4@example.com",
  password: "123",
  is_active: true,
  is_superuser: false,
  is_verified: false
};

document.addEventListener('DOMContentLoaded', function() {
    // const form = document.getElementById('form');
    // const button = document.getElementById('button');
    // button.addEventListener('submit', pressed);
    document.getElementById('button').onclick = function() {
        pressed();
    }
})

async function pressed() {
  let response = await fetch('/auth/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(user)
  });
  
  let result = await response.text();
  alert(result);
}
