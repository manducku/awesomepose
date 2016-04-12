(function(){
  "use strict";

  $(document).ready(function(){
     $(window).scroll(function() { 
			if ($(window).scrollTop() == $(document).height() - $(window).height())
			{ 
				lastPostFunc(); 
			} 
		});  
  });

var page_number = 2; 
var $grid_container = $("#grid");
var $first_grid = $grid_container.children().eq(0);
var $second_grid = $grid_container.children().eq(1);
var $third_grid= $grid_container.children().eq(2);

console.log($first_grid);
console.log($second_grid);
console.log($third_grid);

function lastPostFunc() 
	{ 
     $.ajax({
                url: "/api/posts/?page="+page_number,
                type: "GET",
                error:function(request, status, error){
                    console.log("it`s last page");
                },
                success: function(posts){
                    for (var i=0; i < posts.results.length; i++){
                        var post = posts.results[i];
                        var total_post_num = posts.count
                        if (i%3 == 0){
                            $first_grid.append(
                                    "<div>"+
                                    "<div class=\"thumbnail\">"+
                                    "<img class=\"detail-profile-image\" src="+post.image+">"+
                                    "<div class=\"row\">"+
                                    "<div class=\"caption\">"+
                                    "<div class=\"col-lg-2\">"+
                                    "<img class=\"list-profile-image img-circle\" height=\"50px\" width=\"50px\" data-holder-rendered=\"true\" src=\""+post.profile_image+"\">"+
                                    "</div>"+
                                    "<div class=\"col-lg-10\">"+
                                    "<h4>"+post.title+"</h4>"+
                                    "<h5>"+post.nickname+"</h5>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"
                                    )
                        }
                        else if (i%3 ==1){
                            $second_grid.append(
                                    "<div>"+
                                    "<div class=\"thumbnail\">"+
                                    "<img class=\"detail-profile-image\" src="+post.image+">"+
                                    "<div class=\"row\">"+
                                    "<div class=\"caption\">"+
                                    "<div class=\"col-lg-2\">"+
                                    "<img class=\"list-profile-image img-circle\" height=\"50px\" width=\"50px\" data-holder-rendered=\"true\" src=\""+post.profile_image+"\">"+
                                    "</div>"+
                                    "<div class=\"col-lg-10\">"+
                                    "<h4>"+post.title+"</h4>"+
                                    "<h5>"+post.nickname+"</h5>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"
                                    )
                        }
                        else{
                            $third_grid.append(
                                    "<div>"+
                                    "<div class=\"thumbnail\">"+
                                    "<img class=\"detail-profile-image\" src="+post.image+">"+
                                    "<div class=\"row\">"+
                                    "<div class=\"caption\">"+
                                    "<div class=\"col-lg-2\">"+
                                    "<img class=\"list-profile-image img-circle\" height=\"50px\" width=\"50px\" data-holder-rendered=\"true\" src=\""+post.profile_image+"\">"+
                                    "</div>"+
                                    "<div class=\"col-lg-10\">"+
                                    "<h4>"+post.title+"</h4>"+
                                    "<h5>"+post.nickname+"</h5>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"+
                                    "</div>"
                                    )
                        }
                    }
                            page_number+=1;
                }
            });
	};

})();
