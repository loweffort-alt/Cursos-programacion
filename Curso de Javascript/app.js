// Tipos de datos
"Hello World" // Es un string por ser una cadena de caracteres
'Hello World' // También es un string

//number
console.log("numbers")
console.log(485)
console.log(47.24)
console.log(-12.5)

console.log("")

//boolean
console.log("boolean")
console.log(true)  //boolean
console.log(false) //boolean 

console.log("")

//array: es la lista de items, lo q en python sería "list, tuples, dict"
console.log("array")
console.log(['Joe', 'Ryan', 'Martha']) //list también va entre corchetes
console.log([1, 7, 6, 4, 9])
console.log([true, false, false, true, false])
/*
object: es lo mismo q el dictionary de python, va entre llaves
sirve para agrupar datos q pertenecen a una misma entidad
  "key": 'value', a diferencia de python, el key va entre comillas (no confundir con un string)
*/
console.log({  
    "username": 'Ryan',
    "score": 70.4,
    "hours": 14,
    "proplayer": true,
    "friends": ['Pancho', 'Susana', 'Alex']
})

console.log({
    "username": 'Joe',
    "score": 41.7,
    "hours": 4.5,
    "proplayer": false,
    "friends": ['Pepe', 'Flor', 'Moti']
})

console.log("")

//VARIABLES
console.log("VARIABLES: ")
//puedes crear variables usando cualquiera de las 2 maneras
var username = "Jhon "; 
let lastname = "Salchichon";

username = "Pepito ";
lastname = "Navaja"

console.log(username + lastname)

// Para crear constantes usamos el comando 'const'
const PI = 3.14159;
// PI = 14; //si inserto esto, crea un error por q estas cambiando una constante
console.log(PI)
/*
la primera letra de una variable tiene q ser una letra, $, _
1username = "Alex" //si inserto esto, me da un error
*/

let $dollar ="la primera letra de tu variable puede ser un '$'"
let _underscore = "también puedes usar el '_'"
let any_letter = "y cualquier letra, NO puedes iniciar con número"

console.log($dollar, _underscore, any_letter)

console.log("")

//OPERADORES
console.log("OPERADORES:")
let numberOne = 47;
let numberTwo = 75;

let result = numberOne + numberTwo;
console.log(result);

var nombre = "Darío Alexander";
var apellido= "Farfán Navarro";
var nombre_completo = nombre + ' ' + apellido //agregas el ' ' para insertar un espacio
console.log(nombre_completo)
// TENER EN CUENTA Q NO PUEDES ESCRIBIR 2 O MÁS VARIABLES CON EL MISMO NOMBRE
let number_one = 40;
let number_two = 25;
let comparative1 = number_one <= number_two
console.log(comparative1)
/*  Ojo, los comparadores q podemos usar son:
Mayor igual : ' >= '
Menor igual : ' <= '
Mayor y menor : ' > ' ; ' < ' 
Diferente : ' != '
Igual : ' == '
*/
let comparative2 = number_one != number_two
console.log(comparative2)


console.log("")


//CONDICIONALES
console.log("CONDICIONALES: ")
let passwordDB = "contraseñapepito"
let input = "no es la contraseña"
let verification = input == passwordDB;
/* lo puedes leer como:
SI  verification  es  true entonces 
    imprime en consola "Muy bien prro..." 
SI NO PASA  entonces
    imprime en consola "xD pringao..."
*/
if (verification == true) {
    console.log("Muy bien prro, contraseña correcta");
} else {
    console.log("xD pringao, la contra es incorrecta");
}

let score = 40;
/* se lee como:
SI score es mayor igual q 30 entonces
    imprime en consola "Amazing"
  SI EL ANTERIOR NO PASA Y score es menor q 15 entonces
    imprime en consola "You are improving"
SI NINGUNO DE ESOS PASA entonces
    imprime en consola "you need to..."
*/
if (score >= 30) {
    console.log("Amazing");
} else if (score > 15) {
    console.log("you are improving")
}

else {
    console.log("you need to follow this tutorial")
}

//USO DEL switch
let typeCard = "fajh Card";
/* consta de 3 partes: switch, case y break. También puedes 
establecer un valor por defecto con 'default'
*/
switch(typeCard) {
    case 'Debit Card':
        console.log("This is a debit card");
        break;
    case 'Credit Card':
        console.log("This is a credit card");
        break;
    default:
        console.log("No Card");
}

console.log("")

//BUCLES O ITERADORES
console.log("BUCLES: WHILE & FOR")
//WHILE
console.log("while")
let count = 13;
/* Se puede leer como
MIENTRAS se cumpla la condición entonces
    imprime por consola 'Hello World';
    conste q la condición va cambiando
*/
while(count > 0) {
    console.log(count);
    count = count - 1
}

let random = 1;
while (random <= 50) {
    console.log('Hasta 50');
    random++;      //poner el '++' es como ponerle random = random + 1
}                  //lo mismo sería con '--', es como ponerle random = random - 1     

console.log("")
//FOR en su mayoría es usado en listas
console.log("for")
let names = ['Ryan', 'Joe', 'Jhon', 'Alex']
console.log(names); //muestra la lista
console.log(names.length); //muestra la cantidad de datos en la lista
console.log(names[2]); //muestra el dato que está en el índice 2
console.log("")
/* Se lee:
para una variable i=0, mientras i < cantidad de datos, conste q i aumentará 1, entonces
    imprime en consola el dato de indice i de la lista names
*/
for (let i = 0; i < names.length; i++) {
    console.log(names[i])
}
console.log("")
//si lo quieres en el orden inverso
for (let i = names.length - 1; i >= 0; i--) {
    console.log(names[i])
}

console.log("")

//FUNCIONES
console.log("FUNCIONES")
/* Se compone por: 
[palabra_clave] nombre_de_la_funcion (aqui_van_los_datos) {
    lo q quieras q tu función ejecute;
}
llamas a la función escribiendo:
nombre_de_la_funcion();
*/
function greeting(){
    console.log('Hello');
}
greeting();

function saludo(name){
    console.log('wenos días ' + name)
}
saludo("Alex");
saludo("Flor");
saludo("Vivi");
saludo("Darío");

function add(n1, n2) {
    console.log(n1 + n2)
}
add(54, 6);
add(7, 4);