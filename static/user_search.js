$(document).ready(function(){
    console.log("Loading User Search Typeahead.");
    $.typeahead({
        input: '#search-bar',
        template: function(query, item) {
            return '<span>{{fname}} {{lname}}  -- {{username}} ({{total_articles}})</span>'
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