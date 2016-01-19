var AppDispatcher = require('./appDispatcher');
var Constants = require('./constants');
var assign = require('object-assign');
var EventEmitter = require('events').EventEmitter;

var fermState = {}

var CHANGE_EVENT = 'change';

var store = assign({}, EventEmitter.prototype,  {

	getFermState: function() {
		return fermState;
	},

	emitChange: function() {
		this.emit(CHANGE_EVENT);
	},

	/**
	* @param {function} callback
	*/
	addChangeListener: function(callback) {
		debugger
		this.on(CHANGE_EVENT, callback);
	},

	/**
	* @param {function} callback
	*/
	removeChangeListener: function(callback) {
		this.removeListener(CHANGE_EVENT, callback);
	},

	dispatcherIndex: AppDispatcher.register(function(payload) {
		debugger
		switch (payload.actionType) {
			case Constants.FERM_DATA_FETCHED :
				fermState = payload.data;
				store.emitChange();
				break;
		}

		return true;

	})

});

module.exports = store;