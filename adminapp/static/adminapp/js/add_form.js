    const addMoreBtn = document.getElementById('add-more')
    const totalNewForms = document.getElementById('id_images-TOTAL_FORMS')
    const currentIngredientForms = document.getElementsByClassName('form-group offset-md-2 im-form')

    addMoreBtn.addEventListener('click', add_new_form)

    function add_new_form(event) {
        if (event) {
            event.preventDefault()
        }
        const currentIngredientForms = document.getElementsByClassName('form-group offset-md-2 im-form')
        const currentFormCount = currentIngredientForms.length
        const formCopyTarget = document.getElementById('im-form')
        const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)

        copyEmptyFormEl.setAttribute('class', 'form-group offset-md-2 im-form')
        copyEmptyFormEl.setAttribute('id', `images-${currentFormCount}`)

        const regex = new RegExp('__prefix__', 'g')

        copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)

        totalNewForms.setAttribute('value', currentFormCount + 1)

        formCopyTarget.append(copyEmptyFormEl)
    }
