// Ejecuta la creación de las tablas y las mallas de las letras
function crearLetras(){
  // Obtenemos los numeros a trabajar
  nLetras = Number(document.getElementById("nLetras").value);
  nVariantes = Number(document.getElementById("nVariantes").value);

  // validamos los numeros
  if(nLetras <= 0 || nVariantes <= 0){
    alert("Ingrese valores mayores iguales a cero");
  }else {
    eliminarLetras();
    tableCreate(nVariantes, nLetras);
    crearX(nLetras, nVariantes);
    crearY(nLetras, nVariantes);
  }
}

// Elimina las tablas
function eliminarLetras(){
  var main = document.getElementById('main');
  main.innerHTML = '';

  var outX = document.getElementById('outX');
  outX.innerHTML = '';

  var outY = document.getElementById('outY');
  outY.innerHTML = '';
}

// Crea la tabla que contendra las letras
function tableCreate(filas, columnas){
    var main = document.getElementById('main');
    var tbl  = document.createElement('table');
    tbl.style.border = '1px solid black';

    // Cremos las filas
    for(var i = 0; i < filas; i++){
        var tr = tbl.insertRow();

        // Creamos las columnas
        for(var j = 0; j < columnas; j++){

          // Creamos las celdas
          var td = tr.insertCell();

          // Creamos la malla para la letra correspondiente
          // y la metemos a la celda
          var malla = crearMalla(columnas, filas);
          td.appendChild(malla);
        }
    }

    // Añadimos la tabla a la pagina
    main.appendChild( document.createElement('br') );
    main.appendChild(tbl);
}

// Crea la malla para una letra
function crearMalla(nLetras, nVariantes){
  var tbl  = document.createElement('table');
  tbl.style.border = '1px solid black';

  // Creamos las filas
  for(var i = 0; i < 8; i++){
      var tr = tbl.insertRow();

      // Creamos las columnas
      for(var j = 0; j < 8; j++){
        // Creamos la celda
        var td = tr.insertCell();

        // Creamos el checkbox
        var check = document.createElement("INPUT");
        check.setAttribute("type", "checkbox");

        // Le asignamos una función para cuando se interactua con él
        check.addEventListener("change", function (){
            crearX(nLetras, nVariantes);
          }
        );
        // Añadimos el check en la celda
        td.appendChild( check );
      }
  }
  // Regresamos la malla
  return tbl;
}

// Creamos el contenido de la salida Y, las etiquetas
function crearX(nLetras, nVariantes){
  //alert(me.checked);
  var filas = Number(nLetras * nVariantes);
  var columnas = nLetras;

  // Hay que recorrer la mtriz de mallas
  var checks = document.getElementById('main').getElementsByTagName('input');

  // Creamos la entrada
  var str = 'X = [';

  // Esta es filas = nLetras*nVariantes
  // y columnas = 8x8 = 64
  var cont = 0;
  for(var i = 0; i < checks.length; i++){
    if(cont == 0){
      str += '<br>['
    }
    if(checks[i].checked){
      str += '1,';
    } else {
      str += '0,';
    }
    cont++;
    if(cont >= 64){
      cont = 0;
      str = str.slice(0, -1);
      str += '],'
    }
  }

  str = str.slice(0, -1);
  str += '<br>]';

  document.getElementById('outX').innerHTML = str;
}

// Creamos el contenido de la salida Y, las etiquetas
function crearY(nLetras, nVariantes){
  var filas = Number(nLetras * nVariantes);
  var columnas = nLetras;

  // Creamos la salida
  var str = 'Y = [';

  // Esta es nVariantes veces una matriz diagonal de unos de nLetrasxnLetras
  for(var i = 0; i < nVariantes; i++){
    for(var j = 0; j < nLetras; j++){
      str += '<br>['
      for(var k = 0; k < nLetras; k++){
        if(k == j){
          str += '1';
        }else {
          str += '0';
        }
        str += ','
      }
      str = str.slice(0, -1);
      str += '],'
    }
  }

  str = str.slice(0, -1);
  str += '<br>]';

  document.getElementById('outY').innerHTML = str;
}
