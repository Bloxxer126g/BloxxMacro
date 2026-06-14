alert("Hello, World!")

document.getElementById("RunButton").addEventListener("click", event=>{
    pywebview.api.ExecuteActions(["(20,30)","X"]);
})