const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const loginButton = document.getElementById("login-button");

loginButton.addEventListener("click", function(){

    console.log("Authentication Attempt");
    console.log("Username:", usernameInput.value);
    console.log("Password:", passwordInput.value);

});

loginButton.addEventListener("click", function(){
    usernameInput.value = "";
    passwordInput.value = "";
});

const createfirstnameInput = document.getElementById("first-name");
const createlastnameInput = document.getElementById("last-name");
const createdateInput = document.getElementById("date");
const createnameInput = document.getElementById("create-username");
const createpasswordInput = document.getElementById("create-password");
const createButton = document.getElementById("create-button");

createButton.addEventListener("click", function(){

    console.log("Account Creation Attempt");
    console.log("First Name:", createfirstnameInput.value);
    console.log("Last Name:", createlastnameInput.value);
    console.log("Date:", createdateInput.value);
    console.log("Username:", createnameInput.value);
    console.log("Password:", createpasswordInput.value);
});









