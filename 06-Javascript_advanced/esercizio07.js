
let pi=3.1415

function areaCircle(radius) {
    return radius*radius*pi
}

function lenCircle(radius) {
    return 2*radius*pi
}

console.log(areaCircle(5), lenCircle(5))

circle = {
    "pi": 3.1415,
    "radius":0,
    "area" : function () { return this.radius*this.radius*this.pi},
    "len" : function () { return 2*this.radius*this.pi}
}

circle.radius=10
console.log(circle.area())

circle["radius"]=5
console.log(circle.area())

// Definizione della funzione
console.log(circle["area"])

let c1 = new circle()
c1.radius=4
console.log(c1.len())
