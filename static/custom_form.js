$(document).ready(function(){
    
    // MVP - search engine component
    $("#country_selector").change(function(e){
        e.preventDefault();
        console.log("country changed")
        //let query = url + query -> news output
        let country = $("#country_selector").val();
        let url = ('/api/newsapi/top?country='+country)
  
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
              }
              
            },
            // if user encounters an error during keyword search
            error: function(){
                let internetFailure = `
                <div class="col-md-12">
                  <p class="text-xs-center">Please check your internet connection and try again.</p>
                </div>`;

              $("#newsResults").html(internetFailure);
            }
            
            
          });
        // if user doesn't enter any keyword  
        }else{
          let missingVal = `<div style="font-size:34px; text-align:center; margin-top:40px;">Please enter any search term in the search engine</div>`;
          $("#newsResults").html(missingVal);
        }
        
      });
      
  });