var actions = require('./fermActions');


var api = {

	getFermData: function() {

		var response = {
			currentTemp: 97,
			setTemp: 101.7,
			status: 'on man!'
		}

		actions.handleFermdataGet(response);
	}

};

module.exports = api;