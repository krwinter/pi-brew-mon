var AppDispatcher = require('./appDispatcher');
var Constants = require('./constants');

var actions = {

	handleFermdataGet: function(action) {
		
		AppDispatcher.dispatch({
			actionType: Constants.FERM_DATA_FETCHED,
			data: action
		});
	}

};

module.exports = actions;