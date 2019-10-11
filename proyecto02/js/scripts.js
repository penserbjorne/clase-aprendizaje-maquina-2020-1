var main;

function tableCreate(filas, columnas){
    main = document.getElementById('main');
    var tbl  = document.createElement('table');
    tbl.style.border = '1px solid black';

    for(var i = 0; i < filas; i++){
        var tr = tbl.insertRow();
        for(var j = 0; j < columnas; j++){
          var td = tr.insertCell();
          var malla = crearMalla();
          td.appendChild(malla);
        }
    }
    main.appendChild( document.createElement('br') );
    main.appendChild(tbl);
}

function crearMalla(){
  var tbl  = document.createElement('table');
  tbl.style.border = '1px solid black';

  for(var i = 0; i < 8; i++){
      var tr = tbl.insertRow();
      for(var j = 0; j < 8; j++){
        var td = tr.insertCell();

        var check = document.createElement("INPUT");
        check.setAttribute("type", "checkbox");
        check.addEventListener("change", function (){
            cambioCheck(this);
          }
        );
        td.appendChild( check );
      }
  }
  return tbl;
}

function cambioCheck(me){
  //alert(me.checked);
}

function crearLetras(){
  nLetras = Number(document.getElementById("nLetras").value);
  nVariantes = Number(document.getElementById("nVariantes").value);

  if(nLetras <= 0 || nVariantes <= 0){
    alert("Ingrese valores mayores iguales a cero");
  }else {
    eliminarLetras();
    tableCreate(nVariantes, nLetras);
  }
}

function eliminarLetras(){
  main = document.getElementById('main');
  main.innerHTML = '';
}
