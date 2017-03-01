function getMovieList(){
	var q = document.getElementById('search-value').value;
	
	var url = "https://feature-autocomplete-dormamu.c9users.io/movies/?q="  + q;
	
	$.ajax({
		type: 'GET',
		url: url,
		xhrFields: {
			withCredentials: true
		},
		success: function(response){
			var res = document.getElementById('search-result-container');
			var html = "<ul>";
			for(var i=0;i<response.movie.length;i++){
				var movie_name = response.movie[i];
				html += "<li>";
				html += "<a href='/pharmeasy/movies/coordinates/?search-value="+movie_name+"'>";
				html += movie_name;
				html += "</a>";
				html += "</li>";
			}
			html += "</ul>";
			res.innerHTML = html;
		},

		error: function(e){
			console.log('xhr error: ' + e);
		}
	});
}

$(document).ready(
	function() {
		$("#search-value").on('keypress', function(event){
			getMovieList();
		});
	});