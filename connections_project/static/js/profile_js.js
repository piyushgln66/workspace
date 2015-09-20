function ajaxCall() {
	var id = $("#idBox").val();
	$.ajax({
    url: '/connections/fetch/',
    type: 'get', //this is the default though, you don't actually need to always mention it
    data: {id:id},
    success: function(data) {
        $("#content").html(data);
    },
    failure: function(data) { 
        alert('Got an error dude');
    }
});
}


function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}
