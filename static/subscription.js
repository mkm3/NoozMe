//subscribe and unsubscribe component
$(document).ready(function(){

    $('#subscribe').on('submit', (evt) => {

        //test
        console.log(evt.target)

        evt.preventDefault();
        const formInputs ={
            'profile_user_id' : evt.target[0].value
        };
    
        $.post('/api/toggle-subscribe', formInputs, (res) => {
            alert(res)
            if ($('#subscribe_btn').text() == 'SUBSCRIBE') {
                $('#subscribe_btn').text('UNSUBSCRIBE');
            } else {
                $('#subscribe_btn').text('SUBSCRIBE');
            }
        });

    })
});

