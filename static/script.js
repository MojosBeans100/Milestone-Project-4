function aoi_choice() {

    upload_geojson = document.getElementById("upload_geojson").checked
    select_map = document.getElementById("select_map").checked

    console.log(select_map)
    aoi_input = document.getElementById("aoi_input")

    if (upload_geojson == true) {

        if (aoi_input.childElementCount >= 0) {
            aoi_input.removeChild(aoi_input.lastChild)
            console.log("geo json removed")
        }
        aoi = document.createElement("textarea")
        aoi.placeholder = "Upload co-ordinates in valid GeoJSON format"
        aoi.rows = 4
        aoi_input.appendChild(aoi)
        

    } else if (select_map == true) {
        
        if (aoi_input.childElementCount >= 0) {
            aoi_input.removeChild(aoi_input.lastChild)

        }
        aoi = document.createElement("input")
        aoi.type = "date"
        aoi_input.appendChild(aoi)
    }

}

function hello() {

    console.log(hello)
}