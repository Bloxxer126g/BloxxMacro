let Actions = [];
const centerContent = document.getElementById("CenterContent");

function renderActions() {
    centerContent.innerHTML = "";
    Actions.forEach(action => {
        const actionDiv = document.createElement("div");
        actionDiv.className = "Action Text";

        if (action.startsWith("(")) {
            actionDiv.innerText = `Click ${action}`;
        } else {
            actionDiv.innerText = `Press Key: ${action.toUpperCase()}`;
        }
        
        centerContent.appendChild(actionDiv);
    });
}

document.getElementById("RecordClickBtn").addEventListener("click", async () => {
    const btn = document.getElementById("RecordClickBtn");
    btn.innerText = "Click Anywhere...";
    btn.style.background = "#fee2e2";

    const coords = await pywebview.api.GetClickLocation();
    
    if (coords) {
        Actions.push(coords);
        renderActions();
    }
    
    btn.innerText = "+ Record Click";
    btn.style.background = "";
});

document.getElementById("RecordKeyBtn").addEventListener("click", () => {
    const btn = document.getElementById("RecordKeyBtn");
    btn.innerText = "Press any key...";
    btn.style.background = "#fee2e2";

    const keyListener = (event) => {
        event.preventDefault();

        let key = event.key.toLowerCase();
        if (key === " ") key = "space";
        
        Actions.push(key);
        renderActions();
        btn.innerText = "+ Record Key";
        btn.style.background = "";
        window.removeEventListener("keydown", keyListener);
    };

    window.addEventListener("keydown", keyListener);
});

document.getElementById("RunButton").addEventListener("click", () => {
    if (Actions.length === 0) {
        alert("Add some actions first!");
        return;
    }
    pywebview.api.ExecuteActions(Actions);
});