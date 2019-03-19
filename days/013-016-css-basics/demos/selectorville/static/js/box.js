$(document).ready(function () {
    $("button").click(function () {

        var m = $("#margin").val();
        var p = $("#padding").val();
        var b = $("#border").val();

        $(".inside").css("border-width", b + "px");
        $(".inside").css("padding", p + "px");
        $(".inside").css("margin", m + "px");

        $(".msg").html("The values are set to: <br>" +
            "padding: " + p + "px<br>" +
            "margin: " + m + "px<br>" +
            "border-width" + b + "px<br>");
    });
});