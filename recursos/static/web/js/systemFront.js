$(document).ready(function ()
{
    var SendBack = {}
    var cantidad_Inputs;
    var z
    $('.addInputs').keyup(function ()
    {
        cantidad_Inputs = $(this).val()
        console.log(cantidad_Inputs)
    })

    $('.getZ').keyup(function (){
        z = $(this).val()
    })

    $(".a").keyup(function ()
    {
        SendBack['x'+$(this).attr('id')] = $(this).val();
        console.log(SendBack)
    })


    $('body').on('click','.agregar',function ()
    {
        $('.spaceInputsX').empty()
        $('.spaceInputsY').empty()

        for (var i = 0;i <= cantidad_Inputs-1;i++)
        {
            var contenedorX = $("<label for='x"+i+"'>X"+i+": <input class='inputVarX inputVar' type='number' id='x"+i+"'></label>")
            $('.spaceInputsX').append(contenedorX)

            var contenedorY = $("<label for='x"+i+"'>Y"+i+": <input class='inputVarY inputVar' type='number' id='y"+i+"'></label>")
            $('.spaceInputsY').append(contenedorY)
        }
    })

    $('body').on('click','.calcular',function () {


        var arrayX = []
        var arrayY = []
        var aceptado = false

        $(".inputVarX").each(function() {
            arrayX.push($(this).val())

        });
        $(".inputVarY").each(function() {
            arrayY.push($(this).val())
        });

        SendBack['X'] = arrayX
        SendBack['Y'] = arrayY
        SendBack['Z'] = z

        console.log(SendBack)
        var convertToJson = JSON.stringify(SendBack)
        $('#resultado_global').html('')

        $.post("/funcionCentral/",{data:convertToJson},function (data){
            aceptado = data.success

            if(data.success){
                $('#resultado_global').html("<div class=\"resultados_graficos\">\n" +
                    "                <div class=\"titleSpace \">\n" +
                    "                    <h2 class=\"navColorText\">Resultados</h2>\n" +
                    "                </div>\n" +
                    "                <div class=\"row\">\n" +
                    "                    <div class=\"grafica col-6\">\n" +
                    "                        <img alt='resultado_global' src='"+data.imagen+"'>\n" +
                    "                    </div>\n" +
                    "                    <div class=\"col-4 resultados_variables\">\n" +
                    "                        <h5>Interpolacion Lineal: "+data.lineal_resultado+"</h5>\n" +
                    "                        <h5>Interpolacion Cuadratica: "+data.cuadratica+"</h5>\n" +
                    "                        <h5>Interpolacion Lagrange: "+data.lagrange_resultado+"</h5>\n" +
                    "                    </div>\n" +
                    "                </div>\n" +
                    "            </div>")}
            else
                {
                    alert(data.mensaje)
                }
        })

    })

})