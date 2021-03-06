//Functions to run search engine and custom form
$(document).ready(function(){

  // MVP - custom form component
  let find_and_populate_top_headlines = function(category) {

    let url = `/api/newsapi/top?category=${category}`;
      
    $.ajax({
        
      url: url,
      method: "GET",
      dataType: "json",
      
      beforeSend: function(){
        $("#loader").show();
      },
      
      complete: function(){
        $("#loader").hide();
      },
      

      success: showNews,

      // if user encounters an error during keyword search
      error: function(){
        let internetFailure = `
        <div class="col-md-12">
          <p class="text-xs-center">Please check your internet connection and try again.</p>
        </div>`;
        
      $("#newsResults").html(internetFailure);
      }
    });
  };
  
  // MVP - search engine component
  $("#searchbtn").on("click",function(e) {
      e.preventDefault();
      
      //let query = url + query -> news output
      let query = $("#searchquery").val();
      let url = ('/api/newsapi/everything?keyword=' + query)
      console.log(url)

      //if statement to determine loader response, after 'search' click
      if(query !== ""){
        
        $.ajax({
          //passing through news api URL, ajax call, get request
          url: url,
          method: "GET",
          dataType: "json",
          
          //show loader when searching for news
          beforeSend: function(){
            $("#loader").show();
          },
          
          //hide loader once newsResults appears
          complete: function(){
            $("#loader").hide();
          },

          //if ajax call is successful, return json object from the news server
          success: showNews,

          // if user encounters an error during keyword search (i.e. 404)
          error: function(){
            let internetFailure = `
            <div class="col-md-12">
              <p class="text-xs-center">Please check your internet connection and try again.</p>
            </div>`;
            
            $("#newsResults").html(internetFailure);
          }
          
          
        });
      // if user doesn't enter any keyword  
      } else {
        let missingVal = `<div style="font-size:34px; text-align:center; margin-top:40px;">Please enter any search term in the search engine</div>`;
        $("#newsResults").html(missingVal);

      }
      
    });


  $(".category-links").on("click", function(e) {
    e.preventDefault();
    //'this' refers to the element that was clicked
    //we use preventDefault to avoid the link default behavior <a></a>
    find_and_populate_top_headlines($(this).data("value"));
  })

  showNews(preferred_news);

});