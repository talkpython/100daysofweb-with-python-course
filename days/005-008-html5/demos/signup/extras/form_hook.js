$(document).ready(function () {

    $("form").submit(function (e) {
        e.preventDefault()

        const $inputs = $('form :input');

        let values = {}
        $inputs.each(function () {
            if (this.name) {
                values[this.name] = $(this).val();
            }
        })

        alert(JSON.stringify(values, null, 2))

        return false
    })
})
