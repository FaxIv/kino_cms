let inputs = document.querySelectorAll('input')
for (let elem of inputs) {
    if (elem.type !== 'radio') {
        elem.setAttribute('class', 'form-control')
    }
}
let languageDiv = document.querySelector('#id_language')
languageDiv.setAttribute('class', 'd-flex justify-content-between aling-items-center')

let genderDiv = document.querySelector('#id_gender')
genderDiv.setAttribute('class', 'd-flex justify-content-between aling-items-center')

let hiddenGender = document.querySelector('label[for=id_gender_0]')
hiddenGender.parentNode.setAttribute('class', 'hidden')


// Validation
let thisForm = document.querySelector('form')
let passwordField = document.querySelector('input[name=password-field]')
let confirmPasswordField = document.querySelector('input[name=confirm-password]')
let saveFormBtn = document.querySelector('#save_btn')
let passwordErrorDiv = document.querySelector('.password-error')


let usernameField = document.querySelector('input[name=username]')
let usernameError = document.querySelector('.username-error')

saveFormBtn.addEventListener('click', validation)

// thisForm.addEventListener('submit', validation)
function validation(event) {
    let errorList = []
    let allInputsErr = document.querySelectorAll('.is-invalid')
    for (let elem of allInputsErr) {
        elem.classList.remove('is-invalid')
    }

    let errDiv = document.querySelectorAll('.error-div')
    for (let elem of errDiv) {
        elem.innerHTML = ''
    }

    if (usernameField.value === '') {
        usernameError.prepend('Обовʼязкове поле')
        usernameField.classList.add('is-invalid')
        errorList.push('username')
    }


    if (passwordField.value !== confirmPasswordField.value) {
        passwordErrorDiv.prepend('Паролі не збігаються!')
        passwordField.classList.add('is-invalid')
        confirmPasswordField.classList.add('is-invalid')
        errorList.push('password')
    }

    if (errorList.length !== 0) {
        event.preventDefault()
    }
}