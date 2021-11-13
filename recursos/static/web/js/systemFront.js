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
            var contenedorX = $("<label for='x"+i+"'>X"+i+" <input class='inputVarX' type='number' id='x"+i+"'></label>")
            $('.spaceInputsX').append(contenedorX)

            var contenedorY = $("<label for='x"+i+"'>Y"+i+"<input class='inputVarY' type='number' id='y"+i+"'></label>")
            $('.spaceInputsY').append(contenedorY)
        }
    })

    $('body').on('click','.calcular',function () {


        var arrayX = []
        var arrayY = []

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
        $('#resultado').html('')

        $.post("/funcionCentral/",{data:convertToJson},function (data){
            if(data.success){
                $('#resultado').html("<img alt='resultado' src='"+data.imagen+"'>")
                }
            else
                {
                    alert(data.mensaje)
                }
        })

    })

})