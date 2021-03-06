(function(){
  "use strict";

  $(document).ready(function(){

   $('#commentform').on('submit', function(event){
          event.preventDefault();
             console.log("form submitted!")  // sanity check
   }); 

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;     
    }

   function csrfSafeMethod(method) {
               return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
               }

   var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
       beforeSend: function(xhr, settings) {
               if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                           xhr.setRequestHeader("X-CSRFToken", csrftoken);
                                   }
                             }
                }); 

    var $submit = $("#submit");
    var $comment = $("#comment");
    var $list_elements = $("ul.comment-list");
    var post_id = $list_elements.data("post-id"); 
    var nickname = $list_elements.data("nickname");


    $("#class-submit").click(function(){
            $.ajax({
                url: "/api/posts/"+post_id+"/",
                type: "POST",
                data: {
                    "content": $comment.val(),
                    "post": post_id
                },
                success:
                    function(){
                        $list_elements.append(
                                "<li class=\"list-group-item\">"+
                                "<span class=\"text-warning \">"+
                                nickname+
                                "</span>"+
                                "<span>"+
                                $comment.val()+
                                "</span>"+
                                "</li>");
                        $("#comment").val("");
                    }
            })
            .done(function(data, textStatus, jqXHR){
                console.log("Http request suceeded: "+jqXHR.status);
            })
            .fail(function(jqXHR, textStatus, errorThrown){
                console.log("Http request suceeded: "+jqXHR.status);
                console.log(textStatus);
                console.log(errorThrown);
            });
    });


    $.ajax({
            url: "/api/posts/"+post_id,
            type: "GET",
            success: function(comments){
                for (var i=0; i < comments.length; i++){
                    var comment = comments[i];
                    $list_elements.append(
                            "<li class=\"list-group-item\">"+
                            "<span class=\"text-warning\">"+
                            comment.username+
                            "</span>"+
                            "<span>"+
                            comment.content+
                            "</span>"+
                            "</li>");
                }
            }
    });

    var $detail_like_user = $("#detail-like-user"); 
    function load_like_user(){
        $.ajax({
                url: "/api/like/"+post_id,
                type: "GET",
                success: function(post){
                    if(post.like_user_set.length>5){
                        $detail_like_user.append(
                                    "<span class=\"detail-user-name\">"+
                                    post.like_user_set.length+
                                    "명이 이 포스트를 좋아합니다"+
                                    "</span>"
                                    );
                    }
                    else{
                        for (var i=0; i < post.like_user_set.length;i++){
                            var like_user = post.like_user_set[i];
                            $detail_like_user.append(
                                    "<a href=\""+
                                    "/"+
                                    "profile/"+
                                    like_user.id+
                                    "\">"+ 
                                    "<span class=\"detail-user-name\">"+
                                    like_user.nickname+
                                    "</span>"+
                                    "</a>"
                                    )
                        }
                    }
                }
        });
    }

    function delete_like_user(){
        $(".detail-user-name").remove()
    }
    load_like_user();

    var $heart = $(".heart");

    $heart.click(function(){
        if($heart.hasClass("fa-heart-o")){
            $.ajax({
                url: "/api/like/"+post_id+"/",
                type: "POST",
                data: {
                    "post": post_id,
                },
                success:
                    function(data){
                        $heart.removeClass("fa-heart-o");
                        $heart.addClass("fa-heart");
                        delete_like_user();
                        load_like_user();
                    }
            })
            .done(function(data, textStatus, jqXHR){
                console.log("Http request suceeded: "+jqXHR.status);
            })
            .fail(function(jqXHR, textStatus, errorThrown){
                console.log("Http request suceeded: "+jqXHR.status);
            });

        }
        else{
            $.ajax({
                url: "/api/like/"+post_id+"/",
                type: "DELETE",
                data: {
                    "post": post_id,
                },
                success:
                    function(data){
                        $heart.removeClass("fa-heart");
                        $heart.addClass("fa-heart-o");
                        delete_like_user();
                        load_like_user();
                    }
            })
            .done(function(data, textStatus, jqXHR){
                console.log("Http request suceeded: "+jqXHR.status);
            })
            .fail(function(jqXHR, textStatus, errorThrown){
                console.log("Http request suceeded: "+jqXHR.status);
            });

            
        }
    });

  });
})();
