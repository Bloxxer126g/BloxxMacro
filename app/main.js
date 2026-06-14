alert("Hello, World!")

document.getElementById("RunButton").addEventListener("click", {
    pywebview.api.ExecuteActions(["(20,30)","X"]);
})