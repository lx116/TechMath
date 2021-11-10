$(document).ready(function ()
{
    var SendBack = {}
    var info
    $('.seleccionar_formula').change(function () {
        info = $(this).val()

        switch (info)
        {
            case 'interLineal':


        }
    })




    $('body').on('click','.calcular',function () {

        var convertToJson = JSON.stringify(SendBack)

        switch (info)
        {
            case 'interLineal':
                $.post("/interpolacionLineal/",{data:convertToJson},function (data){
                    var contendor = $("<h4>El resultado de su operacion es: "+ data.resultado+" </h4>")
                        $(".resultados").append(contendor)
                })
                break

            case 'interNewton':
                $.post("/interpolacionNewton/",{data:convertToJson},function (data){

                })
                break

            case 'interLagrange':
                $.post("/interpolacionLagrange/",{data:convertToJson},function (data){

                })
                break
            case 'interCuadratica':
                $.post("/interpolacionCuadratica/",{data:convertToJson},function (data){

                })
                break
        }
    })
})