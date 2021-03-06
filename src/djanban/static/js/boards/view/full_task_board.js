$("document").ready(function(){

    /* Toggle the list of cards of a list */
    $("#full_task_board .list .cards").hide();
    $("#full_task_board #hide-list-cards").hide();
    $("#full_task_board .list .panel-heading").click(function(){
        var $this = $(this);
        var $card_container = $this.siblings(".panel-body.cards");
        if($card_container.data("num_cards") > 0){
            if($card_container.is(":visible")){
                $card_container.slideUp();
            }else{
                $card_container.slideDown();
            }
        }
    });

    // Show/Hide all list cards
    $("#full_task_board .toggle-list-cards").click(function(){
        $("#full_task_board .list .list-heading").each(function(){
            $(this).click();
        });
        if($("#show-list-cards").is(":visible")){
            $("#show-list-cards").hide();
            $("#hide-list-cards").show();
        }else{
            $("#show-list-cards").show();
            $("#hide-list-cards").hide();
        }
    });

    /* Toggle the description of a card */
    $("#full_task_board .list .cards .long_description").hide();
    $("#full_task_board .list .cards .description").click(function(){
        var $this = $(this);
        var $long_description = $this.children(".long_description");
        var $short_description = $this.children(".short_description");
        if($long_description.is(":visible")){
            $long_description.slideUp(function(){
                $short_description.slideDown();
            });
        }else{
            $short_description.slideUp(function(){
                $long_description.slideDown();
            });
        }
    });
});