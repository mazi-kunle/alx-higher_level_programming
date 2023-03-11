$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
	data.results.forEach((i) => $('UL#list_movies').append('<li>' + i.title + '</li>'));
});
