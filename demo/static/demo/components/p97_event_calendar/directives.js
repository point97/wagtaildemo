angular.module('cropApp')
    .directive('eventcalendar', function(){

    function link(scope, elt, attr){
        
    };

    function calCtrl($scope){

        $scope.today = function() {
            $scope.dt = new Date();
        };
        $scope.today();
        $scope.minDate = $scope.dt;
        
    }

    return {
        templateUrl: "/static/demo/components/p97_event_calendar/views/event_calendar.html",
        scope :{},
        link:link,
        controller:calCtrl
    };
});