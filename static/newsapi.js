//Functions to run search engine and custom form
$(document).ready(function(){
  
  // MVP - custom form component
  let find_and_populate_top_headlines = function() {

    let country = $("#country_selector").val();
    console.log(country);
    let category = $("#category_selector").val();
    console.log(category);
    let url = `/api/newsapi/top?country=${country}&category=${category}`;

    
      
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
      
      success: function(news){
        let output = "";
        let latestNews = news.articles;
        
        for(var i in latestNews){
          output +=`
            <div class="col l6 m6 s12">
            <h4>${latestNews[i].title}</h4>
            <img src="${latestNews[i].urlToImage}" class="responsive-img">
            <p>${latestNews[i].description}</p>
            <p>${latestNews[i].content}</p>
            <p>Published on: ${latestNews[i].publishedAt}</p>
            <a href="${latestNews[i].url}" class="btn">Read more</a>
            </div>
          `;

        }
        
        if(output !== ""){
          $("#newsResults").html(output);
            M.toast({
            html: "There you go, nice reading",
            classes: 'green'
          });
          
        }else{
          let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
            $("#newsResults").html(noNews);
          M.toast({
            html: "This news isn't available",
            classes: 'red'
          });
        }  
      },

      // if user encounters an error during keyword search
      error: function(){
          let internetFailure = `
          <div style="font-size:34px; text-align:center; margin-top:40px;">Please check your internet connection and try again.
          <img src="img/internet.png" class="responsive-img">
          </div>`;
          
        $("#newsResults").html(internetFailure);
          M.toast({
            html: "We encountered an error, please try again",
            classes: 'red'
          });
      }
    });
  }


  // MVP - search engine component
  $("#searchbtn").on("click",function(e){
      e.preventDefault();
      
      //let query = url + query -> news output
      let query = $("#searchquery").val();
      let url = ('/api/newsapi/everything?keyword='+query)

      if(query !== ""){
        
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
          
          success: function(news){
            let output = "";
            let latestNews = news.articles;
            
            for(var i in latestNews){
              output +=`
                <div class="col l6 m6 s12">
                <h4>${latestNews[i].title}</h4>
                <img src="${latestNews[i].urlToImage}" class="responsive-img">
                <p>${latestNews[i].description}</p>
                <p>${latestNews[i].content}</p>
                <p>Published on: ${latestNews[i].publishedAt}</p>
                <a href="${latestNews[i].url}" class="btn">Read more</a>
                </div>
              `;
            }
            
            if(output !== ""){
              $("#newsResults").html(output);
               M.toast({
                html: "There you go, nice reading",
                classes: 'green'
              });
              
            }else{
              let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
               $("#newsResults").html(noNews);
              M.toast({
                html: "This news isn't available",
                classes: 'red'
              });
            }
            
          },
          // if user encounters an error during keyword search
          error: function(){
             let internetFailure = `
             <div style="font-size:34px; text-align:center; margin-top:40px;">Please check your internet connection and try again.
             <img src="img/internet.png" class="responsive-img">
             </div>`;
             
            $("#newsResults").html(internetFailure);
             M.toast({
                html: "We encountered an error, please try again",
                classes: 'red'
              });
          }
          
          
        });
      // if user doesn't enter any keyword  
      }else{
        let missingVal = `<div style="font-size:34px; text-align:center; margin-top:40px;">Please enter any search term in the search engine</div>`;
        $("#newsResults").html(missingVal);
         M.toast({
                html: "Please enter something",
                classes: 'red'
              });
      }
      
    });

    //binding the functions for country and category selectors
    $("#country_selector").change(find_and_populate_top_headlines)
    $("#category_selector").change(find_and_populate_top_headlines)
    
});