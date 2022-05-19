document.addEventListener("DOMContentLoaded", addPref)
const formMain = document.querySelector('#main-form-content')
const mainFormAddImageButtons = formMain.querySelectorAll('.add-img-btn')
const mainFormClearImageButtons = formMain.querySelectorAll('.clear-img-btn')
const totalNewImageForms = formMain.querySelector('#id_images-TOTAL_FORMS')
const currentIngredientForms = formMain.querySelectorAll('.im-form')
const formsetAddFormBtn = formMain.querySelector('.add-f-btn')


function addPref() {
    let n = currentIngredientForms.length
    let baseRegex = new RegExp('__base__', 'g')
    for (let i = 0; i < n; i++) {
        currentIngredientForms[i].setAttribute('id', `images-${i}`)
        currentIngredientForms[i].innerHTML = currentIngredientForms[i].innerHTML.replace(baseRegex, i)
    }
}


//Buttons for add image in main form
for (let buttonItem of mainFormAddImageButtons) {
    buttonItem.addEventListener('click', mainFormAddImageBtnClick)
    let mainFormAddImageInput = buttonItem.parentNode.querySelector('input[type=file]')
    mainFormAddImageInput.addEventListener('change', mainFormAddImageInputChange)
}

function mainFormAddImageBtnClick() {
    let btnItem = this
    let mainFormAddImageInput = btnItem.parentNode.querySelector('input[type=file]')
    mainFormAddImageInput.click()
}

function mainFormAddImageInputChange() {
    let imageCard = formMain.querySelector(`#${this.id}-card`)
    getImageUrl(this, imageCard)

    let baseDiv = imageCard.parentNode
    let mainFormClearImageInput = baseDiv.querySelector('input[type=checkbox]')
    let mainFormClearImageBtn = baseDiv.querySelector('.clear-img-btn')
    isActive(mainFormClearImageBtn, mainFormClearImageInput)
}


//Button for clear image in main form
for (let buttonItem of mainFormClearImageButtons) {
    let mainFormClearImageInput = buttonItem.parentNode.querySelector('input[type=checkbox]')
    if (mainFormClearImageInput == null) {
        buttonItem.setAttribute('disabled', 'true')
    }
    buttonItem.addEventListener('click', mainFormClearImageBtnClick)
}

function mainFormClearImageBtnClick() {
    let btnItem = this
    let mainFormImage = btnItem.parentNode
    let mainFormAddImageInput = mainFormImage.querySelector('input[type=file]')
    let mainFormClearImageInput = mainFormImage.querySelector('input[type=checkbox]')
    let imageCard = mainFormImage.parentNode.querySelector('img')
    if (mainFormClearImageInput) {
        mainFormClearImageInput.click()
    }
    mainFormAddImageInput.value = ''
    btnItem.setAttribute('disabled', 'true')
    imageCard.setAttribute('src', "/media/bsimg.jpeg")
}


// Add new form for image input, used Django empty_form.
formsetAddFormBtn.addEventListener('click', formsetAddFormBtnClick)

function formsetAddFormBtnClick() {
    addNewForm()
    noMoreFiveForm()
}

function addNewForm(event) {
    if (event) {
        event.preventDefault()
    }

    let currentFormCount = formMain.querySelectorAll('.im-form').length;

    let targetClassAttribute = 'vis-form d-flex flex-column align-items-center im-form'
    let targetIdAttribute = `images-${currentFormCount}`


    let formCopyTarget = formMain.querySelector('.im-add-more')
    let copyEmptyFormEl = formMain.querySelector('.empty-form').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', targetClassAttribute)
    copyEmptyFormEl.setAttribute('id', targetIdAttribute)

    let regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)

    totalNewImageForms.setAttribute('value', currentFormCount + 1)

    formCopyTarget.before(copyEmptyFormEl)
}


// Add image in formset`s form.
function addImage(e) {
    let addFormsetImageInput = e.parentNode.querySelector('input[type=file]')
    addFormsetImageInput.click()
    addFormsetImageInput.addEventListener('change', formsetAddImageInputChange)

}

function formsetAddImageInputChange() {
    let addFormsetImageInput = this
    let addFormsetImageCard = addFormsetImageInput.parentNode.parentNode.querySelector('img')
    let errorDiv = addFormsetImageCard.parentNode.parentNode.querySelector('.er-im')

    getImageUrl(addFormsetImageInput, addFormsetImageCard)
    isValid(errorDiv, addFormsetImageInput)
}


// Delete image from formset`s form.
function deleteImage(e) {
    let deleteFormsetImageInput = e.parentNode.querySelector('input[type=checkbox]')
    let addFormsetImageInput = e.parentNode.querySelector('input[type=file]')
    deleteFormsetImageInput.click()
    e.parentNode.parentNode.setAttribute('class', 'im-form hidden')
    addFormsetImageInput.value = ''
    noMoreFiveForm()
}
