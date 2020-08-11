async function answer() {
                var quest = document.getElementById("data").value
                var val = await eel.mainBackend(quest)();
                swagAlert({
                           title: "Penty",
                           text: val});
}

async function systemInfo() {
                var val = await eel.platforminfo()();
                swagAlert({
                           title: "Penty",
                           text: val});
}


window.addEventListener("resize", function(){
window.resizeTo(471, 220);
});
