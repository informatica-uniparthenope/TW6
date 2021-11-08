
let currentOperator="NOP"
let currentOperand=NaN

function calc_init() {
    console.log("calc_init")
    let display=document.getElementById("display")
    display.innerText="0"
}

function calc_keyNumPressed(numPressed) {

    let display=document.getElementById("display")

    if (display.innerText=='0') {
        display.innerText=numPressed
    } else {
        display.innerText = display.innerText + numPressed
    }

    console.log("calc_keyNumPressed: "+numPressed+" displayValue:"+display.innerText+" currentOperator:"+currentOperator+" currentOperand:"+currentOperand)
}

function calc_keyOpePressed(ope) {
    currentOperator=ope

    let display=document.getElementById("display")
    let displayValue=parseInt(display.innerText,16)
    currentOperand=displayValue
    display.innerText="0"
}

function calc_keyCalcPressed() {
    let display=document.getElementById("display")
    let displayValue=parseInt(display.innerText,16)
    let result=NaN

    switch (currentOperator) {
        case "ADD":
            result=currentOperand+displayValue
            break
        case "SUB":
            result=currentOperand-displayValue
            break
        case "MUL":
            result=currentOperand*displayValue
            break
        case "DIV":
            result=currentOperand/displayValue
            break
        default:
            result=displayValue
    }

    if (result != NaN) {
        currentOperand=result
        currentOperator="NOP"
        display.innerText=currentOperand.toString(16)
    }
}

function isDotPresent() {
    let result=false
    let display=document.getElementById("display")
    if (display.innerText.indexOf(".")>=0) {
        result=true
    }
    return result
}

function calc_keyDotPressed() {

    if (!isDotPresent()) {
        let display=document.getElementById("display")
        display.innerText=display.innerText+"."
    }
}
