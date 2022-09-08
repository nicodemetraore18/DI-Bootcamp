let input = document.createElement("input");
document.body.appendChild(input);
input.addEventListener('input', check_letter);
function check_letter(e) {
    let check = this.value.split("");
    if (check[check.length-1].toUpperCase() == check[check.length-1].toLowerCase()) {
        check.pop();
    }
    this.value = check.join("");
}