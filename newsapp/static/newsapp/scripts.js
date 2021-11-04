$(document).ready(function(){
    $("#nav-bar").on("click", "a", function(){
        $("#nav-bar>a").removeClass("selected");
        $(this).addClass("selected");
    });

    $("#add-tab").click(function(){
        $("<a href='#' class='tab' contenteditable='true'>New Tab</a>").insertBefore("#add-tab");
    });

    $(".fa-thumbs-up").data("counter",0);
    $(".fa-thumbs-up").click(function(){
        let myCounter = $(this).data("counter");
        $(this).data("counter", myCounter+1);
        $(this).parent().css("opacity", 1/(myCounter+1));
        $(this).next().text(myCounter+1);
    });
});