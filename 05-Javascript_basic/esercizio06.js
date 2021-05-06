
function showTypes() {
    console.log("pi:", pi,typeof pi)
    console.log("x:",x, typeof x)
    console.log("y:",y, typeof y)
    console.log("name:",name, typeof name)

    let password="pluto"
    console.log("password:", password)
}

let pi=3.14, x,y, name="Pippo"

showTypes()
console.log(password)
console.log("-----------------------------")

pi="3.14"
x=true
y=1.44


showTypes()
