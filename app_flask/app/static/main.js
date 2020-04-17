// source code header

// initialize
initialize = function(){
    console.log("initialize.")
};

$(document).ready(function(){
    initialize();
    console.log(test_var);


    // leaflet
    var map = L.map('map').setView([35.65, 139.7], 15);

    //L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    //    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    //}).addTo(map);

    L.marker([35.66, 139.75]).addTo(map)
        .bindPopup('A pretty CSS3 popup.<br> Easily customizable.');
        //.openPopup();

    // http://ktgis.net/service/leafletlearn/index.html
    //地理院地図の標準地図タイル
    var gsi =L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png', 
      {attribution: "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>"});
    //地理院地図の淡色地図タイル
    var gsipale = L.tileLayer('http://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
      {attribution: "<a href='http://portal.cyberjapan.jp/help/termsofuse.html' target='_blank'>地理院タイル</a>"});
    //オープンストリートマップのタイル
    var osm = L.tileLayer('http://tile.openstreetmap.jp/{z}/{x}/{y}.png',
      {  attribution: "<a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors" });
    //baseMapsオブジェクトのプロパティに3つのタイルを設定
    var baseMaps = {
      "地理院地図" : gsi,
      "淡色地図" : gsipale,
      "OpenStreetMap" : osm.addTo(map)  // 1つだけaddToしておくとデフォルト表示になる
    };
    //layersコントロールにbaseMapsオブジェクトを設定して地図に追加
    //コントロール内にプロパティ名が表示される
    //L.control.layers(baseMaps).addTo(map);

    // ToDo 検討事項： https://github.com/mapbox/mapbox-gl-leaflet

    // mapbox 
    // https://stackoverflow.com/questions/37166172/mapbox-tiles-and-leafletjs
    //var mapboxUrl = "https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}"
    var mapboxUrl = "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}";

    var attribution_mapbox = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
    // https://docs.mapbox.com/jp/mapbox-gl-js/example/setstyle/
    var light_v10 = L.tileLayer(mapboxUrl, {id: 'mapbox/light-v10', attribution: attribution_mapbox, maxZoom: 20, accessToken: accessToken});
    var dark_v10 = L.tileLayer(mapboxUrl, {id: 'mapbox/dark-v10', attribution: attribution_mapbox, maxZoom: 20, accessToken: accessToken});
    var outdoors_v11 = L.tileLayer(mapboxUrl, {id: 'mapbox/outdoors-v11', attribution: attribution_mapbox, maxZoom: 20, accessToken: accessToken});
    var satellite_v9 = L.tileLayer(mapboxUrl, {id: 'mapbox/satellite-v9', attribution: attribution_mapbox, maxZoom: 20, accessToken: accessToken});
    var bright_v8 = L.tileLayer(mapboxUrl, {id: 'mapbox/bright-v8', attribution: attribution_mapbox, maxZoom: 20, accessToken: accessToken});
    var streets = L.tileLayer(mapboxUrl, {id: 'mapbox/streets-v11', attribution: attribution_mapbox, maxZoom: 20, accessToken: accessToken});

    var mapboxMaps = {
        "light_v10": light_v10,
        "dark_v10": dark_v10,
        "outdoors_v11": outdoors_v11,
        "satellite_v9": satellite_v9,
        "bright_v8": bright_v8,
        "streets": streets
    };
    var maps = Object.assign(baseMaps, mapboxMaps);

    L.control.layers(maps).addTo(map);

    L.control.scale().addTo(map);
	
	    // event test
    var myLines = [{
        "type": "LineString",
        "coordinates": [[138, 34.5], [139, 35.5], [140, 35]]
    }, {
        "type": "LineString",
        "coordinates": [[-105, 40], [-110, 45], [-115, 55]]
    }];
    var myStyle = {
        "color": "#ff7800",
        "weight": 5,
        "opacity": 0.65
    };
    var myLines_Geo = L.geoJSON(myLines, {
        style: myStyle
    }).addTo(map);
    myLines_Geo.on('click', function(){
      console.log("LineString clicked.");
      map.setZoom(map.getZoom() - 0.25)   // TMP for DEBUG
      console.log(map.getZoom());         // TMP for DEBUG
    });


    var latlngs = [[34.5, 138.3], [35.5, 139.3], [35, 140.3]];
    var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
    polyline.on('mouseover', function(){
      console.log("mouseover");
    }).on('mouseout', function(){
      console.log("mouseout");
      console.log(map.getZoom());   // TMP for DEBUG
    });

    /*  https://leafletjs.com/examples/quick-start/
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
    */


});
