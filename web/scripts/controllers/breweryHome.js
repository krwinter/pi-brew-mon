define([
    'controllers/baseController',
    'models/breweryHomeModel',
    'views/breweryHomeView'
    ],
        function(
        BaseController,
        model,
        view
        ) {


        // this is here to show how you can override stuff from base controller

        var controller = BaseController.extend({

            modelClass: model,
            viewClass: view,

        });

        return controller;

    }
);
