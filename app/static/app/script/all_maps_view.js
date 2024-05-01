// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
ymaps.ready(show_all_maps);

function show_all_maps() {
    let ekb_center = [56.845520, 60.609821];
    let maps_div = document.getElementsByClassName("map");
    //const maps: ymaps.Map[] = []
    for (let i = 0; i < maps_div.length; i++) {
        let div = maps_div[i]
        let lat = parseFloat(div.dataset.lat.replace(',', '.'))
        let lng = parseFloat(div.dataset.lng.replace(',', '.'))
        const map_center = [lat, lng]
        console.log(map_center)

        let new_map = new ymaps.Map(div, {
            center: Array.from(map_center),
            zoom: 10
        });

        new_map.behaviors.disable('scrollZoom');


        new_map.controls.remove('geolocationControl'); // удаляем геолокацию
        new_map.controls.remove('searchControl'); // удаляем поиск
        new_map.controls.remove('trafficControl'); // удаляем контроль трафика
        new_map.controls.remove('typeSelector'); // удаляем тип
        new_map.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
        new_map.controls.remove('zoomControl'); // удаляем контрол зуммирования
        new_map.controls.remove('rulerControl'); // удаляем контрол линейного управления

        let dep = new ymaps.Placemark(map_center, {}, {});

        new_map.geoObjects.add(dep);

        //maps.push(new_map)
    }
    // Создание карты.

}