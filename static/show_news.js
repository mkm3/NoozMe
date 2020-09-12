// // MDB Lightbox Init
// $(function () {
//     $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
// });

function renderNewsCard1(news) {
    let output = "";
    if (news.note != undefined) {
        output +=`
                <figure class="col-md-4">
                    <a class="black-text" href="${news.news_url}"
                    data-size="1600x1067">
                    <img alt="picture" src="${news.image}"
                        class="img-fluid">
                        <div class="row">
                        <br />
                        <div id="newsResults"></div>
                        </div>
                    <h3 class="text-center my-3">"${news.note}"</h3>
                    </a>
                </figure>`
    } else {
        output +=`
            <figure class="col-md-3">
                <a class="black-text" href="${news.news_url}"
                data-size="1600x1067">
                <img alt="picture" src="${news.image}"
                    class="img-fluid">
                    <div class="row">
                    <br />
                    <div id="newsResults"></div>
                    </div>
                <h3 class="text-center my-3" src="${news.news_url}"> Read More </h3>
                </a>
            </figure>`
    };

    //handles remove button - remove shows when article has a saved_news_id
    if (news.origin === "saved") { // implies the article has been `saved to the database
        output +=`
        <button class="remove-article-btn" data-saved_news_id="${news.saved_news_id}">Remove Article</button>
        `
    } else {
        output +=`
            <button data-toggle="modal" data-target="#modalSaveArticle"
                                        data-origin="${news.origin}"
                                        data-title="${news.title}"
                                        data-image="${news.image}"
                                        data-description="${news.description}"
                                        data-content="${news.description}"
                                        data-pub_date="${news.pub_date}"
                                        data-news_url="${news.news_url}"
                                        data-article_id="${news.article_id}"
                                        >Save Article</button>
                                        `;
    }

    //closes the div
    output += `</div>`;  
    return output;
}


function renderNewsCard2(news) {
    let output = "";
    output +=`
            <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
                <div class="card-body">
                <img alt="picture" src="${news.image}"
                    class="img-fluid">
                <p class="card-text">${news.description}</p>
                <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">`

    if (news.origin === "saved") { // implies the article has been `saved to the database
        output +=`<button type="button" class="remove-article-btn btn btn-sm btn-outline-secondary" data-saved_news_id="${news.saved_news_id}">Remove</button>`
    } else {
        output +=`                        
                <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#modalSaveArticle"
                data-origin="${news.origin}"
                data-title="${news.title}"
                data-image="${news.image}"
                data-description="${news.description}"
                data-content="${news.description}"
                data-pub_date="${news.pub_date}"
                data-news_url="${news.news_url}"
                data-article_id="${news.article_id}"
                >Save</button>`
    }

    if (news.note != undefined) {
        output +=`                        
                <a target="_blank" rel="noopener noreferrer" href="${news.news_url}" class="btn btn-sm btn-outline-secondary">Read More</a>
                </div>
                <b><small class="">"${news.note}"</small></b>
                </div>
                </div>
                </div>
                </div>`
    } else {
        output +=`                        
                <a target="_blank" rel="noopener noreferrer" href="${news.news_url}" class="btn btn-sm btn-outline-secondary">Read More</a>
                </div>
                </div>
                </div>
                </div>
                </div>`
    };

    //closes the div
    output += `</div>`;  
    return output;
}





function showNews(news) {
        
    let output = "";
    for(var i in news) {
        output += renderNewsCard2(news[i]);
    }
    
    if (output !== ""){
        $("#newsResults").html(output);


        $('#modalSaveArticle').on('show.bs.modal', function (event) {
            const button = $(event.relatedTarget)
            console.log(button.data())
            var modal = $(this)
            modal.find('#save-article-btn').on("click", function (evt) {
                evt.preventDefault();
                console.log("Saved Button Clicked!");
                article_data = button.data()

                if (article_data.article_id == undefined || article_data.article_id == "undefined") {
                    const formInputs = {
                        'title': article_data.title,
                        'image': article_data.image,
                        'description': article_data.description,
                        'content': article_data.content,
                        'pub_date': article_data.pub_date,
                        'news_url': article_data.news_url,
                        'note' : modal.find('#phrase_selector').val()
                    };

                    $.post('/save-article', formInputs, (res) => {
                        $('#modalSaveArticle').modal('hide');
                    });
                } else {
                    const formInputs = {
                        'article_id' : article_data.article_id,
                        'note' : modal.find('#phrase_selector').val()
                    };
                    
                    $.post('/save-subscribed-article', formInputs, (res) => {
                        $('#modalSaveArticle').modal('hide');
                    });
                }
            });
        });

        $('#modalSaveArticle').on('hide.bs.modal', function (evt) {
            var modal = $(this);
            modal.find('#save-article-btn').off("click");
        });


        $('.remove-article-btn').on('click', (evt) => {
            evt.preventDefault();
            const button = $(evt.target);
            console.log(button.data("saved_news_id"));
            const formInputs = {
                'saved_news_id': button.data("saved_news_id"),
            };

            console.log(formInputs);

            $.post('/remove-article', formInputs, (res) => {
                alert(res)
                location.reload(true);
            });
        });
    
    } else {
        let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
        $("#newsResults").html(noNews);
    }  

}