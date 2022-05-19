// Set formset`s form limit.
function noMoreFiveForm() {
    let currentVisibleForms = formMain.querySelectorAll('.vis-form').length
    if (currentVisibleForms > 4) {
        formsetAddFormBtn.setAttribute('hidden', '')
    } else {
        formsetAddFormBtn.removeAttribute('hidden')
    }
}


// Return download image URL, to set in thumbnail image card. Coll image validation function.
function getImageUrl(inp, card) {
    if (inp.files && inp.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            card.setAttribute('src', e.target.result);
        }
        reader.readAsDataURL(inp.files[0]);
    }
}


// Checked attribute 'disabled' for delete main image button.
function isActive(btn, inp) {
    if (btn.getAttribute('disabled')) {
        if (inp) {
            inp.click()
        }
        btn.removeAttribute('disabled')
    }
}


// Checked image width and height, return error span.
function isValid(errorBlock, fileInput) {
    let _URL = window.URL;
    let file, img;
    if (file = fileInput.files[0]) {
        // let saveFormButton = document.querySelector('[name=save-button]');
        let span = errorBlock.querySelector('.image-error');
        if (span) {
            span.remove();
        }
        img = new Image();
        img.onload = function () {
            if (this.width != 1000 && this.height != 190) {
                let span = document.createElement('span');
                span.setAttribute('class', 'image-error');
                span.innerHTML = 'Невірні розміри';
                errorBlock.append(span);
                // saveFormButton.setAttribute('disabled', 'true')
            } else {
                //saveFormButton.removeAttribute('disabled');
            }
        }
        img.src = _URL.createObjectURL(file);
    }
}
