function on_clickme(url) {
    window.location=url
}

function toggle_element_visibility(element_id) {
    let element = document.getElementById(element_id)
    if (element.style.display === "none") {
        element.style.display = "block"
    } else {
        element.style.display = "none"
    }
}

function toggle_div_visibility(div_id) {
    toggle_element_visibility(div_id+'_content')
    toggle_element_visibility(div_id+'_button_hide')
    toggle_element_visibility(div_id+'_button_show')
}
