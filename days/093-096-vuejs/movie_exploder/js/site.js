// noinspection ES6ModulesDependencies

const base_url = "http://movie_service.talkpython.fm/api/"

app = new Vue({
    el: '#app',
    data: {
        search_text: null,
        movies: movies_temp.hits,
        genres: genres_temp,
        selected_genre: genres_temp[0],
        no_genre: genres_temp[0],
    },
    methods: {
        search: function () {
            let text = this.search_text
            this.load_movies(base_url + "search/" + text)
        },
        top_10: function () {
            console.log("Would have loaded top 10")
        },
        load_genre: function (genre) {
            console.log("Would load " + genre)
        },
        load_movies: function (url) {
            let that = this
            axios.get(url)
                .then(function (response) { // handle success
                    that.movies = response.data.hits
                })
                .catch(function (error) { // handle error
                    console.log("ERROR! " + error);
                })
        }
    }
})
