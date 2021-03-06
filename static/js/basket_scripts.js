jQuery(document).ready(function () {
    $('.basket_list').on('click', 'input[type="number"]', function (event) {
        let target_href = event.target;
        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",
                success: function (data) {
                    $('.basket_list').html(data.result);
                },
            });
        }
        event.preventDefault();
    });
});