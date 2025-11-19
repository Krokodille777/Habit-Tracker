let windowpage = window.location.pathname;
if (windowpage === '/' || windowpage === '/index.html'){
    window.location.href = '/homepage.html';
}
function GetStarted(){
windowpage = "../templates/habitpage.html";
window.location.href = windowpage;
}



window.onload = function(){
    const btn = document.getElementById("GetStartedBtn");
    btn.addEventListener("click", GetStarted);
}