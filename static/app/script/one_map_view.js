// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
ymaps.ready(show_one_map);

function show_one_map() {
    let ekb_center = [56.845520, 60.609821]
    // Создание карты.
    const myMap = new ymaps.Map("map", {
        // Координаты центра карты.
        // Порядок по умолчанию: «широта, долгота».
        // Чтобы не определять координаты центра карты вручную,
        // воспользуйтесь инструментом Определение координат.
        center: ekb_center,
        // Уровень масштабирования. Допустимые значения:
        // от 0 (весь мир) до 19.
        zoom: 10
    });

    myMap.controls.remove('geolocationControl'); // удаляем геолокацию
    myMap.controls.remove('searchControl'); // удаляем поиск
    myMap.controls.remove('trafficControl'); // удаляем контроль трафика
    myMap.controls.remove('typeSelector'); // удаляем тип
    myMap.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
    myMap.controls.remove('zoomControl'); // удаляем контрол зуммирования
    myMap.controls.remove('rulerControl'); // удаляем контрол линейного управления

    let prev_marker_pos = [parseFloat(document.getElementById('id_lat').value),
        parseFloat(document.getElementById('id_lng').value)];
    if (isNaN(prev_marker_pos[0]) || isNaN(prev_marker_pos[1])) {
        prev_marker_pos = ekb_center
    }
    console.log(prev_marker_pos)
    let dep = new ymaps.Placemark(prev_marker_pos, {},
        {
            draggable: true
        });

    dep.events.add('dragend', function (e) {
        let coords = e.get('target').geometry.getCoordinates();
        document.getElementById('id_lat').value = coords[0];
        document.getElementById('id_lng').value = coords[1];
    });

    myMap.geoObjects.add(dep);
}