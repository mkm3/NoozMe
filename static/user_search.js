$.typeahead({
    input: '.js-typeahead-users',
    order: "desc",
    source: {
        data: [
            //User.query.filter(User.username).all()
            //User.query.filter(User.fname and User.lname).all() 
        ]
    },
    callback: {
        onInit: function (node) {
            console.log('Typeahead Initiated on ' + node.selector);
        }
    }
});