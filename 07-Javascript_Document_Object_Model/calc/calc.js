
let currentOperator="NOP"
let currentOperand=NaN

function calc_init() {
    console.log("calc_init")
    let display=document.getElementById("display")
    display.innerText="0"
}

function calc_keyNumPressed(numPressed) {


    let display=document.getElementById("display")
    let displayValue=parseFloat(display.innerText)

    if (displayValue==0 && !isDotPresent()) {
        displayValue=numPressed
    } else {
        if (isDotPresent()) {
            let dotPos=display.innerText.indexOf(".")
            let displayValueInt =display.innerText.substr(0,dotPos)

            let displayValueFloat = display.innerText.substr(dotPos+1,display.innerText.length-dotPos-1)

            console.log("displayValueInt:"+displayValueInt)
            console.log("displayValueFloat:"+displayValueFloat)
            displayValueFloat = displayValueFloat * 10 + numPressed
            displayValue = parseFloat(displayValueInt+"."+displayValueFloat)
        } else {
            displayValue = displayValue * 10 + numPressed
        }
    }
    display.innerText=displayValue

    console.log("calc_keyNumPressed: "+numPressed+" displayValue:"+displayValue+" currentOperator:"+currentOperator+" currentOperand:"+currentOperand)
}

function calc_keyOpePressed(ope) {
    currentOperator=ope

    let display=document.getElementById("display")
    let displayValue=parseFloat(display.innerText)
    currentOperand=displayValue
    display.innerText="0"
}

function calc_keyCalcPressed() {
    let display=document.getElementById("display")
    let displayValue=parseFloat(display.innerText)
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
        display.innerText=result
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
