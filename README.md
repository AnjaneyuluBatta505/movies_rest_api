# movies_rest_api
Site: https://moviesapiapp.herokuapp.com

Admin:

    https://moviesapiapp.herokuapp.com/admin/
    username: anji
    password: anji1234

User:

    https://moviesapiapp.herokuapp.com/
    username: naveen
    password: naveen1234


API end points for User

    URI:
    	https://moviesapiapp.herokuapp.com/api/register/
    Request:
        method	:	POST
    	  data    :	{'username': 'username',   'password': 'password'}
    Response:
    	  {'message': 'Registered successfully'}

    URI:
    	https://moviesapiapp.herokuapp.com/api/login/
    Request:
        method	:	POST
    	data    :	{'username': 'username',   'password': 'password'}
    Response:
    	{'token':'81a4c6a7d77cde40bf1456f2a911f45cf99ec643'}

	URI:
    	https://moviesapiapp.herokuapp.com/api/movies/
    Request:
        method	:	GET
    Rquest Headers:
    	{
    		'Authorization': 'Token <token>',
    		'Content-Type': 'application/json'
	    }
    Request Search Parameters:
    	title, rating, genre, popularity, director


API endpoints for Admin

    Headers to be used:
          {
    		'Authorization': 'Token <token>',
    		'Content-Type': 'application/json'
	  }
    URI:
    	https://moviesapiapp.herokuapp.com/api/login/
    Request:
        method	:	POST
    	data    :	{'username': 'username',   'password': 'password'}
    Response:
    	{'token':'81a4c6a7d77cde40bf1456f2a911f45cf99ec643'}

    Genre:
    	URI:
    		https://moviesapiapp.herokuapp.com/api/genre/
    	Request:
    		method	:	GET
    	Response:
    		List of all genre details

    	URI:
    		https://moviesapiapp.herokuapp.com/api/genre/
    	Request:
    		method	:	POST
    		data	: {'title': 'Some Genre'}
    	Response:
    		genre details
	URI:
    		https://moviesapiapp.herokuapp.com/api/genre/{id}/
    	Request:
    		method	:	GET  	
    	Response:
    		genre details

	URI:
    		https://moviesapiapp.herokuapp.com/api/genre/{id}/
    	Request:
    		method	: PUT
    		data	: {'title': 'Some Genre'}
    	
    	Response:
    		genre details

    	URI:
    		https://moviesapiapp.herokuapp.com/api/genre/{id}/
    	Request:
    		method	: PATCH
    		data	: {'title': 'Some Genre'}
    	
    	Response:
    		genre details

    	URI:
    		https://moviesapiapp.herokuapp.com/api/genre/{id}/
    	Request:
    		method	: DELETE
    	Response:
    		Empty response
    Movies:
    	URI:
	    	https://moviesapiapp.herokuapp.com/api/movies/
	    Request:
	        method	:	GET
	    Response:
	    	List of all movies with pagination

	    URI:
	    	https://moviesapiapp.herokuapp.com/api/movies/{id}/
	    Request:
	        method	:	GET
	        id		: id of movie
	    Response:
	    	Movie Details

	    URI:
	    	https://moviesapiapp.herokuapp.com/api/movies/
	    Request:
	        method	:	POST
	        data	: {
	        	'title': 'title',
	        	'rating': 55,
	        	'genre': ['Adventure', 'Action'],
	        	'popularity': 88
        	}
	    Response:
	    	Movie Details

	   	URI:
	    	https://moviesapiapp.herokuapp.com/api/movies/{id}/
	    Request:
	        method	:	PUT
	        url kwargs : id of movie
	        data	: {
	        	'title': 'title',
	        	'rating': 55,
	        	'genre': ['Adventure', 'Action'],
	        	'popularity': 88
        	}
	    Response:
	    	Movie Details

	    URI:
	    	https://moviesapiapp.herokuapp.com/api/movies/{id}/
	    Request:
	        method	:	PATCH
	        url kwargs : id of movie
	        data	: {
	        	'title': 'title',
	        	'rating': 55,
	        	'genre': ['Adventure', 'Action'],
	        	'popularity': 88
        	}
	    Response:
	    	Movie Details

	    URI:
	    	https://moviesapiapp.herokuapp.com/api/movies/{id}/
	    Request:
	        method	:	DELETE
	        url kwargs : id of movie
	    Response:
	    	Movie Details
