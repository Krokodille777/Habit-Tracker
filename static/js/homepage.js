let windowpage = window.location.pathname;
function GetStarted(){
windowpage = "/habitpage";
window.location.href = windowpage;
}

function GoHome(){
    windowpage = "/";
    window.location.href = windowpage;
}


window.onload = function(){
    const btn = document.getElementById("GetStartedBtn");
    btn.addEventListener("click", GetStarted);

    const btn2 = document.getElementById("homeBtn");
    btn2.addEventListener("click", GoHome);
}

export {GoHome};