<table id="roms" class="table table-bordered table-hover table-condensed">
<thead><tr>
<th>ID</th>
<th>Title</th>
<th>Publisher</th>
<th>Location</th>
<th>Source</th>
<th>Language</th>
<th>CRC32</th>
<th>Comment</th>
</tr></thead>
<tbody>
{% for rom in site.data.ROMs %}
<tr>
{% assign starts_with = rom.Comment | slice: 0,4 %}
<td>{{ rom.ID }}</td>
<td>
{% if starts_with == "http" %}
<a href="{{ rom.Comment }}">
{% endif %}
{{ rom.Title }}
{% if starts_with == "http" %}
</a>
{% endif %}
</td>
<td>{{ rom.Publisher }}</td>
<td>{{ rom.Location }}</td>
<td>{{ rom.Source }}</td>
<td>{{ rom.Language }}</td>
<td>{{ rom.CRC32 }}</td>
{% if starts_with == "http" %}
<td></td>
{% else %}
<td>{{ rom.Comment }}</td>
{% endif %}
</tr>
{% endfor %}
</tbody></table>

<script src="https://unpkg.com/tablefilter@latest/dist/tablefilter/tablefilter.js"></script>

<script src="{{ base.url | prepend: site.url }}/assets/js/filters.js"></script>