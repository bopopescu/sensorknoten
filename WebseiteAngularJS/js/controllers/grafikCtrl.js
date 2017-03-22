angular.module('wettEditor').controller(
    'grafikCtrl',
    [ '$rootScope', '$scope', '$location', '$routeParams' ,'$filter','$http', '$window', 'alertService' ,  'sensorDataService',
        function($rootScope, $scope, $location, $routeParams, $filter, $http, $window , alertService , sensorDataService) {



            $scope.stationList = null;
            $scope.sensorList = null;

            $scope.aktuelleStationId = $routeParams.stationId;
            $scope.aktuelleStationIdBool = false;

            $scope.aktuelleSensorId = $routeParams.unitId;




            $scope.zeitRaumBool =false;

            $scope.loadAllStation = function() {
                sensorDataService.getAllStation().then(
                    function(response) {
                        $scope.stationList = response.data;
                        console.log($scope.stationList);
                        if($scope.aktuelleStationId != undefined){
                            $scope.getStationNow($scope.aktuelleStationId);
                            $scope.aktuelleStationIdBool = true;
                        }else{
                            $scope.aktuelleStationIdBool = false;
                        }

                    }, function(response) {
                        alertService.add("warning", response.data.errorMessage);
                    });
            };

            $scope.getStationNow = function(stationId) {
                sensorDataService.getStationNow(stationId).then(
                    function(response) {
                        $scope.sensorList = response.data;


                        if($scope.aktuelleSensorId != undefined){
                            $scope.zeitRaumBool = true ;
                        }else{
                            $scope.zeitRaumBool = false ;
                        }

                    }, function(response) {
                        alertService.add("warning", response.data.errorMessage);
                    });
            };

            getSensorDataBetween = function() {
                console.log($scope.startDate);
                console.log($scope.endDate);

                startDate = ($filter('number')(($scope.startDate.getTime() / 1000), 0)).replace(/\./g, '');
                endDate = ($filter('number')(($scope.endDate.getTime() / 1000), 0)).replace(/\./g, '');

                sensorDataService.getSensorDataBetween($scope.aktuelleStationId,$scope.aktuelleSensorId,startDate,endDate).then(
                    function(response) {
                        $scope.sensorDataList = response.data;
                        createSensorData();
                    }, function(response) {
                        alertService.add("warning", response.data.errorMessage);
                    });
            };

            $scope.loadAllStation();

            $scope.showAktuelleWerte = function(stationId) {
                $location.path('/stationen/' + stationId );
            };

            $scope.changeStation = function () {
                $scope.getStationNow($scope.aktuelleStationId);
                $scope.aktuelleStationIdBool = true;
            }
            $scope.changeSensor = function (unitID) {
                $scope.aktuelleSensorId = unitID;
                $scope.zeitRaumBool = true ;
            }

            //DATUM auswaehlen
            $scope.startDate = new Date();
            $scope.endDate = new Date();



            $scope.open1 = function() {
                $scope.popup1.opened = true;
            };
            $scope.popup1 = {
                opened: false
            };
            $scope.dateOptions1 = {
                formatYear: 'yy',
                maxDate: $scope.startDate,
                startingDay: 1
            };
            $scope.open2 = function() {
                $scope.popup2.opened = true;
            };
            $scope.popup2 = {
                opened: false
            };
            $scope.dateOptions2 = {
                formatYear: 'yy',
                minDate: $scope.endDate,
                startingDay: 1
            };

            $scope.sensorDataList = null;

            $scope.changeStartDate = function (startDate) {
                $scope.startDate = startDate;
            }
            $scope.changeEndDate = function (endDate) {
                $scope.endDate = endDate;
            }

            //Grafik
            $scope.showGrafik =function () {
                getSensorDataBetween();
                $scope.showGrafikBool = true;

            }
            $scope.showGrafikBool = false;

            createSensorData = function () {
                dataTest = {
                    name: '\'Station: ' + $scope.aktuelleStationId + ' Unit: ' + $scope.aktuelleSensorId + '\'',
                    data: []
                };
                angular.forEach($scope.sensorDataList.Messdaten, function(value, key){
                    array1 = [];
                    array1.push( value.timestamp);
                    array1.push( parseFloat(($filter('number')(value.value, 1)).replace(/\,/g, '.')));
                    dataTest.data.push(array1);

                });
                $scope.dataTest = [];
                $scope.dataTest.push(dataTest);

                $scope.options2 = {
                    title: 'StationId: ' + $scope.aktuelleStationId,
                    subtitle: 'UnitId: ' + $scope.aktuelleSensorId ,
                    width: 900
                };
            }


            $scope.options2 = {}

            $scope.dataTest = [];


        } ]);
