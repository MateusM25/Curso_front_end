function verificar() {
var num1 = window.document.getElementById('numero1')
var num2 = window.document.getElementById('numero2')
var n1 = Number(num1.value)
var n2 = Number(num2.value)

if (n1 > n2){
    alert("Digitação válida, Obrigado");

} else if (n2 > n1) {
    alert("O segundo número é maior que o primeiro, Por favor digite novamente.");

} else if (n1 == n2){
alert("Os Números são iguais.");}
}
