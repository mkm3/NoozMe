const { uniqueSort } = require("jquery");

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
            <button><a href="${news[i].news_url}" class="btn">Read more</a></button>`;


    if (news[i].note != undefined) {
        output +=`
        <p>${user.fname} thought this article was <b>${news[i].note}</b>.</p>
        `
    }

    //handles remove button - remove shows when article has a saved_news_id
    if (news[i].origin === "saved") { // implies the article has been `saved to the database
        output +=`
        <form class="remove-article-form">
            <input type="hidden" name="saved_news_id" value="${news[i].saved_news_id}">
            <button>Remove Article</button>
        </form>
        `

    } else {
        output +=`
            <button data-toggle="modal" data-target="#modalSaveArticle"
                                        data-origin="${news[i].origin}"
                                        data-title="${news[i].title}"
                                        data-image="${news[i].image}"
                                        data-description="${news[i].description}"
                                        data-content="${news[i].description}"
                                        data-pub_date="${news[i].pub_date}"
                                        data-news_url="${news[i].news_url}"
                                        data-article_id="${news[i].article_id}"
                                        >Save Article</button>
                                        `;
    }

    //closes the div
    output += `</div>`;

    }
    
    if (output !== ""){
        $("#newsResults").html(output);


        $('#modalSaveArticle').on('show.bs.modal', function (event) {
            const button = $(event.relatedTarget)
            console.log(button.data())
            var modal = $(this)
            modal.find('#save-article-btn').on("click", function (evt) {
                evt.preventDefault();
                console.log('save-article-btn clicked')
                article_data = button.data()
                const formInputs = {
                    'title': article_data.title,
                    'image': article_data.image,
                    'description': article_data.description,
                    'content': article_data.content,
                    'pub_date': article_data.pub_date,
                    'news_url': article_data.news_url,
                    'note' : modal.find('#phrase_selector').val()
                };
    
                console.log(formInputs)

                $.post('/save-article', formInputs, (res) => {
                    modal('hide');
                });
            });
        });


        $('.remove-article-form').on('submit', (evt) => {
            evt.preventDefault();
            const formInputs = {
            'saved_news_id': evt.target[0].value,
            };

            $.post('/remove-article', formInputs, (res) => {
                alert(res)
                location.reload(true);
            });
        });
    
    } else {
        let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
        $("#newsResults").html(noNews);
    }  


    // // Rating function - to show article notes by user
    // function getRating() {

    // }

}