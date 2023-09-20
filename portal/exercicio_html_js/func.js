function verificar() {
var num1 = window.document.getElementById('numero1')
var num2 = window.document.getElementById('numero2')
var n1 = Number(num1.value)
var n2 = Number(num2.value)

if (n1 > n2){
    alert("Digitação valida, Obrigado");

} else if (n2 > n1) {
    alert("o segundo numero é maior que o primeiro, Por favor digite novamente.");

}else {
        ("Os numeros são iguais.");
}
}
