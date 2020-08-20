// $("#findbtn").on("click",function(e){
//     e.preventDefault();
    
//     //let query = url + query -> news output
//     let query = $("#searchquery").val();
//     let url = ('/api/newsapi?keyword='+query)

//     if(query !== ""){
      
//       $.ajax({
        
//         url: url,
//         method: "GET",
//         dataType: "json",
        
//         // output of news content
//         success: function(news){
//           let output = "";
//           let latestNews = news.articles;
          
//           for(var i in latestNews){
//             output +=`
//               <div class="col l6 m6 s12">
//               <h4>${latestNews[i].title}</h4>
//               <img src="${latestNews[i].urlToImage}" class="responsive-img">
//               <p>${latestNews[i].description}</p>
//               <p>${latestNews[i].content}</p>
//               <p>Published ${latestNews[i].publishedAt}</p>
//               <a href="${latestNews[i].url}" class="btn">Read more</a>
//               </div>
//             `;
//           }
          
//         },
//         // if user encounters an error during keyword search
//         error: function(){
//            let internetFailure = `
//            <div style="font-size:34px; text-align:center; margin-top:40px;">Please check your internet connection and try again.
//            <img src="img/internet.png" class="responsive-img">
//            </div>`;
           
//           $("#newsResults").html(internetFailure);
//            M.toast({
//               html: "We encountered an error, please try again",
//               classes: 'red'
//             });
//         }
        
        
//       });
//     // if user doesn't enter any keyword  
//     }else{
//       let missingVal = `<div style="font-size:34px; text-align:center; margin-top:40px;">Please enter any search term in the search engine</div>`;
//       $("#newsResults").html(missingVal);
//        M.toast({
//               html: "Please enter something",
//               classes: 'red'
//             });
//     }
    
//   });
  
// });