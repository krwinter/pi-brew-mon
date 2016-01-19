var AppDispatcher = require('./appDispatcher');
var Constants = require('./constants');
var assign = require('object-assign');
var EventEmitter = require('events').EventEmitter;
var Backbone = require('backbone-jquery');
//var $ = require('jquery');
//Backbone.$ = $;

var fermState = {}

var CHANGE_EVENT = 'change';

//var store = assign({}, EventEmitter.prototype,  {
var store = Backbone.Model.extend({

	// defaults: {
	// 	currentTemp,
	// 	setTemp,
	// 	status
	// },

	initialize: function() {
    	this.dispatchToken = AppDispatcher.register(this.dispatchCallback);
  	},

	getFermState: function() {
		return this.attributes;
	},

	// emitChange: function() {
	// 	this.emit(CHANGE_EVENT);
	// },

	/**
	* @param {function} callback
	*/
	addChangeListener: function(callback) {
		//debugger
		this.on(CHANGE_EVENT, callback);
	},

	/**
	* @param {function} callback
	*/
	removeChangeListener: function(callback) {
		this.removeListener(CHANGE_EVENT, callback);
	},

	dispatchCallback: function(payload) {
		debugger
		switch (payload.actionType) {
			case Constants.FERM_DATA_FETCHED :
			// we're setting it as an external prop, and as the model's properties
				//fermState = payload.data;
				this.set(payload.data);
				//store.emitChange();
				break;
		}

		return true;

	}

});

module.exports = new store();