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