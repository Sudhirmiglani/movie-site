        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });

        // on page load, fetch movies from the backend,
        // using this endpoint
        // on success, render the data
        $.getJSON("/api/v1/movie", function(result){
            var movieContent = '<div>';
            // this function loops through the array
            $.each(result, function(index, movie){
                movieContent += '<div class="movie-container col-md-6 col-lg-3 movie-tile text-center" data-trailer-youtube-id="' + movie.youtube_link + '" data-toggle="modal" data-target="#trailer">'+
                                    '<img class="image" src="'+movie.image+'" width="220" height="342">'+
                                    '<h2>'+ movie.title + '</h2>'+
                                '</div>';
            });
            movieContent +='</div>';
            // first empty the existing dom, and then append the new data
            $('#movie-wrapper').empty().append(movieContent);
        });

        });