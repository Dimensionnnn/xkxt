function ajaxload() {
    $('.bigblack').show();
    $.ajax({
        url: '/login',
        cache: true,
        async: false,
        success: function(html) {
            $('#loginbox').html(html);
        }
    });
    $('#loginbox').fadeIn();
    var btn2 = document.getElementById('close');

    btn2.addEventListener('click', close, false);
    $('#loginsubmit').attr('onclick', 'sendtheuser()');
    getvcode();
}

var getdvcode = '';

function getvcode() {
    var params = { 1: 1 };
    $.ajax({
        url: 'http://39.107.229.211:5003',
        type: 'post',
        data: params,
        contenttype: 'multipart/form-data',
        success: function(resp) {
            getdvcode = resp.code;
            var newBase = encodeURI(resp.pic);
            $('#vcode').attr('src', 'data:image/png;base64,' + newBase);
            document.getElementById('inputcode').value = '';
        }
    });
}

function close() {
    $('.bigblack').hide();
    $('#loginbox').fadeOut();
}

function sendtheuser() {
    var logn = $('#logn').val();
    var pswd = $('#pswd').val();
    var params = {
        'logn': logn,
        'pswd': pswd,
    }
    $.ajax({
        url: '/login/in',
        type: 'post',
        data: JSON.stringify(params),
        contentType: 'application/json',
        success: function(resp) {
            if (resp.errno == 'notok') {
                $('#login-sms-code-err').html(resp.errmsg);
            } else {
                location.reload();
            }

        }
    })
}