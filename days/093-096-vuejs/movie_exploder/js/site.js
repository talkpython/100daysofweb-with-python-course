// noinspection ES6ModulesDependencies

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
            console.log("Would have searched for " + text)
        },
        top_10: function () {
            console.log("Would have loaded top 10")
        },
        load_genre: function (genre) {
            console.log("Would load " + genre)
        }
    }
})
