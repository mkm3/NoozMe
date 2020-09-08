
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
            <a href="${news[i].news_url}" class="btn">Read more</a>`;

    //handles remove button - remove shows when article has a saved_news_id
    if (news[i].origin === "saved") { // implies the article has been `saved to the database
        output +=`
        <form class="remove-article-form">
            <input type="hidden" name="saved_news_id" value="${news[i].saved_news_id}">
            <button>Remove Article</button>
        </form>`

    } else {
        if (news[i].origin === "subscription") {
            output +=`
            <form class="save-subscribed-article-form">
            `
        } else {
            output +=`
            <form class="save-article-form">
            `
        }

        output +=`
            <input type="hidden" name="title" value="${news[i].title}">
            <input type="hidden" name="image" value="${news[i].image}">
            <input type="hidden" name="description" value="${news[i].description}">
            <input type="hidden" name="content" value="${news[i].content}">
            <input type="hidden" name="pub_date" value="${news[i].pub_date}">
            <input type="hidden" name="news_url" value="${news[i].news_url}">
            <input type="hidden" name="article_id" value="${news[i].article_id}">
            <button data-toggle="modal" data-target="#modalSaveArticle">Save Article</button>
        </form>`;
    }

    //closes the div
    output += `</div>`;

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

        $('.save-subscribed-article-form').on('submit', (evt) => {
            evt.preventDefault();
            const formInputs ={
                'article_id' : evt.target[6].value
            }
            $.post('/save-subscribed-article', formInputs, (res) => {
                alert(res);
            });
        });


        $('.save-article-form').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget) // Button that triggered the modal
            var recipient = button.data('whatever') // Extract info from data-* attributes
            // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
            // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
            var modal = $(this)
            modal.find('.modal-title').text('New message to ' + recipient)
            modal.find('.modal-body input').val(recipient)
            })


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