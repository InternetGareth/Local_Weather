function () {

    // Defining variables that need to be available to some functions
    // modified 4/23/2020
    var infoWindow;

    window.onload = function () {

        // Creating a reference to the mapDiv
        var mapDiv = document.getElementById('map');

        // Creating a latLng for the center of the map
        var latlng = new google.maps.LatLng(47.60, -122.7075);

        // Creating an object literal containing the properties 
        // we want to pass to the map  
        var options = {
            center: latlng,
            zoom: 10,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            scalecontrol: true
        };

        // Creating the map of non telemetered gages current and historic
        var map = new google.maps.Map(document.getElementById('map'), options);




        //Attaching click events to the buttons



        //Adding flow gages to the map

        document.getElementById('getValues').onclick = function () {

            infowindow = new google.maps.InfoWindow();

            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.655599, -122.785862),
                map: map,
                title: 'BB--Big Beef Creek near Seabeck',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>BB Kitsap Big Beef Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/BB_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/BBPopUp/BBPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';


                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding a marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5931, -122.837),
                map: map,
                title: 'BU--Upper Big Beef Creek near Camp Union',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/BU_Recorded_Conditions.aspx", "_blank");
            });


            //Adding a marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.661483, -122.682049),
                map: map,
                title: 'CC--Clear Creek Main Stem',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>CC Kitsap Clear Creek Main Stem Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/CC_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/CCPopUp/CCPopUp-001-001.jpg" alt="" height="200" width="200">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding a marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.665075, -122.682536),
                map: map,
                title: 'CCSW--Clear Main @ Silverdale Way',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/CCSW_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.586061, -122.716311),
                map: map,
                title: 'CT--Chico Trib. @ Taylor Road',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>CT Chico Trib @ Taylor Road Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/CT_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/CTPopUp/CTPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.505354, -122.567265),
                map: map,
                title: 'CU--Curley Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>CU Kitsap Curley Creek Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/CU_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/CUPopUp/CUPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.66992, -122.691508),
                map: map,
                title: 'CW--Clear Creek-West Tributary',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>CW Kitsap Clear Creek-West Tributary Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/CW_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/CWPopUp/CWPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.752384, -122.644918),
                map: map,
                title: 'DC--Dogfish Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>DC Kitsap Dogfish Creek Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/DC_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/DCPopUp/DCPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.579805, -122.712196),
                map: map,
                title: 'KC--Kitsap Creek @ Lake Outlet',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/KC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.429222, -122.567544),
                map: map,
                title: 'OL--Olalla Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>OL Kitsap Olalla Creek Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/OL_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/OLPopUp/OLPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.650491, -122.632021),
                map: map,
                title: 'SL--Steele Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>SL Kitsap Steele Creek Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/SL_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/SLPopUp/SLPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.523747, -122.682422),
                map: map,
                title: 'AC--Anderson Creek - Bremerton',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/AC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.638989, -122.666892),
                map: map,
                title: 'BA--Barker Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/BA_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.414426, -122.631395),
                map: map,
                title: 'BC--Burley Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/BC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.502076, -122.647775),
                map: map,
                title: 'BL--Blackjack Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/BL_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.554961, -122.827203),
                map: map,
                title: 'GO--Gold Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/GO_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.884512, -122.573691),
                map: map,
                title: 'HC--Hansville Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/HC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.601172, -122.758669),
                map: map,
                title: 'WC--Wildcat Creek @ Lake Outlet',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/WC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map (inactive sites start here)
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.567091, -122.968115),
                map: map,
                title: 'AN--Anderson Creek - Holly',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/AN_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6675, -122.6817),
                map: map,
                title: 'CE--Clear Creek-East Tributary',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/CE_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5933, -122.7075),
                map: map,
                title: 'CH--Chico Creek-Mainstem',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>CH Kitsap Chico Creek-Mainstem Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/CH_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/CHPopUp/CHPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.58409, -122.715992),
                map: map,
                title: 'DI--Dickerson Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>DI Kitsap Dickerson Creek Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/DI_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/DIPopUp/DIPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4615, -123.0265),
                map: map,
                title: 'DR--Dewatto River',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/DR_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7889, -122.5799),
                map: map,
                title: 'GA--Gamble Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/GA_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.526734, -122.705457),
                map: map,
                title: 'GC--Gorst Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams.png'
            });

            google.maps.event.addListener(marker, 'click', function () {

                var infoWindow = new google.maps.InfoWindow();
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>GC Kitsap Gorst Creek Stream Gage</h2>' +
                '<p>Click below for Stream Gage Page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/GC_CurrentConditions.aspx" target="_blank">Stream gage data page</a></p>' +
                '<img src="streams/Day_Info/GCPopUp/GCPopUp-001-001.jpg" alt="" height="500" width="414">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.780088, -122.556371),
                map: map,
                title: 'GV--Grovers Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/GV_Recorded_Conditions.aspx", "_blank");
            });


            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.531089, -122.715669),
                map: map,
                title: 'HE--Heins Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/HE_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.611257, -122.611743),
                map: map,
                title: 'IL--Illahee Creek, Upper North Fork',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/IL_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5797, -122.7103),
                map: map,
                title: 'KL--Kitsap Lake @ Control',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/KL_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.733502, -122.662861),
                map: map,
                title: 'LJ--Johnson Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/LJ_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4380555556, -122.950277778),
                map: map,
                title: 'LT--Little Tahuya',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });


            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/LT_Recorded_Conditions.aspx", "_blank");
            });
            
            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5441, -122.6117),
                map: map,
                title: 'OC--Karcher Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/OC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.674146, -122.553551),
                map: map,
                title: 'MZ--Manzanita Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/MZ_Recorded_Conditions.aspx", "_blank");
            });
            
            
            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.529178, -122.713903),
                map: map,
                title: 'PA--Parish Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/PA_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.646689, -122.695846),
                map: map,
                title: 'SC--Strawberry Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/SC_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.634864, -122.836073),
                map: map,
                title: 'SE--Seabeck Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/SE_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.628681, -122.837611),
                map: map,
                title: 'SH--Seabeck Creek off Seabeck Holly Hwy',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/SH_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.624442, -122.874691),
                map: map,
                title: 'ST--Stavis Creek',
                icon: 'http://kpudhydrodata.kpud.org/icons/Flow_Field_DL.png'
            });
            
            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/ST_Recorded_Conditions.aspx", "_blank");
            });


            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4375, -122.9531),
                map: map,
                title: 'TR--Tahuya River @ Tahuya',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/TR_Recorded_Conditions.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4641, -122.83),
                map: map,
                title: 'UR--Union River',
                icon: 'http://kpudhydrodata.kpud.org/icons/streams_inactive.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/UR_Recorded_Conditions.aspx", "_blank");
            });


        }

        document.getElementById('getWells').onclick = function () {


            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7007583333333, -122.6274306),
                map: map,
                title: 'AAA001--KPUD KEYPORT PRODUCTION WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA001.aspx", "_blank");
            });


            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.684675, -122.633791666667),
                map: map,
                title: 'AAA002--KPUD KEYPORT PRODUCTION WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA002.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6442694444444, -122.782863888889),
                map: map,
                title: 'AAA005--U.OF WA.SCH.OF FISHERIES BIG BEEF TEST HOLE 2 Upper 8" PERFORATIONS',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AA005.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5576277777778, -122.978816666667),
                map: map,
                title: 'AAA007--HOLLY WATER SYSTEM WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA007.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5555194444444, -122.9804),
                map: map,
                title: 'AAA008--HOLLY WATER SYSTEM WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA008.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7872111111111, -122.506125),
                map: map,
                title: 'AAA011--KPUD N PENINSULA SOUTH KINGSTON TEST WELL - OBS WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA011.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7871527777778, -122.506144444444),
                map: map,
                title: 'AAA012--KPUD N PENINSULA KINGSTON WELL 5',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA012.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7509083333333, -122.514427777778),
                map: map,
                title: 'AAA013--WISE ACRE (ORIGINALLY A PUD WELL CALLED INDIANOLA 5)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA013.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7521416666667, -122.541491666667),
                map: map,
                title: 'AAA014--KPUD INDIANOLA WELL 6',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA014.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8018083333333, -122.566238888889),
                map: map,
                title: 'AAA015--KPUD N PENINSULA GAMBLEWOOD WELL 3 RITTER ROAD',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA015.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8135833333333, -122.574888888889),
                map: map,
                title: 'AAA016--KPUD N PENINSULA GAMBLEWOOD 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA016.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8015888888889, -122.653991666667),
                map: map,
                title: 'AAA103--KPUD VINLAND WS EDGEWATER WELL 4',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA103.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7801472222222, -122.676405555556),
                map: map,
                title: 'AAA104--KPUD VINLAND WS WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA104.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.805525, -122.506841666667),
                map: map,
                title: 'AAA106--KPUD N PENINSULA KINGSTON WELL 4',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA106.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8023861111111, -122.495241666667),
                map: map,
                title: 'AAA107--KPUD N PENINSULA KINGSTON WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA107.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6162083333333, -122.536066666667),
                map: map,
                title: 'AAA108--ISLAND UTILITY COMPANY MONITORING WELL (160 feet)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA108.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6161388888889, -122.536088888889),
                map: map,
                title: 'AAA109--ISLAND UTILITY COMPANY  WELL 1 (SO-1)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA109.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6466416666667, -122.548947222222),
                map: map,
                title: 'AAA110--PRIVATE WELL (FORMERLY KPUD ISLAND CENTER TW)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA110.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6405277777778, -122.575227777778),
                map: map,
                title: 'AAA111--KPUD FLETCHER BAY OBSERVATION WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA111.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6712277777778, -122.545680555556),
                map: map,
                title: 'AAA113--KPUD NORTH BAINBRIDGE WELL 6',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA113.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5962611111111, -122.846538888889),
                map: map,
                title: 'AAA114--KPUD CAMP DAVID WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA114.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.569025, -122.558583333333),
                map: map,
                title: 'AAA120--ANNAPOLIS WD WATAUGA BEACH WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA120.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4050027777778, -122.569266666667),
                map: map,
                title: 'AAA227--WWS ALPINEWOOD WATER SYSTEM WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA227.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4408777777778, -122.721086111111),
                map: map,
                title: 'AAA230--WWS WICKS LAKE 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA230.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8844166666667, -122.574575),
                map: map,
                title: 'AAA231--KPUD N PENINSULA HANSVILLE 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA231.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6389527777778, -122.814305555556),
                map: map,
                title: 'AAA235--KPUD SEABECK TEST WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA235.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4404444444444, -122.637786111111),
                map: map,
                title: 'AAA236--WWS PARKVIEW TERRACE, WOODLAND RANCHE Well',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA236.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6137861111111, -122.503933333333),
                map: map,
                title: 'AAA238--BILL POINT WATER WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA238.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8833861111111, -122.544763888889),
                map: map,
                title: 'AAA304--KPUD YOUNG WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA304.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7561694444444, -122.677747222222),
                map: map,
                title: 'AAA398--NARDO PRIVATE WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA398.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.501475, -122.661655555556),
                map: map,
                title: 'AAA639--BANIGAN PRIVATE WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA639.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8135833333333, -122.574522222222),
                map: map,
                title: 'AAA706--KPUD N PENINSULA GAMBLEWOOD 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA706.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7869555555556, -122.506091666667),
                map: map,
                title: 'AAA707--KPUD N PENINSULA KINGSTON WELL 6',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA707.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7420361111111, -122.554733333333),
                map: map,
                title: 'AAA710--KPUD SUQUAMISH AUGUSTA 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA710.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7169388888889, -122.567919444444),
                map: map,
                title: 'AAA711--KPUD SUQUAMISH BALZOW WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA711.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7327416666667, -122.566988888889),
                map: map,
                title: 'AAA713--KPUD SUQUAMISH PINE ST WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA713.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7456222222222, -122.575308333333),
                map: map,
                title: 'AAA715--KPUD SUQUAMISH WAGGONER WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA715.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7534027777778, -122.569697222222),
                map: map,
                title: 'AAA717--KPUD SUQUAMISH LINCOLN ROAD WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA717.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7295916666667, -122.558002777778),
                map: map,
                title: 'AAA718--KPUD SUQUAMISH SUQUAMISH SHORES WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA718.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7685083333333, -122.486144444444),
                map: map,
                title: 'AAA722--KPUD N PENINSULA JEFFERSON POINT',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA722.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6317666666667, -122.844311111111),
                map: map,
                title: 'AAA875--KPUD BLUE HERON WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA875.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.634475, -122.811444444444),
                map: map,
                title: 'AAA990--KPUD SEABECK PRODUCTION WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAA990.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6303694444444, -122.767597222222),
                map: map,
                title: 'AAB274--WOODLAND HEIGHTS WATER SYSTEM, SHOBERT CONSTRUCTION',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB274.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.804575, -122.494136111111),
                map: map,
                title: 'AAB401--KPUD N PENINSULA KINGSTON WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB401.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7520861111111, -122.525530555556),
                map: map,
                title: 'AAB406--KPUD INDIANOLA WELL 1A',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB406.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7522222222222, -122.524166650772),
                map: map,
                title: 'AAB407--KPUD INDIANOLA WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB407.aspx", "_blank");
            });


            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7540222222222, -122.527566666667),
                map: map,
                title: 'AAB408--ECOLOGY NW, WELL NO.2 IN INDIANOLA. NO KNOWN WELL LOG.',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB408.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7513194444444, -122.537480555556),
                map: map,
                title: 'AAB410--KPUD INDIANOLA WELL 4',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB410.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.733275, -122.567722222222),
                map: map,
                title: 'AAB454--KPUD SUQUAMISH PINE ST DUG WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB454.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6725416666667, -122.549463888889),
                map: map,
                title: 'AAB455--KPUD NORTH BAINBRIDGE WELL 9',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB455.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7704722222222, -122.701869444444),
                map: map,
                title: 'AAB458--KPUD VINLAND WS BELA VISTA WELL 1 DECOMMISSIONED 10/9/03',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB458.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7729472222222, -122.698480555556),
                map: map,
                title: 'AAB459--KPUD VINLAND WS BELA VISTA WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB459.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5692888888889, -122.554055555556),
                map: map,
                title: 'AAB460--US NAVY MANCHESTER FUEL DEPOT USN-5',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB460.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8090166666667, -122.5525),
                map: map,
                title: 'AAB464--WOLFLE ELEM SCHOOL OLD WELL, USED AS A KPUD WATER LEVEL MONITOR',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB464.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6167083333333, -122.723447222222),
                map: map,
                title: 'AAB471--KPUD ELDORADO HILLS WELL 4',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB471.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6159722222222, -122.714688888889),
                map: map,
                title: 'AAB476--KPUD ELDORADO HILLS WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB476.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8032944444444, -122.665102777778),
                map: map,
                title: 'AAB478--KPUD VINLAND WS EDGEWATER WELL 2 REPLACEMENT',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB478.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7608027777778, -122.542608333333),
                map: map,
                title: 'AAB479--KPUD MILLER BAY ESTATES 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB479.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8033027777778, -122.665177777778),
                map: map,
                title: 'AAB526--KPUD VINLAND WS EDGEWATER WELL 2 ORIGINAL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB526.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8301805555556, -122.519908333333),
                map: map,
                title: 'AAB533--KPUD BONSELL WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB533.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6147861111111, -122.840519444444),
                map: map,
                title: 'AAB607--ELLIS TWO PARTY (ORIGINALLY SCOTT)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAB607.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6177638968362, -122.648024992053),
                map: map,
                title: 'AAC006--DICK LINDBERG',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC006.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8765583333333, -122.571266666667),
                map: map,
                title: 'AAC079--KPUD N PENINSULA CLIFFSIDE',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC079.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6733361111111, -122.520630555556),
                map: map,
                title: 'AAC110--KPUD NORTH BAINBRIDGE WELL 10',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC110.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6164972, -122.536261),
                map: map,
                title: 'AAC113--KPUD ISLAND UTILITY WELL 2 (SO-2)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC113.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.80825, -122.515833333333),
                map: map,
                title: 'AAC117--HANSON DUG WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC117.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8034859055556, -122.487839794444),
                map: map,
                title: 'AAC118--HOSEA',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC118.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8070532777778, -122.485624030556),
                map: map,
                title: 'AAC119--DEBRUYN',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC119.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6559055555556, -122.791125),
                map: map,
                title: 'AAC318--DRURY PRIVATE WELL, FORMERLY SCHOLD',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC318.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6847416666667, -122.633716666667),
                map: map,
                title: 'AAC340--KPUD KEYPORT OBSERVATION WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC340.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4837055555556, -122.570288888889),
                map: map,
                title: 'AAC344--KPUD LONG LAKE 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC344.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4835722222222, -122.572925),
                map: map,
                title: 'AAC345--KPUD LONG LAKE 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC345.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6296027777778, -122.755797222222),
                map: map,
                title: 'AAC377--KPUD NEWBERRY HILL WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC377.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8545833333333, -122.6075),
                map: map,
                title: 'AAC403--SALSBURY POINT COUNTY PARK WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC403.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8157555555556, -122.487763888889),
                map: map,
                title: 'AAC532--APPLE TREE POINT PARTNERS WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC532.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6466416666667, -122.812772222222),
                map: map,
                title: 'AAC547--JUNE COLLIER PRIVATE WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC547.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6658333333333, -122.5775),
                map: map,
                title: 'AAC558--BAINBRIDGE ISLAND PARKS BATTLE POINT PARK',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC558.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8085916666667, -122.499655555556),
                map: map,
                title: 'AAC601--KPUD N PENINSULA KINGSTON WELL 7',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC601.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7046083333333, -122.548672222222),
                map: map,
                title: 'AAC606--BLOEDEL RESERVE DEEP WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC606.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6167388888889, -122.782866666667),
                map: map,
                title: 'AAC707--DAVE DOLEN GROUP B WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC707.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8126638888889, -122.503402777778),
                map: map,
                title: 'AAC718--KPUD CEDAR ACRE 5',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC718.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8331805555556, -122.541825),
                map: map,
                title: 'AAC720--KPUD HANSVILLE HWY MUD-ROTARY TEST WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC720.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.704575, -122.548022222222),
                map: map,
                title: 'AAC759--BLOEDEL RESERVE FARM WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC759.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6464416666667, -122.794655555556),
                map: map,
                title: 'AAC799--KPUD SEABECK TEST WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC799.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5976305555556, -122.818638888889),
                map: map,
                title: 'AAC807--KPUD GREEN MOUNTAIN ELEM SCHOOL CK SCH.DIST.',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC807.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6494416666667, -122.789186111111),
                map: map,
                title: 'AAC809--ANDERSON, PREVIOUSLY SMITH',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC809.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4127944444444, -122.553908333333),
                map: map,
                title: 'AAC820--SEBREN',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC820.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4791805555556, -122.529336111111),
                map: map,
                title: 'AAC824--KPUD DRIFTWOOD COVE 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC824.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4459333333333, -122.661027777778),
                map: map,
                title: 'AAC825--CHRISTIAN LIGHTHOUSE WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC825.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6724527777778, -122.549708333333),
                map: map,
                title: 'AAC826--KPUD NORTH BAINBRIDGE WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC826.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6733222222222, -122.520563888889),
                map: map,
                title: 'AAC832--KPUD NORTH BAINBRIDGE WELL 8',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC832.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6377, -122.828691666667),
                map: map,
                title: 'AAC835--SEABECK CONFERENCE CENTER',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC835.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5122916666667, -122.778202777778),
                map: map,
                title: 'AAC839--KPUD UNION RIVER ACRES',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAC839.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8131194444444, -122.593627777778),
                map: map,
                title: 'ABB943--KPUD PORT GAMBLE PRODUCTION WELL POPE RESOURCE PROPERTY',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABB943.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.617133, -122.535725),
                map: map,
                title: 'AAS286--KPUD ISLAND UTILITY WELL 3 (S0-3)',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AAS286.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6291277777778, -122.784844444444),
                map: map,
                title: 'ABC665--MIGUELO WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABC665.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5938888888889, -122.722675),
                map: map,
                title: 'ABE865--KPUD MARLOW WATER SYSTEM CADY WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABE865.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8220277777778, -122.511927777778),
                map: map,
                title: 'ABP505--KPUD N PENINSULA KINGSTON FARM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABP505.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7522305555556, -122.613533333333),
                map: map,
                title: 'ABP540--KPUD GALA PINES WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABP540.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8438583333333, -122.610375),
                map: map,
                title: 'ABP933--KPUD SAVANTE WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABP933.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5103527777778, -122.616536111111),
                map: map,
                title: 'ABV298--KPUD SALMONBERRY MONITOR WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ABV298.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6039138888889, -122.772463888889),
                map: map,
                title: 'ACC503--WILDCAT LAKE COUNTY PARK',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACC503.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7271777777778, -122.595466666667),
                map: map,
                title: 'ACD351--KPUD KEDROS WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD351.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7657611111111, -122.653008333333),
                map: map,
                title: 'ACD352--KPUD POULSBO HEIGHTS 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD352.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4761888888889, -122.605905555556),
                map: map,
                title: 'ACD354--KPUD STRAWBERRY HILL WS',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD354.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6714222222222, -122.709163888889),
                map: map,
                title: 'ACD355--KPUD AVELLANA WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD355.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6206666666667, -122.532163888889),
                map: map,
                title: 'ACD357--KPUD HARBOR CREST',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD357.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7148083333333, -122.610363888889),
                map: map,
                title: 'ACD358--KPUD INDIAN HILLS WS INDIAN HILLS WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD358.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5063138888889, -122.548516666667),
                map: map,
                title: 'ACD373--KPUD MANCHESTER MONITOR WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD373.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7062277777778, -122.602377777778),
                map: map,
                title: 'ACD374--KPUD NESIKA BAY WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD374.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7787805555556, -122.488719444444),
                map: map,
                title: 'ACD385--KPUD N PENINSULA NEWELLHURST WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD385.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7739305555556, -122.512316666667),
                map: map,
                title: 'ACD855--KPUD BIG CORNER WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD855.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6353194444444, -122.758455555556),
                map: map,
                title: 'ACG501--KPUD NEWBERRY HILL WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACG501.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6135611111111, -122.819916666667),
                map: map,
                title: 'ACG504--KPUD BRIDLETREE WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACG504.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7499333333333, -122.690586111111),
                map: map,
                title: 'ACG506--KPUD CLEAR CREEK TEST WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACG506.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6045194444444, -122.544977777778),
                map: map,
                title: 'ACK364--SOUTH BAINBRIDGE WATER SYSTEM WELL 7',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK364.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5744472222222, -122.891122222222),
                map: map,
                title: 'ACK368--KPUD STAVIS CREEK WATER SYSTEM WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK368.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6482194444444, -122.777275),
                map: map,
                title: 'ACK369--KPUD ECHO VALLEY WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK369.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5916805555556, -122.835394444444),
                map: map,
                title: 'ACK371--KPUD KLAHANIE WATER SYSTEM',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK371.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6057111111111, -122.770066666667),
                map: map,
                title: 'ACK372--KPUD AIRPORT PARK WELL 1, SHALLOW WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK372.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6055888888889, -122.770075),
                map: map,
                title: 'ACK373--KPUD AIRPORT PARK WELL 2 DEEP WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK373.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4830527777778, -122.664033333333),
                map: map,
                title: 'ACK457--KPUD NAVY YARD PARK 3 REPLACEMENT FOR WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACK457.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5979222222222, -122.825908333333),
                map: map,
                title: 'ACR352--KPUD FROG POND WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACR352.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5976611111111, -122.826047222222),
                map: map,
                title: 'ACR353--KPUD FROG POND WELL 2_NEW',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACR353.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6009, -122.8264),
                map: map,
                title: 'ACR354--KPUD FROG POND WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACR354.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4761888888889, -122.605905555556),
                map: map,
                title: 'ACD354--KPUD STRAWBERRY HILL WS',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACD354.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5953861111111, -122.836288888889),
                map: map,
                title: 'ACR355--KPUD FROG POND WELL 4',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACR355.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5954305555556, -122.8349),
                map: map,
                title: 'ACR356--KPUD FROG POND WELL 5',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACR356.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6044611111111, -122.545563888889),
                map: map,
                title: 'ACW030--SOUTH BAINBRIDGE WATER CO WELL 8',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ACW030.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7521583333333, -122.541602777778),
                map: map,
                title: 'AEC948--KPUD INDIANOLA WELL 7',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AEC948.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6725, -122.549552777778),
                map: map,
                title: 'AEK852--KPUD NORTH BAINBRIDGE WELL 7',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AEK852.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6732305555556, -122.547541666667),
                map: map,
                title: 'AEK853--KPUD NORTH BAINBRIDGE WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AEK853.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7842444444444, -122.673583333333),
                map: map,
                title: 'AES172--PIONEER HILL WEST COMM. ASSOC.',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AES172.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8482277777778, -122.603375),
                map: map,
                title: 'AES249--PITMAN',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AES249.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7122611111111, -122.61065),
                map: map,
                title: 'AES259--KPUD INDIAN HILLS WS LEMOLO ACRES WELL',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AES259.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6486111111111, -122.842777777778),
                map: map,
                title: 'AES313--KPUD PRIDDY VISTA WS WELL 1',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AES313.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8523, -122.596736111111),
                map: map,
                title: 'AES315--PORT GAMBLE WATER SYSTEM WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AES315.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6134583333333, -122.819708333333),
                map: map,
                title: 'AET413--KPUD BRIDLETREE WELL 2',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AET413.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8016805555555, -122.654133333333),
                map: map,
                title: 'AFC506--KPUD VINLAND WS EDGEWATER WELL 5',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AFC506.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4791333333333, -122.529425),
                map: map,
                title: 'AKR190--KPUD DRIFTWOOD COVE 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/AKR190.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8054277777778, -122.506822222222),
                map: map,
                title: 'ALK129--KPUD N PENINSULA KINGSTON WELL 8',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ALK129.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6132222222222, -122.819722222222),
                map: map,
                title: 'ALK301--KPUD BRIDLETREE WELL 3',
                icon: 'http://kpudhydrodata.kpud.org/icons/wells.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/wells/ALK301.aspx", "_blank");
            });


        }


        //add rain gage markers

        document.getElementById('getRain').onclick = function () {

            //Adding a marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.755115, -122.667651),
                map: map,
                title: '01--Kitsap PUD',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>01 Kitsap PUD Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/1_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/01_Day_Info/01_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);

            });


            //Adding a marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7563888888889, -122.549722222222),
                map: map,
                title: '03--Indianola - Miller Bay',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/03_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.77, -122.641666666667),
                map: map,
                title: '04--City of Poulsbo - Big Valley Well Site',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/04_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6877777777778, -122.54),
                map: map,
                title: '05--Bloedel Reserve - Shop',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/05_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.49, -122.76),
                map: map,
                title: '06--Bremerton National Airport-Old',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/06_Historical_Rain_Logger.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5913888888889, -122.617777777778),
                map: map,
                title: '08--BWU - Olympus Drive',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/08_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.56, -122.64),
                map: map,
                title: '09--BREMERTON, WASHINGTON',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/09_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4436, -122.6281),
                map: map,
                title: '10--Fish Pro - Burley',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/10_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6444444444444, -122.528888888889),
                map: map,
                title: '12--Sakai Intermediate School',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/12_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4075, -122.816944444444),
                map: map,
                title: '13--Coulter Creek Hatchery',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/13_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7355555555556, -122.658055555556),
                map: map,
                title: '15--Poulsbo - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/15_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6886111111111, -122.699166666667),
                map: map,
                title: '16--SWD - Dawn Park',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/16_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5298, -122.7108),
                map: map,
                title: '18--BWU - Gorst @ Domsea',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/18_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7733333333333, -122.556666666667),
                map: map,
                title: '22--Grovers Creek Hatchery',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/22_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.884366, -122.57464),
                map: map,
                title: '24--Hansville',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>24 Hansville Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/24_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/24_Day_Info/24_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5577777777778, -122.9775),
                map: map,
                title: '25--Holly Beach Club',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>25 Holly Beach Club Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/25_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/25_Day_Info/25_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6183333333333, -122.6025),
                map: map,
                title: '26--Illahee - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/26_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5272222222222, -122.621388888889),
                map: map,
                title: '27--Port Orchard - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/27_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.787157, -122.506142),
                map: map,
                title: '28---Port of Kingston - Port Office',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>28 Port of Kingston Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/28_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/28_Day_Info/28_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5272222222222, -122.786388888889),
                map: map,
                title: '31--BWU - McKenna Falls',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/31_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6669444444444, -122.54),
                map: map,
                title: '32--Meadowmeer Golf Course',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/32_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4327777777778, -122.573055555556),
                map: map,
                title: '34--Olalla - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/34_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.853344, -122.594659),
                map: map,
                title: '35--Port Gamble',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>35 Port Gamble Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/35_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/35_Day_Info/35_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.735638, -122.645844),
                map: map,
                title: '36--Poulsbo Public Works-Office',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/36_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6444444444444, -122.843055555556),
                map: map,
                title: '37--Scenic Beach State Park @ Seabeck',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/37_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6483, -122.8483),
                map: map,
                title: '38--Seabeck - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/38_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6375, -122.725833333333),
                map: map,
                title: '39--SWD - Wixon Site',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/39_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6136111111111, -122.888333333333),
                map: map,
                title: '40--Stavis Bay - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/40_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6394444444444, -122.674444444444),
                map: map,
                title: '41--Tracyton - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/41_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5216666666667, -122.759166666667),
                map: map,
                title: '42--BWU - Twin Lakes @ Well #20',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/42_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.8136111111111, -122.539444444444),
                map: map,
                title: '46--Hansville Road - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/46_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.5227777777778, -122.623055555556),
                map: map,
                title: '49--West Sound Utility District',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/49_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.3905555555556, -122.586388888889),
                map: map,
                title: '50--WA Water Company - Purdy',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/50_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6475, -122.658611111111),
                map: map,
                title: '51--SWD - Nels Nelson @ East End',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/51_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6783333333333, -122.659722222222),
                map: map,
                title: '52--SWD - Crista Camp @ Island Lake',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/52_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7522222222222, -122.611111111111),
                map: map,
                title: '53--Gala Pines Weather Station-Poulsbo (Click for real time data)',
                icon: 'http://kpudhydrodata.kpud.org/icons/iconSquareWeatherStation.png'

            });

            infowindow = new google.maps.InfoWindow();


            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>53 Gala Pines Weather Station</h2>' +
                '<p>Click below for weather station page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/GalaPinesCurrentConditions.aspx" target="_blank">Weather station data page</a></p>' +
                '<img src="Weather_Stations/Gala_Pines/Images/Gala_Pines_Pop_Up/Gala_Pines_Pop_Up-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);

            });



            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.7652777777778, -122.531111111111),
                map: map,
                title: '56--Indianola - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/56_Historical_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.801606, -122.654031),
                map: map,
                title: '59---Edgewater Industrial Park',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>59 Edgewater Industrial Park Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/59_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/59_Day_Info/59_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4919444444444, -122.765277777778),
                map: map,
                title: '61--BA - SSWM (Bremerton National Airport)',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'

            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>61 -BA - SSWM (Bremerton National Airport) Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/61_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/61_Day_Info/61_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.65152, -122.694996),
                map: map,
                title: '62--SW - SSWM (Silverdale-Wixon Site)',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele_with_baro.png'

            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>62 -SW - SSWM (Silverdale-Wixon Site) Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/62_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/62_Day_Info/62_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.6058333333333, -122.768888888889),
                map: map,
                title: '63--AP - SSWM (Airport Park)',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/63_Historical_Rain_Logger.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4083333333333, -122.604166666667),
                map: map,
                title: '64--Purdy - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/64_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4347222222, -122.839722222),
                map: map,
                title: '65--Theler Center',
                icon: 'http://kpudhydrodata.kpud.org/icons/inactive_precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/65_Historical_Rain_Logger.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.4130555555556, -122.552222222222),
                map: map,
                title: '66--Sunny Cove',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/66_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.613446, -122.819809),
                map: map,
                title: '67--Bridletree',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele_with_baro.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>67 Bridletree Rain Gage</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/67_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/67_Day_Info/67_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.83256, -122.542906),
                map: map,
                title: '68--Hansville Road - Private',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/68_Active_Daily_Rain.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.63232, -122.662885),
                map: map,
                title: '70--Kitsap County Fairgrounds Pavilion - Bremerton',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>70 Kitsap County Fairgrounds Pavilion - Bremerton</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/70_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/70_Day_Info/70_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.587327, -122.720579),
                map: map,
                title: '71--Kitsap County Central Road Shed',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>71 Kitsap County Central Road Shed</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/71_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/71_Day_Info/71_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.494538, -122.623984),
                map: map,
                title: '72--Kitsap County South Road Shed',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele_with_baro.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>72 Kitsap South Road Shed</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/72_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/72_Day_Info/72_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.849703, -122.547041),
                map: map,
                title: '74--Hansville Recycling and Garbage Facility',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/74_Historical_Rain_Logger.aspx", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.728311, -122.559813),
                map: map,
                title: '75--Suquamish Village',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>75 Suquamish Village</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/75_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/75_Day_Info/75_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.84967, -122.54716),
                map: map,
                title: '76--RAGF',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>76 RAGF</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/76_CurrentConditions.aspx " target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/76_Day_Info/76_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });


            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.563677, -122.672337),
                map: map,
                title: '77--BWU – Oyster Bay ',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("http://kpudhydrodata.kpud.org/77_Active_Daily_Rain.aspx", "_blank");
            });


            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.605667, -122.523639),
                map: map,
                title: '78--South Bainbridge Island ',
                icon: 'http://kpudhydrodata.kpud.org/icons/precip_tele.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                //Creating the content
                var content = '<div_id="info">' +
                '<h2>78 South Bainbridge Island</h2>' +
                '<p>Click below for rain gage page</p>' +
                '<p><a href="http://kpudhydrodata.kpud.org/78_CurrentConditions.aspx" target="_blank">Rain gage data page</a></p>' +
                '<img src="precip/Day_Info/78_Day_Info/78_Day_Info-001-001.jpg" alt="" height="250" width="212">' +
                '</div>';

                infowindow.setContent(content);
                infowindow.open(map, this);
            });



            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.378299, -122.618909),
                map: map,
                title: 'Purdy Road Shop (Pierce County Weather Station)',
                icon: 'http://kpudhydrodata.kpud.org/icons/iconSquareWeatherStation.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("https://www.hobolink.com/p/64772c8f4708e71015e16f9a8b0eda57", "_blank");
            });

            //Adding another marker to the map
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(47.209523, -122.755025),
                map: map,
                title: 'Longbranch Marina (Pierce County Weather Station)',
                icon: 'http://kpudhydrodata.kpud.org/icons/iconSquareWeatherStation.png'
            });

            google.maps.event.addListener(marker, 'click', function () {
                window.open("https://www.hobolink.com/p/fea2c14bce8f12b4766d5e71baf59f40", "_blank");
            });



        }



    };
})();