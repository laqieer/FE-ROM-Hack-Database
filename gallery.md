<div id="myBtnContainer">
  <button class="myBtn active" onclick="filterSelection('all')"> Show all</button>
  <button class="myBtn" onclick="filterSelection('Japanese')"> Japanese</button>
  <button class="myBtn" onclick="filterSelection('English')"> English</button>
  <button class="myBtn" onclick="filterSelection('Chinese')"> Chinese</button>
  <button class="myBtn" onclick="filterSelection('French')"> French</button>
  <button class="myBtn" onclick="filterSelection('German')"> German</button>
  <button class="myBtn" onclick="filterSelection('Italian')"> Italian</button>
  <button class="myBtn" onclick="filterSelection('Spanish')"> Spanish</button>
</div>

<div class="row fullclick">
{% for rom in site.data.ROMs %}
  <div class="column {{ rom.Language }}">
    <div class="content">
{% assign id = rom.ID | plus: 0 %}
{% if id > 1000 %}
{% assign imgs_dir = "1001-1500" %}
{% elsif id > 500 %}
{% assign imgs_dir = "501-1000" %}
{% else %}
{% assign imgs_dir = "1-500" %}
{% endif %}
      <img src="OfflineList/imgs/laqieer - Fire Emblem - Game Boy Advance/{{ imgs_dir }}/{{ rom.ID }}a.png" alt="Title Screen" style="width:100%">
      <h4>{{ rom.Title }}</h4>
{% if id < 20 %}
      <p>{{ rom.Publisher }}</p>
{% else %}
      <p>{{ rom.Source }}</p>
{% endif %}
{% assign starts_with = rom.Comment | slice: 0,4 %}
{% if starts_with == "http" %}
      <a href="{{ rom.Comment }}"></a>
{% endif %}
    </div>
  </div>
{% endfor %}
</div>

<script src="{{ base.url | prepend: site.url }}/assets/js/gallery.js"></script>
