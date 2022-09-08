let box = document.getElementById("box");
box.setAttribute('draggable', 'true');
box.setAttribute('ondragstart', 'drag(event)');
let big_box = document.getElementById("target");
big_box.setAttribute('ondragover', 'allowDrop(event)')
big_box.setAttribute('ondrop', 'drop(event)')
function allowDrop(event) {
    event.preventDefault();
}
function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}
function drop(event) {
    event.preventDefault();
    let data = event.dataTransfer.getData('text');
    event.target.appendChild(document.getElementById(data));
}
