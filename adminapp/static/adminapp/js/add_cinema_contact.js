const formContact = document.querySelector('#cinema-contact-form')
const addCinemaContactFormBtn = formContact.querySelector('.add-cont-btn')
const totalNewContactForms = formContact.querySelector('#id_contact-TOTAL_FORMS')
const allCurrentForms = formContact.querySelectorAll('.cont-form');


let n = allCurrentForms.length
let baseRegex = new RegExp('__base__', 'g')
for (let i = 0; i < n; i++) {
    allCurrentForms[i].innerHTML = allCurrentForms[i].innerHTML.replace(baseRegex, i)
}


addCinemaContactFormBtn.addEventListener('click', addNewContactsForm)

function addNewContactsForm() {
    let currentFormCount = formContact.querySelectorAll('.cont-form').length;


    let targetClassAttribute = 'cont-form border border-dark contact-form'
    // let targetIdAttribute = `images-${currentFormCount}`

    let formCopyTarget = formContact.querySelector('.add_cont')
    let copyEmptyFormEl = formContact.querySelector('.empty-form').cloneNode(true)


    copyEmptyFormEl.setAttribute('class', targetClassAttribute)
    // copyEmptyFormEl.setAttribute('id', targetIdAttribute)

    let regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)

    totalNewContactForms.setAttribute('value', currentFormCount + 1)

    formCopyTarget.before(copyEmptyFormEl)

}

function addLogo(e) {
    let parentId = e.dataset.parent_id
    let addLogoInput = formContact.querySelector(`#id_${parentId}`)
    addLogoInput.click()
    addLogoInput.addEventListener('change', addLogoInputChange)
}


function addLogoInputChange() {
    let addLogoCard = formContact.querySelector(`#${this.id}-card`)
    getImageUrl(this, addLogoCard)

    let clearLogoBtn = formContact.querySelector(`#${this.id}-clear_btn`)
    let clearLogoInput = this.parentNode.querySelector('input[type=checkbox]')
    isActive(clearLogoBtn, clearLogoInput)

    let errorDiv = addLogoCard.parentNode.querySelector('.error-div')
    let thisWidth = 150
    let thisHeight = 100
    isValid(errorDiv, this, thisWidth, thisHeight)

}


function clearLogo(e) {
    let parentId = e.dataset.parent_id
    let addLogoCard = formContact.querySelector(`#id_${parentId}-card`)
    let addLogoInput = formContact.querySelector(`#id_${parentId}`)
    let clearLogoInput = formContact.querySelector(`#${parentId}-clear_id`)
    let errorDiv = addLogoCard.parentNode.querySelector('.error-div')
    if (clearLogoInput) {
        clearLogoInput.click()
    }
    addLogoInput.value = ''
    errorDiv.innerHTML = ''
    e.setAttribute('disabled', 'true')
    addLogoCard.setAttribute('src', "/media/bsimg.jpeg")
}

function deleteForm(e) {
    let thisContactForm = e.parentNode.parentNode
    let deleteFormInput = e.parentNode.querySelector('input[type=checkbox]')
    deleteFormInput.click()
    thisContactForm.classList.add('hidden')
}