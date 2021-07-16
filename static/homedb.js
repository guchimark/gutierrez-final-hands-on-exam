$(document).ready(function() {

    var columnDefs = [
        {
            data: "name",
            title:  "Name"
        },
        {
            data: "url",
            title: "URL"
        },
        {
            data: "category",
            title: "Category"
        },
        {
            data: "description",
            title: "Description"
        },
        {
            data: "fb_url",
            title: "Facebook URL"
        },
    ];

    var remoteURL = 'http://127.0.0.1:5000/api';
    
    myTable = $('#services').DataTable({
        "sPaginationType": "full_numbers",
        ajax: {
            url : remoteURL,
            contentType: 'application/json',
            dataSrc : 'data',
        },
        columns: columnDefs,
        searching: false,
        paging: false, 
        info: false
    });
});