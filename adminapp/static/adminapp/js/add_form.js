    document.addEventListener("DOMContentLoaded", addPref)

    const addMoreImageFormsBtn = document.getElementById('add-more')
    const totalNewImageForms = document.getElementById('id_images-TOTAL_FORMS')
    const currentIngredientForms = document.getElementsByClassName('form-group col-md-2 im-form')

    const addMainImageInput = document.getElementById('id_movie-main_image')
    const addMainImageBtn = document.getElementById('id_movie-main_image_btn')
    const cleanMainImageInput = document.getElementById('movie-main_image-clear_id')
    const cleanMainImageBtn = document.getElementById('movie-main_image-clear_id_btn')
    const durationMovieInput = document.getElementById('id_movie-duration')

    addMoreImageFormsBtn.addEventListener('click', add_new_form)
    addMainImageBtn.addEventListener('click', add_main_image)
    cleanMainImageBtn.addEventListener('click', delete_main_image)
    addMainImageInput.addEventListener('change', isActive)



    function addPref() {
        if (cleanMainImageInput == null) {
            cleanMainImageBtn.setAttribute('disabled', 'true')
        }

        let n = currentIngredientForms.length
        let baseRegex = new RegExp('__base__', 'g')
        for (let i = 0; i < n; i++) {
            currentIngredientForms[i].setAttribute('id', `images-${i}`)
            currentIngredientForms[i].innerHTML = currentIngredientForms[i].innerHTML.replace(baseRegex, i)
        }
    }

    // Add new form for image input, used Django empty_form.
    function add_new_form(event) {
        if (event) {
            event.preventDefault()
        }

        const currentFormCount = currentIngredientForms.length
        const formCopyTarget = document.getElementById('im-add-more')
        const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)

        copyEmptyFormEl.setAttribute('class', 'form-group col-md-2 im-form')
        copyEmptyFormEl.setAttribute('id', `images-${currentFormCount}`)

        const regex = new RegExp('__prefix__', 'g')
        copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)

        totalNewImageForms.setAttribute('value', currentFormCount + 1)

        formCopyTarget.before(copyEmptyFormEl)
    }

    // Checked attribute 'disabled' for delete main image button.
    function isActive() {
        if (cleanMainImageBtn.getAttribute('disabled') == 'true') {
            if (cleanMainImageInput) {
                cleanMainImageInput.click()
            }
            cleanMainImageBtn.removeAttribute('disabled')
        }
    }

    // Download main image.
    function add_main_image() {
        addMainImageInput.setAttribute('onchange', 'getImageUrl(this)')
        addMainImageInput.click()
    }

    // Delete main image.
    function delete_main_image() {
        let imageCard = document.getElementById('id_movie-main_image-card')
        if (cleanMainImageInput) {
            cleanMainImageInput.click()
        }
        addMainImageInput.value = ''
        cleanMainImageBtn.setAttribute('disabled', 'true')
        imageCard.setAttribute('src', "/media/bsimg.jpeg")
    }

    // Download new image in gallery image forms with thumbnail image card. Call function that return download image URL.
    function add_image(e) {
        let formId = e.parentNode.id
        let addImageInput = document.getElementById(`id_${formId}-image`)
        addImageInput.setAttribute('onchange', 'getImageUrl(this)')
        addImageInput.click()
    }

    // Delete gallery image form from page / set attribute 'hidden'.
    function delete_form(e) {
        let formId = e.parentNode.id
        let addImageInput = document.getElementById(`id_${formId}-image`)
        let checkboxDeleteImg = document.getElementById(`id_${formId}-DELETE`)
        checkboxDeleteImg.click()
        e.parentNode.setAttribute('hidden', '')
        addImageInput.value = ''
    }

    // Return download image URL, to set in thumbnail image card. Coll image validation function.
    function getImageUrl(input) {
        let formImgInputId = input.id
        let imageCard = document.getElementById(`${formImgInputId}-card`)
        if (input.files && input.files[0]) {
            let reader = new FileReader();
            reader.onload = function(e) {
                imageCard.setAttribute('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
        if (formImgInputId != 'id_movie-main_image') {
            isValid(input, imageCard)
        }
    }

    // Make image validation by width and height.
    function isValid(input, imageCard) {
        let fileInput = input;
        let targetId = input.id;
        let errorDiv = imageCard.parentNode.querySelector('[class=error-image-div]');
        var _URL = window.URL;
        var file, img;
        if (file = fileInput.files[0]) {
            let saveFormButton = document.querySelector('[name=save-button]');
            let span = errorDiv.querySelector('[class=image-error]');
                if (span) {
                    span.remove();
                }
            img = new Image();
            img.onload = function () {
                if (this.width != 1000 && this.height != 190) {
                    let span = document.createElement('span');
                    span.setAttribute('class', 'image-error');
                    span.innerHTML = 'Невірні розміри';
                    errorDiv.append(span);
//                    saveFormButton.setAttribute('disabled', 'true')
                } else {
                    //saveFormButton.removeAttribute('disabled');
                }
            }
            img.src = _URL.createObjectURL(file);
        }
    }

    // Set rule: no more 4 number in 'duration' input.
    durationMovieInput.addEventListener('input', function() {
        let durationMaxLength = 4;
        if (this.value.length > durationMaxLength) {
		    this.value = this.value.slice(0, durationMaxLength);
        }
    })

    // Checks if the date is entered correctly.
    let dateInputDiv = document.querySelector('div.date_input')
    dateInputDiv.addEventListener('change', function() {
        let startSaleInput = document.querySelector('[name=movie-start_sale]');
        let finishSaleInput = document.querySelector('[name=movie-finish_sale]');
        let errorDiv = dateInputDiv.querySelector('div.errdiv')
        let span = errorDiv.querySelector('[class=image-error]');
        let saveFormButton = document.querySelector('[name=save-button]');
        if (span) {
            span.remove();
        }
        if (startSaleInput.value > finishSaleInput.value) {
            let span = document.createElement('span');
            span.setAttribute('class', 'image-error');
            span.innerHTML = 'Дата початку прокату не може бути більше дати кінця прокату!';
            errorDiv.append(span);
//            saveFormButton.setAttribute('disabled', 'true')
        } else {
//            saveFormButton.removeAttribute('disabled');
        }
    })



    // Base version button - reload page.
    let baseVersionBtn = document.querySelector('button.base_version')
    baseVersionBtn.addEventListener('click', function() {
        window.location.reload();
    })


    //PAGE VALIDATOR
//    let form = document.querySelector('.basic-form')
//    let allTextFields = form.querySelectorAll('.form-control')
//    form.addEventListener('submit', function(event) {
//        event.preventDefault()
//
//        for (let i=0; i < allTextFields.length; i++) {
//            if (true) {
//                console.log('blank', allTextFields[i])
//            }
//        }
//    })
//    function getUrl(input) {
//        let formImgInputId = input.id
//        let imageCard = document.getElementById(`${formImgInputId}-card`)
//        if (input.files && input.files[0]) {
//            let reader = new FileReader();
//            reader.onload = function(e) {
//                imageCard.setAttribute('src', e.target.result);
//            }
//            reader.readAsDataURL(input.files[0]);
//        }
//    }
//    function getUrl(input) {
//        let imgInput = input
//        let formImgInputId = imgInput.id
//        let imageCard = document.getElementById(`${formImgInputId}-card`)
//        if (input.files && input.files[0]) {
//            let reader = new FileReader();
//            reader.onload = function(e) {
//                imageCard.setAttribute('src', e.target.result);
//            }
//            reader.readAsDataURL(input.files[0]);
//        }
//        var _URL = window.URL;
//        var file, img;
//        if (file = imgInput.files[0]) {
//            img = new Image();
//            img.onload = function () {
//                if (this.width == 1000 && this.height == 190) {
//                    console.log('verno')
//                } else {
//                    console.log('neverno')
//                }
////                imgInput.dataset['imageWidth'] = this.width;
////                imgInput.dataset['imageHeight'] = this.height;
//            }
//            img.src = _URL.createObjectURL(file);
//        }
//
//    }



