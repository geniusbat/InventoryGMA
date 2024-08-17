var instanceId = null;

function deleteButtonClick(id, instanceIdI) {
    var offset = document.getElementById(id).getBoundingClientRect();
    var modal = document.getElementById("DeleteInstanceModal");
    modal.style.display="block";
    modal.style.top = String(offset.top)+"px";
    modal.style.left = String(offset.left)+"px";
    instanceId = instanceIdI;
}

function deleteYes() {
    var url = document.getElementById("deleteUrlInput").value;
    window.location.assign(url.replace("123", instanceId));
    hideModal();
}


function deleteNo() {
    hideModal();
}

function hideModal() {
    document.getElementById("DeleteInstanceModal").style.display="none"
}