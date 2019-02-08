// noinspection ES6ModulesDependencies

app = new Vue({
    el: '#app',
    data: {
        search_text: null,
        movies: movies_temp.hits
    },
    methods: {
        search: function() {
            let text = this.search_text
            console.log("Would have searched for " + text)
        },
        top_10: function() {
            console.log("Would have loaded top 10")
        }
    }
})
