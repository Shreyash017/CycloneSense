// To raise alert if no image is uploaded before submitting the form
// Source (Chatgpt): https://chat.openai.com/share/dc7559ef-d514-42c7-991e-fda8752f774f

function submitForm(event) {
    event.preventDefault(); // Prevent form submission

    var fileInput = document.querySelector('input[type="file"]');
    if (fileInput.files.length === 0) {
        // No image uploaded, invoke your JavaScript function here
        alert("Please upload an image before submitting.");
        return;
    }

    // Submit the form
    var form = document.getElementById('upload-form');
    form.submit();
}

// To fade in the image after it is loaded
function fadeInImage(image) {
    // var imageContainer = document.querySelector('.imgs');
    // imageContainer.classList.add('loaded');
    image.classList.add('loaded');
}
