window.addEventListener("load", inicio);
function inicio(){
    document.getElementById("buttonInput").addEventListener("click", getBotResponse);
}

function cut(lista){
    if(lista.includes("-")){

    }
}

function getBotResponse(){
    var rawText = $("#textInput").val();//almacenar lo que ingrese el usuario
    var userHtml='<div class="me visible">'+rawText+'</div>';//variable para imprimir por pantalla lo que ingreso el usuario
    $("#textInput").val("");//cambia el valor del input a vacio porque su valor ya se imprimio
    $("#chatbox").append(userHtml);//añade el elemento al container
    document.getElementById('userInput').scrollIntoView({block:'start',behaviour:'smooth'});//solo para la barra de dezplazamiento
    $.get("/get",{msg:rawText}).done(function(data){//esto es para obtener el response dek main
        if(data.includes("&")){
            link=data.substring(data.indexOf("&")+1);
            data=data.substr(0,data.indexOf("&"));
            var botHtml='<div class="alicia visible">'+data+'</div>';//aqui se almacenara  la respuesta
            $("#chatbox").append(botHtml);//se  imprime la respuesta
            var linkHtml='<p class="alicia">Para mayor información accede al siguiente link: <a href="'+link+'" target ="_blank">'+link+'</a></p>';//esto es  para el link
            $("#chatbox").append(linkHtml)
        }
        else{
            var botHtml='<div class="alicia visible">'+data+'</div>';//aqui se almacenara  la respuesta
            $("#chatbox").append(botHtml);//se  imprime la respuesta
        }

        //a partir de aqui se ddebe llamar al create
        //primera pruba no probada
        $.get("/create",{answer:data}).done(function(lista){
            while(lista.includes("-")){
                final=lista.substr(0,lista.indexOf("-"));//esto hace un recorte de inicio a fin
                lista=lista.substring(lista.indexOf("-")+1);
                var alternative='<button  id="'+final+'" type="button" value="'+final+'" class="btn btn-green" onclick="alternative(id)" >'+final+'</button>'
                $("#chatbox").append(alternative)
                document.getElementById('userInput').scrollIntoView({block:'start', behaviour:'smooth'});
            }
            /*var alternative='<button  id="button" type="button" value="'+lista+'" class="btn btn-green" onclick="alternative()" >'+data+'</button>'
            $("#chatbox").append(alternative)
            document.getElementById('userInput').scrollIntoView({block:'start', behaviour:'smooth'});//solo para la barra de dezplazamiento*/
        })
        //segunfa prueba
        /*$.get("/create",function(data){
            var alternative='<button  id="button" type="button" value="'+data[0]+'" class="btn btn-green" onclick="alternative()" >'+data+'</button>'
            $("#chatbox").append(alternative)
            document.getElementById('userInput').scrollIntoView({block:'start', behaviour:'smooth'});//solo para la barra de dezplazamiento
        })*/
        /*
        var alternative='<button  id="button" type="button" value="'+data+'" class="btn btn-green" onclick="alternative()" >'+data+'</button>'
        $("#chatbox").append(alternative)
        document.getElementById('userInput').scrollIntoView({block:'start', behaviour:'smooth'});//solo para la barra de dezplazamiento*/
    });
}
$("#textInput").keypress(function(e){//si presiona enter 
    if(e.which==13){
        getBotResponse();
    }
});
$("#buttonInput").click(function(){// si hace click en enviar
    getBotResponse();
})



function alternative(text){
    //document.getElementById("header").innerHTML="Nueva bot"; //solo para saber q  entra ala funcion
    //var alternativeValue=document.getElementById("button").value;
    //document.getElementById("textInput").value=alternativeValue;
    document.getElementById("textInput").value=text;
    getBotResponse();
}