/* Diagnose form Validation */
const form = document.getElementById('diagnose-form');
const submitElement = document.getElementById('diagnose-form-submit');

form.addEventListener("submit", async (e) => {
    /* Stop default submit */
    e.preventDefault();
    submitElement.disable = true;

    let form = e.currentTarget;
    let url = form.action;

    try{
        let formData = new FormData(form);
        let isDataValidated = validateData(formData);

        if (!isDataValidated){
            submitElement.disable = false;
            return false;
        }
        document.getElementById('diagnose-form').submit();
    }catch (error) {
        console.log(error);
    }
});

/* Helper Function */
function addErrorMessage(phoneInput, message) {
    const newItem = document.createElement('span')
    newItem.classList.add('ErrorMessageRequire')
    newItem.innerHTML = message
    newItem.style.color = 'red'
    phoneInput.parentElement.appendChild(document.createElement('br'))
    phoneInput.parentElement.appendChild(newItem)
    return false
}

/* Validation Function */
function validateData(formData) {
    let formDataObject = Object.fromEntries(formData.entries());
    let pass = true;
    const requiredFlags = document.querySelectorAll('.ErrorMessageRequire');
    requiredFlags.forEach(el => {
        el.remove();
    })

    /* phone validation */
    var phoneFormat = /^\966\d{1,9}$/ ;
    var phoneInput = document.getElementById('mobile_number');
    if ((phoneInput.value && phoneInput.value.length != 12) || (phoneInput.value && !phoneInput.value.match(phoneFormat))){
        pass = addErrorMessage(phoneInput, "Please enter valid mobile no.");
    }

    return pass
}

async function postFormFieldsJson({ url, formData }) {
    // Create an object from the form data entries
    let formDataObject = Object.formEntries(formData.entries());
    // Format the plain form data as JSON
    let formDataJsonString = JSON.stringify(formDataObject);

    // Set the fetch options (headers, body)
    let fetchOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Accept : "application/json",
        },
        body: formDataJsonString,
    };

    // Get the response body as JSON string
    // If the response was not OK, throw an error
    let res = await fetch(url, fetchOptions);

    // If the response was not OK, throw an error(for debugging)
    if (!res.ok) {
        let error = await res.text();
        throw new Error(error);
    }
    // If the response was OK, return the response body
    return res.json();

}