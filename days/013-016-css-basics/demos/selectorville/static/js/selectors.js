$(document).ready(function () {
    $("#search_button").click(function (e) {
        e.preventDefault()

        var selector_text = $("#search_entry").val();
        $(".selected").removeClass("selected");


        console.log(selector_text);
        $(selector_text).each(function (i, e) {
            $(e).addClass('selected')
        })

        return false
    })
})