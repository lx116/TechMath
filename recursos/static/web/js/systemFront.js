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

    $(".a").keyup(function ()
    {
        SendBack['a'] = $(this).val();
        console.log(SendBack)
    })
    $(".b").keyup(function ()
    {
        SendBack['b'] = $(this).val();
        console.log(SendBack)
    })
    $(".c").keyup(function ()
    {
        SendBack['c'] = $(this).val();
        console.log(SendBack)
    })
    $(".d").keyup(function ()
    {
        SendBack['d'] = $(this).val();
        console.log(SendBack)
    })
    $(".e").keyup(function ()
    {
        SendBack['e'] = $(this).val();
        console.log(SendBack)
    })


    $('body').on('click','.calcular',function () {

        var convertToJson = JSON.stringify(SendBack)

        switch (info)
        {
            case 'interLineal':
                $.post("/interpolacionLineal/",{data:convertToJson},function (data){

                    for (var i = 0; i<data.resultado.length;i++)
                    {

                    var contendor = $("<h4>El resultado de su operacion es: "+ data.resultado[i].ValOne+" </h4>")
                        $(".resultados").append(contendor)
                        }
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