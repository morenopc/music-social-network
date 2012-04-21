var regex = /(youtube.com|youtu.be|youtube-nocookie.com)/gi; 
var input = "http://www.youtube.com/watch?v=5Y6HSHwhVlYhttp://youtu.be/5Y6HSHwhVlYhttp://www.youtube.com/embed/5Y6HSHwhVlY?rel=0 frameborder=0https://www.youtube-nocookie.com/v/5Y6HSHwhVlY?version=3&amp;hl=en_US"; 
if(regex.test(input)) {
  var matches = input.match(regex);
  for(var match in matches) {
	alert(matches[match]);
  } 
} else {
  alert("No matches found!");
}
