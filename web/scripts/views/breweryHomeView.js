define([
    'marionette',
    'utils/events',
    'views/baseView',
    "text!templates/breweryHome.html"
    ],
        function(
            marionette,
            events,
            BaseView,
            modalHtml
        ) {


    var view = BaseView.extend({

        bindings: {
            'div': 'text:yahoo!'

        },

        template : function(serialized_model) {
            var name = serialized_model.name;
            return _.template(modalHtml)({
                title : serialized_model.title,
                content: serialized_model.content,
                sql: serialized_model.sql,
                repoUrl: serialized_model.repoUrl,
                extra: serialized_model.extra
            });
        },

        onShow: function() {
            console.log('show brew home modal')
        }


    });

    return view;

    }

);
