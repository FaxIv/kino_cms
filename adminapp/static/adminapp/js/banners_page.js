const addBannerFormButtons = document.querySelectorAll('.add-formset')

const topBannersForms = document.querySelectorAll('.top-banner-form')
const newsPromotionBannersForms = document.querySelectorAll('.news_promotion-banner-form')
let baseRegex = new RegExp('__base__', 'g')
let topBanCount = topBannersForms.length
let newsPromotionsBanCount = newsPromotionBannersForms.length

for (let i = 0; i < topBanCount; i++) {
    topBannersForms[i].innerHTML = topBannersForms[i].innerHTML.replace(baseRegex, i)
}

for (let i = 0; i < newsPromotionsBanCount; i++) {
    newsPromotionBannersForms[i].innerHTML = newsPromotionBannersForms[i].innerHTML.replace(baseRegex, i)
}


for (let btnItem of addBannerFormButtons) {
    btnItem.addEventListener('click', addFormInFormset)
}

function addFormInFormset() {
    let parentClass = this.dataset.target_form
    let targetBlockItem = document.querySelector(`.${parentClass}`)
    console.log(targetBlockItem)
    let totalFormsetInitialForms = targetBlockItem.querySelector(`#id_${parentClass}-TOTAL_FORMS`)
    let currentFormCount = targetBlockItem.querySelectorAll('.bn-form').length

    let targetClassAttribute = 'bn-form d-flex flex-column align-items-end'

    let copyEmptyFormEl = targetBlockItem.querySelector('.empty-form').cloneNode(true)

    copyEmptyFormEl.setAttribute('class', targetClassAttribute)


    let regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)


    totalFormsetInitialForms.setAttribute('value', currentFormCount + 1)

    let formCopyTarget = targetBlockItem.querySelector('.add-formset-btn-div')
    formCopyTarget.before(copyEmptyFormEl)
}


// Download image in banner form

const addBannerImageButtons = document.querySelectorAll('.add-bn-im-btn');

function addBanner(e) {
    let targetId = e.dataset.parent_id
    let addBannerImageInput = e.parentNode.querySelector(`#id_${targetId}_image`)
    addBannerImageInput.click()
    addBannerImageInput.addEventListener('change', addBannerImageInputChange)
}

function addBannerImageInputChange() {
    let thisId = this.id
    let bannersImageCard = document.querySelector(`#${thisId}-card`)
    getImageUrl(this, bannersImageCard)
    let errorDiv = bannersImageCard.parentNode.querySelector('.err-div')
    let thisWidth = 1000
    let thisHeight = 190
    isValid(errorDiv, this, thisWidth, thisHeight)
}


// Delete banner`s form

function deleteBannerForm(e) {
    let targetId = e.dataset.target_input
    let deleteFormInput = document.querySelector(`#id_${targetId}-DELETE`)
    deleteFormInput.click()
    e.parentNode.classList.add('hidden')
    e.parentNode.classList.remove('d-flex')
}

let backgroundForm = document.querySelector('#background-form')
let addBackgroundBtn = backgroundForm.querySelector('.add-img-btn')
let deleteBackgroundBtn = backgroundForm.querySelector('.clear-img-btn')
let addBackgroundInput = backgroundForm.querySelector('#id_background-banner_image')
let backgroundImageCard = backgroundForm.querySelector('.img-field')
let backgroundErrDiv = backgroundForm.querySelector('.error-div')
let deleteBackgroundInput = backgroundForm.querySelector('#background-banner_image-clear_id')
let backgroundSimpleRadio = backgroundForm.querySelector('#id_background-background_or_banner_1')
let backgroundPhotoRadio = backgroundForm.querySelector('#id_background-background_or_banner_0')
addBackgroundBtn.addEventListener('click', addBackground)
addBackgroundInput.addEventListener('change', addBackgroundInputChange)
deleteBackgroundBtn.addEventListener('click', deleteBackgroundBtnClick)

if (deleteBackgroundInput == null) {
    deleteBackgroundBtn.setAttribute('disabled', '')
    backgroundSimpleRadio.setAttribute('disabled', '')
    backgroundPhotoRadio.setAttribute('disabled', '')
}

function addBackground() {
    addBackgroundInput.click()
}

function addBackgroundInputChange() {
    let thisWidth = 3000
    let thisHeight = 2000
    getImageUrl(addBackgroundInput, backgroundImageCard)
    isValid(backgroundErrDiv, addBackgroundInput, thisWidth, thisHeight)
    if (deleteBackgroundBtn.hasAttribute('disabled')) {
        if (deleteBackgroundInput) {
            deleteBackgroundInput.click()
        }
        deleteBackgroundBtn.removeAttribute('disabled')
        backgroundSimpleRadio.removeAttribute('disabled')
        backgroundPhotoRadio.removeAttribute('disabled')

    }
}

function deleteBackgroundBtnClick() {
    addBackgroundInput.value = ''
    if (deleteBackgroundInput !== true) {
        deleteBackgroundInput.click()
    }
    deleteBackgroundBtn.setAttribute('disabled', '')
    backgroundErrDiv.innerHTML = ''
    backgroundImageCard.setAttribute('src', "/media/bsimg.jpeg")

    backgroundSimpleRadio.click()
    backgroundSimpleRadio.setAttribute('disabled', '')
    backgroundPhotoRadio.setAttribute('disabled', '')
}
