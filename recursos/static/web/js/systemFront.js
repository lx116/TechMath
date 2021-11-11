$(document).ready(function ()
{
    var SendBack = {}
    var cantidad_Inputs;
    var z
    var arrayX = []
    var arrayY = []
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
            var contenedorX = $("<label for='x"+i+"'>X"+i+" <input class='inputVarX' type='number' id='x"+i+"'></label>")
            $('.spaceInputsX').append(contenedorX)

            var contenedorY = $("<label for='x"+i+"'>Y"+i+"<input class='inputVarY' type='number' id='y"+i+"'></label>")
            $('.spaceInputsY').append(contenedorY)
        }
    })

    $('body').on('click','.calcular',function () {


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
        $.post("/funcionCentral/",{data:convertToJson},function (data){
            var contendorA = $("<img alt='grahp' class='imgGrahp' src=\"../static/web/img/fig.png\">")
                $(".Lineal").append(contendorA)
            var contendorB = $("<img alt='grahp' class='imgGrahp' src=\"../static/web/img/fig.png\">")
                $(".Lagrange").append(contendorB)
            var contendorC = $("<img alt='grahp' class='imgGrahp' src=\"../static/web/img/fig.png\">")
                $(".Cuadratica").append(contendorC)

        })


    })
})