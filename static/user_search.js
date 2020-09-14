$(document).ready(function(){
    console.log("Loading User Search Typeahead.");
    $.typeahead({
        input: '#search-bar',
        template: function(query, item) {
            return `<div class="type-ahead-results">
                        <span>{{fname}} {{lname}}  - {{username}} ({{total_articles}})</span>
                    </div>`
        },
        display: ["username", "fname", "lname"],
        source: {
            users : {
                href: "/user/{{user_id}}",
                url: "/api/all-users"
            } 
        
        },
        generateOnLoad: true,
        callback: {
            onInit: function (node) {
                console.log('Typeahead Initiated');
            }
        }
    });
});