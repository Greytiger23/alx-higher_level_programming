$(document).ready(function() {
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json").click(function(data) {
    $("#character").text(data.name);
  });
});
