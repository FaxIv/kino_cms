const addBannerFormButtons = document.querySelectorAll('.add-formset')

const topBannersForms = document.querySelectorAll('.top-bn-form')
const newsPromotionBannersForms = document.querySelectorAll('.news-promotion-forms')
let baseRegex = new RegExp('__base__', 'g')
let topBanCount = topBannersForms.length
let newsPromotionsBanCount = newsPromotionBannersForms.length

for (let i = 0; i < topBanCount; i++) {
    topBannersForms[i].innerHTML = topBannersForms[i].innerHTML.replace(baseRegex, i)
}

// for (let i = 0; i < topBanCount; i++) {
//     newsPromotionsBanCount[i].innerHTML = newsPromotionsBanCount[i].innerHTML.replace(baseRegex, i)
// }


for (let btnItem of addBannerFormButtons) {
    btnItem.addEventListener('click', addFormInFormset)
}

function addFormInFormset() {
    let parentClass = this.dataset.target_form
    let targetBlockItem = document.querySelector(`.${parentClass}`)
    let totalFormsetInitialForms = targetBlockItem.querySelector(`#id_${parentClass}-INITIAL_FORMS`)
    let currentFormCount = targetBlockItem.querySelectorAll('.top-bn-form').length
    
    let targetClassAttribute = 'top-bn-form d-flex flex-column align-items-end'

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
