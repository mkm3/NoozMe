//Functions to run search engine and custom form
$(document).ready(function(){
  
  // MVP - custom form component
  let find_and_populate_top_headlines = function() {

    let country = $("#country_selector").val();
    let category = $("#category_selector").val();
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

  //passed in news result from the server and renders output
  let renderNews = function(news) {

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

          <form class="save-article-form">
            <input type="hidden" name="title" value="${latestNews[i].title}">
            <input type="hidden" name="urlToImage" value="${latestNews[i].urlToImage}">
            <input type="hidden" name="description" value="${latestNews[i].description}">
            <input type="hidden" name="content" value="${latestNews[i].content}">
            <input type="hidden" name="publishedAt" value="${latestNews[i].publishedAt}">
            <input type="hidden" name="url" value="${latestNews[i].url}">
            <button>Save Article</button>
          </form>
        </div>
        
      `;
    }

      // spits out html output for our div id #newsResults
      if(output !== ""){
        $("#newsResults").html(output);


        //grabs form inputs and submits them to the saved_news tables
        $('.save-article-form').on('submit', (evt) => {
          evt.preventDefault();


          const formInputs = {
            'title': evt.target[0].value,
            'urlToImage': evt.target[1].value,
            'description': evt.target[2].value,
            'content': evt.target[3].value,
            'publishedAt': evt.target[4].value,
            'url': evt.target[5].value
            
          };
        
        console.log(formInputs)

      $.post('/save-article', formInputs, (res) => {
        alert(res);
      });

    });
  }
    //after search, response if no news is available
    else{
      let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
        $("#newsResults").html(noNews);
    }
  }

  // MVP - search engine component
  $("#searchbtn").on("click",function(e){
      e.preventDefault();
      
      //let query = url + query -> news output
      let query = $("#searchquery").val();
      let url = ('/api/newsapi/everything?keyword=' + query)

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
          success: renderNews,


          // if user encounters an error during keyword search (i.e. 404)
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