var startTime = new Date().getTime();
window.addEventListener("beforeunload", function(startTime) {
  var endTime = new Date().getTime();
  var timeSpent = endTime - startTime;
  // Send time spent data to Django backend using AJAX
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/log_time_spent/', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({'time_spent': timeSpent}));
});