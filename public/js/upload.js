String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}
$(document).ready(function() {
	hideLoading();
	var formdata = false, imgName;

	function showUploadedItem (source) {
		addImg({ 'src': source, 'id': imgName, 'class': 'img-instapy', 'data-filter-name': 'Original'}, true)
	}   

	if (window.FormData) {
  		formdata = new FormData();
  		$("#btn-submit").hide();
	}
	
 	$('input').on('change', function(){
 		$('.jumbotron').slideUp('slow');
 		showLoading();
 		var i = 0, len = this.files.length, img, reader, file;
 		if(len > 0){
			for ( ; i < len; i++ ) {
				file = this.files[i];
				imgName = file.name;
				if (!!file.type.match(/image.*/)) {
					if ( window.FileReader ) {
						reader = new FileReader();
						reader.onloadend = function (e) {
							showUploadedItem(e.target.result);
						};
						reader.readAsDataURL(file);
					}
					if (formdata) {
						formdata.append("data", file);
					}
				}	
			}
		
			if (formdata) {
				formdata.append('filter', $('#filter-select').val());
				$.ajax({
					url: "/upload",
					type: "POST",
					data: formdata,
					processData: false,
					contentType: false,
					success: function (data) {
						//addImg({ 'src': data.filtered, 'id': data.filtered.substring(26), 'class': 'img-instapy'});
						addFilters(data.available_filters);
						hideLoading();
					},
					error: function (data) {
						$('#img-container').html('Server Error');
						hideLoading();
					}
				});
			}
		}
	});
	
	// Upload new image
	$('#img-new').on('click', function(){
		newImg();
	});
	
	// Change image
	$('#img-list').on('click', '.img-instapy', function(){
		changeImg($(this));
	});
	
	// Adds image to img list and if 'show' == true shows image
	function addImg(props, show)
	{
		show = (typeof show === "undefined") ? false : show;
		
		$('#img-new').removeClass('hide');
		$('#img-new').prop('disabled', false);
		
		var labelText = props['data-filter-name'];
		
		var div = $('<div />', {'class': 'img-thumbnail'});
		var img = $('<img />', props);
		var label = $('<p />', {'class': 'img-label'}).text(labelText.capitalize());
		
		img.appendTo(div);
		label.appendTo(div);
		div.appendTo('#img-list');
		console.log(div);
		if (show){
			$('#img-container').empty();
			delete props['id'];
			$('<img />', props).appendTo('#img-container');
		}
		$('#img-container').fadeIn();
	}
	
	function addFilters(filterList)
	{
		for(var i = 0; i < filterList.length; i++){
			filter = filterList[i];
			$.ajax({
				url: '/filter/' + imgName + '/' + filter,
				type: 'GET',
				success: function (data) {
					addImg({ 'src': data.src, 'id': data.src.substring(26), 'class': 'img-instapy', 'data-filter-name': data.filter});
				},
				error: function (data) {
					$('#img-container').html('Server Error');
				}
			});
		}
	}
	
	function newImg()
	{
		$('#img-new').prop('disabled', true);
		$('#img-list').empty();
		$('#img-container').fadeOut();
		$('.jumbotron').slideDown('slow');
	}
	
	function changeImg(img)
	{
		$('#img-container').empty();
		var new_img = img.clone().removeProp('id').appendTo("#img-container");
	}
	
	function showLoading()
	{
		$('#loading-gif').show();
	}
	function hideLoading()
	{
		$('#loading-gif').hide();
	}
});