$('#add_btn').click(function(){
    $("#blogPost").show();
    $('#close_btn').removeClass('displayBtn');
    $('#submit_btn').removeClass('displayBtn');
    $('#add_btn').addClass('displayBtn');
});

$('#close_btn').click(function(){
    $("#blogPost").hide();
   $('#close_btn').addClass('displayBtn');
    $('#submit_btn').addClass('displayBtn');
    $('#add_btn').removeClass('displayBtn');
});

$('#submit_btn').click(function() {

    // var user_post = $('#blogPost');
    // $.ajax({
    //         url: "create_post/", //the view we send to the json to
    //         type: "POST",
    //         data: {
    //                 title:$('#title').val(),
    //                 content:$('#content').val(),
    //                 author:$('#author').val()
    //
    //             },
    //
    //         success: function(json) {
    //             console.log(json);
    //         }
    // })

    $('#close_btn').addClass('displayBtn');
    $('#submit_btn').addClass('displayBtn');
    $('#add_btn').removeClass('displayBtn');
})


