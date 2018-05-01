 var main = function () {
"use strict";

$(".worker-input button").on("click", function (event) {
	console.log("Hello, World!");
});
$(".worker-input input").on("keypress", function (event) {
	if (event.keyCode === 13) {
		var worker_login;
		worker_login = $(".worker-input input").val();
		console.log(worker_login);
		// $(".worker-input input").val("");
		$.get("/api/get_worker_position/", {"login":worker_login}, function (response) {
		// этот обратный вызов выполняется при ответе сервера
			console.log("Мы отправили данные и получили ответ сервера!");
			console.log(response);
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