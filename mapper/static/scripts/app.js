 var main = function () {
"use strict";

$(".worker-input button").on("click", function (event) {
		var worker_login = $(".worker-input input").val();
		$.get("/api/get_worker_position/", {"login":worker_login}, function (response) {
				document.write(response);
		});
});
$(".worker-input input").on("keypress", function (event) {
	if (event.keyCode === 13) {
		var worker_login = $(".worker-input input").val();
		$.get("/api/get_worker_position/", {"login":worker_login}, function (response) {
		// этот обратный вызов выполняется при ответе сервера
				// console.log(response);
				// заменяем документ на пришедший от апи ответ
				document.write(response);
			});
	}
});
$(function() {
    $("#worker_search").autocomplete({
      source: "/api/get_worker/",
      select: function (event, ui) { //item selected
        AutoCompleteSelectHandler(event, ui)
      },
      minLength: 3,
    });
  });

  function AutoCompleteSelectHandler(event, ui)
  {
    var selectedObj = encodeURI(ui.item);
  }

};


$(document).ready(main);