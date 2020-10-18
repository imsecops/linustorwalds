$("#intro").on('ended', function() {
    $("#authX").removeClass('d-none');
    $("#intro").addClass('d-none');
});

$("#playbutton").click(function()
    {
        $("#intro").removeClass('d-none');
        $("#consent").addClass('d-none');
        $("video").get(0).play();
    }
)

$("#skipbutton").click(function()
    {
        $("#consent").addClass('d-none');
        $("#authX").removeClass('d-none');
    }
)
