let current = "";
let previous = null;
let operator = null;

function press(num) {
    current += num;
    update();
}

function setOp(op) {
    if (current === "") return;
    previous = parseFloat(current);
    operator = op;
    current = "";
}

function calculate() {
    if (operator === null || current === "") return;

    let curr = parseFloat(current);
    let result;

    switch(operator) {
        case "+": result = previous + curr; break;
        case "-": result = previous - curr; break;
        case "*": result = previous * curr; break;
        case "/": result = curr === 0 ? "Error" : previous / curr; break;
    }

    current = result.toString();
    operator = null;
    update();
}

function clearAll() {
    current = "";
    previous = null;
    operator = null;
    update();
}

function backspace() {
    if (current.length > 0) current = current.slice(0, -1);
    update();
}

function percent() {
    if (current !== "") current = (parseFloat(current)/100).toString();
    update();
}

function square() {
    if (current !== "") current = (parseFloat(current)**2).toString();
    update();
}

function sqrt() {
    if (current !== "") current = Math.sqrt(parseFloat(current)).toString();
    update();
}

function inverse() {
    if (current !== "") {
        let val = parseFloat(current);
        current = val === 0 ? "Error" : (1/val).toString();
    }
    update();
}

function update() {
    document.getElementById("display").value = current || "0";
}
