async function answer() {
                var quest = document.getElementById("data").value
                swagAlert({
                           title: "Penty",
                           text: "Processing.."});
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

window.onload=function(){
  var input = document.getElementById("data");
  input.addEventListener("keyup", function(event) {
      if (event.keyCode === 13) {
          event.preventDefault();
          document.getElementById("enterButton").click();
      }
  });
}
