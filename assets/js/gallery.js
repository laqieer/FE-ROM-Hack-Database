fetch('assets/data/ROMs.json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    appendData(data);
    filterSelection("all");
  })
  .catch(function (err) {
    console.log(err);
  });

function appendData(data) {
  var mainContainer = document.getElementById("roms");
  for (var i = 0; i < data.length; i++) {
    var div = document.createElement("div");
    div.className = 'column ' + data[i].Language;
    var author = data[i].Source
    if(data[i].Index < 20) {
      author = data[i].Publisher
    }
    div.innerHTML = '<div class="content"><img src="OfflineList/imgs/laqieer - Fire Emblem - Game Boy Advance/1-500/' + data[i].Index + 'a.png" alt="Screenshot" style="width:100%"><h4>' + data[i].Title + '</h4><p>' + author + '</p></div>';
    mainContainer.appendChild(div);
  }
}

function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("column");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);     
    }
  }
  element.className = arr1.join(" ");
}


// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("myBtn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}