// $("#auth").submit(function (e) {
//     e.preventDefault()
//     $.ajax({
//         type: "POST",
//         url: this+"/login",
//         crossDomain: true,
//         data: new FormData(this),
//         dataType: "json",
//         contentType: 'multipart/form-data',
//         processData: false,
//         contentType: false,
//         success: function(response) {
//             if (response.status == "success") {
//                 alert("We received your submission, thank you!");
//             } else {
//                 alert("An error occured.");
//             }
//         }
//     })
// })