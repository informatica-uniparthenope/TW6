function submit_form() {
    let text = document.getElementById("text").value
    console.log(text)
    if (text.length<=144) {
        document.getElementById("form_post").submit()
    } else {
        alert("Error:"+text.length)
    }
}
