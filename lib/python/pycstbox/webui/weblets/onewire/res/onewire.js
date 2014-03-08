var _i18n = {
}

function makeSvcUrl(svcName) {
    var root = document.location.href;
    root = /\/$/.test(root) ? root : root + '/';
    return root + svcName ;
}

$(document).ready(function(){
    $(".status").status();
    $("button").button();
    $("[lang]").localize_html(_lang_);

    function refresh_device_list(dom_elt) {
        $.ajax({
            url: makeSvcUrl('ls'),
            success: function(data){
                dom_elt.empty();
                var devices = data.devices;
                for (var i=0 ; i < devices.length ; i++) {
                    var device = devices[i];
                    var html = $.format(
                        '<tr><td class="device-address">{0}</td><td class="device-type">{1}</td></tr>',
                        device[0], device[1]
                        );
                    dom_elt.append(html);
                }
            }
        });
    }

    refresh_device_list($("table#devices"));

    var scroller_bottom_margin = 290;
    function get_scroller_height() {
        return window.innerHeight - scroller_bottom_margin ;
    }


    var scroller = $("#table-body");
    scroller.height(get_scroller_height());

    $(window).resize(function(){
        scroller.height(get_scroller_height());
    });

});
