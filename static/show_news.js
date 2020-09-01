
    function showNews(news) {
            
        let output = "";
        
        for(var i in news){
        output +=`
            <div class="col l6 m6 s12">
                <h4>${news[i].title}</h4>
                <img src="${news[i].image}" class="responsive-img">
                <p>${news[i].description}</p>
                <p>${news[i].content}</p>
                <p>Published on: ${news[i].pub_date}</p>
                <a href="${news[i].news_url}" class="btn">Read more</a>

            <form class="save-article-form">
                <input type="hidden" name="title" value="${news[i].title}">
                <input type="hidden" name="image" value="${news[i].image}">
                <input type="hidden" name="description" value="${news[i].description}">
                <input type="hidden" name="content" value="${news[i].content}">
                <input type="hidden" name="pub_date" value="${news[i].pub_date}">
                <input type="hidden" name="news_url" value="${news[i].news_url}">
                <button>Save Article</button>
            </form>
            </div>
        `;

        }
        
        if (output !== ""){
        $("#newsResults").html(output);
        
        $('.save-article-form').on('submit', (evt) => {
            evt.preventDefault();
            const formInputs = {
            'title': evt.target[0].value,
            'image': evt.target[1].value,
            'description': evt.target[2].value,
            'content': evt.target[3].value,
            'pub_date': evt.target[4].value,
            'news_url': evt.target[5].value
            };
        
            console.log(formInputs)

            $.post('/save-article', formInputs, (res) => {
            alert(res);
            });
        });
        
        } else {
        let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
            $("#newsResults").html(noNews);
        }  
    }